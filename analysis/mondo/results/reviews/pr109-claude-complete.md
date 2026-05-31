---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 109
agent: std_opencode_g55
model: gpt-5.5
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/109
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This gpt-5.5/opencode attempt made exactly that
single-line `def.text` edit and scored F1=1.0 (precision=1.0, recall=1.0,
Jaccard=1.0). The metadiff accurately represents the quality: a byte-exact
reproduction of human gold PR #10094. As with sibling run #129, this is correctly
minimal whereas the same model under the codex runtime (#93) over-edited.

## Strengths

- Edited only the DOSDP source-of-truth YAML, matching the human's single-file,
  single-commit change; new text is identical to gold.
- Correctly reasoned that the pattern's logical definition already uses `inborn
  errors of metabolism` (MONDO:0019052) and that only the generated textual
  definition (which also carried the `is has` typo) needed correction.
- Made "the minimal change" and "committed only the edited pattern file" —
  explicit, correct scope discipline that the same model failed to apply under the
  codex runtime (#93).
- Validated the YAML parses before committing.

## Issues

- None. The diff is identical to the accepted human PR after normalization and the
  scope matches the issue exactly.
