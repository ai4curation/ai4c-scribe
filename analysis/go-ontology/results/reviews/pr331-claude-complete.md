---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 331
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.667
precision: 0.519
recall: 0.933
jaccard: 0.5
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/331
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent produced a clean, correct obsoletion of `GO:0018581` and rename of `GO:0047074` in `go-edit.obo`, identical in substance to the gold PR's `go-edit.obo` changes, but did not remove the obsolete term's participant axioms from the generated OWL import. The `go-edit.obo` diff is effectively a line-for-line match to the human PR; the only substantive shortfall is the missing `imports/go-catalytic-activities-participants.owl` cleanup. F1 0.667 understates the curation quality — the single missing piece is one derived-artifact edit. (Eval base already incorporates companion PR #25904, so the metadiff vs #32008 is a fair reference; not a partial-gold case.)

## Strengths

- Skill-perfect obsoletion of `GO:0018581`: `obsolete `-prefixed name, `OBSOLETE.` definition, all four xrefs and the `is_a: GO:0016702` parent stripped, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity` with `4-hydroxycatechol 1,2-dioxygenase activity` preserved as an EXACT synonym — matching the human PR exactly; correctly noted that `hydroxyquinol` and `4-hydroxycatechol` are both names for benzene-1,2,4-triol.
- Excellent, precise obsoletion comment citing the non-enzymatic second step, RHEA:35595, and the EC equivalence — among the best rationales of any attempt.
- Best-documented methodology of the set: PR comment grounds the decision in the specific issue directives (sjm41, raymond91125), and reports concrete validation evidence — `robot convert` clean, `robot verify` 16/16 SPARQL-QC rules passing, ELK reasoning with no unsatisfiable classes — and honestly flags that full `make travis_build` could not run because `amm` was unavailable.

## Issues

- Omission: did not delete the `GO:0018581` `owl:Class` block (four `RO:0000057` participant restrictions to CHEBI_15378/15379/16971/58139) from `src/ontology/imports/go-catalytic-activities-participants.owl`. The human PR removed these to prevent participant-restriction inference on an obsolete class; this is the entire source of the recall gap and the difference between this attempt and the top-scoring #545.
- Because the agent ran a reasoner but only over `go-edit.obo`, it did not detect the stale obsolete-term axioms living in the generated import artifact — a blind spot in the validation scope rather than a curation error.
