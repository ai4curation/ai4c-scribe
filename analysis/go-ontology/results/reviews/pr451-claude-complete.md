---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 451
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

This attempt **reproduces the selected gold PR #32028 essentially byte-for-byte**: it changes `created_by: PomBase:vw` → `created_by: GOC:vw` on exactly the three terms the human touched — GO:0180067, GO:0180068 (`negative regulation of carbohydrate utilization`), and GO:0180069 — and makes no other edits. Its blob hash `eaa8ef4` is the same as the gold PR's target tree (`eaa8ef407`). The F1=0.0 is purely an artifact of the metadiff configuration ignoring `created_by`; by line-match against the selected gold this attempt is effectively perfect. It is only a partial success in the broader sense because the gold PR itself encoded the interim-wrong `GOC:vw` convention that pgaudet immediately corrected to bare `vw` (companion PR #32032).

## Strengths

- **Exactly matches the human gold PR #32028**: same three terms, same `PomBase:vw` → `GOC:vw` change, no extraneous edits. This is the tightest, most scope-disciplined attempt of all nine.
- Correctly located GO:0180068 `negative regulation of carbohydrate utilization` — the term that is *not* a terreic-acid term and whose `term_tracker_item` points to issue #31261 — implying the agent used a file-wide `grep PomBase:vw` strategy identical to the human curator's, rather than reasoning only from the terreic-acid terms named in issue #31114. This is the correct methodology for a "fix this malformed metadata value" task and explains why it caught the term every other attempt missed.
- No label/synonym/definition churn: it treated the immediate ask (the `created_by` fix requested in the issue comment) as the scope, which is exactly what gold PR #32028 did.

## Issues

- **Wrong final convention (`wrong_pattern`)**: like the gold PR it reproduces, it uses `GOC:vw`. The truly-correct value is bare `vw` (pgaudet, #32032). This is inherited from the (flawed) instruction/gold rather than an independent error — the agent faithfully executed the stated request.
- It did not perform the label↔synonym swap that was also discussed in the issue thread. Given the gold PR #32028 likewise scoped itself to only the `created_by` fix (the swap went to the separate PR #32014), this is a defensible scope choice, not an omission.
- F1=0.0 is entirely misleading here: this is the single best line-level match to the selected gold PR among all attempts, scored zero solely because metadiff drops `created_by`.
