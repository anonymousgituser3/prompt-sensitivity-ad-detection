import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from itertools import combinations
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial

# ============================================================
# CONFIG
# ============================================================

INPUT_CSV = "qwen_prompt_variability_train_long.csv"   # change if needed
ID_COL = "ID"
OUT_PREFIX = "qwen"

OUT_DIR = Path("gee_results_all_interactions")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(INPUT_CSV)

required_cols = {ID_COL, "prompt_id", "predicted_label"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns in {INPUT_CSV}: {missing}")

df[ID_COL] = df[ID_COL].astype(str)
df["prompt_id"] = df["prompt_id"].astype(int)
df["predicted_label"] = df["predicted_label"].astype(int)

# ============================================================
# FACTOR DECODING
# ============================================================

df["pid"] = df["prompt_id"] - 1
pid = df["pid"].values

main_factors = [
    "emphasis",
    "newline_density",
    "instruction_placement",
    "segmentation",
    "criteria_format",
    "ordering",
]

df["emphasis"] = (pid >> 0) & 1
df["newline_density"] = (pid >> 1) & 1
df["instruction_placement"] = (pid >> 2) & 1
df["segmentation"] = (pid >> 3) & 1
df["criteria_format"] = (pid >> 4) & 1
df["ordering"] = (pid >> 5) & 1

# ============================================================
# TARGET: FLIP
# ============================================================

maj = (
    df.groupby(ID_COL)["predicted_label"]
    .agg(lambda x: 1 if x.sum() >= (len(x) / 2) else 0)
    .rename("majority_label")
    .reset_index()
)

df = df.merge(maj, on=ID_COL, how="left")
df["flip"] = (df["predicted_label"] != df["majority_label"]).astype(int)

# ============================================================
# ALL PAIRWISE INTERACTIONS
# ============================================================

interaction_cols = []

for a, b in combinations(main_factors, 2):
    col = f"{a}_x_{b}"
    df[col] = df[a] * df[b]
    interaction_cols.append(col)

predictor_cols = main_factors + interaction_cols

# ============================================================
# MODEL
# ============================================================

X = df[predictor_cols].copy()
X = sm.add_constant(X)

y = df["flip"]
groups = df[ID_COL]

model = GEE(y, X, groups=groups, family=Binomial())
result = model.fit()

print("\n================ GEE WITH ALL PAIRWISE INTERACTIONS ================")
print(result.summary())

# ============================================================
# ODDS RATIOS
# ============================================================

params = result.params
conf = result.conf_int()

or_df = pd.DataFrame({
    "term": params.index,
    "coef": params.values,
    "OR": np.exp(params.values),
    "CI_lower": np.exp(conf[0].values),
    "CI_upper": np.exp(conf[1].values),
    "p_value": result.pvalues.values,
})

or_df["significant"] = or_df["p_value"] < 0.05
or_df["term_type"] = np.where(
    or_df["term"].isin(main_factors),
    "main",
    np.where(or_df["term"] == "const", "const", "interaction")
)

print("\n================ ODDS RATIOS ================")
print(or_df.to_string(index=False))

sig_df = or_df[or_df["p_value"] < 0.05].copy()

print("\n================ SIGNIFICANT FACTORS ================")
if len(sig_df) == 0:
    print("No significant factors at p < 0.05")
else:
    print(sig_df.to_string(index=False))

# ============================================================
# SAVE TABLES
# ============================================================

or_df.to_csv(OUT_DIR / f"{OUT_PREFIX}_gee_all_pairwise_odds_ratios.csv", index=False)
sig_df.to_csv(OUT_DIR / f"{OUT_PREFIX}_gee_all_pairwise_significant.csv", index=False)

pd.DataFrame({"interaction_term": interaction_cols}).to_csv(
    OUT_DIR / f"{OUT_PREFIX}_gee_all_pairwise_interaction_list.csv",
    index=False
)

with open(OUT_DIR / f"{OUT_PREFIX}_gee_all_pairwise_summary.txt", "w", encoding="utf-8") as f:
    f.write("GEE WITH ALL PAIRWISE INTERACTIONS\n\n")
    f.write(str(result.summary()))
    f.write("\n\nODDS RATIOS\n\n")
    f.write(or_df.to_string(index=False))
    f.write("\n\nSIGNIFICANT FACTORS (p < 0.05)\n\n")
    if len(sig_df) == 0:
        f.write("No significant factors at p < 0.05\n")
    else:
        f.write(sig_df.to_string(index=False))
        f.write("\n")

# ============================================================
# HELPER FOR COLORED FOREST PLOTS
# ============================================================

def draw_forest_plot(plot_df: pd.DataFrame, title: str, out_path: Path):
    plot_df = plot_df.copy()
    plot_df = plot_df.sort_values("OR", ascending=True).reset_index(drop=True)

    colors = ["tab:red" if sig else "tab:gray" for sig in plot_df["significant"]]

    plt.figure(figsize=(10, max(4, len(plot_df) * 0.35)))

    for i, row in plot_df.iterrows():
        plt.errorbar(
            x=row["OR"],
            y=i,
            xerr=[[row["OR"] - row["CI_lower"]], [row["CI_upper"] - row["OR"]]],
            fmt="o",
            color=colors[i],
            ecolor=colors[i],
            capsize=3
        )

    plt.axvline(1, linestyle="--")
    plt.yticks(range(len(plot_df)), plot_df["term"])
    plt.xlabel("Odds Ratio")
    plt.ylabel("Factor")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

# ============================================================
# HELPER FOR COLORED COEFFICIENT PLOTS
# ============================================================

def draw_coef_plot(plot_df: pd.DataFrame, title: str, out_path: Path):
    plot_df = plot_df.copy()
    plot_df = plot_df.sort_values("coef", ascending=True).reset_index(drop=True)

    colors = ["tab:red" if sig else "tab:gray" for sig in plot_df["significant"]]

    plt.figure(figsize=(10, max(4, len(plot_df) * 0.35)))
    plt.barh(plot_df["term"], plot_df["coef"], color=colors)
    plt.axvline(0, linestyle="--")
    plt.xlabel("Log-odds coefficient")
    plt.ylabel("Factor")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

# ============================================================
# HELPER FOR COLORED SIGNIFICANCE PLOTS
# ============================================================

def draw_significance_plot(plot_df: pd.DataFrame, title: str, out_path: Path):
    plot_df = plot_df.copy()
    plot_df["minus_log10_p"] = -np.log10(plot_df["p_value"].clip(lower=1e-300))
    plot_df = plot_df.sort_values("minus_log10_p", ascending=True).reset_index(drop=True)

    colors = ["tab:red" if sig else "tab:gray" for sig in plot_df["significant"]]

    plt.figure(figsize=(10, max(4, len(plot_df) * 0.35)))
    plt.barh(plot_df["term"], plot_df["minus_log10_p"], color=colors)
    plt.axvline(-np.log10(0.05), linestyle="--")
    plt.xlabel("-log10(p-value)")
    plt.ylabel("Factor")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

# ============================================================
# DATA SUBSETS FOR PLOTS
# ============================================================

all_df = or_df[or_df["term"] != "const"].copy()
main_df = or_df[or_df["term"].isin(main_factors)].copy()
interaction_df = or_df[or_df["term"].isin(interaction_cols)].copy()

# ============================================================
# PLOT 1: ALL TERMS
# ============================================================

draw_forest_plot(
    all_df,
    "All prompt effects on flip probability",
    OUT_DIR / f"{OUT_PREFIX}_gee_all_terms_forest_plot.png"
)

draw_coef_plot(
    all_df,
    "All GEE coefficients",
    OUT_DIR / f"{OUT_PREFIX}_gee_all_terms_coefficient_plot.png"
)

draw_significance_plot(
    all_df,
    "All factor significance",
    OUT_DIR / f"{OUT_PREFIX}_gee_all_terms_significance_plot.png"
)

# ============================================================
# PLOT 2: MAIN EFFECTS ONLY
# ============================================================

draw_forest_plot(
    main_df,
    "Main effects only",
    OUT_DIR / f"{OUT_PREFIX}_gee_main_effects_forest_plot.png"
)

draw_coef_plot(
    main_df,
    "Main effects coefficients",
    OUT_DIR / f"{OUT_PREFIX}_gee_main_effects_coefficient_plot.png"
)

draw_significance_plot(
    main_df,
    "Main effects significance",
    OUT_DIR / f"{OUT_PREFIX}_gee_main_effects_significance_plot.png"
)

# ============================================================
# PLOT 3: INTERACTIONS ONLY
# ============================================================

draw_forest_plot(
    interaction_df,
    "Interaction effects only",
    OUT_DIR / f"{OUT_PREFIX}_gee_interactions_forest_plot.png"
)

draw_coef_plot(
    interaction_df,
    "Interaction effects coefficients",
    OUT_DIR / f"{OUT_PREFIX}_gee_interactions_coefficient_plot.png"
)

draw_significance_plot(
    interaction_df,
    "Interaction effects significance",
    OUT_DIR / f"{OUT_PREFIX}_gee_interactions_significance_plot.png"
)

# ============================================================
# CONSOLE SUMMARY
# ============================================================

print("\nNumber of main factors:", len(main_factors))
print("Number of pairwise interactions:", len(interaction_cols))
print("Expected pairwise interactions for 6 factors = 6 choose 2 = 15")

print("\nSaved inside:", OUT_DIR.resolve())
print(f"- {OUT_PREFIX}_gee_all_pairwise_odds_ratios.csv")
print(f"- {OUT_PREFIX}_gee_all_pairwise_significant.csv")
print(f"- {OUT_PREFIX}_gee_all_pairwise_interaction_list.csv")
print(f"- {OUT_PREFIX}_gee_all_pairwise_summary.txt")
print(f"- {OUT_PREFIX}_gee_all_terms_forest_plot.png")
print(f"- {OUT_PREFIX}_gee_all_terms_coefficient_plot.png")
print(f"- {OUT_PREFIX}_gee_all_terms_significance_plot.png")
print(f"- {OUT_PREFIX}_gee_main_effects_forest_plot.png")
print(f"- {OUT_PREFIX}_gee_main_effects_coefficient_plot.png")
print(f"- {OUT_PREFIX}_gee_main_effects_significance_plot.png")
print(f"- {OUT_PREFIX}_gee_interactions_forest_plot.png")
print(f"- {OUT_PREFIX}_gee_interactions_coefficient_plot.png")
print(f"- {OUT_PREFIX}_gee_interactions_significance_plot.png")