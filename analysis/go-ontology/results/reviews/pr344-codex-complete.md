---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 344
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/344
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 344 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the full coordinated change for issue #31945: GO:0003400 was obsoleted and replaced by GO:0048208, GO:0006901 and GO:0048208 were renamed to coat-assembly labels, and the relevant inline parent-label comments were refreshed. The 0.900 metadiff score is below perfect mostly because of comment wording and synonym-source attribution differences, not a substantive ontology problem.

## Strengths

- Correctly obsoleted GO:0003400 with obsolete-prefixed label/definition, removed logical definition axioms, `is_obsolete: true`, tracker provenance, and `replaced_by: GO:0048208`.
- Correctly promoted `vesicle coat assembly` and `COPII vesicle coat assembly` to primary labels while preserving the former labels as EXACT synonyms.
- Updated the GO:0016183, GO:0048200, and GO:0048208 inline `is_a: GO:0006901` label comments to `vesicle coat assembly`.
- Kept active-term definitions and logical axioms unchanged, matching the accepted conservative rename.
- The obsoletion comment captures the core biological distinction: annotated proteins are pathway participants, not upstream regulators.

## Issues

- No significant issues. The `COPII vesicle coating` synonym carries a broader set of source tags than the human PR, but the synonym itself and the ontology semantics are correct.
