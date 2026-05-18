---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 596
agent: std_opencode_gpt55
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.8
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/596
-->

## Summary

This is the strongest attempt in the gap-fill set. The agent *replaced*
`is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor
complex`, renamed the label, refined the definition genus *while correctly keeping the
British "recognises"* in both the genus and second clause (closest match to the gold's
minimal edit), and — uniquely among these seven — added the new spelled-out EXACT
synonym `retrograde cargo receptor complex, Golgi to endoplasmic reticulum`. The
metadiff (`F1=0.800`, `P=0.800`, `R=0.800`) slightly *under*-represents quality: the
only gold-relevant gap is the omitted `#31935` `term_tracker_item`; the remaining delta
is the demote-vs-delete synonym convention the agent could not have known without the
post-PR review round.

## Strengths

- **Correct reclassification:** transporter `is_a` *replaced* by
  `is_a: GO:0062137 ! cargo receptor complex`, matching the gold and ValWood's
  GO:0038024-based rationale.
- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`.
- **Added the new EXACT synonym** `retrograde cargo receptor complex, Golgi to
  endoplasmic reticulum`, exactly matching the gold PR's new synonym — the only attempt
  in this set to do so.
- Definition genus updated to `Cargo receptor complex that recognises...` *preserving
  British spelling throughout* — the cleanest minimal genus-only edit here, matching the
  gold's intent (the gold itself only switched the genus word).
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence comment.

## Issues

- **Missed the `#31935` provenance (under_editing):** the gold added a
  `term_tracker_item ".../issues/31935"` alongside the prior `#24444`; this attempt did
  not. This is the single substantive gap from the merged PR.
- **Synonym divergence (over_editing):** demoted the long transporter synonym EXACT→BROAD
  and added a short transporter BROAD synonym. The final gold *deleted* the long
  ER-spelled-out transporter synonym (ValWood follow-up comment) rather than demoting
  it; the agent ran one iteration without that feedback, so this is a defensible
  single-pass choice, not an error.
- No reclassification, scope, or syntax problems otherwise; methodology well documented.
