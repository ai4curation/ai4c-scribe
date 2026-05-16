---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 327
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.75
precision: 0.75
recall: 0.75
jaccard: 0.6
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31295
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32040
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/327
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31295 --repo geneontology/go-ontology
    gh pr diff 32040 --repo geneontology/go-ontology
    gh pr diff 327 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully created `GO:7770070 p24 cargo receptor complex` with the correct parent and process relationship. The remaining differences from the human PR are definition wording and synonym string choices, not ontology errors.

## Strengths

- Correctly placed the term under `GO:0062137 ! cargo receptor complex`.
- Correctly added `capable_of_part_of GO:0006888`.
- Avoided over-localizing the cycling complex with a fixed `part_of` location.
- Included useful p24/TMED synonyms and all relevant PMID support.
- Stayed scoped to the requested new term.

## Issues

- No substantive issues. The synonym set and definition wording differ from the human PR but remain semantically acceptable.
