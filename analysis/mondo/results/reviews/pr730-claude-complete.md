---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 730
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
case_quality: good
f1: 0.857
precision: 1.0
recall: 0.75
jaccard: 0.75
outcome: success
failure_modes:
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9987
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10094
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/730
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This gpt-5.4/opencode attempt made that exact
fix — byte-identical to human gold PR #10094 — and additionally fixed the same
`is has` → `has` grammar typo in the sibling pattern file
`inborn_metabolic.yaml`. F1=0.857 (precision=1.0, recall=0.75, Jaccard=0.75):
the metadiff *under-represents* quality here. Recall is below 1.0 only because
the agent did *more* than gold (one extra defensible edit), not because it
missed anything; precision is a perfect 1.0 because every edit it made is
correct. The issue-scoped change is complete and correct.

## Strengths

- Reproduced the human gold change to `inborn_metabolic_disrupts.yaml` exactly:
  `An acquired metabolic disease that is has its basis...` →
  `An inherited metabolic disease that has its basis...`, addressing both the
  `acquired`→`inherited` semantic error and the `is has`→`has` grammar typo
  that issue #9987 explicitly called out.
- Correctly reasoned (per the PR comment) that the pattern's logical definition
  already references `inborn errors of metabolism` (MONDO:0019052), so only the
  generated textual definition needed correction — no spurious axiom edits.
- The extra edit to `inborn_metabolic.yaml` is a *genuine* pre-existing bug
  fix: that file's def template on mondo `main` still reads `An inherited
  metabolic disease that is has its basis in the disruption of %s.` (verified
  against the live source). Fixing the parallel `is has` typo in the sibling
  inborn-metabolic pattern is defensible quality-control cleanup, consistent
  with the case brief's note that pattern-file errors have multiplicative
  impact and agents should flag/repair such inconsistencies proactively.
- Methodology was sound: read `__issue_context__.json` for scope, grep-checked
  all `dosdp-patterns/*.yaml` for residual `is has its basis` after editing,
  reviewed the staged diff before committing, kept the diff minimal (+2/-2, no
  unrelated churn).

## Issues

- Scope creep (mild, defensible): the issue named only
  `inborn_metabolic_disrupts.yaml`; editing the sibling `inborn_metabolic.yaml`
  goes beyond the literal ask and is what lowers recall to 0.75 / F1 to 0.857.
  A strict reading would split this into a separate PR, but the edit is correct
  and beneficial, not an error. Note the companion codex review (#730) labeled
  this `under_editing` — that is inverted: the agent over-edited (extra correct
  hunk), it did not omit anything; precision=1.0 confirms no missing-or-wrong
  issue-scoped work.
