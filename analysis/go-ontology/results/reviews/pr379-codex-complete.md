---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 379
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.852
precision: 0.86
recall: 0.845
jaccard: 0.742
outcome: partial_success
failure_modes:
- wrong_pattern
- missed_requirement
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/379
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 379 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent completed the core obsoletion work but made two real curation mistakes. It used non-standard MetaCyc xref qualifier syntax on the active parent term, and it left obsolete-term synonyms on two obsolete stanzas. The replacement targets are correct, but the patch is not clean enough to count as a full success.

## Strengths

- Correctly obsoleted all five target Entner-Doudoroff variant terms.
- Correctly used `GO:0061678` and `GO:0006096` as replacement targets.
- Removed the key active logical axioms and added issue tracker metadata.
- Added the intended MetaCyc variant pathway IDs to the parent term at the content level.

## Issues

- Used malformed mapping qualifiers like `{skos:narrowMatch="MetaCyc:..."}` instead of the GO-standard `{source="skos:narrowMatch"}`.
- Left `synonym: "gluconate pathway" RELATED []` on obsoleted terms where the human PR removed obsolete-term synonyms.
- Dropped a pre-existing tracker item on `GO:0061680`.
