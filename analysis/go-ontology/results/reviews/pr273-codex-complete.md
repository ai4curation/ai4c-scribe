---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 273
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32044
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32054
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/273
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32044 --repo geneontology/go-ontology
    gh pr diff 32054 --repo geneontology/go-ontology
    gh pr diff 273 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly added the requested `GO:7770074` term with the accepted label, definition, parent, PMID, and issue tracker. It is missing one of the two exact synonyms from the human PR and did not perform the sibling `GO:0016266` spelling/tracker cleanup. This is still a useful partial success because the core new term is biologically correct and correctly placed.


## Strengths

- Correctly created `GO:7770074` with the requested label and parent `GO:0006493`.
- Used the accepted definition text and PMID `35536957`.
- Added the important exact synonym `protein O-linked GlcNAcylation`.
- Added the issue tracker for #32044.
- Kept the edit scoped to adding the new term and did not damage existing stanzas.


## Issues

- Missed the exact synonym `protein O-linked N-acetylglucosaminylation` that the human PR added.
- Missed all `GO:0016266` sibling-term harmonization from the human PR.
- `created_by` and `creation_date` differ from the curator metadata in the accepted PR.
