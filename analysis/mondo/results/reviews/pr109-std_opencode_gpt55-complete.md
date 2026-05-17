---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 109
agent: std_opencode_g55
agent_config_tag: v3
model: openai/gpt-5.5
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

The agent applied the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, replacing "An acquired metabolic disease that is has its basis in the disruption of %s." with "An inherited metabolic disease that has its basis in the disruption of %s." Byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately represents perfect quality. (This is a second opencode/gpt-5.5 run, parallel to #129.)

## Strengths

- Both requested corrections in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Correct ontological reasoning: explicitly notes the pattern's logical definition already uses `inborn errors of metabolism` (MONDO:0019052), so only the generated textual definition was wrong; validated YAML parses post-edit.
- Tightly scoped — single file, single line, identical to the human PR; minimal change with no over-editing into the sibling pattern or generated OWL artifacts.

## Issues

- None. Identical to gold and fully resolves the issue. Reproduces the perfect result of the parallel opencode/gpt-5.5 run (#129), confirming stability of this configuration on the task.
