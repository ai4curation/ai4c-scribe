---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 139
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.5
precision: 1.0
recall: 0.333
jaccard: 0.333
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31601
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32007
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/139
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31601 --repo geneontology/go-ontology
    gh pr diff 32007 --repo geneontology/go-ontology
    gh pr diff 139 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly made the gold-standard edit to `GO:0140597` protein carrier activity, changing the definition to the parent-aligned "Directly binding..." wording used in human PR #32007. It also edited `GO:0140309` unfolded protein holdase activity, including a definition rewrite and comment grammar fix, which is plausible but outside the final human PR scope. The metadiff F1 of 0.5 is low because the agent added extra lines, but it under-represents the fact that the central accepted edit was exact.


## Strengths

- Correctly updated `GO:0140597` to match the human PR exactly: `Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location.`
- Preserved the existing definition xref `PMID:7628437` for `GO:0140597` and did not alter its synonyms, logical definition, parentage, or metadata.
- The `GO:0140597` wording is ontologically coherent with its parent `GO:0140104` molecular carrier activity, specializing "specific ion or molecule" to protein.
- The additional `GO:0140309` edits retained `PMID:39488384` and fixed real grammar problems in the existing text, changing "it's being delivers" to "it is being delivered" and "an holdase" to "a holdase."


## Issues

- The agent over-edited relative to the merged human solution by changing `GO:0140309` unfolded protein holdase activity. Human PR #32007 was intentionally limited to `GO:0140597`; the PR text says `GO:0140309` had already been updated previously per the original issue body.
- The `GO:0140309` definition rewrite goes beyond a typo fix: it changes "binds to a protein in an unfolded state and escorts it..." to "directly binds to a protein in an unfolded state and delivers it either..." This is a reasonable harmonization with `GO:0140597`, but it was not part of the final accepted patch and should have been proposed separately.
