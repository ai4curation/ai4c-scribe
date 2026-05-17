---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt is identical in substance to pr92. It implements the main taxon-constraint repair by replacing Astacidea plus Brachyura with the common ancestor Pleocyemata on the affected stomatogastric terms.

The review outcome is partial because the import configuration is missing. `NCBITaxon:6692` must be included in the NCBITaxon import seed and regenerated import output for the ontology build to be complete.

## Strengths

- Correctly changes the problematic `in_taxon` restrictions.
- Uses the intended Pleocyemata taxon.
- Keeps the diff narrowly focused and avoids most reserialization noise.

## Issues

- Misses the required NCBITaxon import update.
- Does not refresh `merged_import.owl`.
- Does not include the accepted xref normalization changes.
