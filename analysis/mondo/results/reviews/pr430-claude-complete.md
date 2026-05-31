---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 430
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/430
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 asked for a precise two-part text fix on line 46 of the DOSDP pattern
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`: `acquired` → `inherited`
and the grammar slip `is has` → `has`, while leaving the logical `equivalentTo`
clause (correctly `'inborn errors of metabolism'`, MONDO:0019052) untouched. This
attempt made exactly that single-line `def.text` edit and nothing else, scoring
F1=1.0 (precision=1.0, recall=1.0, Jaccard=1.0). The metadiff score accurately
represents the quality here: this is a byte-faithful reproduction of the human gold
PR #10094.

## Strengths

- Edited only the DOSDP source-of-truth YAML (`inborn_metabolic_disrupts.yaml`),
  exactly matching the human's single-commit, single-file change.
- Correct semantic fix: new text reads `An inherited metabolic disease that has its
  basis in the disruption of %s.`, identical to gold.
- Did not regenerate or hand-edit the derived pattern OWL artifacts
  (`pattern.owl`, `pattern-simple.owl`, `pattern-merged.owl`,
  `pattern-with-imports.owl`, `dosdp-pattern.owl`) — these are build outputs and
  hand-editing them is the scope-creep failure seen in the codex attempts (#93,
  #176). Avoiding them is the correct curation discipline.
- Left the sibling `inborn_metabolic.yaml` alone; that file's `is has` typo is real
  but out of scope for this issue and was not touched by the human.
- Tight scope discipline: recognized this as a tightly-scoped, single-term
  axiom_repair and resisted broadening it.

## Issues

- None. The diff is identical to the accepted human PR after normalization, and the
  scope matches the issue exactly. The PR comment is terse but accurate.
