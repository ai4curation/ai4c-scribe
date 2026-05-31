---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 43
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.952
precision: 0.938
recall: 0.968
jaccard: 0.909
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5 / codex correctly merged MONDO:0034186 into MONDO:0029144. The diff is
identical to attempt #461 (blob `c33ecdb`): canonical obsolete stanza, full
annotation transfer, and the same deliberate removal of the redundant
`is_a: MONDO:0003847 ! hereditary disease` from the survivor. The PR comment
justifies the removal by noting the transferred `MONDO:0019222` parent sits
under "inborn errors of metabolism", which already has hereditary disease as an
ancestor, so the broader assertion is entailed. This is a defensible cleanup
that diverges from the conservative human PR; metadiff F1=0.952
**under-represents** quality.

## Strengths

- Correct, complete merge with canonical obsoletion metadata
  (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`, `is_obsolete`, #9842
  tracker item) and full annotation transfer.
- Transferred synonym correctly re-cited to `[Orphanet:562538]`; scheduling
  artifacts removed.
- Thorough documented validation: `owltools --obsolete-replace`,
  checkout/checkin cleanup, double `make NORM`, `robot convert`, and the six
  merge QC SPARQL queries all passing with 0 violations; `git diff --check`
  clean.
- Redundant-parent removal is ontologically reasoned and correct.

## Issues

- Scope: the `is_a: MONDO:0003847` removal exceeds the literal merge request and
  diverges from gold. Defensible (genuine redundancy, correct chain) but a
  reviewer could prefer the conservative merge-only approach.
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn (left in
  place). Not an error.
- No substantive errors.
