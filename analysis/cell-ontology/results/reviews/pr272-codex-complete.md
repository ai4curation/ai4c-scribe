---
outcome: success
failure_modes:
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt adds a complete transitional principal-intercalated cell term with
the requested definition, creator and contributor annotations, both synonyms,
the correct parent, and the collecting duct location axiom.

The zero score is driven by the temporary ID mismatch: this attempt uses
`CL_9900000`, while the gold PR used `CL_9900001`. The curation content is
otherwise very close.

## Strengths

The definition is the issue text, including the CKD enrichment sentence. The
parent and `part_of` axioms match the gold modeling.

Both synonyms are present and typed appropriately, and the contributor ORCIDs
are included.

## Issues

The primary temp ID differs from gold, which makes the Functional Syntax
line-level comparison fail completely even though the term is recognizable as
the same requested class.

The issue-tracker annotation is written as a plain string rather than an IRI,
which is a small pattern mismatch. It is extra provenance rather than a blocker.
