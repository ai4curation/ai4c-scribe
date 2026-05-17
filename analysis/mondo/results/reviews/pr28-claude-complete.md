---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 28
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.765
precision: 0.765
recall: 0.765
jaccard: 0.619
outcome: success
failure_modes:
  - scope_creep
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/opencode (labeled "pi" runtime in the PR body) produced a correct
obsoletion of MONDO:0009327 plus the MONDO:0007703 rewiring, but additionally
injected an `IAO:0000233` issue-tracker property onto the pre-existing obsolete
MONDO:0007703 stanza, which is an unjustified extra edit. F1 0.765 with balanced
precision/recall; the recall loss is mostly the gold-omitted MONDO:0007703 fix
and comment wording.

## Strengths

- Core obsoletion matches gold: name change, `is_obsolete: true`, both `is_a`
  removed, `obsoletion_candidate` removed, `IAO:0006012` removed,
  `consider: MONDO:0005267` added, obsoletion reason
  `IAO:0000231 OMO:0001000` with `MONDO:excludeHistoricalDisease` source.
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule — a genuine improvement
  over the gold.
- MEDGEN:6748/UMLS:C0018798 → `MONDO:obsoleteEquivalent`, matching gold.

## Issues

- Over-editing: added `property_value: IAO:0000233 "...issues/9771..."` to the
  **MONDO:0007703** stanza (a different, pre-existing obsolete term). The agent
  config says to link the issue via `term_tracker_item` on the term being
  worked, and "don't tag pre-existing terms"; stamping the issue link onto an
  unrelated long-obsolete term is gratuitous and not done by the gold or by the
  cleaner gpt-5.5 variant (#31). Minor but unnecessary.
- OMIM:140500/234750 left as `MONDO:equivalentObsolete` rather than the gold's
  `MONDO:obsoleteEquivalentObsolete`. Small source-qualifier omission.
- Obsoletion comment rewritten in different free text than the gold;
  substantively equivalent, normalization-invisible.
- Extra `MONDO:excludePhenotype` source on the obsoletion reason vs gold's
  single `MONDO:excludeHistoricalDisease`; defensible per issue wording.

Net: correct obsoletion + correct dangling-ref fix, marred by one gratuitous
property_value injection on an unrelated obsolete term.
