import re
import random
import logging
from dataclasses import dataclass
from typing import Optional, Tuple, Dict, Any, List

import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
from transformers import LlamaTokenizer, AutoModelForCausalLM
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)

from prompts_factorial64 import PROMPTS

# ============================================================
# Config
# ============================================================

@dataclass(frozen=True)
class Config:
    seed: int = 1

    model_id: str = "mistralai/Mistral-7B-Instruct-v0.3" ## add here path to real mistral model files

    # Demonstration input. Replace with the authorised ADReSS/DementiaBank CSV for full reproduction.
    csv_path: str = "example_data_dummy.csv"
    id_col: str = "ID"
    out_csv: str = "demo_prompt_variability_long.csv"

    max_context_tokens: int = 32768
    target_max_new_tokens: int = 900

    retry_min_new: int = 64
    retry_max_new: int = 256

    prompt_ids: Tuple[int, ...] = tuple(range(1, 65))


USER_TMPL = "\n<|user|>\nDESCRIPTION: {transcript}\n<|assistant|>\n"

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("mistral_prompt_variability")


# ============================================================
# Seeding
# ============================================================

def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ============================================================
# Data
# ============================================================

def load_data(csv_path: str, id_col: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    if id_col not in df.columns:
        raise ValueError(f"Missing ID column '{id_col}' in {csv_path}")
    if "transcription" not in df.columns:
        raise ValueError(f"Missing required column 'transcription' in {csv_path}")
    if "label" not in df.columns:
        raise ValueError(f"Missing required column 'label' in {csv_path}")

    df["transcription"] = df["transcription"].astype(str)
    df["label"] = df["label"].astype(int)
    return df


# ============================================================
# Model
# ============================================================

def load_model(model_id: str):
    tokenizer = LlamaTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer, model


# ============================================================
# Robust extraction & parsing helpers
# ============================================================

def extract_best_json_object(text: str) -> Optional[str]:
    s = (
        text.replace("’", "'")
        .replace("“", '"')
        .replace("”", '"')
    )
    s = re.sub(r"```.*?\n", "", s)
    s = re.sub(r"</?s>", "", s)
    s = re.sub(r"<\|.*?\|>", "", s)

    spans = []
    depth = 0
    in_str, esc = False, False
    start = None

    for i, ch in enumerate(s):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                if depth == 0:
                    start = i
                depth += 1
            elif ch == "}":
                if depth > 0:
                    depth -= 1
                    if depth == 0 and start is not None:
                        spans.append((start, i + 1))

    if spans:
        for a, b in reversed(spans):
            obj = s[a:b]
            low = obj.lower()
            if "alzheimers_prediction" in low and "probability_score" in low:
                return obj
        a, b = max(spans, key=lambda ab: ab[1] - ab[0])
        return s[a:b]

    if "{" in s:
        return "{" + s.split("{", 1)[1]
    return None


def parse_prediction_json_tolerant(text: str) -> Tuple[Optional[str], Optional[float], str]:
    block = extract_best_json_object(text) or text
    t = block

    t = re.sub(r",\s*([}\]])", r"\1", t)
    t = re.sub(r"(:\s*)(\.\d+)", r"\g<1>0\2", t)
    t = re.sub(
        r'(["\']?probability_score["\']?\s*:\s*"?)([0-9]*\.?[0-9]+)\s*%("?)(?=\s*[},])',
        r"\1\2\3",
        t,
    )
    t = re.sub(
        r'("reasoning"\s*:\s*".*?")\s*(["\']?alzheimers_prediction["\']?)',
        r"\1, \2",
        t,
        flags=re.DOTALL,
    )
    t = re.sub(
        r'(["\']?alzheimers_prediction["\']?\s*:\s*".+?")\s*(["\']?probability_score["\']?)',
        r"\1, \2",
        t,
        flags=re.DOTALL,
    )
    t = re.sub(
        r'(["\']?alzheimers_prediction["\']?\s*:\s*)(YES|NO)(?=\s*[},])',
        r'\1"\2"',
        t,
        flags=re.IGNORECASE,
    )

    m_label = re.search(
        r'["\']?alzheimers_prediction["\']?\s*:\s*["\']?\b(YES|NO)\b["\']?',
        t,
        flags=re.IGNORECASE,
    )
    label = m_label.group(1).upper() if m_label else None

    m_prob = re.search(r'["\']?probability_score["\']?\s*:\s*["\']?([0-9]*\.?[0-9]+)["\']?', t)
    prob = None
    if m_prob:
        try:
            prob = float(m_prob.group(1))
            if 1.0 < prob <= 100.0:
                prob /= 100.0
        except ValueError:
            prob = None

    if prob is not None and not (0.0 <= prob <= 1.0):
        prob = None

    if label is None and prob is not None:
        label = "YES" if prob >= 0.5 else "NO"

    return label, prob, t


# ============================================================
# Generation
# ============================================================

@torch.inference_mode()
def generate_completion(model, tokenizer, prompt: str, max_new_tokens: int) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=False).to(model.device)
    input_len = inputs["input_ids"].shape[-1]

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    out_ids = outputs[0][input_len:] if outputs[0].shape[-1] > input_len else outputs[0]
    return tokenizer.decode(out_ids, skip_special_tokens=True).strip()


