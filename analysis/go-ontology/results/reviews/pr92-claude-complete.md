---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 92
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
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

The agent made the correct source edit — `only_in_taxon: NCBITaxon:2759` (Eukaryota) for `GO:0000956` and `GO:0141065` in `src/taxon_constraints/only_in_taxon.tsv` — the same parent-level strategy the curator chose, but it then also committed the regenerated derived artifacts (`only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl`), producing thousands of lines of blank-node (`genid`) renumbering churn. The metadiff F1 of 0.005 severely under-represents the biological correctness of the underlying change; the score is dominated by derived-file noise the human PR never committed.

## Strengths

- Correct semantic edit and modeling: constraining the parent `GO:0000956` to Eukaryota propagates to `GO:0070478`, `GO:0000184`, and the rest of the nuclear-transcribed mRNA decay subhierarchy — exactly @pgaudet's chosen resolution.
- Added `GO:0141065` maternal mRNA clearance, matching a gold-PR row and the in-thread list.
- Strong methodology reporting: pre/post `make travis_build`, `make check_all_taxon_constraints_columns`, and term verification via `obo-grep.pl`; chose the broader `only_in_taxon: Eukaryota` over a narrow `never_in_taxon: Bacteria` per the skill's parsimony guidance.
- The actual added OWL axioms for `GO:0000956` (RO_0002160 some + RO_0002162 only Eukaryota) are correct and well-formed.

## Issues

- Scope creep / over-editing: committed regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl`. The human PR touched only the source TSV; the generated OWL is rebuilt by CI. The hundreds of `genidNNN` renumberings are pure noise that make the PR effectively unreviewable and crater the metadiff.
- Omission: did not reproduce the gold PR's `GO:0140494` migrasome malformed-row cleanup (not derivable from the issue, so excusable).
- Omission: did not add the third gold constraint `GO:0000958` mitochondrial mRNA catabolic process (correctly noted it was already present in the eval base, so not a final-state error, but the PR is not fully comparable to the human source edit).
- Did not address the companion resolution step (PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process to `never_in_taxon.tsv` as Bacteria-only).
- Identical output blob (`048e8a8`) to attempts pr67 and pr64; the regenerated-artifact behavior is a systematic gpt-5.5 issue here, not a one-off.
