---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 415
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.8
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: partial_success
failure_modes:
  - wrong_pattern
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/415
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 415 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent handled much of the lexical cleanup correctly, but it failed the main reclassification pattern. Instead of replacing `GO:1990351 ! transporter complex` with `GO:0062137 ! cargo receptor complex`, it added the cargo receptor parent while retaining the old transporter parent. That directly contradicts the issue's point that this complex should not remain classified as a generic transporter complex.

## Strengths

- Correctly updated the primary label and definition genus to cargo receptor complex language.
- Correctly added the new spelled-out cargo receptor EXACT synonym.
- Correctly demoted the transporter labels to BROAD synonyms.
- Added the issue #31935 tracker and preserved the existing transport participation relationship.

## Issues

- Retained `is_a: GO:1990351 ! transporter complex` alongside the new cargo receptor parent. This is the central modeling error: the requested change was a reclassification, not an additional parent.
- The PR narrative explicitly defends the two-parent model, so this was not just a mechanical omission.
- Also normalized the second `recognised` in the definition to `recognized`, which was outside the human edit.
- The line-based F1 is not enough to capture the severity of the retained old parent, because the most important conceptual change is the parent replacement.
