---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 119
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 1.0
recall: 0.5
jaccard: 0.5
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31601
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32007
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/119
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31601 --repo geneontology/go-ontology
    gh pr diff 32007 --repo geneontology/go-ontology
    gh pr diff 119 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made the gold-standard edit to `GO:0140597` protein carrier activity, replacing the older "binding to and carrying..." definition with the requested parent-aligned "Directly binding..." wording while preserving `PMID:7628437`. It also edited `GO:0140309` unfolded protein holdase activity, which is a defensible consistency/grammar cleanup but was not part of the merged human PR. The metadiff F1 of 0.667 mostly reflects this extra edit rather than a missed core requirement.


## Strengths

- Correctly updated `GO:0140597` to exactly match the human PR: `Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location.`
- Preserved the existing definition xref `PMID:7628437` and did not alter relationships, synonyms, intersections, or metadata for `GO:0140597`.
- The change is ontologically coherent with `GO:0140597`'s logical definition as `GO:0140104` molecular carrier activity with primary input protein.
- The additional `GO:0140309` edit kept the same reference (`PMID:39488384`) and improved the existing grammatical error from "it's being delivers" to "it is being delivered."


## Issues

- The agent over-edited relative to the gold-standard PR by also changing `GO:0140309` unfolded protein holdase activity. Human PR #32007 was intentionally scoped to `GO:0140597`; `GO:0140309` had already received the original issue-body update before that PR.
- The `GO:0140309` wording change is plausible, but it was not explicitly in the final human patch and subtly rewrites "escorts it..." to "directly binds...and delivers it either...", so it should have been left out or called out as a separate proposed follow-up.
