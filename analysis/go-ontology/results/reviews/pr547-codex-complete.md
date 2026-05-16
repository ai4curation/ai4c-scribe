---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 547
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/547
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 547 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully obsoleted `GO:7770028 glycoprotein cargo receptor activity` and used the correct replacement, `GO:0038024 cargo receptor activity`. It removed the active parent, added the obsolete markers, added the current tracker, and supplied an appropriate obsoletion comment. Differences from the human PR are comment wording and retained historical provenance.

## Strengths

- Correct target term and correct replacement term.
- Correctly removed the active `is_a: GO:0038024` assertion before adding `replaced_by: GO:0038024`.
- Added `is_obsolete: true`, obsolete name/definition prefixes, and the #31948 tracker.
- The rationale correctly identifies substrate type as an unhelpful cargo-receptor classification axis.

## Issues

- No substantive issues. The agent retained older provenance lines and used a shorter comment than the human PR, but the obsoletion itself is correct and complete.
