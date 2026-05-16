---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 370
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/370
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 370 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully resolved issue #31636 for `GO:1990334`. It made the requested species-agnostic rename, preserved both species-specific complex names as narrow synonyms, updated the definition to describe both the budding yeast MEN/Tem1 and fission yeast SIN/Spg1 cases, and added the tracker metadata. The metadiff score is below perfect because the definition wording differs from the human PR, not because the ontology change is materially incomplete.

## Strengths

- Correctly renamed `GO:1990334` to `SIN/MEN two-component GAP complex`.
- Correctly added `Bfa1-Bub2 complex` and `Byr4-Cdc16 GAP complex` as `NARROW` synonyms.
- Replaced the old MEN-only definition with a broader definition that explicitly includes both S. cerevisiae MEN/Tem1 and S. pombe SIN/Spg1 contexts.
- Preserved existing classification and partonomy assertions.
- Added the issue #31636 `term_tracker_item` property.
- Kept the edit limited to the target term.

## Issues

- No substantive ontology issues. The definition is more example-driven than the human PR's wording, but it supports the same species-agnostic label and preserves the intended complex function.
