---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 377
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: structural_refactor
difficulty: hard
case_quality: ok
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
  - wrong_pattern
  - missed_requirement
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.4/codex agent made a minimal, well-scoped but fundamentally misdirected change: it edited three `treat-xrefs-as-reverse-genus-differentia` header directives in `src/ontology/uberon-edit.obo` (`FBdv`, `WBls`, `ZFS`) from `part_of` to `in_taxon`, plus an incidental trailing-blank-line removal. F1=0.000 is a genuine failure on a sound `case_quality: ok` case. These OBO-header directives are not the mechanism the gold PR changes, and `in_taxon` is not a valid `treat-xrefs-as-reverse-genus-differentia` argument in the way `part_of` is here — this edit changes the wrong knob and would likely break the legacy macro expansion rather than fix the bridge relation.

## Strengths

- Recognized that `in_taxon` is the relevant relation for life-stage / taxon-specific mappings, consistent with the issue resolution.
- Kept the edit tightly scoped (one file, three lines) and was honest about the inability to run the `robot convert` reserialization step.
- Correctly restricted the target ontologies to the stage ontologies (`FBdv`, `WBls`, `ZFS`) rather than touching anatomy bridges like `FMA`/`ZFA`.

## Issues

- **Wrong pattern / wrong mechanism**: the gold change is in the active SSSOM/T pipeline (`src/scripts/taxa.py` emitting a two-axiom `EquivalentTo` + `SubClassOf` form) plus `config/taxa.yaml`. The `treat-xrefs-as-reverse-genus-differentia` directives in `uberon-edit.obo` are a different, largely superseded macro path; editing them does not produce the dual-axiom bridge form and does not consistently affect the externally maintained bridges the issue is about.
- **Under-editing / omissions**: misses the entire required refactor — no `taxa.py` generator change, no `unfold_over` → `RO:0002162` in `config/taxa.yaml`, no `RO:0002012` import addition, no `docs/bridges.md` / `docs/combined_multispecies.md` updates. Only three header declarations were touched versus the human's five-file infrastructure change.
- The substituted token `in_taxon` is unlikely to be a valid genus-differentia macro relation in this directive context, so the edit risks breaking the build rather than achieving the intended semantics.
