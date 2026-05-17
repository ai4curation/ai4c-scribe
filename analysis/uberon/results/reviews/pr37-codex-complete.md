---
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt performs both requested changes: it removes `thoracic dorsal root ganglion` from under `thoracic ganglion`, and it renames `thoracic ganglion` to `thoracic paravertebral ganglion`. That is a fuller issue resolution than the accepted one-line gold PR.

The patch is somewhat more editorial than necessary because it rewrites the definition and changes synonym scopes, but the biological intent is correct.

## Strengths

- Removes the incorrect parent from `UBERON:0002835`.
- Clarifies `UBERON:0000961` by renaming it to `thoracic paravertebral ganglion`.
- Preserves the old name as a synonym.
- Keeps the edit limited to the two relevant stanzas.

## Issues

- Rewrites the existing definition.
- Changes generic synonym scopes to `BROAD`, which is plausible but not explicitly requested.
- Adds tracker metadata not present in the accepted PR.
