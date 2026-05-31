---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 461
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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

claude-sonnet-4.5 / claude correctly merged MONDO:0034186 into MONDO:0029144
with full annotation transfer and a canonical obsolete stanza. The lower F1
(0.952 vs the 0.968 top tier) comes from one deliberate, well-reasoned
divergence: the agent **removed** the redundant `is_a: MONDO:0003847 !
hereditary disease` from the survivor, explaining in the PR comment that this
parent is already entailed via the transferred, more specific
`is_a: MONDO:0019222` (MONDO:0019222 → MONDO:0019189 → MONDO:0019052 →
MONDO:0003847). This is a defensible ontological cleanup (eliminating a
redundant subsumption), not an error — but it diverges from the conservative
human PR, which kept both parents. Metadiff therefore **under-represents**
quality here.

## Strengths

- Correct, complete merge; canonical obsoletion metadata
  (`MONDO:TermsMerged`, `replaced_by: MONDO:0029144`, `is_obsolete`, #9842
  tracker item).
- Full annotation transfer with the transferred synonym correctly re-cited to
  `[Orphanet:562538]`; scheduling artifacts (`obsoletion_candidate`,
  `IAO:0006012`) removed.
- Strong, transparent methodology: PR comment documents `owltools
  --obsolete-replace`, double normalization, the six merge QC SPARQL checks all
  passing, and explicit reasoning for the redundant-parent removal with the full
  subsumption chain.
- The redundant-parent removal is ontologically sound; arguably an improvement
  over the gold (no stated asserted+entailed duplication).

## Issues

- Scope: removing `is_a: MONDO:0003847` is beyond the literal merge request and
  diverges from the gold. Defensible (the redundancy is real and the chain is
  correctly identified) but not strictly necessary; a reviewer could prefer the
  conservative approach in a merge-only PR.
- Cosmetic-only: did not reproduce the gold's reorder churn of the two existing
  survivor synonyms (left in place). Not an error.
- No substantive errors.
