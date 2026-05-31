---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 549
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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
  - wrong_pattern
  - over_editing
case_quality: poor
case_quality_reason: gold_pr_used_interim_wrong_created_by_convention
companion_prs: [32014, 32032]
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31114
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32028
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/549
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31114 --repo geneontology/go-ontology
    gh pr diff 32028 --repo geneontology/go-ontology
    gh pr diff 549 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This is a poor scoring case: PR #32028 changed `created_by: PomBase:vw` to `GOC:vw`, but follow-up PR #32032 corrected the convention to bare `vw`, and OBO metadiff ignores `created_by` fields. The agent partially found the relevant metadata problem, but it repeated the interim `GOC:vw` convention, missed one of the three gold metadata edits, and added extra definition/synonym changes.

## Strengths

- Correctly identified `GO:0180067` and `GO:0180069` as terms needing `created_by` attention.
- Preserved the `terreate` logical definition using `CHEBI:233617`, which is consistent with the chemical-entity modeling convention.
- Added a human-facing `terreic acid` synonym on `GO:0180069`, which is related to the broader issue discussion even though it was not part of PR #32028.

## Issues

- Used `GOC:vw`, the interim convention from the selected gold PR, rather than the final-correct bare `vw` convention from PR #32032.
- Missed the third `created_by` edit in PR #32028, though that hunk concerns a different issue and contributes to the poor case quality.
- Added a definition rewrite and synonym edit to `GO:0180069`; these are issue-adjacent but not part of the selected human PR.
- The zero score should not be read literally. It is mostly a metadiff limitation plus a flawed gold reference, but the artifact is still only a partial resolution of the issue discussion.
