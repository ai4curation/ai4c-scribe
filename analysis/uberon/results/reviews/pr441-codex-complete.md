---
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt changes several bridge artifacts from `occurs_in` to `in_taxon`, including generated bridge OWL files and a specific XAO life-stage bridge rule. It is directionally aligned with the relation choice but works at the wrong level and expands into generated outputs.

The accepted PR changes the shared `taxa.py` generator and configuration so bridge outputs can be regenerated consistently. It also adds the two-axiom pattern and updates imports and docs. This attempt does not make those source-of-truth changes.

## Strengths

- Uses `RO:0002162` for taxon-specific life-stage bridge restrictions.
- Applies the idea across multiple bridge artifacts.

## Issues

- Edits generated bridge OWL files instead of the main generation pipeline.
- Does not implement the accepted `EquivalentTo` plus `SubClassOf` pattern.
- Misses `taxa.py`, `taxa.yaml`, `ro_terms.txt`, and documentation updates.
- The generated-output churn makes the patch broader than necessary while still missing the durable fix.
