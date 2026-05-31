---
ontology: cell-ontology
issue_number: 3332
pr_number: 3333
eval_repo_pr: 506
agent: std_opencode_g54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: bulk_edit
difficulty: medium
f1: 0.407
precision: 0.300
recall: 0.632
jaccard: 0.255
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_out_of_scope_reserialization_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly and completely resolved issue #3332, removing every
redundant imported-annotation-property `rdfs:label` axiom (5 IAO properties,
11 oboInOwl properties, and `rdfs:label rdfs:seeAlso`) along with their
now-empty `# Annotation Property:` comment headers — leaving no orphaned
headers behind. The diff is byte-identical to the gpt-5.4/codex attempt #75
(blob `fdd9657`); the runtime is opencode here. F1=0.407 (P=0.300, R=0.632)
**substantially under-represents** quality: ~60% of the gold diff is an
unrelated one-time class-block re-serialization that no agent can or should
reproduce. On substance this is a success.

## Strengths

- Complete, clean removal of all redundant imported AP labels named in the
  issue, including the explicitly-cited motivating cases `obo:IAO_0000115`,
  `obo:IAO_0000424`, `obo:IAO_0000700`, `obo:IAO_0100001`,
  `oboInOwl:hasBroadSynonym`, `oboInOwl:hasDbXref`, `oboInOwl:hasExactSynonym`,
  plus `obo:IAO_0000028` and the rest of the oboInOwl set.
- Removed the now-empty `# Annotation Property:` header comments and blank
  lines for each deleted axiom — avoiding the orphaned-header defect that
  capped pr20 at partial, and directly serving the issue's stated goal of
  eliminating spurious comment-driven diffs.
- Correctly preserved the two CL-meaningful `rdfs:seeAlso` axioms
  (`oboInOwl:hasDbXref` and `oboInOwl:shorthand` on `rdfs:seeAlso`) while
  dropping only the redundant `rdfs:label rdfs:seeAlso`; kept all
  `SubAnnotationPropertyOf` and CL-native subset-property labels.

## Issues

- Also removed `rdfs:label` from `uberon:HUMAN_PREFERRED`, `uberon:LATIN`,
  and `uberon:PLURAL` (keeping their `SubAnnotationPropertyOf`), which the
  gold PR did not. These are imported uberon synonym-type properties, so the
  removal is consistent with the issue's principle ("CL has no business
  stating the label of an imported AP"); defensible, not an error. It
  marginally lowers metadiff recall (0.632 vs. the 0.667 of attempts that
  left them in place).
- Added a trailing newline at end of file (`\ No newline at end of file` →
  newline). Harmless whitespace normalization; a tiny out-of-scope cosmetic
  edit only.
- Only true substantive gap vs. gold is the gold's incidental relocation of
  the misplaced `CL_4072027` / `CL_7770002` / `CL_7770005` class blocks and
  `Declaration(Class(...))` reordering — an explicitly out-of-scope side
  effect of cleaning up a prior AI PR, not inferable from #3332. Not counted
  against the agent (see METADATA case_quality note).
