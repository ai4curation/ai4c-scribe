---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 370
agent: std_claude_op47
model: claude-opus-4.7
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/370
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`), leaving the logical definition untouched. This
attempt made precisely that single-line `def.text` edit and scored F1=1.0
(precision=1.0, recall=1.0, Jaccard=1.0). The metadiff faithfully represents the
quality: a byte-exact reproduction of human gold PR #10094, accompanied by the
strongest verification narrative of any attempt in this case.

## Strengths

- Edited only the DOSDP source-of-truth YAML, exactly matching the human's
  single-file, single-commit change; new text is identical to gold.
- Best-documented reasoning of the cohort: the PR comment explicitly verifies that
  the `equivalentTo` clause (line 51) still references `'inborn errors of
  metabolism'` (MONDO:0019052 via the `classes` block, line 17) and confirms
  `pattern_name` and `description` are consistent with the corrected wording — i.e.
  it independently re-derived why "inherited" is the semantically correct fix
  rather than just pattern-matching the issue text.
- Correctly concluded the logical definition needed no change and that only the
  natural-language `def.text` template was wrong.
- Did not touch the derived pattern OWL build artifacts or the sibling
  `inborn_metabolic.yaml`, avoiding the scope-creep failure mode exhibited by the
  codex attempts (#93, #176).
- Exemplary scope discipline: committed only the single modified file.

## Issues

- None. The diff matches the accepted human PR exactly after normalization, the
  scope is precisely the issue's ask, and the verification is sound.
