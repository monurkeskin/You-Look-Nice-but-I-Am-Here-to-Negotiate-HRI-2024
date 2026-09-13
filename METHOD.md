# Method and evidence

Associated paper: [You Look Nice, but I Am Here to Negotiate: The Influence of Robot Appearance on Negotiation Dynamics](https://doi.org/10.1145/3610978.3640759).

## Scientific contract

Solver-based negotiation with robot appearance varied separately in NAO/Pepper and NAO/QT cohorts.

Two fifteen-minute sessions with preference elicitation before each. Prior attitude is measured before the experiment; Godspeed and thermometer responses follow the specified interactions.

The machine-readable [paper map](paper-map.json) links selected manuscript labels,
source hashes and locations to implementation, independent tests, configurations
and result targets. Only the selected active LaTeX entry was used. Manuscript
working files, inactive drafts and reviewer correspondence are not redistributed.


## What changes between sessions

The author confirmed on 13 September 2026 that **only Destination changes**.
Protocol revision 3 in release 2.1.0 keeps Events, Accommodation and Season
fixed. The first destinations are Barcelona, Rome, London and Boston; the second
are Venice, Lisbon, Sydney and Miami. Robot order changes which robot presents
each session, not this position-specific domain sequence.

The maintained fixed set uses the first alternatives in `tab:holiday_values`:
Hotel/Caravan/House/Boat; Shopping/Museum/Sports/Show; Summer/Winter/Spring/Fall.
The table also lists Duration and other accommodation alternatives. Their exact
historical assignment to cohorts is not recovered. The fixed-option selection
is an explicit maintenance choice, not evidence of identical original stimuli.
Each domain has 256 outcomes. The engine's generic Holiday A/B assets remain
separate; these paper configurations embed their own domains.

Historical domain evidence is required for a historical equivalence claim.
Original questionnaire and instruction requirements still block published-protocol
preparation. These configurations are included in release 2.1.0; the archived
2.0.0 artifact is unchanged. NAO/Pepper and NAO/QT remain separate cohorts.

## From participant rankings to paired preferences

The participant ranks issues and their values from most to least preferred before
**each** session. The maintainer confirmed this workflow on 13 September 2026.
The historical elicitation function converts the four issue ranks to human weights
`0.4, 0.3, 0.2, 0.1`; adjacent rank pairs are exchanged for agent weights
`0.3, 0.4, 0.1, 0.2`. Within each issue, human value scores are
`1, 0.75, 0.5, 0.25` and agent scores are `0.5, 0.25, 1, 0.75` in the same
human-ranked order. The maintained conversion is `rank-linear-paired-v1`.

The general Holiday XML templates also contain `0.48, 0.32, 0.16, 0.04` weights.
Those templates are distinct from the participant profiles written by elicitation.
Using the elicited profiles follows the author-confirmed workflow and source;
it is not a recovered set of original participant records. Rank permutations relabel
the four-by-four utility space under this construction. They do not prove maximal
opposition, equivalent participant experiences or permission to pool cohorts.

A Holiday offer selects one common value per issue. Both parties evaluate that
same deal through their own profiles; there is no fruit-allocation complement.
Utilities retain full precision. No fruit-study target or zero-payoff rule is assumed.
An independent four-rank oracle checks every outcome in
[test_ranked_profiles.py](tests/test_ranked_profiles.py).

## Remaining evidence gaps

- Recover the exact historical fixed issue/value set by cohort; destination-only session changes are confirmed.
- Original pre-study and per-session questionnaires, instructions and timing records.
- Permitted records with cohort, condition order, utility-scale comparability and inclusion rules.

Unknown inputs are not filled with simulated participants or invented historical
constants. The templates are inspectable; preparation requires execution evidence,
while historical equivalence additionally needs the historical records listed above.
A custom study has its own declared configuration and cannot inherit a reproduction
claim merely by using the same strategy name.

## Utility inclusion in both studies

Study I reports 55 participants and 52 included in utility analysis, with a minimum
of two bids. The author confirmed that an insufficient session excludes **both
sessions of that participant**. The maintained analysis for both cohorts counts individual
committed offers from either actor; acceptance and notifications add no offers.
Both sessions must have at least two. This filter concerns utility analysis,
not automatically the questionnaire samples or every measure in the paper.

The author also confirmed that Study II used the same two-offer, pair-level rule.
The synthetic paired-analysis recipe tests the boundary for each cohort separately.
The example's bootstrap is not a reconstruction of the paper's t-tests or signed-rank
tests. The original exclusion ledger remains necessary to verify historical counts.

## Relationship to the research series

NAO/Pepper and NAO/QT are independent cohorts. Equal software interfaces do not justify pooling their participants or domain utilities.

The common engine owns utility, lifecycle, logs, GUI, shared methods and device
contracts. This repository owns paper-specific profiles, protocol choices, analysis
rules, reproduction targets and tests. [framework.json](framework.json) pins the
engine; [NOTICE](NOTICE) preserves original source attribution.
