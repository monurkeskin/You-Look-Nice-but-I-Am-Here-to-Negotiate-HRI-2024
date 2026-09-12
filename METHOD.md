# Method and evidence

Associated paper: [You Look Nice, but I Am Here to Negotiate: The Influence of Robot Appearance on Negotiation Dynamics](https://doi.org/10.1145/3610978.3640759).

## Scientific contract

Solver-based negotiation with robot appearance varied separately in NAO/Pepper and NAO/QT cohorts.

Two fifteen-minute sessions with preference elicitation before each. Prior attitude is measured before the experiment; Godspeed and thermometer responses follow the specified interactions.

The machine-readable [paper map](paper-map.json) links selected manuscript labels,
source hashes and locations to implementation, independent tests, configurations
and result targets. Only the selected active LaTeX entry was used. Manuscript
working files, inactive drafts and reviewer correspondence are not redistributed.


## Unresolved domain assignment

The selected publication source is `LateReport.tex`. Its domain table and prose
are not identical: the table varies several issue values, while the prose describes
a narrower change. The supplied Holiday A/B templates make their choices visible;
they do not resolve the historical ambiguity. Published-protocol start remains
blocked on this evidence. NAO/Pepper and NAO/QT remain separate cohorts, and the
analysis does not silently equate their utility domains.

## Utility, targets and game scores

A bid always states the human share. Agent utility uses the complementary allocation.
Utility is computed at full precision; rendering multiplies by 100 for display.
A target score is distinct from a reservation constraint. In the fruit papers,
a human agreement below 40 points is permitted but earns zero game points;
raw utility and game payoff remain separate logged fields. The Jennifer papers'
30-point goal is not silently turned into a prohibition on lower agreements.
The short Solver and Appearance examples do not claim those fruit reward rules.

## Remaining evidence gaps

- Resolve prose versus table differences in Holiday A/B domains and recover exact session mapping.
- Original pre-study and per-session questionnaires, instructions and timing records.
- Permitted records with cohort, condition order, utility-scale comparability and inclusion rules.

Unknown inputs are not filled with simulated participants or invented historical
constants. The existing templates are inspectable, but their published-protocol
preflight prevents starting before required evidence is supplied and reviewed.
A custom study has its own declared configuration and cannot inherit a reproduction
claim merely by using the same strategy name.

## Relationship to the research series

NAO/Pepper and NAO/QT are independent cohorts. Equal software interfaces do not justify pooling their participants or domain utilities.

The common engine owns utility, lifecycle, logs, GUI, shared methods and device
contracts. This repository owns paper-specific profiles, protocol choices, analysis
rules, reproduction targets and tests. [framework.json](framework.json) pins the
engine; [NOTICE](NOTICE) preserves original source attribution.
