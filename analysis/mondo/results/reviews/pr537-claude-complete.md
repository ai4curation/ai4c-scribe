---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 537
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.935
precision: 0.906
recall: 0.967
jaccard: 0.879
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-sonnet-4.5 / copilot correctly merged MONDO:0034186 into MONDO:0029144
with a canonical obsolete stanza and full annotation transfer. The diff (blob
`36025e7`) is almost identical to the top tier, with one substantive difference:
the transferred autosomal-recessive characteristic was written as
`relationship: has_characteristic HP:0000007 {source="Orphanet:562538"}` —
i.e. the agent added an explicit `Orphanet:562538` source axiom annotation,
whereas both the gold PR and the source term carried this relationship with no
source. The added provenance is arguably *more* correct (Orphanet:562538 is the
true origin of the autosomal-recessive assertion on the merged term), but it
diverges from gold and lowers precision. Metadiff F1=0.935 modestly
**under-represents** quality.

## Strengths

- Correct, complete merge; canonical obsoletion metadata
  (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`, `is_obsolete`, #9842
  tracker item).
- Full annotation transfer (6 subsets, GARD/Orphanet xrefs, `MONDO:0019222`
  parent, autosomal-recessive characteristic) with the transferred synonym
  correctly re-cited to `[Orphanet:562538]`.
- Conservatively kept `is_a: MONDO:0003847 ! hereditary disease` (matches gold).
- Removed obsoletion-scheduling artifacts (`obsoletion_candidate`,
  `IAO:0006012`).

## Issues

- Style/scope: added `{source="Orphanet:562538"}` to the `has_characteristic
  HP:0000007` axiom. This is a defensible (arguably better-provenanced) choice
  but diverges from the gold and the unsourced source-term form; in a tight
  merge PR the conservative form would match the human.
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn (left in
  place). Not an error.
- No substantive errors.
