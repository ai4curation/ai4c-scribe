---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 486
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
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

This run produces a diff byte-identical to pr546 (same blob `5b0ac60`): it
removes the six genuinely redundant `oboInOwl:*` synonym/xref labels gold
PR #3547 targets, but over-removes eight more `AnnotationAssertion(rdfs:label
…)` axioms — `obo:IAO_0000028`, `oboInOwl:SubsetProperty`,
`oboInOwl:consider`, `oboInOwl:inSubset`, `rdfs:seeAlso`, plus
`uberon:HUMAN_PREFERRED`, `uberon:LATIN`, and `uberon:PLURAL`. F1=0.429
accurately reflects substantial information loss; this is a correctness
error, not a metadiff artifact.

## Strengths

- The six gold-targeted redundant labels (`hasBroadSynonym`, `hasDbXref`,
  `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`,
  `hasSynonymType`) are all in the deletion set — the central issue was
  identified.
- Purely subtractive, confined to the annotation-property block; no added
  axioms, no ROBOT/ODK churn or re-serialization noise.

## Issues

- **Over-editing / information loss (error):** identical over-deletion to
  pr546 — removes five non-redundant `oboInOwl:`/`obo:`/`rdfs:` labels plus
  the three UBERON synonym-type labels (`uberon:HUMAN_PREFERRED`,
  `uberon:LATIN`, `uberon:PLURAL`). Per the established case finding, none of
  the five `oboInOwl:`/`obo:`/`rdfs:seeAlso` pairs is labeled in
  `merged_import.owl`, and the UBERON synonym-type labels are local effective
  labels, not imported redundancies. Removing all of these is information loss
  directly contrary to the conservative criterion in issue #3332.
- **Structural drift:** `AnnotationAssertion` lines removed while
  `# Annotation Property: …` comment headers are left dangling — the very
  spurious-diff noise the issue is trying to eliminate.
- F1=0.429 is honest. Grade: failure — significant correctness error causing
  information loss, despite the correct core six.
