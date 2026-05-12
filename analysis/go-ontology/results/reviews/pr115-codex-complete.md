---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 115
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: gpt-5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/115
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 115 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:0005870` (actin capping protein of dynactin complex) with direct replacement `GO:0008290` (F-actin capping protein complex), matching the human PR on all structural ontology edits. The F1 score of 0.9 slightly under-represents the quality of the solution: the only diff-level mismatch is the exact `comment` text, not a missing obsoletion step.


## Strengths

- Applied the expected GO obsoletion pattern to `GO:0005870`: renamed the label with the `obsolete` prefix, prefixed the definition with `OBSOLETE.`, and preserved the existing definition xrefs (`GOC:jl`, `PMID:18221362`, `PMID:18544499`).
- Removed both logical-definition axioms from the obsolete term, including the genus `intersection_of: GO:0008290` and the `part_of GO:0005869` differentia, matching the human PR and avoiding active logical classification for an obsolete term.
- Added the required obsoletion metadata: `property_value: term_tracker_item` pointing to issue `31956`, `is_obsolete: true`, and `replaced_by: GO:0008290`.
- Stayed tightly scoped to the requested term. No unrelated cellular component terms were edited, and the agent reported checking that no other GO terms referenced `GO:0005870`.


## Issues

- Minor wording issue: the agent's obsoletion comment says the reason is that `GO:0005870` is "equivalent to F-actin capping protein complex." The issue and human PR support replacement by `GO:0008290`, but the old logical definition was actually `GO:0008290` plus `part_of GO:0005869` (dynactin complex), so the human wording ("redundant with GO:0008290" and annotations can migrate) is more precise.
- No substantive ontology-editing omissions were found.
