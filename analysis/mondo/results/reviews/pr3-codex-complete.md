---
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt performs the core requested relabel of MONDO:0011996 to `chronic
myeloid leukemia` and preserves the former precise label as an exact synonym.
It also adds the issue tracker item.

It is term-local only. The accepted PR also updated rendered comments on
incoming `is_a` references and performed additional OMIM/QC synonym churn. Much
of that extra gold churn was not derivable from the issue, but the stale
referrer comments would still need regeneration.

## Strengths

- Correct new primary label.
- Preserves the old BCR-ABL1-positive label as a synonym.
- Adds tracker provenance for issue #9892.

## Issues

- Does not update rendered comments on other terms pointing to MONDO:0011996.
- Does not carry over the issue source URLs onto the synonym provenance.
