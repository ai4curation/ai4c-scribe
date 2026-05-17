---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 290
agent: std_claude_sonnet-4.5
model: claude-sonnet-4-5-20250929
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
  - wrong_term
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent understood the issue at a high level (use `in_taxon`/`RO:0002162` for cross-species life-stage bridging) but misapplied it. It edited the **wrong location** — the `TAXREL` switch in `src/ontology/bridge/bridges.rules` — and adopted the **wrong pattern**: it replaced `BFO:0000066` (occurs_in) with `RO:0002162` only for the life-stage branch (`is_a UBERON:0000104/0000105`), keeping a single-axiom form and leaving continuants on `BFO:0000050`. The gold solution instead edits the rule *generator* (`src/scripts/taxa.py`) to emit a **two-axiom** form (`EquivalentTo ... in_taxon` + `SubClassOf %TAXREL ...`) for *all* terms (continuant and occurrent), keeping the `TAXREL` switch untouched as the SubClassOf relation. F1=0 is accurate here: this is a substantively wrong solution, not a metadiff artifact.

## Strengths

- Correctly read the issue discussion and cited the actual consensus (ddooley's "in_taxon is the recommended relation", cmungall's "yes, in-taxon").
- Identified the correct relation IDs: `RO:0002162` (in taxon), `UBERON:0000104` (life cycle), `UBERON:0000105` (life cycle stage), `BFO:0000066` (occurs_in).
- Touched only two files with a small, readable diff (no scope creep, no spurious edits).
- `bridges.rules` is at least a real, related file in the active SSSOM/T pipeline (it defines `%TAXREL`), so the agent was in the right subsystem even though it edited the wrong layer.

## Issues

- **Wrong pattern (core error):** the agent kept the single-axiom equivalence form and merely swapped the relation for the life-stage branch. The issue explicitly asked for the long-intended **dual-axiom** form (`EquivalentTo ... 'in taxon' some taxon` + `SubClassOf: 'part of'/'occurs in' some taxon`) from #2428. The agent's change discards the occurs_in/part_of information entirely for life stages rather than demoting it to a redundant SubClassOf.
- **Wrong scope of relation change:** gold makes `in_taxon` the equivalence relation for *all* bridged terms (continuants and occurrents alike); the agent only changed the `UBERON:0000104`/`UBERON:0000105` branch, leaving continuant bridges on `part_of` — exactly the species-dependent inconsistency the issue set out to eliminate.
- **Wrong file / wrong layer:** editing the static `bridges.rules` template instead of the generator `src/scripts/taxa.py` (and not touching `config/taxa.yaml` `unfold_over`). The Composite Metazoan unfold step is left pointing at `BFO:0000050`/`BFO:0000066`, so composites would be broken/inconsistent with the new equivalence relation.
- **Missed requirements:** no `unfold_over` update in `config/taxa.yaml`; no `RO:0002012` import addition (needed for the FBdv `substage of` property chain); `docs/combined_multispecies.md` not updated. The doc edit in `bridges.md` describes a life-stage-only `in_taxon` exception that does not match the merged design.
