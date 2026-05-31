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

Eval PR #724 (gpt-5.5 / opencode) against human PR #10115 / issue #9855
(new_term, medium). Metadiff F1=0.415, P=0.393, R=0.440 (blob `ab89854`,
identical to #667). The agent minted a new term `MONDO:7770012` with the most
generous synonym recovery in the cohort, but only flipped the obsoleted term's
`consider:` → `replaced_by:` **without stripping the recovered metadata from the
obsolete stanza** — leaving synonyms/xref/malacards duplicated across both the
obsolete and new terms. This double-bookkeeping and the surplus synonyms drive
precision down despite a substantively complete new term.

## Strengths

- Correctly detected obsoleted `MONDO:0014978` and added
  `replaced_by: MONDO:7770012`, establishing the replacement chain gold also made.
- Correct logical definition: `is_a: MONDO:0014769`, `intersection_of` genus +
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6); requested parent preserved.
- `xref: OMIM:617234 {source="MONDO:equivalentTo"}` upgraded correctly.
- Recovered the malacards `curated_content_resource` `property_value` and the
  fullest synonym set (including ClinGen-sourced `"PADI6-related maternal-effect
  disorder"`), closer to gold's recovery intent than #745/#688.
- Thorough validation narrative: PMC→PMID, HGNC, ClinGen affiliation URL checked.

## Issues

- **over_editing / data duplication**: The obsolete `MONDO:0014978` stanza was
  NOT stripped of the recovered synonyms/`xref`/`property_value`; only the last
  line changed (`consider` → `replaced_by`). The same metadata now lives on both
  the obsolete term and `MONDO:7770012`. Gold explicitly *removed* this content
  from the obsolete stub (11 deletions there). This is a correctness defect, not
  just a style difference.
- **over_editing (surplus synonyms)**: Added `subset: omim`, design-pattern
  synonyms (`"PADI6 inherited oocyte maturation defect"`, `"...caused by mutation
  in PADI6"`, `"...type 2"` with `MONDO:RULE_1`) that gold did not carry onto the
  new term — lowers precision.
- **gold_orcid_source**: Used `doi:10.1186/s13326-024-00320-3` as
  `dcterms:creator` instead of gold's curator ORCID.
- Net: substantively the new term is sound, but the failure to clean the obsolete
  stanza means the diff leaves the ontology in a state gold would not accept.