def compute_max_new(cfg: Config, tokenizer, full_prompt: str) -> int:
    input_len = tokenizer(full_prompt, return_tensors="pt", truncation=False)["input_ids"].shape[-1]
    return min(cfg.target_max_new_tokens, cfg.max_context_tokens - input_len)


def compute_retry_max_new(cfg: Config, tokenizer, retry_prefix: str) -> int:
    retry_input_len = tokenizer(retry_prefix, return_tensors="pt", truncation=False)["input_ids"].shape[-1]
    budget = cfg.max_context_tokens - retry_input_len
    return max(cfg.retry_min_new, min(cfg.retry_max_new, budget))


def run_one_prompt(cfg: Config, model, tokenizer, system_prompt: str, transcript: str) -> Dict[str, Any]:
    system_block = f"<|system|>\n{system_prompt}"
    user_block = USER_TMPL.format(transcript=transcript.strip())
    full_prompt = system_block + user_block

    max_new = compute_max_new(cfg, tokenizer, full_prompt)
    if max_new < 1:
        return {
            "ok": False,
            "reason": "context budget exhausted (max_new < 1)",
            "decoded_first": "",
            "decoded_retry": "",
            "label_str": None,
            "prob": None,
            "parsed_json_text": "",
        }

    decoded = generate_completion(model, tokenizer, full_prompt, max_new)
    label_str, prob, parsed_json_text = parse_prediction_json_tolerant(decoded)

    decoded_retry = ""
    if (label_str is None) or (prob is None):
        retry_prefix = full_prompt + '{"reasoning": "'
        retry_max_new = compute_retry_max_new(cfg, tokenizer, retry_prefix)
        retry_tail = generate_completion(model, tokenizer, retry_prefix, retry_max_new)
        decoded_retry = '{"reasoning": "' + retry_tail
        label_str, prob, parsed_json_text = parse_prediction_json_tolerant(decoded_retry)

    ok = (label_str is not None) and (prob is not None)
    reason = ""
    if not ok:
        if (label_str is None) and (prob is None):
            reason = "missing both alzheimers_prediction and probability_score"
        elif label_str is None:
            reason = "missing alzheimers_prediction"
        else:
            reason = "missing probability_score"

    return {
        "ok": ok,
        "reason": reason,
        "decoded_first": decoded,
        "decoded_retry": decoded_retry,
        "label_str": label_str,
        "prob": prob,
        "parsed_json_text": parsed_json_text,
    }


# ============================================================
# Stability metrics
# ============================================================

def compute_stability(long_df: pd.DataFrame, id_col: str) -> pd.DataFrame:
    """
    Per transcript ID:
    - majority_label across prompts
    - flip_rate = fraction of prompt predictions that differ from majority
    - prob_std across prompts (ignoring NaN)
    - n_valid predictions
    """
    rows = []
    for rid, g in long_df.groupby(id_col):
        preds = g["predicted_label"].dropna().astype(int).to_list()
        probs = g["probability_score"].dropna().astype(float).to_list()

        if len(preds) == 0:
            rows.append({
                id_col: rid,
                "n_valid": 0,
                "majority_label": np.nan,
                "flip_rate": np.nan,
                "prob_std": np.nan,
            })
            continue

        # Majority (tie breaks toward 1 if equal count, deterministic)
        ones = sum(preds)
        zeros = len(preds) - ones
        majority = 1 if ones >= zeros else 0

        flip_rate = sum(1 for p in preds if p != majority) / len(preds)
        prob_std = float(np.std(probs)) if len(probs) >= 2 else 0.0

        rows.append({
            id_col: rid,
            "n_valid": len(preds),
            "majority_label": majority,
            "flip_rate": flip_rate,
            "prob_std": prob_std,
        })

    return pd.DataFrame(rows)


# ============================================================
# Main
# ============================================================

