---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 599
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with a direct replacement by GO:0008290 "F-actin capping protein complex", producing a diff functionally identical to human gold PR #31960 (and byte-identical to sibling attempt #645, blob `9071acb`). F1=0.900 under-represents quality: the sole deviation from gold is the free-text `comment:` wording, a metadiff normalization artifact rather than a substantive error. (Note: the auto-generated codex review marked this `partial_success`/`missed_requirement`; that is metadiff-blind — there is no missed requirement here.)

## Strengths

- Fully correct obsoletion mechanics: name → "obsolete actin capping protein of dynactin complex", definition prefixed "OBSOLETE." with the original `[GOC:jl, PMID:18221362, PMID:18544499]` provenance retained verbatim, both defining axioms (`intersection_of: GO:0008290` and `intersection_of: part_of GO:0005869`) stripped, `is_obsolete: true`, `replaced_by: GO:0008290`, and `property_value: term_tracker_item ".../issues/31956" xsd:anyURI` added — every element of the gold edit reproduced.
- Replacement target is correct: GO:0008290 matches the issue's explicitly requested "Replace by" term, and obsoleting the over-specific compositional class is the curatorially correct outcome since the dynactin-localized pool is subsumed by GO:0008290 without the `part_of GO:0005869` constraint.
- Tightly scoped to the single file src/ontology/go-edit.obo with no extraneous edits; precision and recall both 0.900 confirm no over- or under-editing beyond the comment-wording difference.

## Issues

- None substantive. The obsoletion `comment:` ("unused, overly specific compositional class and annotations can be represented with F-actin capping protein complex") differs in wording from gold's ("redundant with GO:0008290 ... annotations can be migrated to the replacement term") but is semantically equivalent and accurate. This wording difference is the sole reason F1 is 0.900 rather than 1.0 — a comment-prose normalization artifact, not a quality deficit.
