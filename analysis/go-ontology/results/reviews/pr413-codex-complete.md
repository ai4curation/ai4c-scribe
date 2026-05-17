---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 413
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- wrong_pattern
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/413
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 413 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent produced a clean and biologically defensible alternative resolution: it added `never_in_taxon: NCBITaxon:2` rows for NMD-related terms, which follows the reporter's literal request. However, the curator's accepted modeling used broader `only_in_taxon: Eukaryota` constraints in a different file and also included additional terms. The F1 of 0 is therefore misleading, but the attempt is still incomplete relative to the final human resolution.

## Strengths

- Correctly recognized that nonsense-mediated decay is not bacterial.
- Made a minimal source TSV edit in `never_in_taxon.tsv`.
- Covered a coherent set of NMD terms, including `GO:0000184`, `GO:0070478`, directional variants, regulatory terms, and the NMD complex.
- Avoided generated artifact churn.

## Issues

- Used the literal `never_in_taxon: Bacteria` pattern rather than the curator's broader `only_in_taxon: Eukaryota` modeling for `GO:0000956`.
- Did not add `GO:0141065` or `GO:0000958` Eukaryota constraints.
- Did not add the companion human PR #31677 row for `GO:1990074`.
- Case caveat: this is a defensible alternative resolution, but it does not match the selected partial gold PR.
