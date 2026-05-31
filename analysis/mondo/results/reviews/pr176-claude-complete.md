---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 176
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.857
precision: 1.0
recall: 0.75
jaccard: 0.75
outcome: partial_success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/176
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` only (`acquired` →
`inherited`; `is has` → `has`). This attempt made that exact, correct fix to the
target file but additionally edited the sibling pattern
`src/patterns/dosdp-patterns/inborn_metabolic.yaml` (fixing its own `is has` typo).
F1=0.857 (precision=1.0, recall=0.75, Jaccard=0.75). Here the metadiff
**under-represents** quality somewhat: the recall hit comes from one extra
*defensible* line (a genuine grammar typo in a closely-related pattern), not from a
wrong or harmful edit — the core issue is fully and correctly resolved.

## Strengths

- The required fix is exactly correct: `inborn_metabolic_disrupts.yaml` line 46 now
  reads `An inherited metabolic disease that has its basis in the disruption of
  %s.`, identical to human gold PR #10094 (precision=1.0; the target edit is a
  perfect match).
- Correct root-cause understanding: identified `acquired` as a copy-paste error and
  recognized the logical definition was already correct, so only text needed
  changing.
- The one extra edit is **defensible, not harmful**: `inborn_metabolic.yaml` really
  does contain the same `is has` grammar slip, and fixing it improves consistency
  across the two inborn-metabolic templates. It is a real bug fix in the
  neighborhood, validated (YAML parsed, `git diff --check`).
- Restrained relative to its sibling codex run #93 (same family, gpt-5.5): it did
  NOT hand-edit the generated pattern OWL artifacts, which is the more serious
  scope error.

## Issues

- Scope creep (minor): the issue explicitly named only
  `inborn_metabolic_disrupts.yaml`; the human did not touch
  `inborn_metabolic.yaml`. Editing the sibling, while a genuine improvement, was
  not requested and is what costs recall here. A maximally disciplined agent would
  fix only the requested file and, at most, flag the sibling typo in a comment for
  curator follow-up.
- Net: a successful core resolution with one defensible out-of-scope cleanup —
  partial_success on scope grounds rather than any correctness defect. A curator
  would likely accept this with at most a note about scope.
