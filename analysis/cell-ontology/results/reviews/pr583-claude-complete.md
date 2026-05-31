---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 583
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: simple
case_quality: ok
f1: 0.480
precision: 0.500
recall: 0.462
jaccard: 0.316
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run produces a diff byte-identical to pr522 (same blob `b791e1e`): it
removes the six genuinely redundant `oboInOwl:*` synonym/xref labels that gold
PR #3547 targets, but over-removes five additional
`AnnotationAssertion(rdfs:label …)` axioms — `obo:IAO_0000028` ("symbol"),
`oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`, and
`rdfs:seeAlso` — none labeled upstream in `merged_import.owl`. F1=0.480
accurately reflects the information loss; this is a correctness error, not a
metadiff artifact.

## Strengths

- Correctly removed the six genuinely redundant imported labels
  (`hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`,
  `hasRelatedSynonym`, `hasSynonymType`) — the core of issue #3332.
- Subtractive only; no re-serialization, no ROBOT/ODK churn, no added axioms.
  The agent's PR comment shows reasonable methodology (read issue context,
  scoped to imported-property labels, reviewed final diff) even though the
  scoping criterion it applied was too broad.

## Issues

- **Over-editing / information loss (error):** removed the `rdfs:label`
  axioms for `obo:IAO_0000028`, `oboInOwl:SubsetProperty`,
  `oboInOwl:consider`, `oboInOwl:inSubset`, and `rdfs:seeAlso`. Per the
  established case finding, none of these five predicate–subject pairs is
  labeled in `src/ontology/imports/merged_import.owl`, so deleting them
  removes the only label these properties carry in the merged product. The
  agent's own rationale ("already provided by imported content") is factually
  wrong for these five — it asserted redundancy it did not verify against the
  imports.
- **Structural drift:** `AnnotationAssertion` lines removed but
  `# Annotation Property: …` comment headers left dangling, generating exactly
  the spurious-diff noise the issue aims to remove. Gold deletes comment +
  axiom as a unit.
- F1=0.480 neither over- nor under-represents quality here. Honest grade:
  failure — correctness error causing information loss, despite the correct
  core six.
