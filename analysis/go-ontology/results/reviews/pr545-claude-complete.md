---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 545
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.881
precision: 0.963
recall: 0.812
jaccard: 0.788
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/545
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This is the strongest of the seven attempts and the only one that fully reproduced the human resolution, including the generated-import cleanup. The agent obsoleted `GO:0018581` per the term-obsoletion skill (name prefixed `obsolete`, `OBSOLETE.` definition, comment, all xrefs and the `is_a: GO:0016702` stripped, `is_obsolete: true`, `replaced_by: GO:0047074`), renamed `GO:0047074` to the EC accepted label `hydroxyquinol 1,2-dioxygenase activity` with the prior label kept as an EXACT synonym, and removed the obsolete term's `RO:0000057` participant axioms from `imports/go-catalytic-activities-participants.owl` — the step every other attempt missed. F1 0.881 slightly under-represents quality: the recall gap is driven by defensible/neutral extras, not omissions. Note the eval base already incorporates companion PR #25904 (the earlier checklist of EC-qualifier/synonym/def fixes), so the metadiff against #32008 alone is a fair reference here and this is not a partial-gold case.

## Strengths

- Complete obsoletion of `GO:0018581` exactly matching the skill exemplar and the human PR: removed `EC:1.13.11.37`, `MetaCyc:RXN-17556`, `RHEA:19441`, `UM-BBD_reactionID:r0232`, and the asserted parent `GO:0016702`; added `is_obsolete: true` and `replaced_by: GO:0047074`; retained both `term_tracker_item` properties for provenance.
- Renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity` and preserved `4-hydroxycatechol 1,2-dioxygenase activity` as an EXACT synonym — fully consistent with the human PR.
- Uniquely performed the "transfer/cleanup of original axioms" the skill requires: deleted the 31-line `GO_0018581` participant `owl:Class` block from `go-catalytic-activities-participants.owl`, preventing the reasoner from inferring participant restrictions on an obsolete class (the exact rationale the human PR author gave in the issue thread).

## Issues

- Added `{source="skos:narrowMatch"}` to `MetaCyc:RXN-10137` on `GO:0047074`. The human PR did not touch this xref; the qualifier is arguably reasonable (RXN-10137 is the complete reaction) but is an unrequested mapping assertion and should be curator-reviewed (defensible over-edit, low risk).
- Also edited the parallel `go-catalytic-activities-participants.obo` variant and trimmed trailing blank lines in the generated artifacts. These are generated/derived files; the change is internally consistent and harmless but is broader than the human PR's single `.owl` edit (style difference, lowers metadiff recall without harming correctness).
- The obsoletion comment ("represents a sub-reaction of hydroxyquinol 1,2-dioxygenase activity") is terser than the human's, which spells out the non-enzymatic second step and the equivalence to `GO:0047074`. Acceptable but less informative provenance.
