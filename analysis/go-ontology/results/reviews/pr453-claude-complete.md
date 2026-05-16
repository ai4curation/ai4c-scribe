---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 453
agent: std_claude_son45
model: claude-sonnet-4.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/453
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent produced a biologically and procedurally correct obsoletion of `GO:0018581` and rename of `GO:0047074` in `go-edit.obo`, but did not perform the generated-import cleanup that the human PR included. The single `go-edit.obo` stanza changes are essentially identical to the gold PR; the only substantive omission is the removal of the `GO:0018581` participant axioms from `imports/go-catalytic-activities-participants.owl`. F1 0.667 under-represents the quality of the core curation work — the missing piece is one derived-artifact edit, not a curation error. (Eval base already includes companion PR #25904, so the metadiff vs #32008 is a fair reference; this is not a partial-gold case.)

## Strengths

- Correct, skill-conformant obsoletion of `GO:0018581`: name prefixed `obsolete`, `OBSOLETE.` definition, all four xrefs (`EC:1.13.11.37`, `MetaCyc:RXN-17556`, `RHEA:19441`, `UM-BBD_reactionID:r0232`) and the `is_a: GO:0016702` parent removed, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to the EC accepted name `hydroxyquinol 1,2-dioxygenase activity` and added the prior label as an EXACT synonym — matching the human PR exactly.
- Detailed, accurate obsoletion comment that explicitly describes the non-enzymatic second step (3-hydroxy-cis,cis-muconate → maleylacetate) — the most thorough rationale of any attempt and closest in substance to the human's comment.
- Strong methodology evidence: PR comment documents impact analysis (zero annotations, no internal references), term-obsoletion skill checklist, and obo-checkout/checkin workflow. Tightly scoped to the two relevant terms.

## Issues

- Omission: did not remove the obsolete `GO:0018581` `owl:Class` participant block (four `RO:0000057` restrictions to CHEBI_15378/15379/16971/58139) from `src/ontology/imports/go-catalytic-activities-participants.owl`. The human PR removed these so the reasoner does not infer participant superclasses on an obsolete term; the term-obsoletion skill's "original axioms transferred/cleaned as appropriate" guidance covers this. This is the sole reason for the recall gap vs the gold PR.
- The PR comment claims "Only src/ontology/go-edit.obo modified (correct)" — an explicit but incorrect conclusion that the import file did not need cleanup, indicating the agent reasoned about and then dismissed the step rather than overlooking it.
