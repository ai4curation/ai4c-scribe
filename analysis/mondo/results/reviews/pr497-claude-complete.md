---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 497
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

A second claude-sonnet-4.5 / copilot run; the diff is byte-identical to attempt
#537 (blob `36025e7`), confirming the runtime's behavior is stable here. The
agent correctly merged MONDO:0034186 into MONDO:0029144 with a canonical
obsolete stanza and full annotation transfer. The only divergence from the top
tier is the explicit `{source="Orphanet:562538"}` provenance added to the
transferred `has_characteristic HP:0000007` axiom (gold and source term carried
it unsourced) — a defensible, arguably better-provenanced choice that lowers
precision against gold. Metadiff F1=0.935 modestly **under-represents** quality.

## Strengths

- Reproducible: identical to #537, indicating stable behavior on this merge.
- Correct, complete merge with canonical obsoletion metadata
  (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`, `is_obsolete`, #9842
  tracker item).
- Full annotation transfer with the transferred synonym correctly re-cited to
  `[Orphanet:562538]`; conservatively kept `is_a: MONDO:0003847` (matches gold).
- Removed obsoletion-scheduling artifacts (`obsoletion_candidate`,
  `IAO:0006012`).

## Issues

- Style/scope: same `{source="Orphanet:562538"}` annotation on the
  `has_characteristic HP:0000007` axiom as #537 — defensible but diverges from
  the gold/source-term unsourced form.
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn (left in
  place). Not an error.
- No substantive errors.
