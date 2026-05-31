---
ontology: cell-ontology
issue_number: 2967
pr_number: 3309
eval_repo_pr: 84
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.500
precision: 0.500
recall: 0.500
jaccard: 0.333
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: metadiff_conjunct_reorder_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-haiku-4.5 produced the exactly correct fix for issue #2967, replacing
obsolete `GO:0051024` with `GO:0002639` in the CL:0002038 (T follicular helper
cell) `EquivalentClasses` axiom — identical in substance to the merged gold PR
#3309. The metadiff F1 of 0.500 **severely under-represents** quality: the
agent's axiom is logically equivalent to gold's, differing only in the
commutative ordering of the two `RO_0002215` conjuncts (serialization artifact).

## Strengths

- Correct biological edit: `GO:0051024` → `GO:0002639` per @addiehl's
  recommendation and GO's `term replaced by` annotation.
- Good methodology documented in PR body: located CL:0002038, confirmed the
  obsolete reference, verified `GO:0051024` appears nowhere else in the file,
  and correctly noted the broader release-time `deprecated_class_reference`
  check as the ideal long-term solution while still delivering the immediate
  manual fix (matching how the human curators and gold PR scoped it).
- Tight single-line scope, no whitespace/EOF collateral.

## Issues

- None substantive. Divergence from gold is solely conjunct order within a
  commutative `ObjectIntersectionOf` (gold serialized `GO_0002639` before
  `GO_0045830`; agent left `GO_0045830` first). Semantically equivalent — a
  metadiff line-diff artifact, not an error.
- Minor: PR body cites "Line 14283" as the edit location; the gold/base diff
  hunk header is at line 14280 and the EquivalentClasses line is ~14283 — an
  imprecise but harmless line reference; the actual edit is correct.
