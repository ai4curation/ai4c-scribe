---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 461
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/461
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31873 --repo geneontology/go-ontology
    gh pr diff 32022 --repo geneontology/go-ontology
    gh pr diff 461 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly made GO:0061817 obsolete, but it modeled the outcome as a direct replacement by GO:0160214 and omitted the GO:0051643 fallback. The 0.818 metadiff score reflects an incomplete obsoletion pattern rather than a failure to identify the right term.

## Strengths

- Correctly prefixed the obsolete term name and definition.
- Removed the active synonym and biological-process parent relationships.
- Added `is_obsolete: true` and the term tracker property.
- Identified GO:0160214 as the relevant molecular-function target.

## Issues

- Wrong pattern: the human PR intentionally used `consider: GO:0160214`, not `replaced_by: GO:0160214`, because the target is cross-namespace and curator judgment is needed.
- Missing requirement: the attempt omits `consider: GO:0051643`, which the human PR retained for the biological-process aspect.
- The shorter comment does not provide the annotation migration and BP fallback guidance included in the reference change.
