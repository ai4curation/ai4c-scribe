---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 490
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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
acceptor molecule or to a specific location."` [PMID:7628437]) and also made
a minimal grammar-only fix to `GO:0140309` ("while it's being delivers" →
"while it's being delivered"), leaving the rest of the holdase definition
intact. The metadiff F1 of 0.500 substantially **under-represents** quality:
the dominant penalty is the `GO:0102067` geranylgeranyl line that is base/
scaffold contamination present in all 12 eval PRs, not an agent edit. The core
issue is solved correctly; the only true agent extra is a one-word typo fix.

## Strengths

- `GO:0140597` definition is byte-identical to gold PR #32007, xref
  `PMID:7628437` preserved, synonyms/logical-definition/parentage untouched.
- Excellent rationale: explicitly aligned with parent `GO:0140104` and sibling
  `GO:0005319` lipid carrier activity genus-differentia pattern.
- The `GO:0140309` change is the most conservative possible — it touches only
  the broken verb form ("delivers" → "delivered") and leaves the rest of the
  sentence exactly as it was, rather than rewriting the whole definition.
  This is a genuine, low-risk defect fix.
- Thorough, accurate PR writeup and validation checklist; correctly notes the
  parent-child consistency improvement.

## Issues

- Scope: gold PR #32007 changed only `GO:0140597`. The `GO:0140309` grammar
  fix, while a real and harmless improvement, is beyond the selected gold and
  is the only legitimate reason recall is below the 0.667 attempts. This is
  defensible "fix-while-in-the-neighborhood" cleanup, not a substantive error.
- The diff also contains the unrelated `GO:0102067` geranylgeranyl change;
  cross-attempt evidence shows this is eval base/scaffold contamination from
  source PR #32006, not an agent edit, and should not be charged against this
  run.
