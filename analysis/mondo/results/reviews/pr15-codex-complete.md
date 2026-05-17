---
outcome: partial_success
failure_modes:
  - under_editing
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt creates a TSEN2-related disease term with the correct main label,
TSEN2 gene relationship, tracker provenance, and a usable clinical definition.
It also classifies the term under neurodevelopmental disease.

It misses the accepted ClinGen-qualified exact synonym for the full label and
uses `MONDO:0100500` as the logical-definition genus instead of the accepted
`MONDO:0700092`. It also adds extra TRACK/atypical-HUS synonyms and uses a DOI
as creator metadata.

## Strengths

- Correctly grounds the term in HGNC:28422 / TSEN2.
- Adds a gene-based logical definition.
- Captures many of the clinical features from the request.

## Issues

- Logical definition uses the wrong genus compared with the accepted pattern.
- Missing the accepted full-label ClinGen synonym.
- Extra synonyms and bad creator metadata would need curator cleanup.
