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
precision: 0.4
recall: 0.002
jaccard: 0.002
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/92
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 92 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a biologically reasonable core fix for issue #31670 by adding an `only_in_taxon` Eukaryota constraint to `GO:0000956` (nuclear-transcribed mRNA catabolic process), which should cover `GO:0070478` and related nuclear/nonsense-mediated mRNA decay descendants, and by adding the same constraint for `GO:0141065` (maternal mRNA clearance). However, compared with the human PR it missed part of the curated TSV delta and introduced large generated-file churn in `only_in_taxon.ofn` and `go_taxon_constraints.owl`. The very low metadiff score (F1 0.005) overstates the biological failure because the central requested constraint was addressed, but it correctly flags that the PR shape differs substantially from the human solution.

## Strengths

- Correctly chose the broader `only_in_taxon: NCBITaxon:2759` pattern rather than a narrow direct `never_in_taxon: NCBITaxon:2` assertion, matching the human solution's strategy of excluding bacteria by constraining eukaryote-specific mRNA decay processes to Eukaryota.
- Added `GO:0000956 nuclear-transcribed mRNA catabolic process` to Eukaryota, which is the important parent-level fix for the reported bacterial use of `GO:0070478 nuclear-transcribed mRNA catabolic process, 3'-5' exonucleolytic nonsense-mediated decay`.
- Added `GO:0141065 maternal mRNA clearance` to Eukaryota, matching one of the human PR's related-term additions.
- The agent's PR notes show it checked the relevant term hierarchy and recognized that constraining a parent term was preferable to patching only `GO:0070478`.

## Issues

- The agent did not add the human PR's `GO:0000958 mitochondrial mRNA catabolic process` Eukaryota row in `src/taxon_constraints/only_in_taxon.tsv`. The agent said this row was already present in its checkout, so this may be a baseline mismatch rather than a reasoning error, but relative to the gold-standard diff it under-edited the requested family of mRNA catabolic processes.
- The agent did not make the human PR's cleanup to `GO:0140494 migrasome`, where the TSV row was corrected from a malformed/too-narrow `NCBITaxon:7742` entry to `NCBITaxon:2759 Eukaryota` with the PMID sources in the proper column. This was not central to the issue text, but it is part of the accepted human fix.
- The agent regenerated and committed `src/taxon_constraints/only_in_taxon.ofn` and `src/ontology/imports/go_taxon_constraints.owl`, producing hundreds of blank-node identifier changes for unrelated terms. The human PR touched only `only_in_taxon.tsv`, and the GO action reported the classified ontology was identical, so these generated-file edits are noisy over-editing for this task.
- Because the generated OWL was committed without the `GO:0140494` TSV correction, it preserved the bad migrasome taxon constraint/source structure rather than converging to the human PR's cleaned TSV semantics.
