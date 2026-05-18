---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 677
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.706
recall: 0.923
jaccard: 0.667
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode produced a clean, correctly-scoped obsoletion of
MONDO:0009327 that matches the core of the gold PR. This run is a
byte-identical replicate of #733 (same blob `ad1b398`, same metadiff
F1 0.800 / P 0.706 / R 0.923); the attempt file carries only the diff,
no PR comment or checklist. Like #733 it did **not** rewire the dangling
`MONDO:0007703 replaced_by: MONDO:0009327` reference that the agent
config explicitly requires, so the high recall modestly
**over-represents** completeness against the documented quality target.

## Strengths

- Core obsoletion correct and matches gold: name → `obsolete heart,
  malformation of`, `is_obsolete: true` added, both `is_a` parents
  (MONDO:0003847, MONDO:0019512) removed, `subset: obsoletion_candidate`
  removed, `consider: MONDO:0005267` (heart disorder) added — the exact
  term the issue recommended.
- Added the obsoletion-reason axiom `property_value: IAO:0000231
  OMO:0001000 {source="MONDO:excludeHistoricalDisease"}`, matching the
  gold and the issue's "historical/placeholder term" framing.
- Reclassified MEDGEN:6748 and UMLS:C0018798 to
  `MONDO:obsoleteEquivalent`, matching the gold and honoring the issue
  comment that the MedGen concept remains active for HPO (xref retained).
- Tightly scoped to a single stanza; no gratuitous edits and no scope
  creep.

## Issues

- Missed requirement (documented quality target): did not rewire
  `MONDO:0007703`, which still carries `replaced_by: MONDO:0009327` —
  now a dangling pointer to a freshly-obsoleted term, contrary to the
  mondo-agent-config rule "No relationship should point to an obsolete
  term". 11 of 14 attempts performed this rewiring; this one did not.
- Under-editing: deleted the `comment:` line entirely rather than
  rewording it as the gold does (gold retains an "has been obsoleted..."
  rationale). Loses curatorial context.
- OMIM:140500 / OMIM:234750 left as `MONDO:equivalentObsolete` instead
  of the gold's `MONDO:obsoleteEquivalentObsolete`. Minor
  source-qualifier divergence.
- Retained the stale `property_value: IAO:0006012 "2026-02-01"`
  scheduled date that the gold removes post-obsoletion.
- No PR/issue comment captured for this run, so methodology cannot be
  independently assessed here (the identical #733 documented ROBOT
  syntax validation and a checkout/checkin workflow).

Net: substantively correct and well-scoped obsoletion satisfying the
issue's primary ask, but stops short of the dangling-reference cleanup
that the case treats as the real quality bar. Duplicate of #733.
