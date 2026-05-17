---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 235
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: structural_refactor
difficulty: hard
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent produced a diff that is byte-identical to the gold PR #3466 across all five files (`docs/bridges.md`, `docs/combined_multispecies.md`, `src/ontology/config/taxa.yaml`, `src/ontology/imports/ro_terms.txt`, `src/scripts/taxa.py`). The F1=1.0 is genuine — not a leakage/no-op/serialization artifact. The agent independently identified the *active* SSSOM/T-OWL bridge pipeline (the `taxa.py` rule generator + `config/taxa.yaml` compositing config), implemented the exact dual-axiom form (`EquivalentTo: %object_id and (RO:0002162 some {taxon})` plus `SubClassOf: %TAXREL some {taxon}`), switched `unfold_over` to `RO:0002162`, and added `RO:0002012` to the RO import — matching the human's reasoning that `occurrent part of` is needed as a parent of FBdv `substage of` for the property chain. This is an exemplary result on a hard infrastructure-level task; F1 accurately represents the quality.

## Strengths

- Correctly located the live bridging mechanism: the SSSOM/T ruleset emitted by `src/scripts/taxa.py` (with `%TAXREL` resolved in `bridges.rules`), not the legacy `treat-xrefs-as-reverse-genus-differentia` directives or the `make-bridge-ontologies-from-xrefs.pl` Perl script that three other attempts mistakenly edited.
- Implemented the precise two-axiom pattern from the issue/PR #2428 lineage: `RO:0002162` (in taxon) carries the cross-species equivalence; the existing `%TAXREL` switch (`BFO:0000050` default, `BFO:0000066` for `UBERON:0000104`/`UBERON:0000105` descendants) is retained as a redundant SubClassOf so the part-of/occurs-in distinction is not lost.
- Applied the change to **both** the `-uberon` and `-cl` rule blocks, matching gold — the CL bridges are maintained in Uberon and gouttegd explicitly noted this in the PR thread.
- Changed `defaults.compositing.unfold_over` from `[BFO:0000050, BFO:0000066]` to `[RO:0002162]`, exactly mirroring the human's second commit ("Unfold composite ontologies over 'in taxon'").
- Independently reproduced the non-obvious `RO:0002012` (occurrent part of) import addition with a justification matching gouttegd's commit message (needed so the `part of o in taxon -> in taxon` chain reaches FBdv `substage of` / `FBdv:00018001`).
- Updated both documentation worked examples (ZFA gonad primordium `UBERON:0005564`; FBbt ovary `UBERON:0000992` / `FBbt:00004865`/`FBbt:00004911`) consistently with the axiom change.
- Strong, accurate methodology in the PR comment: verified the `RO:` prefix is declared in `bridges.rules`, checked `dosdp-patterns/dev/taxon_specific.yaml` already uses `RO:0002162`, and surfaced the reviewer-relevant question of whether the SubClassOf axiom is wanted — the same point cmungall and gouttegd actually debated on the gold PR.

## Issues

- None. The diff is substantively and line-for-line equivalent to the merged gold PR, the ontological reasoning is correct, and scope discipline is perfect (exactly the five files the human touched, no extras).
