---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 586
agent: std_opencode_g55
model: gpt-5.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/586
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent produced a skill-conformant obsoletion of `GO:0018581` and rename of
`GO:0047074`, and — unlike most attempts — did perform the
`go-catalytic-activities-participants.owl` participant-axiom cleanup that the
human PR considered essential to avoid the reasoner inferring restrictions on an
obsolete class. The two substantive deviations from gold are an omission (no
EXACT synonym added to `GO:0047074`, so the historical label is lost) and an
over-edit (it also rewrote the parallel generated `.obo` import and trimmed
trailing blank lines in both generated artifacts). F1 0.893 is a fair reflection
of quality here: the eval base already incorporates companion PR #25904, so
metadiff vs #32008 alone is a sound reference and this is not a partial-gold
case.

## Strengths

- Correct, complete obsoletion of `GO:0018581`: `obsolete `-prefixed name,
  `OBSOLETE.` definition, all four xrefs (`EC:1.13.11.37`, `MetaCyc:RXN-17556`,
  `RHEA:19441`, `UM-BBD_reactionID:r0232`) and the asserted parent
  `is_a: GO:0016702` removed, `is_obsolete: true`, `replaced_by: GO:0047074`,
  both `term_tracker_item` provenance properties retained — exactly matching the
  gold stanza.
- Renamed `GO:0047074` to the EC:1.13.11.37 accepted label
  `hydroxyquinol 1,2-dioxygenase activity`, the rename explicitly requested by
  curator @raymond91125 on the issue thread.
- Performed the generated-import cleanup the gold PR author flagged as
  necessary: removed the four-restriction `GO_0018581` `owl:Class` participant
  block (`RO:0000057` to CHEBI:15378/15379/16971/58139) from
  `go-catalytic-activities-participants.owl`. Only the strongest attempts did
  this.

## Issues

- Omission: did not add `synonym: "4-hydroxycatechol 1,2-dioxygenase activity"
  EXACT []` to `GO:0047074`. The gold PR preserves the prior label as an EXACT
  synonym so the previous name remains findable; dropping it silently discards
  curatorial history (`missed_requirement`). This is the main correctness gap
  versus gold.
- Over-edit: also modified the parallel generated
  `go-catalytic-activities-participants.obo` and removed trailing blank lines in
  both generated artifacts. These files are derived; the edits are internally
  consistent and harmless but broader than the human PR's single `.owl` change,
  and lower metadiff recall without improving correctness.
- The obsoletion comment ("equivalent to GO:0047074 hydroxyquinol
  1,2-dioxygenase activity") is terser than the human's, which spells out the
  non-enzymatic second step. Acceptable but less informative provenance (style).
