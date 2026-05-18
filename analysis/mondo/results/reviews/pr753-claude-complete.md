---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 753
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

Byte-identical agent diff to attempt #698 (same blob `b8b607e`, same gpt-5.4/opencode
config) — same metadiff F1=0.390, recall=0.714. This is the strongest in-scope provenance
cleanup of the five reviewed attempts: every Orphanet:1671 `source=` qualifier (ICD10CM,
MedDRA, OMIM) retargeted to Orphanet:573278, equivalentTo xref swapped, subsets and the
`diastematomyelia` synonym xref retargeted, #9871 tracker added, and the orphaned
Orphanet:573278 mapping cleaned off obsolete MONDO:0035542. The one in-scope misstep is
*deleting* the "SCM type 1" / "split cord malformation type 1" synonyms rather than
demoting them to NARROW. F1 **under-represents** quality given the established off-issue
gold expansion (METADATA.md Curation Note). This run includes the full PR/issue comments
documenting the rationale.

## Strengths

- Most complete provenance correction in this set: `source="Orphanet:1671"` qualifiers on
  `xref: ICD10CM:Q06.2`, `xref: MedDRA:10012750`, and `xref: OMIM:222500` all moved to
  Orphanet:573278; equivalentTo xref swapped to `xref: Orphanet:573278`.
- Retargeted all orphanet subsets and the `diastematomyelia` EXACT synonym xref list to
  Orphanet:573278; added the `IAO:0000233` #9871 term tracker.
- Correctly handled the cross-stanza consequence: removed the now-orphaned
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}` and
  `xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}` from obsolete MONDO:0035542,
  avoiding a duplicate live/obsolete mapping. Sound reasoning, partially overlapping the
  human merge workflow.
- Explicit, well-reasoned PR comment: states the broader-vs-narrower rationale, confirms
  Orphanet:573278 was previously only on obsolete MONDO:0035542, documents checkout/checkin
  and ROBOT validation, and honestly reports ODK NORM was skipped (no Docker).

## Issues

- Synonym deletion vs. demotion (under_editing / modeling divergence): *deleted*
  `synonym: "SCM type 1" EXACT [Orphanet:1671]` and
  `synonym: "split cord malformation type 1" EXACT [Orphanet:1671]`. The human kept these
  as NARROW synonyms; the agent's PR comment justifies deletion as removing over-specific
  labels, but demotion (the gold approach) preserves useful searchable terminology.
- Did not upgrade `synonym: "split cord malformation"` / `"split spinal cord malformation"`
  to EXACT (left RELATED) — the human promoted both, citing the reporter's SNOMED CT
  445308004 synonymy evidence.
- Minor over-editing (over_editing): carried `Orphanet:573278/e` provenance fragments onto
  the retargeted ICD10CM/MedDRA/OMIM `source=` qualifiers, which the human dropped.
  Cosmetic, lowers precision.
- Did not create MONDO:1060220-1060222 nor perform the full TermsMerged obsoletion-merge —
  the dominant F1 gap, but the established case-quality artifact (issue explicitly flagged
  subtypes "may or may not be in scope"), not an agent failure.
