---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 385
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.006
precision: 0.400
recall: 0.003
jaccard: 0.003
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
  - syntax_error
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the copilot/Sonnet sibling of pr470: it rewrote and re-sorted the entire `only_in_taxon.tsv` (~990 changed lines) while adding `only_in_taxon: NCBITaxon:2759` for `GO:0000184` and a cluster of mitochondrial RNA-processing terms. Critically it did **not** add `GO:0000956` (the parent the curator constrained) and instead constrained only `GO:0000184`. The metadiff F1 of 0.006 accurately reflects a destructive, near-total failure.

## Strengths

- Correct high-level biology in the PR narrative: NMD requires nuclei, splicing, and the exon-junction complex and is therefore eukaryote-restricted.
- Targeted the correct file (`src/taxon_constraints/only_in_taxon.tsv`).

## Issues

- Massive over-editing: full-file reorder/rewrite of `only_in_taxon.tsv`, moving hundreds of unrelated rows. The gold PR changed 4 lines.
- Wrong target term for the parent constraint: the agent added `GO:0000184` (nuclear-transcribed mRNA catabolic process, nonsense-mediated decay) rather than the broader `GO:0000956` (nuclear-transcribed mRNA catabolic process) that @pgaudet chose. Constraining `GO:0000184` covers the NMD subbranch but not the sibling decay processes (no-go, non-stop, deadenylation-dependent) the curator's parent-level choice was designed to cover.
- Syntax/data regressions introduced by the reorder: duplicate rows (`GO:0005214`, `GO:0007159`, `GO:0008316`, `GO:0009887` duplicated with conflicting taxa), stray trailing space in `GO:0005883 ` neurofilament.
- Did not add `GO:0141065` maternal mRNA clearance as a clean targeted row matching the gold; did not address the companion `never_in_taxon` step (PR #31677, `GO:1990074`).
- Net effect: unmergeable. The correct-direction semantic intent is lost in destructive churn plus a sub-optimal parent choice.
