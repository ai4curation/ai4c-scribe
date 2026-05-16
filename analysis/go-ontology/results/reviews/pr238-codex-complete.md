---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 238
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.818
precision: 0.818
recall: 0.818
jaccard: 0.692
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/238
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31873 --repo geneontology/go-ontology
    gh pr diff 32022 --repo geneontology/go-ontology
    gh pr diff 238 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made GO:0061817 obsolete and pointed at GO:0160214, but it used the wrong obsoletion relationship and removed existing provenance metadata. The metadiff score captures real issues: the core term is obsolete, yet the output is not a complete or clean GO obsoletion.

## Strengths

- Correctly added the `obsolete` name prefix, `OBSOLETE.` definition prefix, tracker property, and `is_obsolete: true`.
- Removed the prior synonym and active `is_a` relationships.
- Identified GO:0160214 as the relevant molecular-function target.

## Issues

- Wrong pattern: GO:0160214 should be a `consider` target, not `replaced_by`, for this cross-namespace MF correction.
- Missing requirement: the attempt omits `consider: GO:0051643`, so it loses the biological-process fallback retained by the human PR.
- Metadata regression: the original `created_by` and `creation_date` lines were removed. Those provenance fields should be preserved when obsoleting an existing term.
