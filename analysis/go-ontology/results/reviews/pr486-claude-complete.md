---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 486
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

A repeat run of the same model/runtime as #490 with an identical resulting
diff: the agent produced the exact gold `GO:0140597` definition from human PR
#32007 (`"Directly binding to a protein and delivering it either to an
acceptor molecule or to a specific location."` [PMID:7628437]) plus the
minimal `GO:0140309` grammar fix ("it's being delivers" → "it's being
delivered"). The metadiff F1 of 0.500 **under-represents** quality — the main
penalty is the `GO:0102067` geranylgeranyl line, which is base/scaffold
contamination shared by all 12 eval PRs, not an agent edit. The issue is
solved correctly with one conservative typo cleanup.

## Strengths

- `GO:0140597` definition byte-identical to gold PR #32007; `PMID:7628437`
  xref preserved; synonyms, `intersection_of` logical definition, and
  parentage left unchanged.
- Strong design-pattern reasoning: explicitly consulted parent `GO:0140104`
  molecular carrier activity and sibling `GO:0005319` lipid carrier activity,
  and correctly framed the new wording as a protein-specific specialization.
- The `GO:0140309` edit is the minimal correct fix — only the malformed verb
  phrase is changed; the rest of the holdase definition and its comment are
  preserved verbatim.
- Reproducible behavior across the two sonnet/claude runs (#490, #486) is a
  positive consistency signal.

## Issues

- Scope: gold PR #32007 (issue #31601 round 2) changed only `GO:0140597`. The
  `GO:0140309` grammar correction, though real and harmless, is outside the
  selected gold and is the sole legitimate driver of the sub-0.667 recall.
  Defensible cleanup, not an error.
- The diff also contains the unrelated `GO:0102067` geranylgeranyl change;
  this is eval base/scaffold contamination from source PR #32006 (identical
  across all 12 attempts, including no-op runs), not an agent edit, and should
  not count against this run.
