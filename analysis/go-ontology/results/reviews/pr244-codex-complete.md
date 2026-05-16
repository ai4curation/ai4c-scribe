---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 244
agent: std_opencode_gem4
model: gemma-4-31b
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
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31877
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31973
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/244
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 244 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made the correct minimal `go-edit.obo` obsoletion for `GO:0010381`, and the very low F1 is mostly an artifact of the gold PR's generated taxon-constraint OWL churn. However, the attempt is still incomplete: it used `replaced_by: GO:7770065` for a cross-aspect BP-to-MF obsoletion where curators settled on `consider:`, and it did not remove the obsolete term's four source `never_in_taxon.tsv` rows.

## Strengths

- Correctly marked `GO:0010381` obsolete with the obsolete name and definition pattern.
- Removed the active `is_a` and synonym assertions from the obsolete term.
- Added the issue #31877 tracker item and an obsoletion comment.
- Stayed scoped to `go-edit.obo`, avoiding the generated OWL churn that makes the human gold a poor scoring reference.

## Issues

- Used `replaced_by: GO:7770065` instead of `consider: GO:7770065`. Because this is a biological_process term pointing to a molecular_function term, automatic replacement is not appropriate.
- Missed the source taxon-constraint cleanup: the four `GO:0010381` rows should be removed from `src/taxon_constraints/never_in_taxon.tsv`.
- Did not provide much impact analysis in the PR body.
