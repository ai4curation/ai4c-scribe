---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 385
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.006
precision: 0.4
recall: 0.003
jaccard: 0.003
outcome: failure
failure_modes:
- over_editing
- scope_creep
- syntax_error
- missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs:
- 31677
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/385
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 385 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This attempt fails despite recognizing some of the relevant biology. It rewrote and re-sorted nearly the entire `only_in_taxon.tsv` file, introduced duplicate/conflicting rows, and constrained the narrower `GO:0000184` rather than the broader `GO:0000956` parent the curator chose. The result is unreviewable and incomplete.

## Strengths

- Correctly identified that the NMD branch is eukaryote-specific.
- Edited the relevant taxon-constraint source file rather than `go-edit.obo`.

## Issues

- Massive full-file rewrite/reorder of `only_in_taxon.tsv`.
- Introduced duplicate or conflicting rows and formatting problems.
- Constrained `GO:0000184` instead of the broader `GO:0000956`, leaving sibling nuclear-transcribed mRNA decay processes uncovered.
- Did not add clean targeted rows for `GO:0141065` and `GO:0000958`.
- Did not address companion PR #31677's `GO:1990074` never-in-taxon change.