def main():
    cfg = Config()
    seed_everything(cfg.seed)

    df = load_data(cfg.csv_path, cfg.id_col)
    tokenizer, model = load_model(cfg.model_id)

    all_rows: List[Dict[str, Any]] = []
    parse_fails: List[Dict[str, Any]] = []

    log.info("Running prompts %s on %d samples", cfg.prompt_ids, len(df))

    for row in tqdm(df.itertuples(index=False), total=len(df)):
        rid = getattr(row, cfg.id_col)
        transcript = str(getattr(row, "transcription")).strip()
        true_label = int(getattr(row, "label"))

        for pid in cfg.prompt_ids:
            out = run_one_prompt(cfg, model, tokenizer, PROMPTS[pid], transcript)

            if not out["ok"]:
                parse_fails.append({
                    cfg.id_col: str(rid),
                    "prompt_id": pid,
                    "reason": out["reason"],
                    "decoded_raw": out["decoded_first"],
                    "decoded_retry": out["decoded_retry"],
                })
                continue

            pred = 1 if out["label_str"] == "YES" else 0
            all_rows.append({
                cfg.id_col: rid,
                "prompt_id": pid,
                "true_label": true_label,
                "predicted_label": pred,
                "probability_score": float(out["prob"]),
                "model_output": out["parsed_json_text"],
                "transcript": transcript,
            })

    long_df = pd.DataFrame(all_rows)
    long_df.to_csv(cfg.out_csv, index=False)
    log.info("Saved long results to %s", cfg.out_csv)

    if parse_fails:
        pd.DataFrame(parse_fails).to_csv("parse_fails.csv", index=False, encoding="utf-8")
        log.info("Saved parse fails to parse_fails.csv (n=%d)", len(parse_fails))

    if len(long_df) == 0:
        log.warning("No valid predictions were produced.")
        return

    # --------------------------------------------------------
    # Per-prompt performance (distribution over prompts)
    # --------------------------------------------------------
    print("\n================ PER-PROMPT METRICS ================")
    per_prompt_rows = []
    for pid, g in long_df.groupby("prompt_id"):
        y_true = g["true_label"].astype(int)
        y_pred = g["predicted_label"].astype(int)
        acc = accuracy_score(y_true, y_pred)
        f1m = f1_score(y_true, y_pred, average="macro")
        per_prompt_rows.append({"prompt_id": int(pid), "n": len(g), "accuracy": acc, "macro_f1": f1m})
        print(f"Prompt {int(pid):2d} | n={len(g):3d} | acc={acc:.3f} | macroF1={f1m:.3f}")

    per_prompt_df = pd.DataFrame(per_prompt_rows).sort_values("prompt_id")
    per_prompt_df.to_csv("per_prompt_metrics.csv", index=False)

    # --------------------------------------------------------
    # Stability across prompts (flip rate per transcript)
    # --------------------------------------------------------
    stab_df = compute_stability(long_df, cfg.id_col)
    stab_df.to_csv("stability_per_transcript.csv", index=False)

    print("\n================ STABILITY METRICS ================")
    valid_flip = stab_df["flip_rate"].dropna().astype(float)
    valid_std = stab_df["prob_std"].dropna().astype(float)

    print(f"Transcripts evaluated: {len(stab_df)}")
    print(f"Mean flip rate: {valid_flip.mean():.3f}")
    print(f"Median flip rate: {valid_flip.median():.3f}")
    print(f"90th percentile flip rate: {valid_flip.quantile(0.90):.3f}")
    print(f"Mean prob std: {valid_std.mean():.3f}")
    print(f"Median prob std: {valid_std.median():.3f}")

    # --------------------------------------------------------
    # Majority vote prediction (10 prompts) as an optional output
    # --------------------------------------------------------
    maj_rows = []
    for rid, g in long_df.groupby(cfg.id_col):
        preds = g["predicted_label"].astype(int).to_list()
        probs = g["probability_score"].astype(float).to_list()
        y_true = int(g["true_label"].iloc[0])

        ones = sum(preds)
        zeros = len(preds) - ones
        maj = 1 if ones >= zeros else 0

        maj_prob = float(np.mean(probs)) if len(probs) else np.nan
        maj_rows.append({
            cfg.id_col: rid,
            "true_label": y_true,
            "majority_pred": maj,
            "mean_prob": maj_prob,
            "n_prompts": len(preds),
        })

    maj_df = pd.DataFrame(maj_rows)
    maj_df.to_csv("majority_vote.csv", index=False)

    y_true = maj_df["true_label"].astype(int)
    y_pred = maj_df["majority_pred"].astype(int)

    print("\n================ MAJORITY VOTE (10 prompts) ================")
    print(classification_report(y_true, y_pred, target_names=["HC", "AD"]))
    print(f"Majority vote accuracy: {accuracy_score(y_true, y_pred):.3f}")
    print(f"Majority vote macro F1: {f1_score(y_true, y_pred, average='macro'):.3f}")

    if maj_df["mean_prob"].notna().sum() >= 2 and maj_df["true_label"].nunique() == 2:
        auc = roc_auc_score(maj_df["true_label"], maj_df["mean_prob"])
        print(f"Majority vote ROC AUC (using mean_prob): {auc:.3f}")

    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    if cm.size == 4:
        tn, fp, fn, tp = cm.ravel()
        print(f"CM - TN:{tn} FP:{fp} FN:{fn} TP:{tp}")

    if torch.cuda.is_available():
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()