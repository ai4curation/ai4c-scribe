---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 522
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

The agent correctly identified and removed the six genuinely redundant
`oboInOwl:*` synonym/xref labels that gold PR #3547 targets, but it
over-removed five additional `AnnotationAssertion(rdfs:label …)` axioms —
`obo:IAO_0000028` ("symbol"), `oboInOwl:SubsetProperty`, `oboInOwl:consider`,
`oboInOwl:inSubset`, and `rdfs:seeAlso` — none of which is labeled upstream in
`src/ontology/imports/merged_import.owl`. Deleting these is information loss,
not redundant cleanup. F1=0.480 accurately reflects genuinely worse work (it
matches the over-removing pr202/pr145 pattern); this is a correctness error,
not a metadiff artifact.

## Strengths

- Correctly identified and removed the six genuinely redundant imported labels
  (`hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`,
  `hasRelatedSynonym`, `hasSynonymType`) — the exact core of issue #3332.
- Change is purely subtractive; no re-serialization noise, no ROBOT/ODK churn,
  and no unrelated ontology axioms added. The edit stays localized to the
  annotation-property header block.

## Issues

- **Over-editing / information loss (error):** removed
  `AnnotationAssertion(rdfs:label obo:IAO_0000028 "symbol")`,
  `… oboInOwl:SubsetProperty "subset_property"`,
  `… oboInOwl:consider "consider"`,
  `… oboInOwl:inSubset "in_subset"`, and
  `… rdfs:seeAlso "see also"`. Direct inspection of `merged_import.owl`
  (per the established case finding) confirms none of these five
  predicate–subject pairs carries an upstream `rdfs:label`, so removing them
  strips the only label these properties have in the merged product. Issue
  #3332 and gold #3547 are deliberately conservative ("that *already* have a
  label … from the import modules"); the agent applied a blanket removal that
  ignores that qualifier.
- **Structural drift:** the agent deleted the `AnnotationAssertion` lines but
  left the `# Annotation Property: …` comment headers in place, producing
  dangling comment blocks with no axiom — precisely the kind of edit-file
  noise the issue is trying to eliminate. Gold removes comment + axiom
  together.
- F1=0.480 is not an under-representation; it correctly captures the
  missing-precision (extra wrong deletions) and residual structural divergence.
  Honest grade: failure — significant correctness error causing information
  loss, despite getting the core six right.
