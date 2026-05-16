---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 70
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

gpt-5.5/opencode obsoleted MONDO:0009327 and correctly rewired the dangling
MONDO:0007703, but introduced a malformed synonym evidence citation — a raw
GitHub issue URL placed inside the synonym brackets — which is an invalid
OBO xref/evidence and a real defect. Blob `630ad3f` is byte-identical to
attempt #51. F1 0.722; the core obsoletion is sound but the synonym error is a
genuine quality problem (not a metadiff artifact).

## Strengths

- Core obsoletion correct: name change, `is_obsolete: true`, both `is_a`
  removed, `obsoletion_candidate` removed, `IAO:0006012` removed,
  `consider: MONDO:0005267` added.
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; improvement over gold.
- MEDGEN:6748/UMLS:C0018798 → `MONDO:obsoleteEquivalent`, matching gold.
- Reasonable obsoletion comment explaining the phenotype/historical-placeholder
  rationale.

## Issues

- **Error**: changed `synonym: "heart, malformation of" EXACT []` to
  `EXACT [https://github.com/monarch-initiative/mondo/issues/9771]`. A bare URL
  is not a valid synonym evidence/xref token (should be a CURIE such as
  `MONDO:Lexical` or left empty as the gold did). This is an invalid edit, not
  just a style difference.
- Dropped the obsoletion-reason source qualifier — emitted
  `property_value: IAO:0000231 OMO:0001000` with no `{source=...}` whereas the
  gold used `{source="MONDO:excludeHistoricalDisease"}`. The bare form is
  acceptable per the agent-config example but loses the issue's stated reason.
- Removed `property_value: curated_content_resource ... MalaCards`; the gold
  retained it. Minor over-edit (the merge-terms skill would strip it, but this
  is a non-merge obsoletion where the gold kept it).
- OMIM:140500/234750 left as `MONDO:equivalentObsolete` rather than the gold's
  `MONDO:obsoleteEquivalentObsolete`. Source-qualifier omission.

Net: correct skeleton + correct dangling-ref fix, but a genuinely invalid
synonym citation drags this to partial success.
