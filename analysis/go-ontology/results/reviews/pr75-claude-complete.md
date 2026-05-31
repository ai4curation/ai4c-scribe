---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 75
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.857
precision: 0.9
recall: 0.818
jaccard: 0.75
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt produced a diff byte-identical to attempt #95 (same blob `04afd40`, same `gpt-5.5`/`opencode` agent). The agent correctly *replaced* `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`, renamed the primary label, demoted the transporter labels to BROAD, added the EXACT spelled-out cargo-receptor synonym, and added the `#31935` `term_tracker_item`. The metadiff (`F1=0.857`, `precision=0.900`, `recall=0.818`) is a fair signal: ontologically correct, with a more extensive definition rewrite than the minimal genus edit the curator specified.

## Strengths

- Correct ontological move: parent *replaced*, not duplicated — `is_a: GO:0062137 ! cargo receptor complex` only, matching the merged gold.
- Primary label change matches the gold and the requester's explicit ask.
- Old primary label correctly demoted to `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`, honoring ValWood's "not restricted to cargo" instruction.
- Added `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`, matching the human PR.
- Preserved `capable_of_part_of GO:0006890`; no logical-definition over-specification.

## Issues

- **Definition over-rewrite** (identical to #95): rewrote the whole first sentence to `A cargo receptor complex that recognizes and binds ... and returns them to the ER` plus `recognised` → `recognized`, where the issue and human PR changed only the genus phrase. Valid but beyond the requested minimal edit; the leading indefinite article deviates from GO definition style.
- Retained `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`, which the human removed after a follow-up review round. Defensible for a single-iteration run.
- Reproducibility note: identical output to #95 confirms the deviation is a stable behavior of this agent/model rather than sampling noise. Net substance is correct; partial_success reflects definitional scope drift only.
