---
ontology: cell-ontology
issue_number: 3332
pr_number: 3333
eval_repo_pr: 569
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
redundant imported-annotation-property `rdfs:label` axiom and its now-empty
`# Annotation Property:` comment header. The agent diff is byte-identical to
pr506 and the gpt-5.4/codex attempt #75 (blob `fdd9657`); the difference here
is a more thorough PR narrative documenting the reasoning and validation.
F1=0.407 (P=0.300, R=0.632) **substantially under-represents** quality: ~60%
of the gold diff is an unrelated one-time class-block re-serialization no
agent can reproduce. On substance this is a success.

## Strengths

- Complete, clean removal of all redundant imported AP labels — 5 IAO
  properties (`IAO_0000028/0000115/0000424/0000700/0100001`), 11 oboInOwl
  properties (`SubsetProperty`, `SynonymTypeProperty`, `consider`,
  `hasBroadSynonym`, `hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`,
  `hasRelatedSynonym`, `hasSynonymType`, `inSubset`, `shorthand`), and
  `rdfs:label rdfs:seeAlso` — with their empty header comments removed (no
  orphaned headers, unlike pr20).
- Strong, transparent methodology in the PR comment: explicitly itemizes the
  removed properties, distinguishes pure label-only blocks from properties
  retaining CL-specific axioms, confirms the issue discussion supported the
  removal, and reports running `robot convert` to verify syntax post-edit.
- Correctly preserved CL-owned axioms: the two meaningful `rdfs:seeAlso`
  assertions, `SubAnnotationPropertyOf` relations, and CL-native
  subset-property labels.

## Issues

- Like pr506, also removed `rdfs:label` from `uberon:HUMAN_PREFERRED`,
  `uberon:LATIN`, `uberon:PLURAL` (keeping `SubAnnotationPropertyOf`), which
  the gold did not. Consistent with the issue's stated principle for imported
  APs; defensible, not an error. Marginally lowers recall (0.632 vs. 0.667).
- Added a trailing newline at end of file — harmless whitespace
  normalization, a cosmetic out-of-scope edit only.
- The agent issue comment contains the literal placeholder `PR #<NN>`
  ("Implemented and committed locally for PR #<NN>."), an unsubstituted
  template token. Cosmetic narrative artifact, no effect on the ontology
  edit.
- Only true substantive gap vs. gold is the gold's out-of-scope relocation of
  the misplaced `CL_4072027` / `CL_7770002` / `CL_7770005` class blocks and
  `Declaration(Class(...))` reordering — an explicit side effect of cleaning
  up a prior AI PR, not inferable from #3332. Not counted against the agent
  (see METADATA case_quality note).
