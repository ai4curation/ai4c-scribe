---
outcome: partial_success
failure_modes:
  - wrong_pattern
  - under_editing
  - gold_orcid_source
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
agent: std_codex_gpt54
---

## Summary

Eval PR #572 (gpt-5.4 / codex) against human PR #10115 / issue #9855 (new_term,
medium). Metadiff F1=0.566, P=0.536, R=0.600. The agent correctly recognized the
duplication with obsoleted `MONDO:0014978` but chose a different resolution
strategy: it **un-obsoleted and revived `MONDO:0014978` in place** (renamed it to
the new label, dropped `is_obsolete`/`consider`) rather than minting a new term
and pointing `replaced_by` at it as gold did. This is a defensible alternative
but a methodological divergence from the gold workflow, which is why metadiff
lands mid-pack despite recovering the correct OMIM linkage.

## Strengths

- Recognized that `OMIM:617234` already existed only on the obsoleted term and
  reasoned explicitly about not minting a duplicate MONDO ID — the underlying
  insight (one MONDO concept, recover the obsoleted equivalent) is correct.
- Correct logical structure: `is_a: MONDO:0014769`, `intersection_of` with
  `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/20449`
  (PADI6); requested parent preserved.
- `xref: OMIM:617234 {source="MONDO:equivalentTo"}` correctly upgraded from
  `MONDO:obsoleteEquivalent`, matching gold's intent.
- Retained the `curated_content_resource` malacards `property_value` (gold also
  keeps this in the MONDO concept) — better metadata fidelity here than #745/#688.
- Ran ODK `make NORM` and `robot convert`; cited literature accurately.

## Issues

- **wrong_pattern**: Reviving the obsoleted term in place contradicts the gold
  curator's chosen pattern (new term + `replaced_by: MONDO:1010200`, obsoleted
  stub retained with comment). Un-obsoleting a deprecated MONDO ID is generally
  discouraged because downstream consumers may have already retired it; gold
  deliberately kept `MONDO:0014978 is_obsolete: true` and minted a fresh ID.
- **under_editing**: Dropped recoverable content the obsoleted term carried —
  the `consider: HP:0032479`, `IAO:0000231 OMO:0001000 {MONDO:excludePhenotype}`,
  and several legacy synonyms (`"preimplantation embryonic lethality 2"`,
  `"...caused by mutation in PADI6"`, `"...type 2"`) — without a `replaced_by`
  trail since no new term exists.
- **gold_orcid_source**: No `dcterms:creator` ORCID added; gold recorded curator
  ORCID `https://orcid.org/0000-0002-5002-8648`.
- Loses the obsoletion/replacement provenance chain entirely (no `replaced_by`),
  which the case is specifically designed to test.
