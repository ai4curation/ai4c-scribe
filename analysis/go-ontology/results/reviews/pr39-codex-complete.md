---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 39
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.8
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/39
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 39 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully obsoleted `GO:0008785` and used the correct replacement, `GO:0102039`. It also cleaned up two comments elsewhere that referred to the obsoleted activity. Those extra edits are outside the human PR and explain the lower metadiff, but they are related cleanup rather than a correctness problem.

## Strengths

- Correct obsolete name and definition prefixes.
- Correctly removed the active parent, added `is_obsolete: true`, and used `replaced_by: GO:0102039`.
- Preserved the existing tracker items and added #31961.
- Updated or removed stale comments that referenced the now-obsolete term.

## Issues

- Extra cleanup to `GO:0009321` and `GO:0070937` was not part of the accepted PR. It is defensible curation, but it broadens the review surface beyond the single-stanza human edit.
- The obsoletion comment is shorter than the human version and omits the explicit EC 1.11.1.26 rationale, but the replacement is still correct.
