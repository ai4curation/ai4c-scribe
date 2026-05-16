---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 463
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.964
precision: 0.952
recall: 0.976
jaccard: 0.93
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31882
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32036
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/463
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31882 --repo geneontology/go-ontology
    gh pr diff 32036 --repo geneontology/go-ontology
    gh pr diff 463 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the final obsoletion decision for issue #31882. It obsoleted both `GO:0097711` and `GO:1905353`, set both as `replaced_by: GO:1905349`, and removed the now-invalid `starts_with GO:0097711` relationship from `GO:0060271`. The score is slightly below perfect because of harmless metadata and comment wording differences, not because of a missed ontology requirement.

## Strengths

- Correctly handled both target terms, not just the term named in the issue title.
- Added the expected obsolete names, `OBSOLETE.` definition prefixes, issue tracker property values, `is_obsolete: true`, and replacement target.
- Removed the active logical structure from both obsolete stanzas.
- Deleted the dangling `starts_with` relationship from `GO:0060271`, matching the human PR's modeling choice.

## Issues

- No substantive issues. The agent retained `created_by` and `creation_date` provenance lines that the human PR removed, and it used shorter obsoletion comments, but the ontological result is correct and complete.
