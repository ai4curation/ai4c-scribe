---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 546
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

The agent removed the six genuinely redundant `oboInOwl:*` synonym/xref labels
that gold PR #3547 targets, but over-removed eight additional
`AnnotationAssertion(rdfs:label …)` axioms: `obo:IAO_0000028`,
`oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`,
`rdfs:seeAlso`, **plus** the UBERON synonym-type properties
`uberon:HUMAN_PREFERRED`, `uberon:LATIN`, and `uberon:PLURAL`. This is the
broadest over-deletion of the five reviewed runs. F1=0.429 accurately reflects
substantial information loss; it is a correctness error, not a metadiff
artifact.

## Strengths

- The six gold-targeted redundant labels (`hasBroadSynonym`, `hasDbXref`,
  `hasExactSynonym`, `hasNarrowSynonym`, `hasRelatedSynonym`,
  `hasSynonymType`) are all in the deletion set, so the agent identified the
  central issue.
- Change is subtractive and confined to the annotation-property block; no
  added axioms or re-serialization noise. The PR comment claims a `robot
  convert` syntax validation was run.

## Issues

- **Over-editing / information loss (error):** beyond the five non-redundant
  removals shared with pr522/pr583 (`obo:IAO_0000028`,
  `oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`,
  `rdfs:seeAlso`), this run also strips the labels for the UBERON
  synonym-type properties `uberon:HUMAN_PREFERRED`, `uberon:LATIN`, and
  `uberon:PLURAL`. These are **not** imported redundant labels — they are the
  effective labels for those properties. The PR comment's checklist claim
  ("Confirmed no matching imported annotation-property label assertions
  remain") is contradicted by the diff: it removed local, non-redundant
  labels. This is the most damaging deletion set of the reviewed runs.
- **Structural drift:** `AnnotationAssertion` lines removed while
  `# Annotation Property: …` comment headers are left in place (and the
  `uberon:*` `SubAnnotationPropertyOf` lines now sit under header-only blocks),
  producing exactly the spurious-diff noise the issue targets.
- F1=0.429 is honest and arguably still generous given the breadth of
  information loss. Grade: failure — significant correctness error.
