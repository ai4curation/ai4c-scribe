---
ontology: cell-ontology
issue_number: 3332
pr_number: 3547
eval_repo_pr: 145
agent: std_claude_haiku45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: axiom_repair
difficulty: simple
f1: 0.522
precision: 0.500
recall: 0.545
jaccard: 0.353
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Identical outcome to attempt #202 (same `17912f0` blob): the agent removed the
six genuinely redundant `oboInOwl:*` synonym/xref labels (correct) but also
deleted the `rdfs:label` axioms for `obo:IAO_0000028` ("symbol"),
`oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`, and
`rdfs:seeAlso`, none of which is labeled in `merged_import.owl`. That is
information loss, not redundant cleanup. F1=0.522 accurately represents
genuinely worse work; this is a correctness error, not a metadiff artifact.

## Strengths

- Correctly removed the six properties whose labels are redundant with
  `merged_import.owl` (`hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`,
  `hasNarrowSynonym`, `hasRelatedSynonym`, `hasSynonymType`) — the core ask.
- Purely subtractive; no re-serialization or unrelated edits.

## Issues

- **Over-editing / information loss (error):** deleted the only label for
  `obo:IAO_0000028` ("symbol"), `oboInOwl:SubsetProperty`,
  `oboInOwl:consider`, `oboInOwl:inSubset`, and `rdfs:seeAlso`. Verified in
  `merged_import.owl` that none of these five has an upstream `rdfs:label`, so
  these are not redundant and gold deliberately keeps them. The agent applied
  a blanket "remove all annotation-property labels" heuristic instead of the
  issue's conservative "already labeled in merged_import" criterion.
- **Stylistic inconsistency:** removed only the `AnnotationAssertion` lines
  while leaving the `# Annotation Property: …` comment headers, creating
  orphan comment blocks — the same structural-drift pattern the issue is
  meant to prevent. Gold removes comment + axiom as a unit.
- F1=0.522 does not under-represent quality here; it correctly reflects the
  extra wrong deletions and residual structural divergence. Honest grade:
  failure (significant correctness error / information loss) despite the core
  six being handled correctly.
