---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 230
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
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

gemma-4-31b / opencode produced a diff byte-identical to the top-scoring
attempts (blob `eee8c63`) and correctly merged MONDO:0034186 into MONDO:0029144.
Notably for a 31B model, the PR comment is a precise, accurate change log
(subsets/xrefs/axioms transferred, synonym evidence fixed from `[MONDO:0034186]`
to `[Orphanet:562538]`, scheduling artifacts removed) and reports running
`make NORM` and a reference-integrity check. Metadiff F1=0.968
**under-represents** quality — the 2 unmatched deletions are only the gold PR's
reorder churn of two unchanged survivor synonyms.

## Strengths

- Strong result for a small open model: output identical to the haiku/kimi/gpt
  top tier.
- Self-documented validation: `make NORM` normalization and verification that no
  references to MONDO:0034186 remain outside its stanza.
- Canonical obsoletion (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`,
  `is_obsolete`, #9842 tracker item) and complete annotation transfer.
- Correctly re-cited the transferred synonym to `[Orphanet:562538]` and removed
  `subset: obsoletion_candidate` / `IAO:0006012` from the survivor.

## Issues

- Cosmetic-only divergence: did not reproduce the gold's synonym-block reorder
  churn (left the two existing synonyms in place). Not an error.
- Kept the redundant `is_a: MONDO:0003847 ! hereditary disease` (matches gold).
- No substantive issues.
