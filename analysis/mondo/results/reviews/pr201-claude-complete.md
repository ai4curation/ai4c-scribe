---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 201
agent: std_claude_hai45
model: claude-haiku-4.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/201
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This attempt made exactly that single-line
`def.text` edit and scored F1=1.0 (precision=1.0, recall=1.0, Jaccard=1.0). The
metadiff accurately represents the quality: a byte-exact reproduction of human gold
PR #10094.

## Strengths

- Edited only the DOSDP source-of-truth YAML, matching the human's single-file,
  single-commit change; new text is identical to gold.
- Correctly addressed both parts of the issue (the `acquired` → `inherited`
  semantic fix and the `is has` → `has` grammar fix) and quoted the exact resulting
  text, demonstrating it understood the requested target precisely.
- Pinpointed the change to line 46, the exact line called out in the issue.
- Tight scope discipline: did not hand-edit the derived pattern OWL build artifacts
  or the sibling `inborn_metabolic.yaml`, avoiding the scope-creep failure seen in
  the codex attempts (#93, #176) — a good result for the smallest Claude model in
  the cohort.

## Issues

- The PR comment is minimal (a heading only); the substantive explanation is in the
  issue comment instead. This is a presentation nit with no effect on correctness.
- No substantive issues. The diff is identical to the accepted human PR after
  normalization and the scope matches the issue exactly.
