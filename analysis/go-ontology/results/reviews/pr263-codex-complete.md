---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 263
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.571
precision: 0.4
recall: 1.0
jaccard: 0.4
outcome: partial_success
failure_modes:
- missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs:
- 31677
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/263
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 263 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a clean, biologically sound source TSV edit, but it is incomplete against the union of the human resolution. It added Eukaryota `only_in_taxon` constraints for `GO:0000956` and `GO:0141065`, matching the curator's broad parent-level modeling strategy. It missed the `GO:0000958` row, the incidental migrasome formatting fix, and the companion `never_in_taxon` step from PR #31677.

## Strengths

- Correctly used `only_in_taxon.tsv` and `NCBITaxon:2759` Eukaryota rather than editing ontology terms.
- Correctly constrained `GO:0000956`, which covers the nuclear-transcribed mRNA decay branch more parsimoniously than per-leaf constraints.
- Correctly added `GO:0141065` maternal mRNA clearance.
- Kept the diff minimal and avoided generated artifact churn.

## Issues

- Did not add the gold PR's `GO:0000958` mitochondrial mRNA catabolic process Eukaryota constraint.
- Did not reproduce the incidental `GO:0140494` migrasome TSV formatting cleanup.
- Did not address the companion PR #31677 `never_in_taxon.tsv` addition for `GO:1990074`.
- Case caveat: the selected gold PR is partial and includes incidental cleanup, so the raw metadiff does not fully reflect issue-level quality.
