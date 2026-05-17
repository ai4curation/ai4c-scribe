---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 280
agent: std_claude_haiku-4.5
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: structural_refactor
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
  - wrong_pattern
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent edited the **legacy** `make-bridge-ontologies-from-xrefs.pl` Perl script (both copies, `src/ontology/` and `src/scripts/`), changing the life-stage relation `$rel` from `occurs_in` to `in_taxon` and adding an `in_taxon`/`RO:0002162` OBO `[Typedef]`. This is not the active bridging mechanism: the current pipeline is the SSSOM/T-OWL ruleset emitted by `src/scripts/taxa.py` driven by `config/taxa.yaml`, which is what the gold PR #3466 modified. The agent also kept a single-axiom form rather than the required dual-axiom (`EquivalentTo ... in_taxon` + `SubClassOf ... part_of/occurs_in`) pattern. F1=0 is accurate; the work targets a deprecated code path and uses the wrong pattern.

## Strengths

- Identified the correct target relation `RO:0002162` (in_taxon) and the existing `occurs_in`/`BFO:0000066` it was meant to replace for the life-stage path.
- Added a syntactically reasonable OBO `[Typedef]` declaration for the new `in_taxon` relation in the script's generated header, showing awareness that a new relation needs declaring.
- Minimal, contained diff; no spurious unrelated edits.

## Issues

- **Wrong mechanism (core error):** `make-bridge-ontologies-from-xrefs.pl` is the old xref-based bridge generator; the live pipeline gold modified is the SSSOM/T ruleset generator `src/scripts/taxa.py` plus `config/taxa.yaml`. None of the five files the human changed were touched.
- **Edited a duplicated/derived copy:** the diff modifies both `src/ontology/make-bridge-ontologies-from-xrefs.pl` and the identical `src/scripts/make-bridge-ontologies-from-xrefs.pl`, indicating the agent did not determine which (if either) is canonical/invoked.
- **Wrong pattern:** still single-axiom; does not implement the long-intended dual-axiom (`in taxon` equivalence + `part of`/`occurs in` SubClassOf) form requested in the issue and #2428.
- **Missed requirements:** no `config/taxa.yaml` `unfold_over` change (Composite Metazoan unfold left on `part_of`/`occurs_in`), no `RO:0002012` import for the FBdv `substage of` property chain, no documentation updates (`docs/bridges.md`, `docs/combined_multispecies.md`).
- The change only addresses life-stage (`$lsxrefs`) terms, not the general continuant case, so the species-dependent inconsistency the issue targets would persist even on the legacy path.
