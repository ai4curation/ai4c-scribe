---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is the same substantive patch as pr12. It performs the core curation correctly by replacing the contradictory Astacidea and Brachyura `in_taxon` restrictions with `NCBITaxon:6692` on the affected stomatogastric terms.

It remains incomplete because the new taxon is not added to the NCBITaxon import seed file and the merged import is not regenerated. That is a real build/ontology requirement, separate from the noisy reserialization artifacts in the gold diff.

## Strengths

- Applies the Pleocyemata common-ancestor taxon to the relevant terms.
- Removes the problematic pair of narrower taxon restrictions.
- Keeps the main ontology edit focused on the reported violation.

## Issues

- Misses the `ncbitaxon_terms.txt` import update for `NCBITaxon:6692`.
- Does not regenerate the imported NCBITaxon axioms in `merged_import.owl`.
- Does not fully reproduce the accepted xref normalization and synonym-scope cleanup.
