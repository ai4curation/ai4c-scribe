---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 680
agent: std_opencode_gpt55
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.737
precision: 0.7
recall: 0.778
jaccard: 0.583
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/680
-->

## Summary

The agent did the core reclassification of `GO:0061852` correctly, *replacing*
`is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor
complex` and updating the label and definition genus. It falls short of the gold only
on the new spelled-out EXACT synonym and the `#31935` `term_tracker_item`, plus a
demote-vs-delete difference on the long transporter synonym. The metadiff (`F1=0.737`,
`P=0.700`, `R=0.778`) somewhat *over*-penalizes: the residual differences are
provenance/synonym-cleanup convention, not an incorrect ontology edit. This diff is
byte-identical to attempt #679 (blob `49c53cf`).

## Strengths

- **Correct reclassification:** the transporter `is_a` was *replaced* by
  `is_a: GO:0062137 ! cargo receptor complex`, matching the gold PR and ValWood's
  GO:0038024-based rationale (cargo receptors transport by vesicular, not transmembrane,
  transport). This is the pivotal decision in the case.
- Primary label correctly changed to `retrograde cargo receptor complex, Golgi to ER`.
- Definition genus minimally edited to `Cargo receptor complex that recognizes...`.
- Preserved `relationship: capable_of_part_of GO:0006890` and the ERV41 evidence comment.
- Strong documented methodology: pre-validation `robot convert`, full `make travis_build`,
  term-search of GO:0061852/GO:0062137, design-pattern check, checkout/checkin workflow.

## Issues

- **Missed the new EXACT synonym (under_editing):** the gold added
  `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`;
  this attempt did not.
- **Missed the `#31935` provenance (under_editing):** no `term_tracker_item` for the
  current issue was added; the gold included it alongside the prior `#24444` link.
- **Synonym divergence (over_editing):** demoted the long transporter synonym EXACT→BROAD
  and added a short transporter BROAD synonym; the final gold *deleted* the long
  ER-spelled-out form (ValWood follow-up) rather than demoting it. The agent had no
  access to the second review round, so the BROAD demotion is a defensible single-pass
  choice but still differs from the merged PR.
- Minor: `recognized by COPI-coated` over-anglicizes the second clause vs the gold's
  retained British `recognised`; non-substantive.
