---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 206
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.824
precision: 0.7
recall: 1.0
jaccard: 0.7
outcome: partial_success
failure_modes: [wrong_pattern, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent renamed the term, refined the definition genus, added the new BROAD transporter synonym, and added the `#31935` `term_tracker_item` — but it **added** `is_a: GO:0062137 ! cargo receptor complex` while **retaining** `is_a: GO:1990351 ! transporter complex`, producing a dual-parent classification. The issue was a *reclassification* ("Missing parent" + demote the transporter wording because it is "not restricted to cargo"), and the merged human PR *replaced* the transporter parent. The metadiff (`F1=0.824`, `precision=0.700`, `recall=1.000`) is roughly fair but the recall=1.000 is misleading: it captured all human-added lines yet introduced an incorrect retained parent that the line-diff treats as an unchanged context line rather than an error.

## Strengths

- Primary label change to `retrograde cargo receptor complex, Golgi to ER` matches the gold and the requester's ask.
- Definition genus minimally edited (`Transporter complex that recognises` → `Cargo receptor complex that recognizes`), preserving the rest including the second British `recognised` — closest to the human's minimal edit.
- Added `synonym: "retrograde transporter complex, Golgi to ER" BROAD []` (old primary label demoted), honoring ValWood's instruction.
- Added the `#31935` `term_tracker_item`; preserved `capable_of_part_of GO:0006890`; recall=1.000 confirms it captured every change the human made.

## Issues

- **Classification error (wrong_pattern)**: kept `is_a: GO:1990351 ! transporter complex` *in addition to* the new `is_a: GO:0062137 ! cargo receptor complex`. This is the central defect. The issue title is "Missing *parent*" but the requester explicitly wanted the transporter label demoted to a broad synonym because the term is not a generic transporter; the human PR removed the transporter parent entirely. Cargo receptor complex is not subsumed by transporter complex (cf. `GO:0038024`: cargo receptors transport by vesicular, not transmembrane, transport), so asserting both is ontologically incorrect, not merely redundant. The PR comment's claim that the term "functions ... in addition to its role as a transporter complex" misreads the biology the issue corrected.
- **Did not demote the spelled-out transporter synonym**: left `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" EXACT []` at EXACT scope. The human demoted it to BROAD (and ultimately removed it). Keeping a transporter-wording synonym at EXACT against the new cargo-receptor primary label is inconsistent.
- **Missing the new spelled-out synonym**: did not add `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []` that the human PR added for the new label.
- Net: the lexical edits are good but the reclassification — the actual point of the issue — was implemented as an addition rather than a replacement, which is the most consequential error among all attempts. The precision=0.700 correctly flags the divergence, but the failure is qualitative (wrong classification semantics), not just over-editing.
