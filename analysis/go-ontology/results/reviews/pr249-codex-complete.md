---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 249
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.857
recall: 0.857
jaccard: 0.75
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31636
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31925
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/249
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31636 --repo geneontology/go-ontology
    gh pr diff 31925 --repo geneontology/go-ontology
    gh pr diff 249 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent partially addressed issue #31636 for `GO:1990334`. It made the central species-agnostic label change, added the two expected narrow synonyms, and added the issue tracker property. However, it did not actually broaden the definition to cover both MEN/Tem1 and SIN/Spg1. The metadiff score of 0.857 is therefore too generous for ontology quality: the term now has the right name and synonyms, but the definition remains the old budding-yeast-specific text.

## Strengths

- Correctly changed the primary label from `Bfa1-Bub2 complex` to `SIN/MEN two-component GAP complex`.
- Correctly added `Bfa1-Bub2 complex` as a `NARROW` synonym, preserving the old species-specific label.
- Correctly added `Byr4-Cdc16 GAP complex` as a `NARROW` synonym for the fission yeast counterpart.
- Preserved the existing `is_a` and `part_of` structure for the cellular component term.
- Added the `term_tracker_item` property for issue #31636, matching the provenance pattern in the human PR.

## Issues

- Missed the requested definition update. The agent left the definition text focused only on `Tem1 GTPase`, the mitotic exit network (MEN), and `Bub2/Bfa1`, whereas the human PR broadened it to `Tem1/Spg1`, MEN/SIN, and generic complex wording.
- Dropped the `GOC:bhm` definition xref while leaving the old definition text otherwise unchanged. That is a small metadata regression relative to both the original term and the human PR.
