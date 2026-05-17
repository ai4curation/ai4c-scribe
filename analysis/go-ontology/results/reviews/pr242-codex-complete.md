---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 242
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
- scope_creep
- wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31114
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32028
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/242
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31114 --repo geneontology/go-ontology
    gh pr diff 32028 --repo geneontology/go-ontology
    gh pr diff 242 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed parts of the broader terreic-acid issue, but it did not cleanly solve the selected PR #32028 task. It changed `created_by` from `PomBase:vw` to `GOC:vw` on `GO:0180067` and `GO:0180069`, but missed the third human-PR target `GO:0180068`; it also bundled label, synonym, and definition changes from the separate label-swap discussion. The F1 of 0.0 is misleading because `created_by` edits are ignored by metadiff, but the attempt is still only a partial success and follows the interim wrong `GOC:vw` convention rather than the final `vw` correction.


## Strengths

- Identified two relevant terreic-acid terms, `GO:0180067` and `GO:0180069`, from issue #31114.
- Made the selected PR's intended kind of metadata change on those two terms by replacing `created_by: PomBase:vw`.
- The label/synonym direction, making `terreic acid ...` primary and `terreate ...` a synonym, is grounded in the broader issue discussion and open PR #32014.
- Did not introduce changes outside the terreic/terreate term cluster.


## Issues

- Missed `GO:0180068`, the negative-regulation term whose `created_by` value was changed in human PR #32028 and final PR #32032.
- Used `created_by: GOC:vw`, which reproduces the interim human PR but is not the final GO convention; follow-up PR #32032 corrected these fields to bare `vw`.
- Over-scoped the selected #32028 task by changing labels, synonyms, and definitions for `GO:0180067` and `GO:0180069`. Those changes belong to the separate label-swap discussion, not the created-by metadata fix.
- The metadiff score is not a useful quality signal here because it ignores `created_by`, but the missing third term and wrong final convention are real issues.
