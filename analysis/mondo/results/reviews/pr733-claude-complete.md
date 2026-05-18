---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 733
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
MONDO:0009327 that matches the core of the gold PR, but unlike the
strongest attempts (#31, #28, #27, #33, #70, #51, #26) it did **not**
rewire the dangling `MONDO:0007703 replaced_by: MONDO:0009327` reference
that the agent config explicitly requires. F1 0.800 (recall 0.923,
precision 0.706) modestly **over-represents** completeness here: the
high recall reflects close line-match with the (incomplete) gold, while
the case's documented quality target — also fixing the dangling
reference — was missed.

## Strengths

- Core obsoletion correct and matches gold: name → `obsolete heart,
  malformation of`, `is_obsolete: true` added, both `is_a` parents
  (MONDO:0003847 hereditary disease, MONDO:0019512 congenital heart
  malformation) removed, `subset: obsoletion_candidate` removed,
  `consider: MONDO:0005267` (heart disorder) added — exactly the term
  the issue suggested.
- Added the obsoletion-reason axiom `property_value: IAO:0000231
  OMO:0001000 {source="MONDO:excludeHistoricalDisease"}`, matching the
  gold's intent and consistent with the issue's "historical/placeholder
  term" framing.
- Reclassified MEDGEN:6748 and UMLS:C0018798 from `MONDO:equivalentTo`
  to `MONDO:obsoleteEquivalent`, matching the gold and correctly
  honoring the issue comment that the MedGen concept stays active for
  HPO (xref retained, not deleted).
- Tightly scoped: single file, single stanza, no gratuitous edits — no
  precision-eroding scope creep (contrast #28's spurious IAO:0000233
  injection onto MONDO:0007703).
- Methodology documented: confirmed MONDO:0005267 exists, inspected the
  target stanza, ran `robot convert` syntax validation; honestly flagged
  that Docker-based `make NORM` could not run in-environment.

## Issues

- Missed requirement (the documented quality target): did not rewire
  `MONDO:0007703`, whose stanza still reads `replaced_by:
  MONDO:0009327` — now a pointer to a freshly-obsoleted term, a
  QC-violating dangling reference. The mondo-agent-config CLAUDE.md
  states "No relationship should point to an obsolete term"; 11 of 14
  attempts handled this. This attempt did not, leaving the same defect
  the gold PR left behind.
- Under-editing: removed the `comment:` line entirely. The gold does not
  delete it — it *rewords* it from "scheduled for obsoletion" to "has
  been obsoleted...", retaining a user-facing obsoletion rationale.
  Dropping the comment loses curatorial context.
- OMIM:140500 / OMIM:234750 left as `MONDO:equivalentObsolete` rather
  than the gold's obsolete-aware `MONDO:obsoleteEquivalentObsolete`.
  Minor source-qualifier divergence; defensible but not the convention
  the gold applied for an obsoleted term.
- Retained `property_value: IAO:0006012 "2026-02-01"` (the scheduled
  date); the gold removes it once obsoletion is executed. Small
  stale-metadata omission.

Net: a substantively correct, well-scoped obsoletion that satisfies the
issue's primary ask, but it stops short of the dangling-reference
cleanup that distinguishes the best attempts and that this case treats
as the real quality bar. Identical diff to #677 (same blob `ad1b398`).
