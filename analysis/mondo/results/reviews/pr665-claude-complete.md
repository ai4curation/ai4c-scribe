---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 665
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.378
precision: 0.250
recall: 0.778
jaccard: 0.233
outcome: partial_success
failure_modes: [under_editing, over_editing, wrong_pattern]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent performed the requested core fix on MONDO:0009106 — added
`xref: Orphanet:573278 {source="MONDO:equivalentTo"}` and demoted the narrower SCM type 1
synonyms — but instead of *deleting* the now-incorrect `xref: Orphanet:1671 {source="MONDO:equivalentTo"}`
it *re-qualified* it as `source="MONDO:mondoIsBroaderThanSource"`, keeping a live Orphanet:1671
xref the human removed. F1=0.378 (recall 0.778) **under-represents** quality because the
dominant missing mass is the 3 off-issue subtype terms (MONDO:1060220-1060222) and the
obsoletion-merge rewrite that came from a curator 1:1, not the issue (METADATA.md Curation
Note); but this attempt also has a genuine in-scope modeling divergence and an incomplete
provenance cleanup. Identical blob (`4c6b2f8`) to attempt #721.

## Strengths

- Correct primary intent: added `xref: Orphanet:573278 {source="MONDO:equivalentTo"}`,
  satisfying the issue's explicit ask for the broader Orphanet equivalent.
- Retargeted the `ordo_disorder`/`orphanet` subset provenance and the `diastematomyelia`
  EXACT synonym xref list from Orphanet:1671 to Orphanet:573278.
- Demoted `synonym: "SCM type 1"` and `synonym: "split cord malformation type 1"` from
  EXACT to NARROW `[Orphanet:1671]`, and upgraded `synonym: "split cord malformation"` to
  EXACT `[GARD:0001851, Orphanet:573278]` — this matches the human gold's synonym-scope
  modeling decision exactly (the human additionally tagged ABBREVIATION on "SCM type 1").
- Added `property_value: IAO:0000233 ".../issues/9871"` term tracker.
- Tightly scoped to the one stanza; PR comment documents the workflow and a ROBOT
  syntax-conversion validation step.

## Issues

- Modeling divergence (wrong_pattern): retained `xref: Orphanet:1671` re-qualified as
  `MONDO:mondoIsBroaderThanSource`. The human *deleted* the Orphanet:1671 xref outright.
  Keeping a non-equivalent Orphanet xref on the term is a defensible mapping pattern in
  principle, but it diverges from how the human (and gold) resolved the over-narrow mapping
  and leaves Orphanet:1671 attached to a concept it is no longer equivalent to.
- Incomplete provenance cleanup (under_editing): left stale `source="Orphanet:1671"`
  qualifiers on `xref: ICD10CM:Q06.2`, `xref: MedDRA:10012750`, and `xref: OMIM:222500`
  (and the `Orphanet:1671/e` / `Orphanet:1671/specific` fragments). The human moved all of
  these to Orphanet:573278. This is the largest correctness gap within the in-scope ask.
- Subset over-collapse (over_editing): replaced the four orphanet subset lines with just
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}` + `subset: orphanet`,
  dropping `ordo_morphological_anomaly` and `orphanet_rare`. The human kept
  `ordo_disorder`, `ordo_morphological_anomaly`, `orphanet`, `orphanet_rare` (retargeted to
  573278). `ordo_group_of_disorders` is the *group*-concept subset and was likely copied
  from the obsolete MONDO:0035542 stanza; this is a questionable invention.
- Did not create MONDO:1060220-1060222 nor run the obsoletion-merge. This is the dominant
  F1 gap but is the established case-quality artifact (issue explicitly flagged subtypes
  "may or may not be in scope"), not an agent failure.
- Did not touch the obsolete MONDO:0035542 stanza (no orphaned-mapping cleanup) — unlike
  the gpt-5.4/opencode attempts #698/#753.
