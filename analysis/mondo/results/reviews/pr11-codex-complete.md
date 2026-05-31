---
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt creates a reasonable TSEN2-related neurodevelopmental disorder term
with the right full label, ClinGen-preferred synonym, neurodevelopmental parent,
TSEN2 logical definition, gene relationship, and issue tracker.

It is incomplete relative to the accepted PR and adds an extra TRACK syndrome
synonym. The accepted syndromic-disease parent and creator metadata are missing,
and the evidence list differs from gold.

## Strengths

- Correct full disease label.
- Correct HGNC:28422 logical definition.
- Includes the important ClinGen-qualified exact synonym.

## Issues

- Missing accepted creator metadata and syndromic-disease parent.
- Adds a TRACK syndrome synonym not present in gold.
- Uses a different and incomplete provenance set on the gene relationship.
