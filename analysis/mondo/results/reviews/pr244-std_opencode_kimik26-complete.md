---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 244
agent: std_opencode_kimik26
agent_config_tag: v3
model: togetherai/moonshotai/Kimi-K2.6
runtime: opencode
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

The agent applied the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, replacing "An acquired metabolic disease that is has its basis in the disruption of %s." with "An inherited metabolic disease that has its basis in the disruption of %s." The diff is byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately represents perfect quality.

## Strengths

- Both requested corrections in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Clear, well-structured PR comment with a before/after table and a checklist; correctly identifies the bug as a copy-paste from `acquired.yaml`.
- Correct ontological reasoning: confirmed the `equivalentTo` clause already references inborn errors of metabolism (MONDO:0019052), so the logical definition was untouched and only the human-readable template was corrected.
- Tightly scoped — single file, single line, identical to the human PR; did not edit the sibling `inborn_metabolic.yaml` or any generated OWL artifacts.

## Issues

- None. Identical to gold and fully resolves the issue.
