---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 249
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.45
precision: 0.321
recall: 0.75
jaccard: 0.29
outcome: partial_success
failure_modes: [under_editing, over_editing]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly performed the only change issue #9871 actually requested: swapping the
incorrect Orphanet equivalent `Orphanet:1671` (SCM type I, too narrow) for `Orphanet:573278`
(split cord malformation) on MONDO:0009106, with consistent propagation across subsets, the
"diastematomyelia" synonym xref list, and the cross-references. It also added the issue
term-tracker and linked the obsolete MONDO:0035542 to MONDO:0009106 via `replaced_by`. The
F1=0.45 substantially **under-represents** quality: the bulk of the gold diff is 3 new subtype
terms (MONDO:1060220-1060222) plus an obsoletion-merge rewrite of MONDO:0035541/0035542 that
the issue did *not* request and that emerged from a private curator 1:1 (see Curation Note in
METADATA.md). Against the issue's explicit ask this is a solid, near-correct response.

## Strengths

- Correct core fix: `xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}`
  removed; `xref: Orphanet:573278 {source="MONDO:equivalentTo", source="OMIM:222500"}` added.
- Consistent provenance propagation: all four `subset:` lines, the `diastematomyelia` EXACT
  synonym xref list, and the ICD10CM/MedDRA/OMIM `source=` qualifiers were retargeted from
  Orphanet:1671 to Orphanet:573278 — matching the human's intent.
- Removed the now-misleading narrow synonyms "SCM type 1" and "split cord malformation type 1"
  that only existed because of the wrong equivalent mapping; this is a defensible curatorial
  judgment (the human instead demoted them to NARROW rather than deleting — both are
  reasonable, see Issues).
- Upgraded `synonym: "split cord malformation"` RELATED→EXACT with Orphanet:573278 added,
  matching the gold exactly.
- Added `property_value: IAO:0000233 ".../issues/9871"` term tracker and
  `replaced_by: MONDO:0009106` on obsolete MONDO:0035542 — a sensible linkage the human also
  made (the human used the new MONDO:1060221 for MONDO:0035541's replaced_by, but pointing the
  generic "obsolete split cord malformation" at MONDO:0009106 is correct).
- Good methodology: PR comment documents NORM run, `robot convert` validation, and a check
  that Orphanet:1671 no longer appears in the file.

## Issues

- Did not create the 3 subtype terms or perform the obsoletion-merge workflow. This is the
  main F1 gap, but the issue explicitly said subtypes "may or may not be in scope for Mondo,"
  so declining is a defensible scope decision — not a true failure (case flagged poor).
- Did not apply the human's synonym-scope refinements to "split spinal cord malformation"
  (RELATED→EXACT) and "SSCM" (RELATED→EXACT ABBREVIATION); left these unchanged.
- Minor over-editing: appended `/specific` and `/e` provenance fragments to the ICD10CM and
  MedDRA xref `source=` qualifiers (e.g.
  `xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/specific", source="Orphanet:573278/e"}`)
  that the human dropped entirely. Cosmetic but reduces precision.
- Did not add the MalaCards `split_cord_malformation` curated_content_resource the human added
  (low-importance, off-issue anyway).
