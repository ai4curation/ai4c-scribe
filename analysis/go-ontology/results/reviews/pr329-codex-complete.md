---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 329
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.857
recall: 0.857
jaccard: 0.75
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31636
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31925
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/329
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 329 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed issue #31636 for `GO:1990334`. It renamed the term to the requested species-agnostic `SIN/MEN two-component GAP complex`, retained the budding yeast name as a narrow synonym, added the fission yeast narrow synonym, broadened the definition to cover Tem1/Spg1 and MEN/SIN biology, and added the tracker property. The F1 score of 0.857 reflects wording differences in the definition rather than a substantive ontology defect.

## Strengths

- Correctly changed the primary label from `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`.
- Added both expected narrow synonyms: `Bfa1-Bub2 complex` and `Byr4-Cdc16 GAP complex`.
- Rewrote the definition to cover the Tem1/Spg1 family GTPase context and both MEN and SIN signaling, matching the biological intent of the human PR.
- Preserved the existing `is_a: GO:1902773 ! GTPase activator complex` and `part_of GO:0005816 ! spindle pole body` assertions.
- Added the `term_tracker_item` property for issue #31636.
- Stayed tightly scoped to the target term in `src/ontology/go-edit.obo`.

## Issues

- No substantive ontology issues. The definition wording is not identical to the human PR, but it captures the same species-agnostic scope and functional meaning.
