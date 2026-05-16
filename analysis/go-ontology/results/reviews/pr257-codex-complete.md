---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 257
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.87
precision: 0.909
recall: 0.833
jaccard: 0.769
outcome: partial_success
failure_modes:
- wrong_pattern
- missed_requirement
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31873
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32022
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/257
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31873 --repo geneontology/go-ontology
    gh pr diff 32022 --repo geneontology/go-ontology
    gh pr diff 257 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent mostly obsoleted GO:0061817, but it used `replaced_by: GO:0160214` instead of the human's consider-only pattern and it dropped the existing `created_by` and `creation_date` metadata. The 0.870 metadiff score is directionally fair: the core obsolete state is present, but the replacement semantics and provenance preservation are incomplete.

## Strengths

- Correctly prefixed the term name and definition for obsoletion.
- Removed the active synonym and parent relationships.
- Added `is_obsolete: true`, the issue tracker property, and a `consider` pointer to GO:0051643.

## Issues

- Wrong pattern: GO:0160214 should have been recorded as `consider: GO:0160214`; the human PR explicitly avoided `replaced_by` for this cross-namespace MF target.
- Missing requirement: the original `created_by` and `creation_date` lines were removed. Obsoletion should preserve term provenance metadata.
- The comment does not include the human PR's fuller guidance that GO:0160214 is the annotation migration target while GO:0051643 covers any residual BP aspect.
