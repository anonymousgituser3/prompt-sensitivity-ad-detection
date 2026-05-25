\# Prompt Sensitivity in LLM-Based Alzheimer’s Detection



This anonymous repository contains the code used for the paper:



\*\*Prompt Sensitivity in LLM-Based Alzheimer’s Detection\*\*



The repository provides scripts for generating 64 factorial prompt variants, running prompt-based inference, parsing model outputs, computing prompt-stability measures, and performing Generalized Estimating Equation (GEE) analysis.



\## Repository contents



```text

prompts\_factorial64.py

Mistral\_prompt\_variability.py

gee\_prompt\_factor.py

factors\_interaction.py

example\_data\_dummy.csv

requirements.txt

.gitignore

README.md

```



\## Dataset access restriction



The ADReSS 2020 and DementiaBank/Pitt transcripts are not included in this repository because they are subject to dataset access restrictions and cannot be redistributed.



The file `example\_data\_dummy.csv` is provided only to show the expected input format. Researchers with authorised access to the dataset can reproduce the experiments by preparing the input CSV using the same column structure.



\## Expected input format



The inference script expects a CSV file with at least the following columns:



```text

ID,transcription,label

```



Optional metadata such as MMSE can also be included.



Example:



```csv

ID,transcription,label,mmse

demo\_001,"the boy is taking cookies and the water is overflowing",0,30

demo\_002,"uh the thing there and xxx the boy uh",1,18

```



Label convention:



```text

0 = Healthy Control

1 = Alzheimer's Disease

```



\## Prompt design



The file `prompts\_factorial64.py` contains the 64 prompt variants generated from a full 2^6 factorial design. The six binary factors are:



```text

emphasis

newline density

instruction placement

segmentation

criteria format

class ordering

```



\## Running inference



The main inference script is:



```bash

python Mistral\_prompt\_variability.py

```



The same script can be used for another model, such as Qwen3-14B, by changing the `model\_id`, input CSV path, and output CSV name in the configuration section.



The script produces a long-format CSV containing one row per transcript and prompt variant.



\## Running GEE analysis



After obtaining the long-format prediction file, run:



```bash

python gee\_prompt\_factor.py

```



This computes:



```text

main prompt-factor effects

all pairwise interaction effects

odds ratios

95% confidence intervals

p-values

forest plots

coefficient plots

significance plots

```



\## Important note on reproducibility



Because the original transcripts cannot be redistributed, this repository supports code-level reproducibility. Full experimental reproduction requires authorised access to the ADReSS/DementiaBank data.

