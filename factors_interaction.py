import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv("mistral_prompt_variability_train_long.csv")
# df = pd.read_csv("qwen_prompt_variability_train_long.csv")


df["prompt_id"] = df["prompt_id"].astype(int)
df["predicted_label"] = df["predicted_label"].astype(int)

# ============================================================
# FACTOR DECODING
# ============================================================

df["pid"] = df["prompt_id"] - 1
pid = df["pid"].values

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
    df.groupby("ID")["predicted_label"]
    .agg(lambda x: 1 if x.sum() >= (len(x) / 2) else 0)
    .rename("majority_label")
    .reset_index()
)

df = df.merge(maj, on="ID", how="left")
df["flip"] = (df["predicted_label"] != df["majority_label"]).astype(int)

# ============================================================
# INTERACTIONS
# ============================================================

df["seg_x_format"] = df["segmentation"] * df["criteria_format"]
df["seg_x_instr"] = df["segmentation"] * df["instruction_placement"]
df["format_x_instr"] = df["criteria_format"] * df["instruction_placement"]

# ============================================================
# MODEL
# ============================================================

X = df[
    [
        "emphasis",
        "newline_density",
        "instruction_placement",
        "segmentation",
        "criteria_format",
        "ordering",
        "seg_x_format",
        "seg_x_instr",
        "format_x_instr",
    ]
]

X = sm.add_constant(X)

y = df["flip"]
groups = df["ID"]

model = GEE(y, X, groups=groups, family=Binomial())
result = model.fit()

print("\n================ GEE WITH INTERACTIONS ================")
print(result.summary())

# ============================================================
# ODDS RATIOS
# ============================================================

params = result.params
conf = result.conf_int()

or_df = pd.DataFrame({
    "OR": np.exp(params),
    "CI_lower": np.exp(conf[0]),
    "CI_upper": np.exp(conf[1]),
    "p_value": result.pvalues
})

print("\n================ ODDS RATIOS (INTERACTIONS) ================")
print(or_df)

or_df.to_csv("gee_odds_ratios_interactions.csv")