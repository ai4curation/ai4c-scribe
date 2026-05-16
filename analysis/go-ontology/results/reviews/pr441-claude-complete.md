---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 441
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- wrong_pattern
case_quality: poor
case_quality_reason: gold_pr_partial_and_metadiff_blind_to_created_by
companion_prs:
- 32032
- 32014
scoring_caveat: "Metadiff ignores created_by, so F1=0.0 is mechanical even though this attempt reproduces gold PR #32028 byte-for-byte. Final-correct is bare vw (#32032)."
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

This attempt is identical to eval PR #451 (same agent slug, same blob `eaa8ef4`, same diff) and **reproduces the selected gold PR #32028 byte-for-byte**: `created_by: PomBase:vw` → `created_by: GOC:vw` on exactly the three human-touched terms (GO:0180067, GO:0180068 `negative regulation of carbohydrate utilization`, GO:0180069), with no other changes. F1=0.0 is solely an artifact of metadiff ignoring `created_by`; against the selected gold this is a near-perfect line match. It is partial success in the broader sense only because the gold PR itself used the interim-wrong `GOC:vw` that pgaudet corrected to bare `vw` (companion PR #32032).

## Strengths

- **Exact reproduction of the human gold PR #32028**: correct three terms, correct `GOC:vw` change, zero extraneous edits — maximally scope-disciplined.
- Located GO:0180068 `negative regulation of carbohydrate utilization` despite it belonging to a different issue (#31261), indicating a file-wide `grep PomBase:vw` strategy that mirrors the human curator's and is the correct methodology for a malformed-metadata cleanup.
- No label/synonym/definition churn — appropriately treated the `created_by` fix as the whole scope, exactly as gold PR #32028 did (the label swap went to separate PR #32014).

## Issues

- **Wrong final convention (`wrong_pattern`)**: `GOC:vw` rather than the final-correct bare `vw` (pgaudet, #32032). This is inherited from the flawed instruction/gold, not an independent reasoning error.
- Does not perform the label↔synonym swap discussed in the issue thread; defensible since the gold PR #32028 also did not (that work was the separate PR #32014).
- This run is a duplicate of #451; it provides no additional signal beyond confirming reproducibility of the gold-matching behavior for this agent (copilot / claude-sonnet-4.5).
- F1=0.0 is misleading: this is among the two best line-level matches to the selected gold PR, scored zero only because metadiff drops `created_by`.
