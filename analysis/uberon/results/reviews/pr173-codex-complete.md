---
outcome: partial_success
failure_modes:
  - syntax_error
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt adds the five requested HRA/HuBMAP oral anatomy terms, but it has serious OBO syntax and scope problems.

## Strengths

The requested labels, broad definitions, salivon hierarchy, gland-specific ducto-acinar units, and dentogingival junction are all recognizable. It follows the issue-thread proposal more closely than the later reviewer-edited gold in some places.

## Issues

The patch uses invalid or deprecated OBO syntax such as `part_of:` and `EXACT_SYNONYM`/`RELATED_SYNONYM`, quotes URLs inside definition xref lists, and adds `in_taxon NCBITaxon:9606` constraints that the issue discussion did not settle and the gold omitted.
