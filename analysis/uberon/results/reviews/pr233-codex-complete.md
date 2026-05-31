---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt makes the right ontology-level taxon change: the affected stomatogastric terms are constrained to Pleocyemata rather than separately to crab and lobster taxa. It is intentionally minimal and therefore avoids most of the noisy gold reserialization.

The missing import maintenance is still substantive. The accepted solution updates the NCBITaxon import inputs and regenerated import output so the new taxon is available to the build.

## Strengths

- Correctly scopes the edit to the reported taxon-constraint violations.
- Uses `NCBITaxon:6692 ! Pleocyemata`, the accepted common ancestor.
- Avoids unrelated term edits.

## Issues

- Does not add `NCBITaxon:6692` to `ncbitaxon_terms.txt`.
- Does not regenerate `merged_import.owl`.
- Omits the accepted xref formatting cleanup.
