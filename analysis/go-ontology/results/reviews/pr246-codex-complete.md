---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 246
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/246
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 246 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully completed the obsoletion. It marked `GO:0043713` obsolete, removed the active parent, added the #31966 tracker, and supplied the correct replacement term `GO:0140175`. The only meaningful difference from the human PR is that the obsoletion comment is shorter.

## Strengths

- Correctly performed the required obsoletion fields and parent removal.
- Correctly used `GO:0140175` as the replacement term.
- Kept the edit narrowly scoped to the target stanza.
- Produced a concise but accurate comment tying the obsolete term to the broader replacement activity.

## Issues

- No substantive issues. The PR and issue comments were sparse and the obsoletion comment lacks the full EC/RHEA explanation from the human PR, but the artifact itself is correct.
