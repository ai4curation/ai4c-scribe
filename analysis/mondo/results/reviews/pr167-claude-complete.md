---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 167
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.968
precision: 0.938
recall: 1.0
jaccard: 0.938
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.4 / codex produced a diff byte-identical to the top tier (blob `eee8c63`)
and correctly merged MONDO:0034186 into MONDO:0029144. This attempt has the
strongest documented methodology of the batch: the PR comment reports using
`owltools --obsolete-replace`, `make NORM`, `robot convert`, and a targeted
`robot verify` against six merge-relevant QC SPARQL queries
(qc-proxy-merge-missing-preferred, qc-misused-replaced-by, qc-obsoletion-reason,
qc-deprecated-class-reference, qc-xref-without-precision,
qc-duplicate-exact-synonym-no-abbrev), all passing. Metadiff F1=0.968
**under-represents** quality — the 2 unmatched deletions are only the gold PR's
reorder churn of two unchanged survivor synonyms.

## Strengths

- Best-documented validation in the batch: tool-driven merge
  (`owltools --obsolete-replace`) plus targeted ROBOT QC against the exact merge
  QC query set, with explicit confirmation of no stale MONDO:0034186 references,
  no obsolete-ID synonym evidence, and no `alt_id`.
- Canonical obsoletion stanza and complete annotation transfer (subsets, GARD
  /Orphanet xrefs, `MONDO:0019222` parent, `has_characteristic HP:0000007`,
  #9842 tracker item).
- Correctly re-attributed the transferred synonym to `[Orphanet:562538]` and
  removed the scheduling artifacts (`obsoletion_candidate`, `IAO:0006012`).

## Issues

- Cosmetic-only divergence from gold: kept the survivor's two existing synonyms
  in place rather than reproducing the gold's delete+re-add reorder. Not an
  error; arguably cleaner.
- Kept the redundant `is_a: MONDO:0003847 ! hereditary disease` (matches gold).
- No substantive issues.
