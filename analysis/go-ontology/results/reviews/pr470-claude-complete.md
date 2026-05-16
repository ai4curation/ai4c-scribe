---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 470
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.011
precision: 0.800
recall: 0.006
jaccard: 0.006
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
  - syntax_error
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent did add a biologically correct `only_in_taxon: NCBITaxon:2759` (Eukaryota) constraint for `GO:0000956` (and `GO:0000184`), but it then **re-sorted and rewrote the entire `only_in_taxon.tsv` file** (~970 changed lines), moving hundreds of unrelated rows and introducing duplicate rows. The metadiff F1 of 0.011 correctly represents this as a near-total failure: the genuinely useful two-line change is buried in massive destructive churn and new errors.

## Strengths

- The underlying biological judgment was sound: it recognized NMD/nuclear-transcribed mRNA catabolism is eukaryote-specific and added `only_in_taxon: NCBITaxon:2759` for `GO:0000956` and related mitochondrial RNA-processing terms.
- Edited the correct file family (`src/taxon_constraints/only_in_taxon.tsv`) and used the `/taxon-constraint` skill conceptually.

## Issues

- Massive over-editing: the agent reordered the whole TSV (deleting and re-inserting the first several rows, alphabetizing/relocating the entire file). The human PR touched 3 lines plus one formatting fix; this PR rewrites the file. This is the dominant failure mode and makes the PR unreviewable and unmergeable.
- Syntax/data errors introduced: the diff introduces duplicate rows (e.g. `GO:0005214 structural constituent of chitin-based cuticle` appears twice; `GO:0007159 leukocyte cell-cell adhesion` duplicated with conflicting taxa; `GO:0009887 animal organ morphogenesis` duplicated; a stray trailing space in `GO:0005883 ` neurofilament). These are regressions not present in the base file.
- Scope creep: dozens of unrelated terms (immune, plant, bacterial, Golgi/ER component terms) were added or relocated that have nothing to do with issue #31670.
- Did not add `GO:0141065` maternal mRNA clearance as a clear targeted row matching the gold (the change is lost in the reorder noise), and did not address the companion `never_in_taxon` step (PR #31677, `GO:1990074`).
- Net effect: even though the correct semantic axiom is present somewhere in the diff, the PR cannot be accepted; the destructive reformatting and introduced duplicates outweigh the correct content.
