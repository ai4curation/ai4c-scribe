---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 132
agent: std_opencode_g55
model: gpt-5.5
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
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/132
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 132 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the requested obsoletion of `GO:0005870` actin capping protein of dynactin complex, using `GO:0008290` F-actin capping protein complex as the direct replacement requested in the issue. The metadiff F1 of 0.9 accurately reflects a near-identical solution: the ontology edits match the human PR except for the exact free-text obsoletion comment.


## Strengths

- Correctly targeted the requested cellular component term, `GO:0005870`, and renamed it to `obsolete actin capping protein of dynactin complex`.
- Correctly added the standard GO obsoletion structure: prefixed the definition with `OBSOLETE.`, added `is_obsolete: true`, and added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31956" xsd:anyURI`.
- Correctly removed the logical axioms that should not remain on an obsolete term: `intersection_of: GO:0008290` and `intersection_of: part_of GO:0005869`.
- Correctly added `replaced_by: GO:0008290`, matching the issue request that annotations can be safely moved to `GO:0008290` F-actin capping protein complex.
- Kept the edit tightly scoped to the single requested term in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- No substantive ontology issues. The agent's only difference from the human PR is the obsoletion comment text: the human wrote that `GO:0005870` is redundant with `GO:0008290` and that annotations can be migrated, while the agent wrote that it is equivalent to F-actin capping protein complex.
- Minor style/completeness difference: the agent's comment does not explicitly name the replacement ID `GO:0008290` or mention annotation migration, but that information is still captured by the separate `replaced_by: GO:0008290` tag and the edit satisfies the issue.
