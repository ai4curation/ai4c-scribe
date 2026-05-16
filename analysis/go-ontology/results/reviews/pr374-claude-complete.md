---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 374
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.651
precision: 0.519
recall: 0.875
jaccard: 0.483
outcome: partial_success
failure_modes:
- under_editing
- over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/374
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent correctly obsoleted `GO:0018581` and renamed `GO:0047074` with the prior label preserved as an EXACT synonym, but it both missed the generated OWL import cleanup (under-editing) and added an extra `RELATED` synonym to `GO:0047074` that was not requested and that the issue history had deliberately removed (over-editing). The core obsoletion is sound; the metadiff F1 0.651 is roughly fair here because the recall loss reflects a genuine extra edit on top of the missing import cleanup. (Eval base already incorporates companion PR #25904; metadiff vs #32008 is a fair reference, not a partial-gold case.)

## Strengths

- Correct obsoletion of `GO:0018581`: `obsolete `-prefixed name, `OBSOLETE.` definition, all four xrefs and `is_a: GO:0016702` removed, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity` and added `4-hydroxycatechol 1,2-dioxygenase activity` as an EXACT synonym — matching the human PR.
- Accurate obsoletion comment identifying the sub-reaction/complete-reaction (RHEA:35595) distinction.

## Issues

- Over-editing: added `synonym: "benzene-1,2,4-triol:oxygen 1,2-oxidoreductase (decyclizing)" RELATED []` to `GO:0047074`. This is the IUBMB systematic name and was an EC:1.13.11.37-attributed synonym that companion PR #25904 had explicitly removed from `GO:0018581`; re-introducing it here (unattributed, no xref) was not requested by the issue or the directive comments and reduces precision. Defensible at best, but it reverses a prior deliberate cleanup and should be curator-reviewed.
- Omission: did not remove the `GO:0018581` participant `owl:Class` block from `src/ontology/imports/go-catalytic-activities-participants.owl`, the cleanup the human PR performed to avoid obsolete-term reasoning artifacts.
- Methodology is the least documented of the claude-family attempts — the PR/issue comments give a high-level summary with no validation evidence or impact-analysis trail.
