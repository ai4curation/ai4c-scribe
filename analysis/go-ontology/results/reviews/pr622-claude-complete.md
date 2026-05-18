---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 622
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.952
precision: 0.952
recall: 0.952
jaccard: 0.909
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent obsoleted both `GO:0097711 ciliary basal body-plasma membrane docking` and `GO:1905353 ciliary transition fiber assembly`, each with `replaced_by: GO:1905349 ciliary transition zone assembly`, matching the final curator decision in the issue thread. The diff is byte-identical to sibling attempt #676 (same gpt-5.4/opencode, blob `efa43c8`, F1=0.952). The metadiff F1 of 0.952 slightly under-represents quality: the only deltas from the human PR are a defensible `starts_with` rewire (vs the human's deletion) and retained provenance lines; the core obsoletion is complete and correct.

## Strengths

- Obsoleted **both** terms from the final consensus (`GO:1905353` + `GO:0097711`), not just the issue-title term — correctly interpreted raymond91125's explicit obsoletion request and hattrill's combined recommendation.
- Full standard obsoletion structure on both stanzas: `obsolete` name prefix, `OBSOLETE.` def prefix with original text/dbxrefs preserved, `is_obsolete: true`, `replaced_by: GO:1905349`, and `term_tracker_item` pointing at issue 31882.
- Removed all active logical structure: `GO:0097711`'s `is_a: GO:0140056` and `part_of GO:0060271`; `GO:1905353`'s `intersection_of` axioms and full synonym list.
- Handled the only in-ontology dangling reference by rewiring the `starts_with GO:0097711` edge on `GO:0060271 cilium assembly` to the replacement `GO:1905349` rather than leaving it broken.
- Tightly scoped to `src/ontology/go-edit.obo`; consistent, reproducible result across two independent runs (#622 and #676 identical).

## Issues

- **Style / scope (minor)**: Human deleted `starts_with GO:0097711` from `GO:0060271` (its existing `has_part GO:1905349` already covers it); the agent rewired to `starts_with GO:1905349` instead. Valid and dangling-ref-free, but creates a likely-redundant edge alongside `has_part GO:1905349`; the human's deletion is cleaner. Accounts for part of the recall gap.
- **Style (cosmetic)**: Retained `created_by: pr` / `creation_date` on both obsoleted stanzas where the human removed them — metadiff-only noise, no semantic effect.
- **Omission (minor)**: Obsoletion comments are shorter than the human's and omit the `PMID:27646273` rationale; substance ("redundant with GO:1905349 ciliary transition zone assembly") is preserved and correct.
- No errors, syntax issues, or scope creep. F1=0.952 under-represents the true quality of a complete, correct obsoletion.
