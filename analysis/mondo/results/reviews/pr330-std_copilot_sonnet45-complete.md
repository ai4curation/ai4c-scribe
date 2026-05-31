---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 330
agent: std_copilot_son45
agent_config_tag: v3
model: claude-sonnet-4.5
runtime: copilot
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
case_type: axiom_repair
difficulty: simple
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

The agent made the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, converting "An acquired metabolic disease that is has its basis in the disruption of %s." to "An inherited metabolic disease that has its basis in the disruption of %s." Byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately reflects perfect quality.

## Strengths

- Both requested corrections applied in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Good validation narrative: correctly notes the `equivalentTo` clause already references inborn errors of metabolism (MONDO:0019052) so only the text template needed changing; cites concrete affected terms generated from the pattern (e.g., 5-oxoprolinase deficiency MONDO:0009825, inborn aminoacylase deficiency MONDO:0017686), demonstrating awareness that DOSDP pattern edits have multiplicative impact across ~51 instantiated terms.
- Tightly scoped — single file, single line, matching the human PR exactly; did not over-reach into the sibling `inborn_metabolic.yaml`.

## Issues

- None. Identical to the gold standard and fully resolves the issue's two-part request.
