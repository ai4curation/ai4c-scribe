---
ontology: go-ontology
issue_number: 31877
pr_number: 31973
eval_repo_pr: 454
agent: std_claude_son45
model: claude-sonnet-4.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/454
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31877 --repo geneontology/go-ontology
    gh pr diff 31973 --repo geneontology/go-ontology
    gh pr diff 454 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent completed the central `go-edit.obo` obsoletion for `GO:0010381`, and its very low metadiff score mostly reflects the flawed gold's generated-file churn. It remains a partial success because it used automatic `replaced_by` across ontology aspects and did not remove the obsolete term's taxon-constraint source rows.

## Strengths

- Correctly changed the name and definition to obsolete form.
- Correctly removed the active `is_a` and synonym lines.
- Added `is_obsolete: true`, issue tracker provenance, and an obsoletion comment.
- Avoided committing generated OFN/OWL files.

## Issues

- Used `replaced_by: GO:7770065` rather than the final-correct `consider: GO:7770065`.
- Missed the `never_in_taxon.tsv` cleanup for the four rows that reference `GO:0010381`.
- PR documentation was thin compared with the better attempts.
