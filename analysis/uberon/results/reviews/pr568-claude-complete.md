---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 568
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
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
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.5/opencode agent flipped `BFO:0000066` to `RO:0002162` in the static SSSOM-T rule files (`bridge-xao-ls.rules`, `bridges.rules` `%TAXREL` switch) and hand-patched the generated bridge OWL artifacts (`uberon-bridge-to-fbdv.owl`, `uberon-bridge-to-sslso.owl`, and more — `50d23d8` blob family, the same wrong-level approach as eval PRs #629 and #441). F1=0.000 is a real failure on a sound `case_quality: ok` case, not a metadiff artifact. The agent never edited the active generator `src/scripts/taxa.py`, `src/ontology/config/taxa.yaml`, `src/ontology/imports/ro_terms.txt`, or the docs files that constitute the gold change.

## Strengths

- Correctly identified `in taxon` (`RO:0002162`) as the agreed relation from the issue thread for life-cycle / life-cycle-stage (`UBERON:0000104` / `UBERON:0000105`) bridge restrictions.
- Internally consistent relation substitution including prefix/`declare` plumbing in `bridge-xao-ls.rules`.

## Issues

- **Wrong pattern**: single-axiom relation swap rather than the gold dual-axiom form (`EquivalentTo` with `RO:0002162` plus a retained `SubClassOf %TAXREL some {taxon}`); the part_of/occurs_in distinction is dropped.
- **Missed source-of-truth**: edits the static/legacy rule files and generated `*.owl` products instead of the live `taxa.py` generator + `config/taxa.yaml` compositing config; the durable, regenerable fix is absent.
- **Omissions**: no `RO:0002012` import addition, no `unfold_over` → `RO:0002162` change in `config/taxa.yaml`, and no `docs/bridges.md` / `docs/combined_multispecies.md` updates.
- **Over-editing / scope creep**: large churn across multiple checked-in generated bridge OWL files that the build regenerates; touched-file set well beyond the human's five files.
