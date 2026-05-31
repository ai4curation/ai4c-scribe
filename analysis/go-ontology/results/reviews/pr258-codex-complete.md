---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 258
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/258
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 258 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent produced a clean, mostly correct obsoletion of `GO:0010381` in `go-edit.obo`. The raw metadiff score is misleading because the selected gold includes generated-file noise that curators had instructed should not be committed. Substantively, the remaining problems are the cross-aspect `replaced_by` relation and the missing source TSV taxon-constraint cleanup.

## Strengths

- Correctly changed the term to `obsolete peroxisome-chloroplast membrane tethering`.
- Correctly prefixed the definition with `OBSOLETE.` and removed the active parent/synonym structure.
- Added the issue tracker property and obsoletion comment.
- Avoided committing generated taxon-constraint artifacts.
- Documented annotation impact and the relationship to the new MF term reasonably well.

## Issues

- Used `replaced_by: GO:7770065` where `consider: GO:7770065` is the curator-endorsed pattern for BP-to-MF obsoletion.
- Did not remove the four `GO:0010381` rows from `never_in_taxon.tsv`, leaving source constraints pointing at an obsolete term.
- Full build validation was not available in the eval environment.
