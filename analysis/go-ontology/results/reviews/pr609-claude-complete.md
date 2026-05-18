---
ontology: go-ontology
issue_number: 31981
pr_number: 31995
eval_repo_pr: 609
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
case_quality: good
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent correctly resolved geneontology/go-ontology#31981 by adding `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` plus a `property_value: term_tracker_item` linking issue #31981 to the `GO:0072318` clathrin coat disassembly stanza. The resulting diff is byte-identical to the merged human gold PR #31995 (same +2/-0 hunk at the same offset, same `f53920e0d..5b4d6c89f` blob transition); F1 1.0 / P 1.0 / R 1.0 faithfully reflects substantive quality with no over- or under-representation.

## Strengths

- Made exactly the change the curators converged on: `part_of` (not a second `is_a`) to `GO:0072583`, which is the modeling pgaudet explicitly requested in the issue discussion ("This should be part_of, right?") and which preserves the existing `is_a: GO:0072319 ! vesicle uncoating` parent and the `intersection_of` logical definition unchanged.
- Added the `term_tracker_item` provenance annotation in the correct OBO format (`"https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI`), satisfying ValWood's explicit request for the term tracker ID.
- Tightly scoped: a single 2-line addition to `src/ontology/go-edit.obo` with no collateral edits to legacy `created_by`/`creation_date` metadata or neighboring stanzas, so precision is not eroded by scope creep.

## Issues

No issues. The change is identical to the human gold PR and fully satisfies both explicit asks in the issue (missing superclass as `part_of`, plus term tracker item). This attempt record contains only the diff (no PR/issue comment narrative), so process methodology cannot be assessed from the artifact — but the outcome is exactly correct.
