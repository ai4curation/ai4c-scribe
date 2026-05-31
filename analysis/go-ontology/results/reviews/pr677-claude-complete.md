---
ontology: go-ontology
issue_number: 32046
pr_number: 32047
eval_repo_pr: 677
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.667
precision: 0.733
recall: 0.611
jaccard: 0.500
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced a diff byte-identical to eval PR #629 (same blob `72fef7d`): both requested receptor terms created correctly, but with an out-of-scope third term `left-handed Z-RNA binding` (GO:7770072) that shifts the dsRNA and Z-RNA receptor terms to GO:7770073 and GO:7770074, off-by-one from the gold IDs. The gold standard's logical definition on the dsRNA receptor term (`intersection_of: GO:0038023` ∩ `has_primary_input CHEBI:67208`) was omitted. F1 of 0.667 fairly captures a biologically-correct-but-incompletely-axiomatised, slightly over-scoped result. This run additionally documents thorough methodology in its PR/issue comments. Partial success.

## Strengths

- **Both receptor terms correct and correctly hierarchised**: `double-stranded RNA immune receptor activity` under `GO:0038187 pattern recognition receptor activity`, and `left-handed Z-RNA immune receptor activity` as its child — matching the gold parent-child structure.
- **Definitions drop "across the cell membrane" appropriately**, matching gold and the real sibling `GO:0001873 polysaccharide immune receptor activity` (cytosolic sensors NLRP1/NLRP6/MDA5/ZBP1).
- **Synonyms match gold exactly** ("dsRNA immune receptor activity" / "Z-RNA immune receptor activity", both EXACT).
- **`has_part GO:0003725 double-stranded RNA binding`** on the dsRNA receptor term matches gold.
- **Strong, transparent methodology**: the PR comment documents pre/post `make travis_build` validation, `linkml-reference-validator` reference checks, a complete and specific checklist, term-search for existing receptor/binding/dsRNA terms, and explicit (if ultimately over-scoped) rationale for the modelling choices. All four PMIDs are validated with correct titles.
- The agent honestly explains *why* it added the binding term (to support consistent immune-receptor modelling) — good communication even though the decision diverges from gold.

## Issues

- **Out-of-scope extra term (scope/precision)**: `GO:7770072 left-handed Z-RNA binding` was not requested and is absent from the gold PR. The gold curator intentionally left the Z-RNA receptor unaxiomatised (cf. the unaxiomatised `GO:0003692 left-handed Z-DNA binding`) rather than mint a new binding class. The agent's stated rationale ("keep modeling consistent... particularly for Z-RNA") is defensible but over-engineers a tightly-scoped request; this drives the reduced precision (0.733).
- **ID drift**: the spurious binding term consumes GO:7770072, so the two requested receptor terms become GO:7770073 / GO:7770074 instead of the gold GO:7770072 / GO:7770073. Allocation difference, not a biology error, but it depresses the metadiff.
- **Missing equivalence axiom on the dsRNA receptor term (under-editing/recall)**: gold carries `intersection_of: GO:0038023 ! signaling receptor activity` + `intersection_of: has_primary_input CHEBI:67208 ! double-stranded RNA`. The agent explicitly chose "weaker asserted axioms rather than adding `intersection_of` axioms" — but `CHEBI:67208` for double-stranded RNA does exist and the gold term (plus higher-scoring attempts #354/#289) uses exactly this compositional pattern. Omitting it is a genuine completeness gap, the main cause of recall=0.611, not merely a style choice.
- **Extra `has_part GO:7770072` on the Z-RNA receptor term**, absent from the deliberately minimal gold Z-RNA term — internally consistent with the agent's (out-of-scope) binding term but diverging from gold.

Core biology and hierarchy correct with good process documentation, but an avoidable omission of the standard equivalence axiom and an unrequested extra binding term keep this from being a clean success.
