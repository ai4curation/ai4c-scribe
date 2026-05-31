---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 698
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.390
precision: 0.268
recall: 0.714
jaccard: 0.242
outcome: partial_success
failure_modes: [under_editing, over_editing]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The most thorough in-scope provenance cleanup of the five attempts: the agent retargeted
*every* Orphanet:1671 `source=` qualifier (ICD10CM, MedDRA, OMIM) to Orphanet:573278,
replaced the equivalentTo xref, retargeted the subsets and the `diastematomyelia` synonym
xref list, added the #9871 tracker, AND cleaned the now-orphaned Orphanet:573278 mapping
off the obsolete MONDO:0035542 stanza — partially overlapping the human's obsoletion-merge
work. Its one notable in-scope misstep is *deleting* the "SCM type 1" / "split cord
malformation type 1" synonyms outright rather than demoting them to NARROW as the human
did. F1=0.390 (recall 0.714) **under-represents** quality given the established off-issue
gold expansion (METADATA.md Curation Note). Identical blob (`b8b607e`) to attempt #753.

## Strengths

- Most complete provenance correction in this set: `xref: ICD10CM:Q06.2`,
  `xref: MedDRA:10012750`, and `xref: OMIM:222500` all had their `source="Orphanet:1671"`
  qualifiers moved to `source="Orphanet:573278"`, and the equivalentTo xref swapped to
  `xref: Orphanet:573278 {source="MONDO:equivalentTo", source="OMIM:222500"}`. This is the
  level of cleanup the #665/#721 attempts missed.
- Retargeted all orphanet subsets and the `diastematomyelia` EXACT synonym xref to
  Orphanet:573278; added the `IAO:0000233` #9871 tracker.
- Correctly recognized the cross-stanza consequence: removed the orphaned
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}` and
  `xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}` from obsolete MONDO:0035542
  (since Orphanet:573278 is now the live equivalent on MONDO:0009106, leaving it as an
  obsoleteEquivalent would create a duplicate mapping). This is sound reasoning and
  partially overlaps the human's merge workflow — better cross-term awareness than #665/#721.
- PR comment documents the workflow, ROBOT syntax validation, and honestly reports ODK
  NORM could not run (no Docker).

## Issues

- Synonym deletion vs. demotion (under_editing / modeling divergence): *deleted*
  `synonym: "SCM type 1" EXACT [Orphanet:1671]` and
  `synonym: "split cord malformation type 1" EXACT [Orphanet:1671]` entirely. The human
  *kept* these as NARROW synonyms (preserving useful terminology). Outright deletion loses
  searchable labels; demotion to NARROW is the gold approach and is cleaner.
- Did not promote `synonym: "split cord malformation"` or `"split spinal cord malformation"`
  to EXACT (left them RELATED) — the human upgraded both, supported by the reporter's cited
  SNOMED CT 445308004 synonymy evidence.
- Minor over-editing (over_editing): appended `Orphanet:573278/e` provenance fragments to
  the retargeted ICD10CM/MedDRA/OMIM `source=` qualifiers; the human dropped these
  fragments rather than carrying them over. Cosmetic, lowers precision.
- Did not create MONDO:1060220-1060222 nor perform the full TermsMerged obsoletion-merge
  (only the orphaned-mapping cleanup) — the dominant F1 gap, but the established
  case-quality artifact (issue flagged subtypes as uncertain scope), not an agent failure.
