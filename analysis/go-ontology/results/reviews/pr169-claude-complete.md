---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 169
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.5
precision: 1.0
recall: 0.333
jaccard: 0.333
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
acceptor molecule or to a specific location."` [PMID:7628437]) and went
further on `GO:0140309`, rewriting the holdase definition to mirror the new
parent wording, fixing the "it's being delivers" grammar, and additionally
correcting "an holdase" → "a holdase" in the term comment. The metadiff F1 of
0.500 **under-represents** the core edit (the `GO:0102067` precision hit is
base contamination, not an agent error) but the broad `GO:0140309` rewrite is
a genuine expansion beyond gold #32007's single-term scope.

## Strengths

- `GO:0140597` definition byte-identical to gold PR #32007; `PMID:7628437`
  xref preserved; synonyms, logical definition, and parentage untouched.
- Sound rationale tying the new wording to parent `GO:0140104` and noting the
  cargo specialization to protein.
- The `GO:0140309` changes are all individually defensible: harmonizing the
  child with the broadened parent, fixing the real "delivers" grammar bug, and
  the "an holdase" → "a holdase" article correction is a legitimate (if very
  minor) copy-edit since "holdase" is consonant-initial.
- Clear, accurate PR/issue summary; explicitly states no logical axioms,
  parentage, synonyms, or xrefs were changed.

## Issues

- Scope: this is the broadest of the 0.500 attempts. Gold PR #32007 (issue
  #31601 round 2) changed only `GO:0140597`; the holdase destination wording
  was already handled by round-1 PR #31602 in the eval base. The full
  `GO:0140309` def rewrite plus comment edit goes well beyond the selected
  gold — defensible curation but the reason recall is depressed.
- The diff also contains the unrelated `GO:0102067` geranylgeranyl change;
  cross-attempt evidence (identical line in all 12 eval PRs including no-op
  runs) shows this is eval base/scaffold contamination from source PR #32006,
  not an agent edit, and should not be charged as over-editing.
