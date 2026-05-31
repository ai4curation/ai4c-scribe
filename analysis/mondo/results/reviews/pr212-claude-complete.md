---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 212
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/212
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 asked for a precise two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This attempt — notable for being a small (31B)
open model — made exactly that single-line `def.text` edit and scored F1=1.0
(precision=1.0, recall=1.0, Jaccard=1.0). The metadiff accurately represents the
quality: a byte-exact reproduction of human gold PR #10094.

## Strengths

- Edited only the DOSDP source-of-truth YAML, matching the human's single-file,
  single-commit change; new text is identical to gold.
- Correct semantic understanding stated concisely: "The pattern is intended for
  inborn errors of metabolism, not acquired diseases," and identified `is has` as a
  grammatical error.
- Tight scope discipline despite being a much smaller model than most of the
  cohort: did not hand-edit the derived pattern OWL artifacts or the sibling
  `inborn_metabolic.yaml`, avoiding the scope-creep failure seen in the codex
  attempts (#93, #176). This is a strong result for a 31B model on a task where two
  larger codex models over-edited.

## Issues

- The PR comment does not explicitly note that the logical `equivalentTo` clause
  was already correct (MONDO:0019052) — a minor documentation gap relative to the
  Opus/Kimi/Copilot attempts — but the edit itself correctly left the logic
  untouched, so there is no substantive issue.
- No substantive issues. The diff is identical to the accepted human PR after
  normalization and the scope matches the issue exactly.
