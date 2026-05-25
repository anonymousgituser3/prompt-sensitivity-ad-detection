# prompts_factorial64.py
# Auto-generated factorial prompt set (64 prompts) from prompts_mistral.py baseline.

PROMPT_1 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_2 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_3 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC). HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""


PROMPT_4 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC). HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_5 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_6 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_7 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing). If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_8 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing). If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_9 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_10 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_11 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_12 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_13 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_14 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_15 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_16 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_17 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_18 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_19 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_20 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_21 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_22 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_23 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_24 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_25 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_26 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_27 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_28 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_29 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_30 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_31 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_32 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_33 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_34 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_35 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""


PROMPT_36 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC). AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""


PROMPT_37 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_38 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_39 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing). If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_40 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion. HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect). The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing). If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR. Transcript conventions: - "xxx" = unintelligible - Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_41 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_42 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_43 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_44 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_45 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_46 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_47 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_48 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD: AD speech is often marked by: frequent word-finding difficulty, many repetitions, reduced specificity, overuse of vague/indefinite terms, unclear or incorrect pronoun references, short/incomplete utterances, and weaker coherence/cohesion.
HC: HC speech is often marked by: more specific nouns/verbs, clearer references, more complete event structure, better coherence, and broader accurate coverage of picture details (even if not perfect).
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_49 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_50 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_51 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_52 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_53 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_54 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_55 = """You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
Transcript conventions:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_56 = """YOU ARE AN EXPERT EVALUATOR FOR ALZHEIMER’S DISEASE (AD) DETECTION FROM LANGUAGE. PERSON A IS DESCRIBING THE “COOKIE THEFT” PICTURE USING SPONTANEOUS SPEECH. GIVEN THE TRANSCRIPT, PREDICT WHETHER THE SPEAKER IS AD OR HEALTHY CONTROL (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
IF UNCERTAIN, CHOOSE THE MORE LIKELY CLASS, NEVER OUTPUT MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
TRANSCRIPT CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_57 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_58 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_59 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_60 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_61 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_62 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).

OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}

AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)

SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).

RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.

CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_63 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
Output ONLY valid JSON in this exact format (no extra text):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPT_64 = """TASK: You are an expert evaluator for Alzheimer’s Disease (AD) detection from language. Person A is describing the “Cookie Theft” picture using spontaneous speech. Given the transcript, predict whether the speaker is AD or Healthy Control (HC).
OUTPUT ONLY VALID JSON IN THIS EXACT FORMAT (NO EXTRA TEXT):
{
  "reasoning": "brief justification",
  "alzheimers_prediction": "YES" or "NO",
  "probability_score": float between 0 and 1 (likelihood of AD)
}
AD: AD speech is often marked by:
- frequent word-finding difficulty
- many repetitions
- reduced specificity
- overuse of vague/indefinite terms
- unclear or incorrect pronoun references
- short/incomplete utterances
- weaker coherence/cohesion
HC: HC speech is often marked by:
- more specific nouns/verbs
- clearer references
- more complete event structure
- better coherence
- broader accurate coverage of picture details (even if not perfect)
SCENE: The image can be described using seven concepts (woman doing dishes, sink overflowing, boy on stool, children stealing cookies, girl reaching for cookie, stool falling, woman not noticing).
RULE: If uncertain, choose the more likely class, never output MAYBE/UNCERTAIN/UNDEFINED/UNDETERMINED/UNCLEAR.
CONVENTIONS:
- "xxx" = unintelligible
- Pauses: "(short pause)", "(medium pause)", "(long pause)"
"""

PROMPTS = {
    1: PROMPT_1,
    2: PROMPT_2,
    3: PROMPT_3,
    4: PROMPT_4,
    5: PROMPT_5,
    6: PROMPT_6,
    7: PROMPT_7,
    8: PROMPT_8,
    9: PROMPT_9,
    10: PROMPT_10,
    11: PROMPT_11,
    12: PROMPT_12,
    13: PROMPT_13,
    14: PROMPT_14,
    15: PROMPT_15,
    16: PROMPT_16,
    17: PROMPT_17,
    18: PROMPT_18,
    19: PROMPT_19,
    20: PROMPT_20,
    21: PROMPT_21,
    22: PROMPT_22,
    23: PROMPT_23,
    24: PROMPT_24,
    25: PROMPT_25,
    26: PROMPT_26,
    27: PROMPT_27,
    28: PROMPT_28,
    29: PROMPT_29,
    30: PROMPT_30,
    31: PROMPT_31,
    32: PROMPT_32,
    33: PROMPT_33,
    34: PROMPT_34,
    35: PROMPT_35,
    36: PROMPT_36,
    37: PROMPT_37,
    38: PROMPT_38,
    39: PROMPT_39,
    40: PROMPT_40,
    41: PROMPT_41,
    42: PROMPT_42,
    43: PROMPT_43,
    44: PROMPT_44,
    45: PROMPT_45,
    46: PROMPT_46,
    47: PROMPT_47,
    48: PROMPT_48,
    49: PROMPT_49,
    50: PROMPT_50,
    51: PROMPT_51,
    52: PROMPT_52,
    53: PROMPT_53,
    54: PROMPT_54,
    55: PROMPT_55,
    56: PROMPT_56,
    57: PROMPT_57,
    58: PROMPT_58,
    59: PROMPT_59,
    60: PROMPT_60,
    61: PROMPT_61,
    62: PROMPT_62,
    63: PROMPT_63,
    64: PROMPT_64,
}