---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 676
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/676
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9987 requested a tightly-scoped two-part text fix on line 46 of
`src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` (`acquired` →
`inherited`; `is has` → `has`). This gpt-5.4/opencode attempt produced a diff
byte-identical to attempt #730: it makes the exact gold fix to
`inborn_metabolic_disrupts.yaml` (matching human PR #10094) plus the same
parallel `is has` → `has` grammar repair in the sibling `inborn_metabolic.yaml`.
F1=0.857 (precision=1.0, recall=0.75, Jaccard=0.75): the metadiff
*under-represents* quality. Recall is below 1.0 solely because the agent did
*more* than gold (one extra, correct, defensible edit), and precision=1.0
because every edit is right. The issue-scoped change is complete and correct.

## Strengths

- Reproduced the human gold change to `inborn_metabolic_disrupts.yaml` exactly:
  `An acquired metabolic disease that is has its basis...` →
  `An inherited metabolic disease that has its basis...`, covering both the
  `acquired`→`inherited` semantic error and the `is has`→`has` grammar typo
  the issue explicitly flagged.
- No spurious axiom edits: the logical definition (referencing `inborn errors
  of metabolism`, MONDO:0019052) was correctly left untouched; only the textual
  def template was changed.
- The extra `inborn_metabolic.yaml` edit fixes a real pre-existing bug — that
  file on mondo `main` still reads `An inherited metabolic disease that is has
  its basis in the disruption of %s.` (verified against the live source).
  Correcting the sibling pattern's identical `is has` typo is defensible QC
  cleanup, aligned with the case brief's observation that DOSDP pattern errors
  propagate multiplicatively across instantiated terms.
- Minimal, surgical diff (+2/-2 across the two pattern files) with no unrelated
  churn or serialization noise.

## Issues

- Scope creep (mild, defensible): the issue named only
  `inborn_metabolic_disrupts.yaml`; the additional `inborn_metabolic.yaml`
  edit exceeds the literal ask and is what depresses recall to 0.75 / F1 to
  0.857. The edit is correct and beneficial rather than erroneous; a strict
  reviewer would prefer it as a separate PR. The companion codex review (#676)
  characterizes the attempt as materially incomplete / `under_editing` — that
  framing is inverted here: the agent over-delivered (an extra correct hunk)
  and omitted nothing from the issue's scope (precision=1.0).
