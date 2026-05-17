---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 330
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/330
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 asked for a precise two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`), leaving the logical definition unchanged. This
attempt made exactly that single-line `def.text` edit and scored F1=1.0
(precision=1.0, recall=1.0, Jaccard=1.0). The metadiff accurately represents the
quality — a byte-exact match to human gold PR #10094 — with a notably thorough
impact analysis in the PR comment.

## Strengths

- Edited only the DOSDP source-of-truth YAML, matching the human's single-file,
  single-commit change; new text is identical to gold.
- Strong impact awareness: the PR comment explicitly notes the pattern instantiates
  ~51 terms (citing concrete examples MONDO:0009825 "5-oxoprolinase deficiency",
  MONDO:0019222, MONDO:0017686) and that the fix corrects the text definition for
  all of them — exactly the multiplicative-impact reasoning the case brief flags as
  desirable for DOSDP edits.
- Correctly identified that the `equivalentTo` clause already references `inborn
  errors of metabolism` (MONDO:0019052) and therefore the logical definition needed
  no change — only the natural-language template.
- Did not hand-edit the derived pattern OWL artifacts or the sibling
  `inborn_metabolic.yaml`, avoiding the scope-creep failure seen in the codex
  attempts (#93, #176).

## Issues

- None. The diff is identical to the accepted human PR after normalization and the
  scope matches the issue exactly.
