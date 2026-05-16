---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 464
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.879
precision: 0.895
recall: 0.864
jaccard: 0.785
outcome: partial_success
failure_modes:
- wrong_pattern
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/464
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 464 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted the five Entner-Doudoroff pathway variants and chose the right replacement targets. The main defect is the mapping qualifier syntax on the parent `GO:0061678` xrefs: the intended narrow matches are present, but encoded in a non-standard form that does not match GO convention.

## Strengths

- Correctly obsoleted all target variant terms.
- Correct replacement targets for both the ED variants and the glycolytic process variant.
- Removed active logical axioms and added obsoletion metadata.
- Preserved creation metadata on obsolete terms.

## Issues

- Encoded MetaCyc narrow matches as `{skos:narrowMatch="MetaCyc:..."}` rather than `{source="skos:narrowMatch"}`.
- Dropped an existing tracker item on `GO:0061680`.
- Comment wording is less precise than the human PR but not harmful.
