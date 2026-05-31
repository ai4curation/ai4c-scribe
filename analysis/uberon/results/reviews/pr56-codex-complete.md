---
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is the same substantive solution as pr37. It completes both issue asks by removing the bad parent and renaming the paravertebral ganglion term, while keeping `thoracic ganglion` as a less precise synonym.

Metadiff underrates it because the accepted PR did only the parent removal and skipped the rename.

## Strengths

- Removes the incorrect dorsal-root-ganglion classification.
- Renames `UBERON:0000961` to the clearer paravertebral label.
- Adjusts synonyms to reflect the broader meaning of the old name.

## Issues

- Definition and synonym-scope changes go beyond the minimal accepted edit.
- Adds tracker metadata not present in gold.
