---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 51
agent: std_opencode_gpt5.5
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.722
precision: 0.765
recall: 0.684
jaccard: 0.565
outcome: partial_success
failure_modes:
  - syntax_error
  - scope_creep
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/opencode re-run; the produced blob (`630ad3f`) is byte-identical to
attempt #70, so the assessment matches: a correct core obsoletion of
MONDO:0009327 plus the gold-omitted MONDO:0007703 dangling-reference fix,
undermined by the same invalid synonym evidence citation (a raw GitHub URL
inside the synonym brackets). F1 0.722; the synonym defect is a genuine error,
not a metadiff artifact.

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  parents removed, `obsoletion_candidate` removed, `IAO:0006012` removed,
  `consider: MONDO:0005267` added.
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; improvement over gold.
- MEDGEN:6748/UMLS:C0018798 → `MONDO:obsoleteEquivalent`, matching gold.
- Deterministic reproduction of #70 (same blob), indicating stable behavior.

## Issues

- **Error**: `synonym: "heart, malformation of" EXACT
  [https://github.com/monarch-initiative/mondo/issues/9771]` — a bare URL is
  not a valid synonym evidence/xref token. Should be a CURIE or empty (the gold
  kept `EXACT []`). Invalid edit.
- Obsoletion reason emitted as bare `property_value: IAO:0000231 OMO:0001000`
  without the `{source="MONDO:excludeHistoricalDisease"}` qualifier the gold
  used; acceptable form but loses the issue-stated reason.
- Removed `curated_content_resource` MalaCards property the gold retained;
  minor over-edit for a non-merge obsoletion.
- OMIM:140500/234750 left as `MONDO:equivalentObsolete` vs gold's
  `MONDO:obsoleteEquivalentObsolete`. Source-qualifier omission.

Net: same as #70 — correct skeleton + correct dangling-ref fix with an invalid
synonym citation; partial success.
