---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 275
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.811
precision: 0.882
recall: 0.750
jaccard: 0.682
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

kimi-k2.6/opencode produced one of the most complete and correct solutions in
the set: a textbook Mondo obsoletion of MONDO:0009327 plus the MONDO:0007703
rewiring, with xref source qualifiers matching the gold exactly
(`MONDO:obsoleteEquivalent` for MEDGEN/UMLS, `MONDO:obsoleteEquivalentObsolete`
for the two OMIMs). The F1 of 0.811 **under-represents** quality; the recall
penalty comes almost entirely from the MONDO:0007703 fix that the gold omitted
and from a synonym-citation addition.

## Strengths

- Obsoletion exactly matches gold on the load-bearing edits: name change,
  `is_obsolete: true`, both `is_a` removed, `obsoletion_candidate` removed,
  `IAO:0006012` removed, `consider: MONDO:0005267` added.
- Xref source qualifiers match the gold precisely:
  MEDGEN:6748/UMLS:C0018798 → `MONDO:obsoleteEquivalent`, OMIM:140500/234750 →
  `MONDO:obsoleteEquivalentObsolete`. This is the correct obsolete-aware
  convention and most attempts got the OMIM form wrong.
- Fixed the dangling MONDO:0007703 `replaced_by: MONDO:0009327` → `consider:
  MONDO:0005267`, per the agent config's explicit "no relationship should point
  to an obsolete term" rule. Correctly recognized this is a real defect the
  gold left behind.
- Strong rationale in PR body: correctly explained the OMIM split underlying
  the obsoletion and verified no remaining references to MONDO:0009327.

## Issues

- Added `[MONDO:Lexical]` as the synonym citation, changing
  `synonym: "heart, malformation of" EXACT []` to `EXACT [MONDO:Lexical]`. The
  gold kept the empty brackets. This is a defensible cleanup (empty evidence
  brackets are non-ideal) but diverges from gold and is unnecessary for the
  issue.
- Obsoletion-reason source is only `MONDO:excludePhenotype`; the gold used
  `MONDO:excludeHistoricalDisease`. The issue text supports either ("phenotype
  or a historical term"); minor divergence, not an error.
- Free-text comment wording differs from gold ("OBSOLETE. This term is a
  phenotype..."), normalization-invisible. Substantively fine.

Net: substantively complete and arguably more correct than the gold (only
attempt to both match gold xref qualifiers and fix the dangling ref). F1
under-represents quality.
