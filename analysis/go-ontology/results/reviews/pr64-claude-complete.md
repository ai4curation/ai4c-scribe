---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 64
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.005
precision: 0.400
recall: 0.002
jaccard: 0.002
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent made the correct source edit — `only_in_taxon: NCBITaxon:2759` (Eukaryota) for `GO:0000956` and `GO:0141065` in `src/taxon_constraints/only_in_taxon.tsv`, matching the curator's parent-level strategy — and additionally ran `/research` (logged a validated `RESEARCH.md`) before committing the regenerated derived artifacts (`only_in_taxon.ofn`, `go_taxon_constraints.owl`). The metadiff F1 of 0.005 severely under-represents the biological correctness; the score is dominated by `genid` renumbering churn in the regenerated OWL that the human PR never committed. Output blob (`048e8a8`) is identical to pr92 and pr67.

## Strengths

- Correct semantic modeling: parent-level `only_in_taxon: NCBITaxon:2759` on `GO:0000956` covers `GO:0070478` (reported term) and the whole nuclear-transcribed mRNA decay branch via inheritance — the curator's chosen approach, more parsimonious than per-leaf `never_in_taxon: Bacteria`.
- Added `GO:0141065` maternal mRNA clearance, matching a gold-PR row.
- Best-documented methodology of the gpt-5.5 trio: explicit pre/post `make travis_build`, `make check_all_taxon_constraints_columns`, `obo-grep.pl` term verification, and `linkml-reference-validator` on its research excerpts.
- The added OWL axioms for `GO:0000956` are correct and well-formed.

## Issues

- Scope creep / over-editing: committed regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl`; the human PR touched only the source TSV. Hundreds of blank-node renumberings make the PR unreviewable and crater the metadiff.
- Omission: did not reproduce the gold PR's `GO:0140494` migrasome malformed-row cleanup (incidental, not derivable from the issue).
- Omission: did not add the third gold constraint `GO:0000958` mitochondrial mRNA catabolic process (already present in the eval base, so not a final-state error, but the PR is not fully comparable to the human source edit).
- Did not address the companion resolution step (PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process to `never_in_taxon.tsv` as Bacteria-only).
- Consistent with the pre-existing codex self-review, which also graded this `partial_success`. The identical blob across pr92/pr67/pr64 confirms the regenerated-artifact behavior is systematic for gpt-5.5 here.
