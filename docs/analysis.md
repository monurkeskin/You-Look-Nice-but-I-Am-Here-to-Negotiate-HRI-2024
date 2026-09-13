# Analyze this paper's session records

The analysis unit is the **participant**. Two fifteen-minute sessions with preference elicitation before each. Prior attitude is measured before the experiment; Godspeed and thermometer responses follow the specified interactions.

## Available example

```bash
negotiator reproduce reproduction/paired-example.json --output paired-output
```

The three synthetic participant pairs have differences 0.4, 0.1 and -0.2; their
mean is 0.1. This number is a hand-checkable fixture, not a result from the paper.
`paired-output/results.csv` contains computed group summaries and interval bounds;
`table.tex` formats those same values and `paired-contrasts.svg`/`.pdf` plots them.
Rounding is applied only when formatting the table. Full precision remains in JSON/CSV.

## Input dictionary

| Field | Meaning |
| --- | --- |
| `study_id`, `participant_id`, `session_id` | Stable identities; participants are paired within one study |
| `condition`, `cohort`, `domain` | Experimental condition and distinct design groups |
| `rounds` | In this example: individual committed offers from both actors, not human–agent cycles |
| `utility` | Selected normalized outcome measure in [0,1], or null when missing |
| `practice` | Excluded from main-condition inference |

Choose explicitly whether the intended outcome is raw agreement utility or the
game payoff. Failure/no agreement and missing/incomplete measurement are different
states. Never turn missing data into zero. The example rejects duplicated session
or participant-condition identities; it excludes the complete pair when either
required member is missing or fails the declared round criterion.

Cohorts and domains remain separate unless a protocol justifies a named domain
mapping. Inspect counts and exclusion reasons before any inference. Do not select a
significance test by searching for a favorable result. The paper's original decisions
and records are required to claim exact recomputation of its tables or figures.
The modern percentile bootstrap in the example is a separate declared analysis.

For utility analysis in both cohorts, exclude the entire participant pair if either
session has fewer than **two individual offers**. Two offers meet the threshold.
The author confirmed the same pair-level rule for NAO/Pepper and NAO/QT. This
filter does not automatically apply to questionnaire outcomes. The synthetic
recipe checks the rule; it does not establish the original exclusion counts.
