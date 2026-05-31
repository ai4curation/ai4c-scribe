---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 322
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: simple
case_quality: ok
f1: 0.429
precision: 0.500
recall: 0.375
jaccard: 0.273
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The codex/gpt-5.4 run removes the six genuinely redundant `oboInOwl:*`
synonym/xref labels gold PR #3547 targets, but over-removes eight additional
`AnnotationAssertion(rdfs:label …)` axioms — `obo:IAO_0000028`,
`oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`,
`rdfs:seeAlso`, plus the UBERON synonym-type labels `uberon:HUMAN_PREFERRED`,
`uberon:LATIN`, and `uberon:PLURAL` (same over-deletion as pr546/pr486;
distinct blob `77f430a`). F1=0.429 accurately reflects substantial
information loss; this is a correctness error, not a metadiff artifact. (The
existing codex-authored review reaches the same conclusion independently.)

## Strengths

- The six gold-targeted redundant labels (`hasBroadSynonym`, `hasDbXref`,
  `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`,
  `hasSynonymType`) are all in the deletion set — the central issue was
  identified.
- Subtractive only, confined to the annotation-property area; no added
  axioms, no ROBOT/ODK churn. The PR comment is transparent that `robot` was
  unavailable for syntax validation rather than falsely claiming a check
  (better methodology disclosure than pr546's contradicted checklist).

## Issues

- **Over-editing / information loss (error):** the deletion set explicitly
  includes `obo:IAO_0000028`, `uberon:HUMAN_PREFERRED`, `uberon:LATIN`,
  `uberon:PLURAL`, `oboInOwl:SubsetProperty`, `oboInOwl:consider`,
  `oboInOwl:inSubset`, and `rdfs:seeAlso` (per the agent's own PR comment).
  Per the established case finding, none of the `oboInOwl:`/`obo:`/`rdfs:`
  pairs is labeled in `merged_import.owl`, and the UBERON synonym-type labels
  are local effective labels. The agent's stated rationale ("already supplied
  by imported content") is factually wrong for these eight — it asserted
  redundancy it never verified against the imports, the precise judgment the
  conservative issue #3332 criterion requires.
- **Structural drift:** `AnnotationAssertion` lines removed while
  `# Annotation Property: …` comment headers remain — the same spurious-diff
  noise the issue is meant to eliminate.
- F1=0.429 is honest and not under-representing quality. Grade: failure —
  significant correctness error causing information loss, despite the correct
  core six.
