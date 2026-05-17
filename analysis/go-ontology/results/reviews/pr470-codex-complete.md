---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 470
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.011
precision: 0.8
recall: 0.006
jaccard: 0.006
outcome: failure
failure_modes:
- over_editing
- scope_creep
- syntax_error
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/470
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 470 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This attempt fails operationally. It includes some correct Eukaryota-only constraint intent, but it rewrote and re-sorted the whole `only_in_taxon.tsv` file, introduced duplicate rows and formatting regressions, and mixed in unrelated term movement. The small amount of useful taxon-constraint content is buried in destructive churn.

## Strengths

- Correctly recognized that nuclear-transcribed mRNA catabolism/NMD should be restricted to eukaryotes.
- Touched the taxon-constraint source file rather than attempting to model this in `go-edit.obo`.

## Issues

- Reordered and rewrote hundreds of unrelated `only_in_taxon.tsv` rows.
- Introduced duplicate rows and syntax/data quality regressions.
- Added or relocated unrelated constraints outside the issue scope.
- Did not cleanly reproduce the gold rows or the companion PR #31677 never-in-taxon step.
- The resulting PR would not be reviewable or mergeable without reverting the broad TSV churn.
