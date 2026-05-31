---
outcome: partial_success
failure_modes:
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt updates `multi cell part structure` in the right semantic direction, allowing structures made mainly of cell components to contain some complete cells. That addresses the core issue behind PR #3585.

## Strengths

The new definition and comment are close to the upstream FBbt wording that motivated the human fix. The attempt identifies the exact target term and does not broaden the change to unrelated classes.

## Issues

The patch over-edits the term. It removes the `xref: CARO:0001000`, changes the definition source from CARO to the issue URL, rewrites `external_ontology_notes`, and adds tracker metadata. Gold deliberately retained the CARO xref and only changed the definition/comment text.
