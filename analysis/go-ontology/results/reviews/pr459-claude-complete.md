---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 459
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.800
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: partial_success
failure_modes: [over_editing, under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly *replaced* `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`, renamed the primary label, demoted both transporter labels to BROAD, and added the `#31935` `term_tracker_item`. The ontological core is right. The metadiff (`F1=0.800`, balanced `precision=recall=0.800`) is a fair signal: one over-edit (Americanizing the second `recognised`) and one omission (the new spelled-out cargo-receptor EXACT synonym the human added).

## Strengths

- Correct reclassification: parent *replaced*, not duplicated — `is_a: GO:0062137 ! cargo receptor complex` only. Biologically correct and matching the merged gold.
- Primary label change matches the gold and the requester's ask.
- Old primary label correctly demoted to `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`.
- Definition genus minimally rephrased (`Transporter complex that recognises` → `Cargo receptor complex that recognizes`) rather than fully rewritten — closer to the curator's intent than the gpt-5.5/opencode rewrites.
- Preserved `capable_of_part_of GO:0006890`; no logical-definition over-specification; added the `#31935` provenance.

## Issues

- **Over-edit**: also changed the second-sentence British spelling `recognised` → `recognized` ("HDEL motif recognized by COPI-coated vesicles"). The human PR deliberately left that second `recognised` British. A harmless, defensible normalization but a real precision delta versus the gold and not requested.
- **Omission (under_editing)**: did not add `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`, the new spelled-out synonym for the new primary label that the human PR added. This is the recall gap.
- Retained `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`, which the human removed only after a follow-up review round — defensible for a single-iteration run.
- Net: ontology fully correct; F1=0.800 fairly reflects the missing new synonym and the extra spelling normalization, neither of which is an ontological error.
