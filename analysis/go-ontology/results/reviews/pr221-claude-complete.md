---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 221
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 1.0
recall: 0.5
jaccard: 0.5
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: base_contamination_GO_0102067
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent produced the exact gold edit for issue #31601, replacing the
`GO:0140597` (protein carrier activity) definition with the parent-aligned
`"Directly binding to a protein and delivering it either to an acceptor
molecule or to a specific location."` [PMID:7628437], byte-identical to human
PR #32007, and explicitly (and correctly) declined to touch
`GO:0140309`. The metadiff F1 of 0.667 **under-represents** quality: precision
is depressed only by the `GO:0102067` geranylgeranyl line that appears
identically in all 12 eval PRs for this issue and is base/scaffold
contamination from unrelated source PR #32006, not an agent edit. On the
issue's substance this is a clean success.

## Strengths

- Implemented the exact accepted `GO:0140597` definition from PR #32007 with
  the `PMID:7628437` xref preserved; no wording drift.
- Strong reasoning: explicitly identified the genus-differentia pattern of
  parent `GO:0140104` and produced a definition that is a faithful
  protein-specific specialization of it.
- Correctly diagnosed that `GO:0140309` (unfolded protein holdase activity)
  "already had the correct definition" — true, because round-1 PR #31602's
  destination-wording fix is already present in the eval base — and made no
  change there, matching the human #32007 scope precisely.
- Did not introduce new references, did not alter synonyms, logical
  definition, parentage, or term tracker metadata.
- PR/issue comments are accurate and appropriately scoped.

## Issues

- The diff includes the unrelated `GO:0102067` geranylgeranyl diphosphate
  reductase activity definition/xref change. Cross-attempt evidence (the same
  line, verbatim, in every one of the 12 eval PRs including no-op runs) shows
  this is eval base/scaffold contamination from source PR #32006 (refs
  #31963), not behavior of this agent — so it should not be charged against
  this run as over-editing.
- No genuine agent-side issues; the change is correct and minimal relative to
  the issue's actual ask.
