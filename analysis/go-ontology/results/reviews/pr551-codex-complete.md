---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 551
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31873
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32022
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/551
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31873 --repo geneontology/go-ontology
    gh pr diff 32022 --repo geneontology/go-ontology
    gh pr diff 551 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent completed the mechanical obsoletion of GO:0061817, but it used `replaced_by: GO:0160214` where the human PR and issue discussion deliberately used `consider` for the MF target. The 0.870 metadiff score reflects this substantive pattern mismatch: the term is obsolete, but the replacement semantics are too strong for this BP-to-MF correction.

## Strengths

- Correctly renamed the term with the `obsolete` prefix and prefixed the definition with `OBSOLETE.`.
- Removed the prior synonym and `is_a` relationships.
- Added `is_obsolete: true`, the issue tracker property, and a `consider` pointer to GO:0051643.
- Preserved the existing creation metadata.

## Issues

- Wrong pattern: `GO:0160214` should be a `consider` target, not a `replaced_by` target. The source issue explicitly notes the curator should check the correct MF annotation, and the human PR avoided `replaced_by` for both targets.
- Missing requirement: because GO:0160214 is expressed only as `replaced_by`, the final term lacks the human PR's `consider: GO:0160214` guidance.
- The obsoletion comment is much less informative than the human comment about annotation migration and the residual BP aspect.
