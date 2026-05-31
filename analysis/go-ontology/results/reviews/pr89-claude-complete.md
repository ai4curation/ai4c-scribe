---
ontology: go-ontology
issue_number: 32046
pr_number: 32047
eval_repo_pr: 89
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.765
precision: 0.867
recall: 0.684
jaccard: 0.619
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt produced the **identical diff** (blob `a7c1bb2`) to attempt #109 — same gpt-5.5/opencode configuration. The agent created both terms with the fully correct gold-standard axiomatisation for GO:7770072 (parentage, `GO:0038023` ∩ `has_primary_input CHEBI:67208`, `has_part GO:0003725`) plus a sound `is_a`-based GO:7770073. F1 0.765 (recall 0.684) is driven entirely by additive over-generation, not by errors. Partial success: correct content, weak scope discipline.

## Strengths

- **GO:7770072 axiomatisation is identical to gold**: `is_a: GO:0038187`, `intersection_of: GO:0038023`, `intersection_of: has_primary_input CHEBI:67208`, `relationship: has_part GO:0003725`.
- **GO:7770073** correctly placed `is_a: GO:7770072` with no fabricated logical definition for Z-RNA — consistent with the GO:0003692 precedent.
- Definitions correctly omit "across the cell membrane" (cytosolic sensors), matching gold and sibling GO:0001873.
- EXACT synonyms ("dsRNA immune receptor activity", "Z-RNA immune receptor activity") and PMID-to-receptor assignments are correct.

## Issues

- **Synonym over-generation (over_editing / scope_creep)** — the main recall hit. Adds unrequested BROAD synonyms on both terms ("double-stranded RNA receptor activity", "dsRNA receptor activity", "left-handed Z-RNA receptor activity", "Z-RNA receptor activity"), none of which are in the gold.
- **Extra `has_part GO:0003725` on GO:7770073**, absent in the gold's deliberately minimal Z-RNA term. Defensible but divergent.
- Minor: "Combining with a double-stranded RNA molecule and..." inserts "molecule"; off-pattern relative to gold/GO:0001873.
- This attempt's file contains only the diff (no PR/issue comment, no checklist), so methodology evidence is absent here; the substance is identical to #109 whose comment documents PMID validation.

Correct ontology content; the entire F1 gap is strippable additive extras. Duplicate of attempt #109 (same blob a7c1bb2) — should be deduplicated in aggregate scoring.
