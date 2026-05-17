---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 336
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/336
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31114 --repo geneontology/go-ontology
    gh pr diff 32028 --repo geneontology/go-ontology
    gh pr diff 336 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent worked in the right terreic-acid area but combined the narrow #32028 metadata fix with broader label/definition changes and used the interim wrong `GOC:vw` convention. It changed `created_by` on `GO:0180067` and `GO:0180069` but missed `GO:0180068`, and it changed primary labels, synonyms, definitions, and the rendered label on a regulation axiom. The zero metadiff is mostly a scoring artifact for `created_by`, but this remains only a partial success.


## Strengths

- Identified `GO:0180067` and `GO:0180069` as relevant terms from issue #31114.
- Made the selected PR's kind of metadata edit on those two terms, replacing `PomBase:vw` values.
- The extra `terreic acid` label direction is based on actual issue discussion rather than hallucinated content.
- Did not edit unrelated ontology branches outside the terreic-acid cluster.


## Issues

- Missed `GO:0180068`, which was part of the three-term created-by correction.
- Used `created_by: GOC:vw`, which matches the interim selected PR but conflicts with the final convention established in follow-up PR #32032: bare `vw`.
- Over-scoped the metadata fix by changing labels, definitions, synonyms, and an intersection label.
- The attempt should receive credit for relevant work despite F1=0.0, but it would still need both a third metadata edit and cleanup of out-of-scope label/definition changes.
