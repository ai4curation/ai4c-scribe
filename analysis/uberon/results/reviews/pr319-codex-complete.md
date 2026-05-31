---
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is the cleanest full resolution of the actual issue. It removes the incorrect `thoracic dorsal root ganglion` parent and renames `thoracic ganglion` to `thoracic paravertebral ganglion`, converting the old name into a synonym.

The accepted PR only performed the first half, so metadiff undervalues this attempt.

## Strengths

- Removes the erroneous subclass axiom.
- Implements the requested rename.
- Keeps the old label available as a synonym.
- Avoids unrelated file churn.

## Issues

- The new `thoracic ganglion` synonym has an empty xref list, which is not ideal, but the curation itself is sound.
