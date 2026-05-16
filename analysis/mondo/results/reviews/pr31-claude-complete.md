---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 31
agent: std_opencode_gpt5.5
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.812
precision: 0.765
recall: 0.867
jaccard: 0.684
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/opencode correctly obsoleted MONDO:0009327 following the standard Mondo
obsoletion pattern, and additionally rewired the already-obsolete MONDO:0007703
so it no longer carries `replaced_by: MONDO:0009327`. The metadiff F1 of 0.812
(the best of all 14 attempts) **under-represents** the work: the MONDO:0007703
rewiring is required by the agent config's explicit rule ("No relationship
should point to an obsolete term") but is absent from the gold PR, so it counts
against recall even though it is a genuine improvement over the gold.

## Strengths

- Core obsoletion done correctly: `is_obsolete: true`, name → `obsolete heart,
  malformation of`, both `is_a` parents (MONDO:0003847, MONDO:0019512) removed,
  `subset: obsoletion_candidate` removed, `IAO:0006012` scheduled date removed,
  `consider: MONDO:0005267` added — all matching the gold exactly.
- Added the obsoletion reason `property_value: IAO:0000231 OMO:0001000` with
  `MONDO:excludeHistoricalDisease` source, matching the gold's intent (added an
  extra `MONDO:excludePhenotype` source, defensible given the issue text says
  "phenotype or a historical term").
- Updated MEDGEN:6748 and UMLS:C0018798 to `MONDO:obsoleteEquivalent`, matching
  the gold.
- Correctly identified and fixed the dangling reference: MONDO:0007703 was
  `replaced_by: MONDO:0009327`; rewired to `consider: MONDO:0005267`. This is
  mandated by the agent config and the merge-terms skill (Step 6, rewire
  references to obsoleted terms) and is a real defect the gold PR left behind
  (still broken in the live ontology).
- Sound methodology documented: confirmed MONDO:0005267 exists, swept all
  mentions of MONDO:0009327, ran ROBOT syntax validation.

## Issues

- OMIM:140500/OMIM:234750 left as `MONDO:equivalentObsolete` rather than the
  gold's `MONDO:obsoleteEquivalentObsolete`. Minor source-qualifier divergence;
  the gold's form is the obsolete-aware convention, so this is a small omission.
- Free-text obsoletion comment differs in wording from the gold ("represents a
  phenotype or historical term..." vs gold's "has been obsoleted based on..."),
  which metadiff cannot normalize. Substantively equivalent.
- Scope: the MONDO:0007703 rewiring is an extra edit vs the gold, but it is
  justified (fixes a dangling `replaced_by` to a now-obsolete term) rather than
  over-editing. No precision concern in substance.

Net: a substantively complete and arguably superior solution to the gold. F1
under-represents quality.
