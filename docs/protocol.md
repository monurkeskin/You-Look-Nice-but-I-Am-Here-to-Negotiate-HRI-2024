# Configure and conduct this protocol

Two fifteen-minute sessions with preference elicitation before each. Prior attitude is measured before the experiment; Godspeed and thermometer responses follow the specified interactions.

## First inspection

Run `negotiator gui`, open **New study**, import `configs/protocol-nao-pepper-nao-first.json`, and inspect
Study, Preferences, Sessions and Review. The conductor sees protocol readiness;
the participant sees only their own preferences, offers, timer and current phase.
Use pseudonymous participant IDs. The application serves the two views locally,
including separate monitors; it is not a remote Internet study service.

| Position | Condition | Role | Deadline | Following break |
| --- | --- | --- | --- | --- |
| 1 | NAO | main | 900 s | 0 s |
| 2 | Pepper | main | 900 s | 0 s |

Alternative order files are listed in [CONFIGURATIONS](../CONFIGURATIONS.md).
Where profiles change by position, changing condition order does not swap the
position-specific score table. Practice blocks remain attached to their main
condition. The break follows the preceding session's result and any scheduled
questionnaire. A restart conservatively restarts the full break and records this fact.

## Before using a published-protocol template

- Inspect the fixed-option choice in [METHOD](../METHOD.md#what-changes-between-sessions); only destinations change between sessions.
- Original pre-study and per-session questionnaires, instructions and timing records.
- Original cohort domain records are needed for historical equivalence, not to execute a new declared domain choice.

The templates contain hash-pinned scientific configuration and named evidence
requirements. Supply only validated local files and their SHA-256 for the appropriate
requirement. File integrity alone does not establish scientific or hardware validity.
Resolve the method/protocol choices and configure approved questionnaire wording and
timing before starting. [protocol-schedule.json](../protocol-schedule.json) records
what is known and unknown. Missing original questionnaire text is not replaced with
invented questions. Synthetic examples remain demonstrations.

The next configuration revision embeds two 256-outcome domains. Events,
Accommodation and Season stay fixed while Destination changes by session position.
Both cohorts use this declared maintained set; the unresolved table alternatives
are not silently assigned to a cohort. These revisions await a matching engine
release; the archived 2.0.0 configurations remain unchanged.

## During and after the session

Before **each** main session, ask the participant to rank every issue and every
value from most to least preferred. Confirm these rankings in Preferences; the
framework constructs and records both profiles using `rank-linear-paired-v1`.
Do not reuse the first session's ranking or substitute a generic XML weight table.
The agent's issue and value ranks use the paired transformation explained in
[METHOD](../METHOD.md#from-participant-rankings-to-paired-preferences).

Use **Start session** after preferences and required surveys. Follow the selected
turn protocol. Notifications and rejected offers do not create additional offers.
Duplicate or delayed commands must refer to the same session and displayed offer.
The application records agreement, deadline, withdrawal, interruption and operator
termination distinctly. A recording failure requires conductor attention before
continuing; restarting an interrupted session does not invent elapsed time.

After completion use **Build report**, or run `negotiator report PATH --output NEW_DIR`.
Keep original records and the generated report together, and export citations using
`negotiator cite PATH --format bibtex`. [Analysis guide](analysis.md).

## Materials for a new session

Each protocol requirement names its purpose. `execution` requirements cover the
model, instruments and presentation materials needed to run the configured study.
Their availability and hashes are checked before a session starts.
`historical-analysis` requirements describe evidence needed to assess the original
experiment; unavailable participant records do not prevent a new session.

This separation does not establish equivalence with the historical experiment.
A demonstration remains synthetic, and a missing runtime asset still blocks a
published-protocol run. Inspect historical requirements separately with
`protocol_readiness(spec, operation="historical-analysis")`.
