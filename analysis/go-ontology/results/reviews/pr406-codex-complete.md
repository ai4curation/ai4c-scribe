---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 406
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.634
precision: 0.481
recall: 0.929
jaccard: 0.464
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/406
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 25870 --repo geneontology/go-ontology
    gh pr diff 32008 --repo geneontology/go-ontology
    gh pr diff 406 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:0018581` and renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity`, but it missed two pieces of the accepted PR: preserving the old `GO:0047074` label as an exact synonym and removing `GO:0018581` reaction-participant axioms from the generated OWL import. The biological direction is right, but the patch is incomplete.


## Strengths

- Correctly made `GO:0018581` obsolete with `is_obsolete: true` and `replaced_by: GO:0047074`.
- Correctly removed active xrefs and parentage from `GO:0018581`.
- Correctly renamed `GO:0047074` to the EC accepted name.
- The obsoletion comment identifies the sub-reaction vs complete-reaction rationale.
- No unrelated terms were changed in the main edit file.


## Issues

- Did not add `synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []` to `GO:0047074`, so the former label is not preserved for searchability.
- Did not remove the obsolete `GO:0018581` participant axioms from `imports/go-catalytic-activities-participants.owl`.
- The obsoletion comment is less detailed than the human PR's rationale about the non-enzymatic second step.
