---
outcome: partial_success
failure_modes:
  - syntax_error
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt adds the requested uterine fundus term, but the stanza has OBO-structure and metadata problems.

## Strengths

The main label, definition, parentage, uterus relationship, and `fundus uteri` synonym are present.

## Issues

The patch inserts a mid-file `format-version` header and uses a bare `term_tracker_item:` line. It also duplicates modeling with both `is_a` and `intersection_of`, uses a generic contributor label, and omits the `fundus of uterus` synonym.
