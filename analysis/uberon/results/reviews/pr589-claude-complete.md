---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 589
agent: std_opencode_gpt54
model: gpt-5.4
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

This is a near-duplicate of eval PR #651 (same gpt-5.4/opencode, same `90ee60c` / `50b49faa7` blob signature on the FBdv bridge): the agent flipped `BFO:0000066` to `RO:0002162` in the static `bridge-xao-ls.rules` and `bridges.rules` `%TAXREL` switch and then hand-patched the generated bridge OWL artifacts (`uberon-bridge-to-fbdv.owl`, `-fma.owl`, and more). F1=0.000 is a genuine failure, not a metadiff artifact — the case is `case_quality: ok` with a sound gold. The agent correctly identified the relation but never touched the active generator (`src/scripts/taxa.py`), the compositing config (`src/ontology/config/taxa.yaml`), the RO import, or the docs that the gold PR changed.

## Strengths

- Correctly extracted the issue resolution: standardize life-stage bridge restrictions on `in taxon` (`RO:0002162`) instead of the species-varying `BFO:0000066`/`BFO:0000050`.
- Consistent relation substitution including the `prefix RO:` declaration and `declare(RO:0002162, /type="object_property")` in `bridge-xao-ls.rules`, and both `UBERON:0000104` / `UBERON:0000105` branches in `bridges.rules`.

## Issues

- **Wrong pattern**: keeps a single existential restriction with the relation swapped, rather than the gold two-axiom form (`EquivalentTo ... RO:0002162 some {taxon}` plus a separate `SubClassOf %TAXREL some {taxon}`); the part_of/occurs_in distinction is lost.
- **Missed source-of-truth**: the live SSSOM/T pipeline is emitted by `src/scripts/taxa.py`; editing the static rule files and generated `*.owl` outputs does not produce the regenerable fix gold delivers.
- **Omissions**: no `RO:0002012` added to `src/ontology/imports/ro_terms.txt`; no `docs/bridges.md` / `docs/combined_multispecies.md` worked-example updates; `config/taxa.yaml` `unfold_over` left unchanged.
- **Over-editing / scope creep**: large hand-edited churn across generated bridge OWL files (including trailing-blank-line trimming such as `uberon-bridge-to-fbdv.owl` line 316) that the next build will overwrite; touched-file count far exceeds the human's five.
