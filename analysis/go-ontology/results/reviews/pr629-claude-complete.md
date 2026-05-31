---
ontology: go-ontology
issue_number: 32046
pr_number: 32047
eval_repo_pr: 629
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

The agent created both requested receptor terms with correct names, synonyms, parentage and biologically accurate definitions, but introduced an out-of-scope third term — `left-handed Z-RNA binding` — and gave it the ID GO:7770072, shifting both receptor terms down by one ID (dsRNA receptor → GO:7770073, Z-RNA receptor → GO:7770074) relative to the gold standard. It also omitted the gold standard's logical definition (the `intersection_of: GO:0038023` ∩ `has_primary_input CHEBI:67208` equivalence axiom) on the dsRNA receptor term. F1 of 0.667 fairly represents a partly-correct result: the core biology is right but the axiomatisation is incomplete on one side and over-extended on the other. This is a partial success.

## Strengths

- **Both requested receptor terms are biologically correct**: `double-stranded RNA immune receptor activity` is correctly a child of `GO:0038187 pattern recognition receptor activity`, and `left-handed Z-RNA immune receptor activity` is correctly a child of the new dsRNA receptor term — exactly the parent-child hierarchy the gold PR establishes.
- **Correct judgment dropping "across the cell membrane"**: the definitions match the gold and the real sibling term `GO:0001873 polysaccharide immune receptor activity` ("...transmitting the signal to initiate an innate immune response"), correctly recognising NLRP1/NLRP6/MDA5/ZBP1 as cytosolic sensors.
- **Synonyms match gold exactly**: "dsRNA immune receptor activity" EXACT and "Z-RNA immune receptor activity" EXACT, with sensible trimming of the requester's typo.
- **`has_part GO:0003725 double-stranded RNA binding`** on the dsRNA receptor term matches the gold standard.
- All four PMIDs (33243852, 34678144, 23273991 for dsRNA; 32200799 for Z-RNA) are carried correctly and map accurately to the cited receptors.

## Issues

- **Out-of-scope extra term (scope/precision)**: the agent invented `GO:7770072 left-handed Z-RNA binding`, which the issue never requested and the gold PR did not create. The gold curator deliberately left the Z-RNA term unaxiomatised, mirroring `GO:0003692 left-handed Z-DNA binding`, rather than minting a new binding class. This is the primary driver of the reduced precision (0.733) and an unrequested ontology addition a reviewer would likely strip.
- **ID drift from gold**: because the spurious binding term took GO:7770072, the dsRNA receptor is GO:7770073 and the Z-RNA receptor is GO:7770074, none of which align with the gold IDs (GO:7770072 / GO:7770073). This penalises the metadiff but is not in itself a biological error (IDs are allocated, not semantically meaningful).
- **Missing logical definition on the dsRNA receptor term (under-editing/recall)**: the gold standard term carries `intersection_of: GO:0038023 ! signaling receptor activity` + `intersection_of: has_primary_input CHEBI:67208 ! double-stranded RNA` (the canonical `signaling_receptor_activity_by_input` equivalence axiom). The agent asserted only `is_a` + `has_part`, omitting the equivalence axiom entirely. This is the main cause of the reduced recall (0.611) and is a genuine completeness gap, not just style — the higher-scoring attempts (#354, #289) reproduced this axiom.
- **Extra `has_part` on the Z-RNA receptor term**: `relationship: has_part GO:7770072 ! left-handed Z-RNA binding` is added to GO:7770074; the gold Z-RNA term has no `has_part`. This is consistent with the agent's own (out-of-scope) modelling but diverges from the deliberately minimal gold term.

Core task substantially achieved (both receptor terms, correct hierarchy and biology) but with a notable omission (the equivalence axiom) and an out-of-scope extra term causing ID drift. Defensible reasoning, partially over-engineered relative to the tightly-scoped gold.
