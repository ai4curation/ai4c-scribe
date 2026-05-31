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

Eval PR #688 (gpt-5.4 / opencode) against human PR #10115 / issue #9855
(new_term, medium). Metadiff F1=0.667, P=0.679, R=0.655 — tied for best in the
cohort. The diff is byte-identical to attempt #745 (shared blob `ad38d78`); this
is a re-run of the same model/runtime and the assessment is the same. The agent
correctly executed the new-term + `replaced_by` obsoleted-equivalent recovery
pattern that most cohort attempts missed. Metadiff modestly under-represents
quality (minted ID line and sourcing-convention differences, not substance).

## Strengths

- Same correct core as #745: detected obsoleted `MONDO:0014978`, stripped its
  obsolete-only metadata, added `replaced_by: MONDO:7770012` and issue #9855
  provenance — the central reconciliation the issue/PR required.
- Correct genus-differentia logical definition: `is_a: MONDO:0014769`,
  `intersection_of` with `has_material_basis_in_germline_mutation_in`
  `http://identifiers.org/hgnc/20449` (PADI6), correct requested parent
  `inherited oocyte maturation defect`.
- `xref: OMIM:617234 {source="MONDO:equivalentTo"}` correctly upgraded from the
  obsoleted term's `MONDO:obsoleteEquivalent`, matching gold.
- Tightly scoped, single relevant file, valid OBO syntax.

## Issues

- **Incomplete metadata recovery (under_editing)**: As with #745, the
  `curated_content_resource` malacards `property_value` and the ClinGen-sourced
  label synonym + `"PADI6 preimplantation embryonic lethality"` synonym were not
  migrated from the obsoleted term to the new term as gold did.
- **gold_orcid_source mismatch**: Used `doi:10.1186/s13326-024-00320-3` as
  `dcterms:creator` instead of gold's curator ORCID
  `https://orcid.org/0000-0002-5002-8648`.
- Benign EOF trailing-newline deletion (serialization artifact, not substantive).
- `IAO:0000231 MONDO:TermsMerged` on the obsoleted stanza vs gold's free-text
  `comment:` — defensible convention difference.
- Duplicate of #745: provides corroboration of reproducibility but no independent
  signal.
