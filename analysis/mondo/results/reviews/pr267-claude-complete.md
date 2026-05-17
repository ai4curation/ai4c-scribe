---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 267
agent: std_opencode_kimi
model: kimi-k2.6
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

kimi-k2.6 / opencode produced a diff byte-identical to the haiku attempts (blob
`eee8c63`) and correctly merged MONDO:0034186 into MONDO:0029144. The PR comment
shows accurate reasoning: it traced the alignment chain
(ORDO:562538 → OMIM:618148 → MONDO:0029144) before executing the merge. Obsolete
stanza is in canonical form and all annotations were transferred. Metadiff
F1=0.968 **under-represents** quality — the 2 unmatched deletions are only the
gold PR's reorder churn of two unchanged survivor synonyms.

## Strengths

- Sound methodology articulated in the PR comment: explicitly justified the
  merge via the Orphanet→OMIM→MONDO equivalence chain stated in the issue.
- Canonical obsoletion metadata complete (`MONDO:TermsMerged`, `replaced_by`,
  `is_obsolete`, #9842 tracker item).
- Full, correct annotation transfer including re-citation of the transferred
  synonym to `[Orphanet:562538]` and addition of `is_a: MONDO:0019222` and
  `has_characteristic HP:0000007` to the survivor.
- Removed obsoletion-scheduling artifacts from the survivor.

## Issues

- Cosmetic-only divergence: did not reproduce the gold's delete+re-add reordering
  of the survivor's two existing synonyms (left them in place). Not an error.
- Kept the redundant `is_a: MONDO:0003847 ! hereditary disease` (matches gold,
  conservative).
- No substantive issues.
