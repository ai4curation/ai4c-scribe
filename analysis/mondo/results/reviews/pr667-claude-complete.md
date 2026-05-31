---
outcome: partial_success
failure_modes:
  - over_editing
  - under_editing
  - gold_orcid_source
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
agent: std_opencode_gpt55
---

## Summary

Eval PR #667 (gpt-5.5 / opencode) against human PR #10115 / issue #9855
(new_term, medium). Metadiff F1=0.415, P=0.393, R=0.440. The diff is
byte-identical to attempt #724 (shared blob `ab89854`); this is a re-run of the
same model/runtime and the assessment is identical. New term `MONDO:7770012`
created with strong synonym recovery, but the obsolete `MONDO:0014978` stanza was
only minimally edited (`consider` → `replaced_by`) without removing the recovered
metadata, leaving content duplicated across both terms.

## Strengths

- Same correct core as #724: detected obsoleted `MONDO:0014978`, added
  `replaced_by: MONDO:7770012`, establishing the replacement chain.
- Correct genus-differentia logical definition with `is_a: MONDO:0014769` and
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6); requested parent preserved.
- `xref: OMIM:617234 {source="MONDO:equivalentTo"}` upgraded correctly; malacards
  `curated_content_resource` and the fullest synonym set recovered.

## Issues

- **over_editing / data duplication**: The obsolete `MONDO:0014978` stanza
  retains the synonyms/`xref`/malacards `property_value` instead of being stripped
  as gold did (gold deleted 11 lines from that stub). Metadata is duplicated on
  both the obsolete and new terms — a correctness defect.
- **over_editing (surplus synonyms)**: `subset: omim` and several design-pattern
  synonyms beyond what gold carried, depressing precision.
- **gold_orcid_source**: `doi:10.1186/s13326-024-00320-3` used as
  `dcterms:creator` instead of gold's curator ORCID.
- Duplicate of #724: corroborates reproducibility, no independent signal.
