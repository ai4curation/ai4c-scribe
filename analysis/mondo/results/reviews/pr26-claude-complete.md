---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 26
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.698
precision: 0.882
recall: 0.577
jaccard: 0.536
outcome: partial_success
failure_modes:
  - over_editing
  - syntax_error
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/codex obsoleted MONDO:0009327 and rewired the dangling MONDO:0007703,
but stripped substantially more from the stanza than the gold (removed all four
subsets and the MalaCards `curated_content_resource`) and introduced the same
invalid raw-URL synonym citation. High precision (0.882) but low recall
(0.577) — partly the gold-omitted MONDO:0007703 fix, partly genuine
over-stripping. Mixed quality.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  removed, `obsoletion_candidate` removed, `IAO:0006012` removed,
  `consider: MONDO:0005267` added, obsoletion reason
  `IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}`.
- Xref qualifiers strong: GARD/MEDGEN/UMLS → `MONDO:obsoleteEquivalent`,
  OMIM:140500/234750 → `MONDO:obsoleteEquivalentObsolete` (correct
  obsolete-aware convention; OMIM form matches the gold).
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; improvement over gold.

## Issues

- **Over-editing**: removed `subset: gard_rare`, `subset: nord_rare`,
  `subset: rare` (in addition to `obsoletion_candidate`). The gold removed only
  `obsoletion_candidate` and kept the rare-disease subsets. For a non-merge
  obsoletion these subsets are typically retained; the merge-terms skill's
  "strip subsets" guidance applies to merges, not this case. Genuine
  over-stripping vs gold.
- Removed `curated_content_resource` MalaCards property the gold retained;
  another over-edit.
- **Error**: `synonym: "heart, malformation of" EXACT
  [https://github.com/monarch-initiative/mondo/issues/9771]` — bare URL is not
  a valid evidence token. Should be a CURIE or empty.
- Over-editing: stamped `IAO:0000233` issue link onto the pre-existing
  MONDO:0007703 stanza; contrary to "don't tag pre-existing terms".

Net: correct obsoletion + correct dangling-ref fix, but aggressive
over-stripping plus an invalid synonym citation → partial success. The high
precision overstates quality given the recall-side over-deletion.
