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
precision: 0.4
recall: 0.002
jaccard: 0.002
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/67
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 67 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent partially solved the taxon-constraint request by adding Eukaryota-only constraints for `GO:0000956` and `GO:0141065`, which addresses the main problem of bacterial annotations to `GO:0070478` and related nuclear/NMD mRNA decay terms. The metadiff F1 of 0.005 under-represents the semantic overlap because the agent chose the same broad `GO:0000956` strategy, but it also reflects real mismatch: the agent omitted the human PR's `GO:0140494` TSV cleanup and committed noisy generated taxon-constraint artifacts.


## Strengths

- Correctly avoided editing `go-edit.obo` or adding a narrow direct constraint only to `GO:0070478`; constraining `GO:0000956` "nuclear-transcribed mRNA catabolic process" to `NCBITaxon:2759` is a good broad fix because `GO:0070478` is a child in that nuclear-transcribed mRNA decay branch.
- Added `GO:0141065` "maternal mRNA clearance" as only-in Eukaryota, matching one of the curator-listed additions in the issue comment.
- Used the same taxon-constraint style as the human PR for the source rows: `only_in_taxon.tsv` entries with `NCBITaxon:2759` / `Eukaryota`, rather than an explicit `never_in_taxon.tsv` entry for `NCBITaxon:2`.
- The generated OWL/OFN additions for `GO:0000956` and `GO:0141065` are internally consistent with the TSV source rows, using `RO_0002160 some NCBITaxon_2759` and `RO_0002162 only NCBITaxon_2759`.


## Issues

- The agent did not reproduce the human PR's cleanup for `GO:0140494` "migrasome". The human changed a malformed/overly narrow row from `NCBITaxon:7742` with the label/evidence shifted into later columns to a clean Eukaryota-only row (`NCBITaxon:2759`, label `Eukaryota`, evidence `PMID:40712579|PMID:25342562`); the agent left that problem untouched.
- The agent's diff does not add a new source-row change for `GO:0000958` "mitochondrial mRNA catabolic process", which was one of the curator-listed/human PR additions. In the agent PR base context `GO:0000958` already appears to have an Eukaryota-only row, so this may be a base-state mismatch rather than a functional omission, but the submitted diff is still not the same complete curated patch.
- The PR over-edits generated artifacts: `src/taxon_constraints/only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl` are committed with many blank-node renumbering changes around unrelated terms. Those generated changes add review noise and account for much of the very low precision/recall relative to the small human TSV-only PR.
- Row placement differs from the human solution. This is probably not semantically important, but the human PR grouped the new rows together near the existing tail of `only_in_taxon.tsv`, while the agent inserted `GO:0000956` and `GO:0141065` into earlier blocks, making the edit harder to compare.
