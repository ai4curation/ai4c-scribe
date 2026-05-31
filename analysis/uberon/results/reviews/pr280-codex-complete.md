---
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This is the same patch as pr161. It makes a relevant but incomplete change in the older bridge Perl scripts by switching life-stage handling from `occurs_in` to `in_taxon`.

The accepted fix is not just a relation substitution. It changes the current `taxa.py` generator to produce two axioms, updates compositing configuration and RO imports, and documents the changed bridge semantics.

## Strengths

- Identifies `in_taxon` as the right relation for taxon-specific life-stage equivalence.
- Applies the edit consistently in both copies of the Perl script.

## Issues

- Targets the wrong bridge-generation layer.
- Does not implement the two-axiom form.
- Misses the config, import, and documentation updates.
