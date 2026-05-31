---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 229
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.571
precision: 0.471
recall: 0.727
jaccard: 0.400
outcome: partial_success
failure_modes:
  - missed_requirement
  - syntax_error
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gemma-4-31b/opencode performed a minimal obsoletion: it marked MONDO:0009327
obsolete, removed the `is_a` parents and `obsoletion_candidate`, added
`consider:`, and rewired the dangling MONDO:0007703 — but it omitted every
metadata-modernization step the gold performed (no obsoletion-reason
`IAO:0000231`, no xref source-qualifier updates, did not remove the stale
`IAO:0006012` date) and used an invalid synonym evidence token. Lowest
precision (0.471) in the set. Partial success.

## Strengths

- Basic obsoletion mechanics present: name → `obsolete heart, malformation of`,
  `is_obsolete: true`, both `is_a` parents (MONDO:0003847, MONDO:0019512)
  removed, `subset: obsoletion_candidate` removed, `consider: MONDO:0005267`
  added (correctly used `consider`, not `replaced_by`).
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; matches the
  better attempts and improves on the gold here.

## Issues

- **Missed requirement**: did not add the obsoletion reason
  `property_value: IAO:0000231 OMO:0001000` at all — a required element of the
  Mondo obsoletion pattern (present in the gold and every other attempt).
- **Missed requirement**: left `xref: MEDGEN:6748 {source="MONDO:equivalentTo"...}`,
  `OMIM:140500/234750 {source="MONDO:equivalentObsolete"}`,
  `UMLS:C0018798 {source="MONDO:equivalentTo"...}` entirely unchanged. The gold
  retargeted these to `MONDO:obsoleteEquivalent` /
  `MONDO:obsoleteEquivalentObsolete`; leaving active-equivalence qualifiers on
  an obsolete term is incorrect.
- **Missed requirement**: did not remove the stale
  `property_value: IAO:0006012 "2026-02-01"` scheduled-obsoletion date.
- **Error**: synonym citation changed to `EXACT [MONDO:obsolete]` —
  `MONDO:obsolete` is not a valid CURIE/evidence token. The gold kept
  `EXACT []`.
- Ordering oddity: placed `is_obsolete: true` / `consider:` near the top of the
  stanza (right after `name:`) rather than at the end; harmless after
  normalization but reflects weak format adherence.

Net: a partial obsoletion — the term is marked obsolete and the dangling ref
fixed, but the xref-provenance and obsoletion-reason modernization the gold
required is entirely missing. The 0.727 recall overstates completeness; the
0.471 precision better reflects the many missed/odd edits.
