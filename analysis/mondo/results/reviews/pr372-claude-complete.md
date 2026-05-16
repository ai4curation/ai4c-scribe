---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 372
agent: std_claude_opus4.7
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.941
recall: 0.696
jaccard: 0.667
outcome: success
failure_modes:
  - scope_creep
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-opus-4.7/claude obsoleted MONDO:0009327 correctly with the highest
precision in the set (0.941), but added two extra `consider:` tags
(MONDO:0800321, MONDO:0014000) beyond the gold's single MONDO:0005267, and
changed the GARD xref source qualifier. It did *not* rewire MONDO:0007703.
F1 0.800 modestly under-represents the core obsoletion quality but the extra
`consider` tags are a defensible-but-not-required scope expansion.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  parents removed, `obsoletion_candidate` (and other subsets) removed,
  `IAO:0006012` removed, `consider: MONDO:0005267` present, obsoletion reason
  `IAO:0000231 OMO:0001000 {source="MONDO:excludeHistoricalDisease"}` matching
  the gold's source exactly.
- Xref qualifiers largely match gold: MEDGEN/UMLS → `MONDO:obsoleteEquivalent`,
  OMIM:140500/234750 → `MONDO:obsoleteEquivalentObsolete` (the correct
  obsolete-aware form; matched the gold).
- Excellent issue-grounded reasoning: correctly traced OMIM:140500→OMIM:306955
  (MONDO:0800321) and OMIM:234750→OMIM:614980 (MONDO:0014000) from the issue
  body, and honored @kanems' comment that MEDGEN:6748 stays active for HPO by
  retaining that xref. Explicitly asked the curator whether a single
  `consider` was preferred — good calibration on an ambiguous judgment call.

## Issues

- Scope: added `consider: MONDO:0800321` and `consider: MONDO:0014000` in
  addition to MONDO:0005267. The issue's "Suggested term to consider" lists
  only MONDO:0005267; the two split-target Mondo terms are accurate context but
  go beyond what was asked. Defensible (the agent flagged it for review) but
  reduces recall vs the single-consider gold.
- Changed `xref: GARD:0024658 {source="MONDO:GARD"}` to
  `{source="MONDO:obsoleteEquivalent"}`. The gold left GARD unchanged
  (`MONDO:GARD`). Minor over-edit / divergent style.
- Folded the issue context into the `comment` field but dropped the original
  comment text the gold edited in place; substantively fine but
  normalization-invisible difference.
- Did not rewire MONDO:0007703 (`replaced_by: MONDO:0009327`). Unlike the
  gpt-5.5/kimi attempts, this leaves the same dangling reference the gold left
  — an omission relative to the agent config's "no relationship should point to
  an obsolete term" rule, though it matches the (incomplete) gold.

Net: a correct, well-reasoned obsoletion with minor defensible scope expansion.
