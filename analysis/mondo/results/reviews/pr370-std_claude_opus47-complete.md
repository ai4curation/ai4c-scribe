---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 370
agent: std_claude_op47
agent_config_tag: v3
model: claude-opus-4-7
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

The agent applied the exact single-line fix requested by issue #9987, changing the `def.text` template in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` from "An acquired metabolic disease that is has its basis in the disruption of %s." to "An inherited metabolic disease that has its basis in the disruption of %s." The diff is byte-identical to gold PR #10094 (blob `a1b9149`). F1=1.0 accurately represents perfect quality, and the methodology here is the strongest of the cohort.

## Strengths

- Both requested corrections in the single line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Excellent verification methodology documented in the PR comment: confirmed the `equivalentTo` clause still references `'inborn errors of metabolism'` (MONDO:0019052) so the logical definition was already correct and needed no change; confirmed `pattern_name` and `description` are consistent with the new wording; explicitly checked no other occurrences of the buggy phrase were touched.
- Correct scope discipline — single file, single line, identical to the human's PR by sabrinatoro (approved first time by katiermullen). Critically, the agent did NOT chase the same `is has` typo into the sibling `inborn_metabolic.yaml` (which the issue did not ask for and the human never fixed), unlike the two codex attempts.

## Issues

- None. Identical to gold, fully satisfies the issue, with the best-documented reasoning of all attempts.
