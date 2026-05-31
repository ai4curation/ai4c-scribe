---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 119
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 1.0
recall: 0.5
jaccard: 0.5
outcome: success
failure_modes:
- scope_creep
case_quality: poor
case_quality_reason: base_contamination_GO_0102067
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent produced the exact gold `GO:0140597` definition from human PR
#32007 (`"Directly binding to a protein and delivering it either to an
acceptor molecule or to a specific location."` [PMID:7628437]) and
additionally rewrote the `GO:0140309` (unfolded protein holdase activity)
definition to mirror the new parent wording and fix the long-standing
"it's being delivers" grammar defect. The metadiff F1 of 0.667 mixes two
effects: it **under-represents** quality on the core gold edit (the
`GO:0102067` precision hit is base contamination, not an agent error), but the
extra `GO:0140309` rewrite is a genuine out-of-scope-for-#32007 change.
Net: substantively correct on the issue, with one defensible scope expansion.

## Strengths

- `GO:0140597` definition is byte-identical to gold PR #32007, with the
  `PMID:7628437` xref preserved and no change to synonyms, logical definition,
  or parentage.
- Sound rationale: cited parent `GO:0140104` and sibling `GO:0005319` lipid
  carrier activity as the design-pattern precedent for the new wording.
- The `GO:0140309` rewrite is biologically defensible — it harmonizes the
  holdase child with the broadened parent ("directly binds ... delivers it
  either to an acceptor molecule or to a specific location") and fixes the
  real grammar error ("while it's being delivers" → "while it is being
  delivered").
- Claims `make travis_build` passed both before and after edits — appropriate
  validation discipline for codex runtime.

## Issues

- Scope: human PR #32007 (round 2 of issue #31601) changed only
  `GO:0140597`. The round-1 holdase destination fix was already done in PR
  #31602 and is present in the eval base, so the only residual `GO:0140309`
  defect was the cosmetic grammar typo. Rewriting the whole holdase sentence
  goes beyond what #32007 did. This is defensible cleanup but lowers recall
  against the selected gold and is the reason this attempt is not a clean
  scope match.
- The diff also contains the unrelated `GO:0102067` geranylgeranyl change.
  Cross-attempt evidence (identical line in all 12 eval PRs, including no-op
  runs) shows this is eval base/scaffold contamination from source PR #32006,
  not this agent's edit, and should not be charged as over-editing.
