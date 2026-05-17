---
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is the same patch family as pr35. The core ontology change is right: the affected stomatogastric terms are retaxed to Pleocyemata rather than separately constrained to Astacidea and Brachyura.

The attempt falls short on the import side. The accepted PR explicitly adds the Pleocyemata taxon to the NCBITaxon import configuration and carries the regenerated import output; this attempt does not.

## Strengths

- Replaces the invalid pair of `in_taxon` relationships with the intended common ancestor.
- Applies the change consistently across the stomatogastric nerve and ganglion terms.
- Keeps the affected terms under the same anatomical hierarchy.

## Issues

- Misses the NCBITaxon import seed update.
- Does not refresh `merged_import.owl`.
- Adds tracker annotations and serialization changes outside the core requested fix.
