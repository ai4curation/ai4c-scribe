---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 243
agent: std_opencode_gem4
model: gemma-4-31b
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/243
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 243 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully handled the obsoletion request for `GO:0005870`. It marked the term obsolete, prefixed the name and definition, removed the defining logical axioms, added `replaced_by: GO:0008290`, and linked the issue tracker. The metadiff gap is only comment wording.

## Strengths

- Correctly obsoleted `GO:0005870` `actin capping protein of dynactin complex`.
- Correctly removed the `intersection_of` axioms that made the term a pre-composed dynactin-specific capping protein complex.
- Correctly added `replaced_by: GO:0008290`.
- Added the issue #31956 tracker property.
- Stayed scoped to the target term.

## Issues

- No substantive issues. The obsoletion comment is shorter than the human PR's wording but gives the same direct-replacement rationale.
