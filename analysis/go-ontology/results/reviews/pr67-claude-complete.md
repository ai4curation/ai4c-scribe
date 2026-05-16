---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 67
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

This run produced an output blob (`048e8a8`) identical to attempts pr92 and pr64: the correct source edit (`only_in_taxon: NCBITaxon:2759` Eukaryota for `GO:0000956` and `GO:0141065`) plus committed regenerated derived artifacts (`only_in_taxon.ofn`, `go_taxon_constraints.owl`) causing thousands of lines of blank-node renumbering churn. The metadiff F1 of 0.005 severely under-represents the correctness of the underlying axiom change, which is dominated by derived-file noise the human PR never committed.

## Strengths

- Correct semantic modeling: a parent-level `only_in_taxon: NCBITaxon:2759` constraint on `GO:0000956` propagates to `GO:0070478`, `GO:0000184`, and the rest of the nuclear-transcribed mRNA decay subhierarchy — matching the curator's chosen resolution rather than the literal `never_in_taxon: Bacteria` request.
- Added `GO:0141065` maternal mRNA clearance, matching a gold-PR row.
- The added OWL axioms for `GO:0000956` (RO_0002160 some / RO_0002162 only NCBITaxon:2759) are correct and well-formed.

## Issues

- Scope creep / over-editing: committed regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl`; the human PR touched only the source TSV. Hundreds of `genidNNN` renumberings are pure noise that crater the metadiff and make the PR unreviewable.
- Omission: did not reproduce the gold PR's `GO:0140494` migrasome malformed-row cleanup (incidental, not derivable from the issue).
- Omission: did not add the third gold constraint `GO:0000958` mitochondrial mRNA catabolic process (already present in the eval base, so not a final-state error).
- Did not address the companion resolution step (PR #31677 added `GO:1990074` to `never_in_taxon.tsv` as Bacteria-only).
- Identical blob to pr92/pr64 confirms the regenerated-artifact behavior is a systematic gpt-5.5/opencode-codex pattern on this case, not stochastic.
