---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 27
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

gpt-5.5/codex obsoleted MONDO:0009327 correctly and rewired the dangling
MONDO:0007703 reference, with xref source qualifiers closely matching the gold.
This run's blob (`648307b`) is byte-identical to attempt #33. It diverges from
gold by adding the issue-tracker property onto the unrelated MONDO:0007703
stanza and by not removing `IAO:0006012`. F1 0.757 under-represents the
substantive correctness given the gold-omitted MONDO:0007703 fix.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  removed, `obsoletion_candidate` removed, `consider: MONDO:0005267` added,
  obsoletion reason `IAO:0000231 OMO:0001000`.
- Best xref-qualifier fidelity in the gpt-5.5/codex group: GARD →
  `MONDO:obsoleteEquivalent`, MEDGEN/UMLS → `MONDO:obsoleteEquivalent`,
  OMIM:140500/234750 → `MONDO:obsoleteEquivalentObsolete` (the correct
  obsolete-aware form, matching the gold for the OMIMs).
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule — improvement over gold.
- Documented methodology: read issue context incl. the MedGen comment, swept
  MONDO:0009327 references, ran ROBOT convert + `git diff --check`.

## Issues

- Did **not** remove `property_value: IAO:0006012 "2026-02-01"` (the scheduled
  obsoletion date). The gold removed it; once obsoleted the scheduled-date
  marker is stale. Genuine omission.
- Over-editing: stamped `property_value: IAO:0000233 "...issues/9771..."` onto
  the pre-existing MONDO:0007703 stanza (a different long-obsolete term);
  unnecessary, not done by the gold, contrary to "don't tag pre-existing
  terms".
- Changed `xref: GARD:0024658 {source="MONDO:GARD"}` to
  `MONDO:obsoleteEquivalent`; the gold left GARD unchanged. Minor divergence.
- Obsoletion comment is terse free text differing from gold;
  normalization-invisible, substantively acceptable.

Net: substantively correct obsoletion + correct dangling-ref fix; minor stale
`IAO:0006012` left behind and one gratuitous tag on an unrelated term.
