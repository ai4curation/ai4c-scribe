---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 237
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
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

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/237
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 237 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the accepted obsoletion of `GO:7770028` glycoprotein cargo receptor activity. It adds the obsolete name/definition, removes the active parent, adds `is_obsolete: true`, and uses `replaced_by: GO:0038024`, matching the issue's intended migration. The metadiff score is below exact match only because the obsoletion comment and some metadata cleanup differ from the human PR.


## Strengths

- Correctly marks `GO:7770028` obsolete and routes users/annotations to `GO:0038024` cargo receptor activity.
- Removes the active `is_a` relationship so the obsolete term no longer participates in the live classification hierarchy.
- Uses an obsoletion comment that captures the main ontology rationale: glycoprotein substrate type is not a useful classification axis for cargo receptors.
- Adds the current issue tracker for #31948 and avoids unrelated changes.
- Keeps the edit in the correct single stanza and preserves the original definition text as obsolete historical text.


## Issues

- The comment is worded differently from the human PR and in some variants is less explicit about `has_input` as the right way to represent substrates.
- Metadata cleanup differs slightly from the accepted PR, especially around the older issue tracker or original creator metadata.
- These are minor curation differences; the central obsoletion and replacement are correct.
