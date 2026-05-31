---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is a clean minimal version of the substantive fix. It changes the affected crab/lobster stomatogastric terms from two separate `in_taxon` restrictions to a single `in_taxon NCBITaxon:6692 ! Pleocyemata` restriction, matching the core accepted curation.

Its low F1 is mostly a scoring artifact because it avoids the gold's import regeneration and serializer noise. The real defect is that avoiding the import regeneration also means the new NCBITaxon term is not added to the import configuration.

## Strengths

- Correctly identifies and uses Pleocyemata.
- Applies the replacement consistently to the affected terms.
- Avoids unrelated OBO reserialization churn.

## Issues

- Does not add `NCBITaxon:6692` to `ncbitaxon_terms.txt`.
- Does not regenerate `merged_import.owl`.
- Does not perform the accepted xref-format cleanup.
