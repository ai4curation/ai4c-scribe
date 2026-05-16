---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 346
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.870
precision: 1.0
recall: 0.769
jaccard: 0.769
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly resolved the core of issue #31935: it *replaced* the asserted parent `GO:1990351 ! transporter complex` with `GO:0062137 ! cargo receptor complex`, renamed the primary label, performed a minimal genus-only definition edit, demoted the transporter labels to BROAD synonyms, and added the `#31935` `term_tracker_item`. The PR narrative shows strong methodology (explicit reasoning about why no logical definition is needed, citing the `GO:0062137` equivalence axiom). The metadiff (`F1=0.870`, `precision=1.000`, `recall=0.769`) materially *under*-represents quality: the recall gap is driven almost entirely by a clerical synonym duplication and by retaining a synonym the human only removed after a second review round.

## Strengths

- Correct reclassification: `is_a: GO:1990351 ! transporter complex` replaced by `is_a: GO:0062137 ! cargo receptor complex` — ontologically correct and matching the merged gold.
- Excellent methodology in the PR comment: explicitly reasons that `GO:0062137` already carries the equivalence axiom (`protein-containing complex ∩ capable_of cargo receptor activity ∩ part_of membrane`) and that adding a sibling intersection here would over-specify. This is exactly the right call and matches the human's restraint.
- Minimal genus-only definition edit (`Transporter complex that recognises` → `Cargo receptor complex that recognizes`), preserving the rest verbatim including the second British `recognised` — the closest possible match to the human's minimal edit.
- Primary label and `#31935` provenance match the gold; `capable_of_part_of GO:0006890` preserved; precision is a perfect 1.000.
- Cited the relevant `GO:0038024` comment distinguishing cargo receptors from transmembrane transporters as the biological rationale — well-grounded, not hand-waved.

## Issues

- **Clerical duplicate synonym**: the diff emits `synonym: "retrograde receptor complex, Golgi to endoplasmic reticulum" EXACT []` *twice* (once as a context line, once as an added line). This appears to be an obo-checkin reordering/duplication artifact rather than an intentional edit, but it is a real defect that should not have shipped and accounts for part of the recall penalty.
- Retained `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`, which the human deleted only after ValWood's follow-up review comment. In a single-iteration run with no access to that feedback this is defensible, mirroring the human's first commit.
- Net effect: every substantive ontological decision is correct; the recall=0.769 is mostly an artifact of the duplicate-line defect plus the post-review synonym, so the F1 understates the actual quality.
