---
outcome: failure
failure_modes:
  - missed_requirement
  - under_editing
  - gold_orcid_source
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
agent: std_claude_haiku45
---

## Summary

Eval PR #601 (claude-haiku-4.5 / claude) against human PR #10115 / issue #9855
(new_term, medium). Metadiff F1=0.244, P=0.179, R=0.385 — lowest in the cohort
(blob `20cd5f3`, identical to #513). The agent created a minimal new term
`MONDO:7770012` but **never touched the obsoleted `MONDO:0014978` term at all**:
no `replaced_by`, no metadata recovery, no recognition that the requested concept
duplicated an existing obsoleted equivalent. That reconciliation is the defining
requirement of this case (it is what the gold PR description and METADATA
explicitly center on), so the attempt is graded a failure despite the new-term
stanza being syntactically valid.

## Strengths

- The new-term stanza is syntactically well-formed and follows the
  disease-series-by-gene skeleton: `is_a: MONDO:0014769`, `intersection_of` genus
  + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6), requested parent `inherited oocyte maturation defect`.
- Correct PMC→PMID validation (PMID:27545678, PMID:29693651) and HGNC:20449.
- Used the ClinGen affiliation URL for `dcterms:creator`, which is closer to
  gold's attribution intent than the DOI other attempts used (though gold used a
  curator ORCID).

## Issues

- **missed_requirement (defining miss)**: Did not detect or act on obsoleted
  `MONDO:0014978`. No `replaced_by`, no obsoletion-cleanup, no provenance link.
  The duplicate-with-obsoleted-equivalent reconciliation is the entire point of
  the case; omitting it is a substantive failure, not a style gap.
- **under_editing**: No recovery of the obsoleted term's synonyms, the
  `xref: OMIM:617234 {source="MONDO:equivalentTo"}` (absent entirely — the OMIM
  linkage gold preserved is lost), or the malacards `curated_content_resource`.
- Synonym scoping errors: `"early embryonic arrest"` marked `EXACT` where gold
  used `RELATED`; only 3 minimal synonyms vs gold's recovered set; all sourced to
  a single PMID rather than OMIM/ClinGen as gold did.
- **gold_orcid_source**: `dcterms:creator` is the ClinGen org URL, not the
  curator ORCID `https://orcid.org/0000-0002-5002-8648` gold recorded.
- Note: this universal-core miss (obsoleted-equivalent recovery) reflects a
  genuine difficulty of the case rather than a poor evaluation reference; the
  case remains `case_quality: ok`.
