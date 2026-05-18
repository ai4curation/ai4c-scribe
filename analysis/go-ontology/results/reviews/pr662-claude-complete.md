---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 662
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.893
precision: 0.926
recall: 0.862
jaccard: 0.806
outcome: partial_success
failure_modes:
- missed_requirement
- over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/662
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

Functionally equivalent to attempt #586 (same opencode runtime, gpt-5.4): a
correct skill-conformant obsoletion of `GO:0018581`, the requested rename of
`GO:0047074`, and — notably — the `go-catalytic-activities-participants.owl`
participant-axiom cleanup that most attempts missed. It carries the same two
deviations from gold: it omits the EXACT synonym on `GO:0047074` (losing the
historical label) and over-edits the parallel generated `.obo` import plus
trailing blank lines. F1 0.893 is a fair reflection of quality; the eval base
already includes companion PR #25904, so metadiff vs #32008 is a sound reference
and this is not a partial-gold case.

## Strengths

- Correct, complete obsoletion of `GO:0018581`: `obsolete `-prefixed name,
  `OBSOLETE.` definition, all four xrefs (`EC:1.13.11.37`, `MetaCyc:RXN-17556`,
  `RHEA:19441`, `UM-BBD_reactionID:r0232`) and `is_a: GO:0016702` removed,
  `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item`
  properties retained — matching the gold stanza.
- Renamed `GO:0047074` to the EC:1.13.11.37 accepted label
  `hydroxyquinol 1,2-dioxygenase activity`, the rename curator @raymond91125
  explicitly requested on the issue thread.
- Performed the generated-import cleanup the gold PR author flagged as needed:
  removed the four-restriction `GO_0018581` `owl:Class` participant block
  (`RO:0000057` to CHEBI:15378/15379/16971/58139) from
  `go-catalytic-activities-participants.owl`, preventing reasoning artifacts on
  the obsolete class.
- Obsoletion comment is slightly more informative than #586's — it states the
  term "represents a sub-reaction of GO:0047074 and is replaced by the full
  EC:1.13.11.37 reaction term," closer to the human's rationale.

## Issues

- Omission: did not add `synonym: "4-hydroxycatechol 1,2-dioxygenase activity"
  EXACT []` to `GO:0047074`. The gold PR keeps the prior label as an EXACT
  synonym so the old name stays findable; silently dropping it discards
  curatorial history (`missed_requirement`) — the main correctness gap vs gold.
- Over-edit: also modified the parallel generated
  `go-catalytic-activities-participants.obo` and removed trailing blank lines in
  both generated artifacts. Derived files; internally consistent and harmless
  but broader than the human PR's single `.owl` change, lowering metadiff recall
  without improving correctness.
