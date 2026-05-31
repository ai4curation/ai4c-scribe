---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 7
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.750
precision: 0.750
recall: 0.750
jaccard: 0.600
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of CL_0001203 and CL_0001204 and stripped "CD44-high, and CD122-high"
from both definitions — the complete substantive repair. F1 of 0.750
**under-represents** quality: the divergence from gold is the addition of
PMID:41254224 (issue-requested, gold-omitted) plus xref ordering, not any
ontological error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all remaining differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224), more
  faithfully satisfying the issue's explicit reference instruction than the
  gold PR (which added only two).
- Kept CL_0001203's definition text verbatim ("CD45RO and CD127-positive"),
  matching the issue's proposed wording exactly — better than the sibling
  attempts that paraphrased to "CD45RO-positive".
- Minimal, tightly scoped diff with no extraneous edits.

## Issues

- Very terse PR/issue comments ("Changes have been committed ...") with no
  rationale or validation evidence. The edit is correct, but the lack of a
  documented research/validation process is weaker methodology than the
  Sonnet/Opus siblings on this case.
- Added a leading "A" to the CL_0001204 definition, diverging from the issue's
  verbatim text (and from gold). Cosmetic.
- No `term_tracker_item` added — minor process miss vs config guidance.
