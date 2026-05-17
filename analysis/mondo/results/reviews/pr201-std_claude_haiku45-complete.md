---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 201
agent: std_claude_hai45
agent_config_tag: v3
model: claude-haiku-4-5-20251001
runtime: claude
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

The agent applied the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, replacing "An acquired metabolic disease that is has its basis in the disruption of %s." with "An inherited metabolic disease that has its basis in the disruption of %s." Byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately represents perfect quality.

## Strengths

- Both requested corrections applied in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Tightly scoped — single file, single line at line 46, identical to the human PR by sabrinatoro (approved first time). No over-editing into the sibling `inborn_metabolic.yaml` or generated OWL files.
- Clear issue comment stating the corrected text precisely.

## Issues

- None. Identical to the gold standard and fully resolves the issue's two-part request. A solid result for the smallest Claude model in the cohort.
