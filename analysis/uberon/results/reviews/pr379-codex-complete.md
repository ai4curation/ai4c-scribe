---
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt adds a plausible uterine fundus term with good synonyms, xrefs, contributor, tracker, and creator metadata, but its modeling differs from the gold pattern.

## Strengths

The anatomy is clear and the synonyms are strong, including the OMO-tagged Latin synonym. The extra FMA/SCTID/UMLS xrefs are relevant.

## Issues

The gold models uterine fundus as an `organ part` with an explicit `part_of uterus` relationship. This attempt instead uses `intersection_of: zone of organ` and `intersection_of: part_of uterus`, which changes the intended pattern.
