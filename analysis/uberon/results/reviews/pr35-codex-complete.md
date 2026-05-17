---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt fixes the central taxon problem by changing the affected stomatogastric terms to `relationship: in_taxon NCBITaxon:6692 ! Pleocyemata`. It also adds tracker annotations and picks up some serializer-driven ordering changes.

The result is still incomplete because it does not add Pleocyemata to the import term list or refresh the merged import. Without that import maintenance, the edit may still fail downstream ontology build expectations.

## Strengths

- Correctly identifies Pleocyemata as the common ancestor for the crab and lobster taxa.
- Applies the replacement across the affected stomatogastric terms.
- Adds readable labels on the new `in_taxon` lines.

## Issues

- Does not update `src/ontology/imports/ncbitaxon_terms.txt`.
- Does not regenerate `src/ontology/imports/merged_import.owl`.
- Adds term tracker annotations not present in the accepted PR.
- Leaves some accepted normalization changes unmatched.
