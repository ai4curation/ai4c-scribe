---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 676
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

The agent obsoleted both `GO:0097711 ciliary basal body-plasma membrane docking` and `GO:1905353 ciliary transition fiber assembly`, each with `replaced_by: GO:1905349 ciliary transition zone assembly`, matching the final curator decision (raymond91125's explicit `@dragon-ai-agent please obsolete GO:1905353 and GO:0097711`). The metadiff F1 of 0.952 slightly under-represents quality: the only deltas from the human PR are a defensible `starts_with` rewire (vs the human's deletion) and retained `created_by`/`creation_date` provenance lines. The core obsoletion is complete and correct.

## Strengths

- Obsoleted **both** terms from the final decision, not just the issue-title term `GO:0097711` — correctly read the thread consensus (hattrill's "obsolete GO:1905353 ... and GO:0097711 and replace by GO:1905349").
- Full standard obsoletion structure on both stanzas: `obsolete` name prefix, `OBSOLETE.` definition prefix with original text/dbxrefs preserved, `is_obsolete: true`, `replaced_by: GO:1905349`, and `property_value: term_tracker_item ".../issues/31882" xsd:anyURI`.
- Removed all active logical structure: `GO:0097711`'s `is_a: GO:0140056` and `relationship: part_of GO:0060271`; `GO:1905353`'s `intersection_of GO:0022607`/`results_in_assembly_of GO:0097539` axioms and the full 19-line synonym block.
- Handled the dangling reference: identified the `starts_with GO:0097711` edge on `GO:0060271 cilium assembly` via `obo-grep.pl` and rewired it to `GO:1905349` (the replacement term) rather than leaving a broken reference.
- Sound, documented methodology: pre/post `make travis_build` validation, `obo-checkout.pl`/`obo-checkin.pl` workflow, term-search for internal references, single-file scope (`src/ontology/go-edit.obo` only).

## Issues

- **Style / scope (minor)**: The human *deleted* `starts_with GO:0097711` from `GO:0060271` outright (its `relationship: has_part GO:1905349` already covers the relationship), whereas the agent rewired it to `starts_with GO:1905349`. This is defensible (no dangling ref, valid axiom) but introduces a likely-redundant edge alongside the existing `has_part GO:1905349`; the human's deletion is cleaner. Drives part of the recall miss.
- **Style (cosmetic)**: The agent retained `created_by: pr` / `creation_date` on both obsoleted stanzas; the human removed them. Standard obsoletion practice trims stale provenance, but this is metadiff-only noise with no semantic effect.
- **Omission (minor)**: The obsoletion comments are shorter than the human's and omit the `PMID:27646273` citation explaining that transition-zone assembly begins with mother-centriole docking. The substance ("redundant with GO:1905349 ciliary transition zone assembly") is preserved and accurate.
- No errors, no syntax problems, no scope creep. Net assessment: a complete and correct obsoletion; F1=0.952 under-represents true quality.
