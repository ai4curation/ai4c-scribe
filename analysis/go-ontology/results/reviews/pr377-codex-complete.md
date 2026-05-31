---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 377
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: hard
f1: 0.016
precision: 0.008
recall: 0.8
jaccard: 0.008
outcome: partial_success
failure_modes:
- wrong_pattern
- missed_requirement
case_quality: poor
case_quality_reason: gold_pr_self_contradicting_generated_artifact_noise
companion_prs:
- 31929
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/377
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 377 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made the same clean `go-edit.obo` obsoletion as its sibling attempts. It correctly avoided generated-file churn, but it did not fully match the curator-endorsed final behavior: the obsolete BP term should `consider` the new MF term rather than use `replaced_by`, and the source taxon-constraint rows for the obsolete term should be removed.

## Strengths

- Correctly obsoleted `GO:0010381` and removed active classification/synonym content.
- Added issue provenance and a reasonable obsoletion comment.
- Demonstrated useful design-pattern awareness for peroxisome-organelle membrane tether activity terms.
- Kept the diff limited to `go-edit.obo`.

## Issues

- Used `replaced_by: GO:7770065` instead of `consider: GO:7770065` for a cross-aspect BP-to-MF obsoletion.
- Missed the required cleanup of four `GO:0010381` rows from `never_in_taxon.tsv`.
- Did not report meaningful build validation.
