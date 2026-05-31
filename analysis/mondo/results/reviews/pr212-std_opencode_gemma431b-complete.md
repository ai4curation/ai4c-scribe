---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 212
agent: std_opencode_gem4
agent_config_tag: v3
model: togetherai/google/gemma-4-31B-it
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

Despite being the smallest model in the cohort, the agent made the exact single-line fix requested by issue #9987 in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`, changing "An acquired metabolic disease that is has its basis in the disruption of %s." to "An inherited metabolic disease that has its basis in the disruption of %s." Byte-identical to gold PR #10094 (blob `a1b9149`); F1=1.0 accurately represents perfect quality.

## Strengths

- Both requested corrections applied in the single `def.text` line: semantic ("acquired" → "inherited") and grammar ("is has" → "has").
- Correct, concise rationale: recognized the pattern is for inborn errors of metabolism (not acquired disease) and the "is has" was a grammar error.
- Tightly scoped — single file, single line, identical to the human PR; no over-editing into sibling files or generated artifacts. A strong result for a 31B model on a task where two larger codex runs lost scope discipline.

## Issues

- The PR comment is terse and does not explicitly confirm the logical `equivalentTo` clause was already correct (other attempts cited MONDO:0019052). This is a documentation thinness, not a correctness defect — the edit itself is exactly right and matches gold.
