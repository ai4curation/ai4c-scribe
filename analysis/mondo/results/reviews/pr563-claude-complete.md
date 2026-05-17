---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 563
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.405
precision: 0.268
recall: 0.833
jaccard: 0.254
outcome: partial_success
failure_modes: [under_editing, over_editing]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent did the requested xref correction on MONDO:0009106 (Orphanet:1671 → Orphanet:573278)
and, notably, demoted the narrower synonyms "SCM type 1" and "split cord malformation type 1"
to NARROW rather than deleting them — which matches the human gold's synonym-scope approach
more closely than any other attempt. It also added the issue term tracker and the
`replaced_by: MONDO:0009106` link on obsolete MONDO:0035542. F1=0.405 (recall 0.833)
**under-represents** quality: the missing mass is the 3 off-issue subtype terms and the
obsoletion-merge rewrite that emerged from a curator 1:1, not from the issue (see METADATA.md
Curation Note).

## Strengths

- Correct core fix: `xref: Orphanet:1671 {...}` → `xref: Orphanet:573278 {source="MONDO:equivalentTo"}`.
- Best-aligned synonym handling of any attempt: kept "SCM type 1" and
  "split cord malformation type 1" but changed them to `NARROW [Orphanet:1671]`, and upgraded
  "split cord malformation" to `EXACT [GARD:0001851, Orphanet:573278]` — this is exactly the
  human's modeling decision (the human additionally tagged ABBREVIATION on "SCM type 1").
- Correctly handled the obsolete MONDO:0035542 stanza: removed the now-orphaned
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}` and
  `xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}` (since Orphanet:573278 is now
  the live equivalent on MONDO:0009106, leaving it as an obsoleteEquivalent would create a
  duplicate mapping), added the #9871 tracker and `replaced_by: MONDO:0009106`. This is sound
  reasoning and partially overlaps the human's merge workflow.
- Added `property_value: IAO:0000233 ".../issues/9871"` term tracker.

## Issues

- Did not create MONDO:1060220-1060222 or run the full obsoletion-merge (TermsMerged on
  MONDO:0035541/0035542). Defensible given the issue's explicit "may or may not be in scope"
  hedge; this is the dominant F1 gap and is a case-quality artifact, not an agent failure.
- Over-editing of subsets: collapsed the four orphanet subset lines into just
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}` + `subset: orphanet {...}`,
  dropping `ordo_disorder`, `ordo_morphological_anomaly`, and `orphanet_rare`. The human kept
  `ordo_disorder`, `ordo_morphological_anomaly`, `orphanet`, `orphanet_rare` (retargeted to
  573278). Inventing `ordo_group_of_disorders` here is questionable — that subset belongs to
  the *group* concept, and the agent likely copied it from the obsolete MONDO:0035542 stanza.
- Did not retarget the ICD10CM/MedDRA/OMIM xref `source=` qualifiers from Orphanet:1671 to
  Orphanet:573278, nor update the "diastematomyelia" synonym xref list — leaving stale
  Orphanet:1671 provenance on the term (the human cleaned all of these).
- Did not apply RELATED→EXACT to "split spinal cord malformation" / "SSCM".
