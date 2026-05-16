---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 332
agent: std_copilot_sonnet4.5
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.585
precision: 0.706
recall: 0.500
jaccard: 0.414
outcome: partial_success
failure_modes:
  - over_editing
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-sonnet-4.5/copilot obsoleted MONDO:0009327 with correct core mechanics
and the gold-omitted MONDO:0007703 rewiring, but flattened all xref source
qualifiers (dropping the `MONDO:MEDGEN`/`MEDGEN:6748` provenance) and stripped
all subsets. F1 0.585 is the third-lowest; the recall loss is part
gold-omission artifact and part genuine provenance/subset over-deletion.
Partial success.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  parents removed, `obsoletion_candidate` removed, `IAO:0006012` and
  `curated_content_resource` removed, `consider: MONDO:0005267` added,
  `IAO:0000231 OMO:0001000` obsoletion reason added.
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; improvement over gold.
- Good rationale in PR/issue comments: explained the OMIM split and explicitly
  honored @kanems' note that MEDGEN:6748 stays active for HPO.

## Issues

- **Over-editing / provenance loss**: collapsed every xref to a single bare
  `{source="MONDO:obsoleteEquivalent"}`, discarding the secondary provenance
  qualifiers the gold preserved — e.g. `MEDGEN:6748` lost
  `{source="MONDO:MEDGEN"}` and `UMLS:C0018798` lost
  `{source="MONDO:MEDGEN", source="MEDGEN:6748"}`. Destroying mapping
  provenance is a real defect, not a style choice.
- OMIM:140500/234750 → `MONDO:obsoleteEquivalent` rather than the gold's
  `MONDO:obsoleteEquivalentObsolete`. Minor relative to the provenance loss.
- Over-editing: removed all subsets including `rare`/`gard_rare`/`nord_rare`;
  the gold kept them.
- Empty PR body ("# Obsoletion of MONDO:0009327" with no content) — weak
  documentation relative to the other claude-family attempts.

Net: correct core obsoletion + correct dangling-ref fix, but xref-provenance
flattening and subset over-stripping are genuine quality losses → partial
success. F1 modestly under-represents the core correctness but the provenance
defect is real.
