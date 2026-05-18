---
outcome: partial_success
failure_modes:
  - under_editing
  - gold_orcid_source
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
agent: std_opencode_gpt54
---

## Summary

Eval PR #745 (gpt-5.4 / opencode) against human PR #10115 / issue #9855 (new_term,
medium). Metadiff F1=0.667, P=0.679, R=0.655 — the best score in the 13-attempt
cohort, tied with #688 (identical blob `ad38d78`). The agent correctly recognized
that the requested concept duplicated the obsoleted `MONDO:0014978` and executed
the new-term + `replaced_by` reconciliation pattern, which most attempts missed.
The metadiff slightly under-represents quality: it penalizes the minted ID line
(`MONDO:7770012` vs gold's `MONDO:1010200`, an expected eval divergence) and
sourcing-convention differences rather than substantive errors.

## Strengths

- Correctly identified the obsoleted-equivalent term `MONDO:0014978` and applied
  the recovery workflow: stripped the obsolete-only metadata, added
  `replaced_by: MONDO:7770012`, and recorded issue #9855 provenance. This is the
  core insight the haiku attempts (#601/#513) entirely missed.
- New term has a correct genus-differentia logical definition matching gold:
  `is_a: MONDO:0014769`, `intersection_of` with
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6), parent `inherited oocyte maturation defect` as requested in the issue.
- `xref: OMIM:617234 {source="MONDO:equivalentTo"}` correctly upgraded from the
  obsoleted term's `MONDO:obsoleteEquivalent`, matching gold exactly.
- Validated identifiers: PMC→PMID conversion (PMID:27545678, PMID:29693651),
  HGNC:20449 for PADI6, OMIM:617234. Ran `robot convert` syntax check.
- Tightly scoped to the one relevant file with no gratuitous edits.

## Issues

- **Incomplete metadata recovery (under_editing)**: Gold migrated the
  `property_value: curated_content_resource "...malacards..."` annotation from the
  obsoleted term onto the new term; #745 dropped it entirely. Gold also recovered
  the ClinGen-sourced label synonym `"PADI6-related oocyte/zygote/embryo maturation
  arrest 16 and maternal-effect disorder" EXACT [https://clinicalgenome.org/...]`
  and `"PADI6 preimplantation embryonic lethality"`; #745's synonym set is leaner
  (OMIM-sourced only plus a RELATED "early embryonic arrest").
- **gold_orcid_source mismatch**: Gold used
  `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648`
  (a curator ORCID). #745 used `doi:10.1186/s13326-024-00320-3` (the design-pattern
  paper DOI) as creator — semantically wrong attribution, and a recurring
  cross-attempt confusion.
- Trailing-newline deletion at EOF (`-` on the `transmitted by` stanza tail) is
  a benign serialization artifact, not a substantive error.
- Used `property_value: IAO:0000231 MONDO:TermsMerged` on the obsoleted stanza
  where gold used a free-text `comment:`; defensible but divergent convention.
