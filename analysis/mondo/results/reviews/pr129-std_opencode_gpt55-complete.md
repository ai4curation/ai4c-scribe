---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 129
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

The agent made the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, changing "An acquired metabolic disease that is has its basis in the disruption of %s." to "An inherited metabolic disease that has its basis in the disruption of %s." Byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately represents perfect quality.

## Strengths

- Both requested corrections in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Good methodology: confirmed the logical `equivalentTo` clause already references inborn errors of metabolism so only the text template needed changing, and validated the edited YAML parses with PyYAML.
- Tightly scoped — single file, single line, identical to the human PR. Notably, this opencode/gpt-5.5 run kept scope discipline whereas the codex/gpt-5.5 run (#93) over-edited into sibling YAML and four generated OWL artifacts.

## Issues

- None. Identical to gold and fully resolves the issue. (Minor: the runtime footer is mislabeled "pi agent" while the metadata records `runtime: opencode` — a provenance-stamp inconsistency, not a quality issue.)
