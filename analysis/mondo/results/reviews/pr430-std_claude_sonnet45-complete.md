---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 430
agent: std_claude_sonnet45
agent_config_tag: v3
model: claude-sonnet-4-5-20250929
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

The agent made the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, changing the `def.text` template from "An acquired metabolic disease that is has its basis in the disruption of %s." to "An inherited metabolic disease that has its basis in the disruption of %s." This is byte-identical to gold PR #10094 (blob `a1b9149`). F1=1.0 accurately represents the quality — this is a perfect resolution.

## Strengths

- Both requested corrections applied in the single `def.text` line: the semantic fix ("acquired" → "inherited") and the grammar fix ("is has" → "has").
- Tightly scoped: touched only the one file and one line the issue identified, matching the human's `pr_author: sabrinatoro` PR exactly (1 addition, 1 deletion).
- The agent's issue comment correctly explains both fixes; no spurious edits to the logical `equivalentTo` clause (which correctly references inborn errors of metabolism, MONDO:0019052, and required no change).

## Issues

- None. The diff is identical to the gold standard and fully satisfies the issue's explicit two-part request.
