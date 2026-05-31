---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 388
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/388
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 388 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully performed the `GO:0005870` obsoletion. It removed the active-term axioms, marked the term obsolete, added `replaced_by: GO:0008290`, and included the issue tracker property. The attempt is substantively equivalent to the human PR.

## Strengths

- Correctly prefixed the name with `obsolete`.
- Correctly prefixed the definition with `OBSOLETE.`.
- Removed the `intersection_of` lines from the active logical definition.
- Correctly added `is_obsolete: true` and `replaced_by: GO:0008290`.
- Added issue #31956 tracker metadata.

## Issues

- No substantive issues. The obsoletion comment is not textually identical to the human PR but carries the same redundancy/replacement rationale.
