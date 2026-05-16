---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 343
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/343
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 343 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a clean and well-reasoned `go-edit.obo` obsoletion for `GO:0010381`, and its low F1 is mostly due to not reproducing generated artifact churn in the flawed gold PR. It is still only a partial success because it used `replaced_by` for a cross-aspect BP-to-MF target and missed the `never_in_taxon.tsv` cleanup.

## Strengths

- Correctly applied the obsolete name, definition prefix, tracker, comment, and `is_obsolete: true` pattern.
- Correctly removed the active parent and synonym from the obsolete term.
- Explained the MF modeling rationale and annotation impact clearly.
- Avoided the generated taxon-constraint OWL churn.

## Issues

- Used `replaced_by: GO:7770065` rather than `consider: GO:7770065`; curators explicitly avoid automatic replacement across ontology aspects.
- Did not remove the four `GO:0010381` entries from `src/taxon_constraints/never_in_taxon.tsv`.
- The attempt's claimed validation did not catch the cross-aspect `replaced_by` problem.
