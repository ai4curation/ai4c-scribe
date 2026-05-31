---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 405
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.8
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/405
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 405 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028` and added `replaced_by: GO:0038024`, so the core issue is solved. It also removed the old tracker and creator metadata like the human PR did. The main differences are a very terse obsoletion comment and an inline label on the `replaced_by` line; neither changes the intended migration, but the comment is less informative for future curators.


## Strengths

- Correctly changes the term label to `obsolete glycoprotein cargo receptor activity`.
- Correctly prefixes the definition with `OBSOLETE.` and removes the active parent relationship.
- Correctly adds `is_obsolete: true` and `replaced_by: GO:0038024`.
- Uses the current issue tracker for #31948 and drops the older tracker/creator metadata in line with the accepted PR's cleanup.
- No unrelated ontology terms were touched.


## Issues

- The obsoletion comment says only that the term was added in error. The human PR records the more useful rationale about glycoprotein substrate type being an unhelpful axis and transport domain plus `has_input` being the correct modeling approach.
- The `replaced_by` line includes an inline label comment (`! cargo receptor activity`), whereas the human PR used the bare ID. This is not a substantive error.
