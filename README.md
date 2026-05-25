# Prompt Sensitivity in LLM-Based Alzheimer's Detection

This anonymous repository contains code for the paper **Prompt Sensitivity in LLM-Based Alzheimer's Detection**.

The repository provides scripts for generating 64 factorial prompt variants, running prompt-based inference, parsing model outputs, computing prompt-stability measures, and performing Generalized Estimating Equation analysis.

## Repository contents

- `prompts_factorial64.py`: contains the 64 factorial prompt variants.
- `run_prompt_variability.py`: runs model inference across prompt variants and computes stability metrics.
- `gee_prompt_factor.py`: performs GEE analysis with main effects and pairwise interactions.
- `factors_interaction.py`: auxiliary script for prompt-factor interaction analysis.
- `example_data_dummy.csv`: dummy example showing the expected input format.
- `requirements.txt`: Python dependencies.

## Dataset access restriction

The ADReSS 2020 and DementiaBank/Pitt transcripts are not included in this repository because they are subject to dataset access restrictions and cannot be redistributed.

The file `example_data_dummy.csv` is provided only to show the expected input format. Researchers with authorised access to the dataset can reproduce the experiments by preparing the input CSV using the same column structure.

## Expected input format

The inference script expects a CSV file with at least the following columns:

```text
ID,transcription,label
```

Optional metadata such as MMSE can also be included.

Example:

```csv
ID,transcription,label,mmse
demo_001,"the boy is taking cookies and the water is overflowing",0,30
demo_002,"uh the thing there and xxx the boy uh",1,18
```

Label convention:

```text
0 = Healthy Control
1 = Alzheimer's Disease
```

## Prompt design

The file `prompts_factorial64.py` contains the 64 prompt variants generated from a full 2^6 factorial design.

The six binary prompt factors are:

- emphasis
- newline density
- instruction placement
- segmentation
- criteria format
- class ordering

## Running inference

Run:

```bash
python run_prompt_variability.py
```

The same script can be used for Mistral-7B-Instruct-v0.3 and Qwen3-14B by changing the model identifier, input CSV path, and output CSV name in the configuration section.

## Running GEE analysis

After obtaining the long-format prediction file, run:

```bash
python gee_prompt_factor.py
```

This computes main prompt-factor effects, pairwise interaction effects, odds ratios, confidence intervals, p-values, and plots.

## Reproducibility note

Because the original transcripts cannot be redistributed, this repository supports code-level reproducibility. Full experimental reproduction requires authorised access to the ADReSS/DementiaBank data.