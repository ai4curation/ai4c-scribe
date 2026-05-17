---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt correctly performs the core Pleocyemata replacement on the affected stomatogastric terms. Its low raw score reflects the fact that it does not reproduce the accepted PR's ODK import refresh and serializer-driven OBO cleanup, much of which is not independent curation.

The attempt is nevertheless incomplete because the import refresh is not only score noise: `NCBITaxon:6692` needs to be present in Uberon's NCBITaxon import configuration.

## Strengths

- Applies the intended common-ancestor taxon to the affected terms.
- Removes the incompatible Astacidea and Brachyura `in_taxon` pair.
- Keeps the patch compact and easy to inspect.

## Issues

- Misses the `ncbitaxon_terms.txt` update.
- Does not regenerate `merged_import.owl`.
- Does not include the accepted xref and synonym cleanup around the affected block.
