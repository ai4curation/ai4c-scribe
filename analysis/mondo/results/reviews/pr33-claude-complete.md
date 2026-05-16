---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 33
agent: std_codex_gpt5.5
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.757
precision: 0.824
recall: 0.700
jaccard: 0.609
outcome: success
failure_modes:
  - scope_creep
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/codex re-run; the produced blob (`648307b`) is byte-identical to
attempt #27, so the assessment is the same: a substantively correct obsoletion
of MONDO:0009327 plus the gold-omitted MONDO:0007703 dangling-reference fix,
with the same two minor defects (stale `IAO:0006012` left in place; issue-link
property gratuitously added to the unrelated MONDO:0007703 stanza). F1 0.757
under-represents quality because the MONDO:0007703 rewiring it correctly
performs is absent from the gold.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  parents removed, `obsoletion_candidate` removed, `consider: MONDO:0005267`
  added, obsoletion reason `IAO:0000231 OMO:0001000`.
- Xref qualifiers closely match gold: GARD/MEDGEN/UMLS →
  `MONDO:obsoleteEquivalent`, OMIM:140500/234750 →
  `MONDO:obsoleteEquivalentObsolete` (correct obsolete-aware convention).
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config's no-dangling-reference rule;
  a real improvement over the gold.
- Consistent, deterministic output across the two codex runs (#27 ≡ #33),
  indicating stable behavior on this task.

## Issues

- Stale `property_value: IAO:0006012 "2026-02-01"` not removed; the gold
  removed it (scheduled-obsoletion date is moot once obsoleted). Omission.
- Over-editing: `IAO:0000233` issue link added to the pre-existing
  MONDO:0007703 stanza; unnecessary, contrary to "don't tag pre-existing
  terms", not done by the gold.
- GARD xref source changed (`MONDO:GARD` → `MONDO:obsoleteEquivalent`) where
  the gold left it unchanged; minor style divergence.
- Free-text comment differs from gold wording; normalization-invisible,
  substantively acceptable.

Net: identical to #27 — correct obsoletion + correct dangling-ref fix with two
minor blemishes. Deterministic reproduction is a positive signal.
