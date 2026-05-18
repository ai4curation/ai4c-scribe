---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 629
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

This gpt-5.5/opencode attempt shares the `50d23d8` blob signature with eval PR #568: it swaps `BFO:0000066` for `RO:0002162` in the static `bridges.rules` `%TAXREL` switch and `bridge-xao-ls.rules`, claims to update the legacy `src/scripts/` and `src/ontology/` Perl xref scripts, and refreshes the generated bridge OWL products (`uberon-bridge-to-fbdv.owl`, `-wbls.owl`, `-xao.owl`, `-zfs.owl`, `-sslso.owl`). The PR comment additionally claims it "regenerated the SSSOM/T-OWL bridge rules from `taxa.py`" and ran ELK reasoning — but the diff shows **no change to `src/scripts/taxa.py`, `config/taxa.yaml`, `ro_terms.txt`, or the docs**, so those validation claims are not reflected in source-of-truth edits. F1=0.000 is a genuine failure on a sound `case_quality: ok` case.

## Strengths

- Correctly identified the agreed relation `in taxon` (`RO:0002162`) and the relevant subtree anchors `UBERON:0000104` (life cycle) / `UBERON:0000105` (life cycle stage).
- More thorough self-reported validation than sibling attempts (Perl syntax checks, `robot convert`, ELK reasoning over each modified bridge).

## Issues

- **Wrong pattern**: single-axiom relation swap, not the gold two-axiom form (`EquivalentTo` with `RO:0002162` plus separate `SubClassOf %TAXREL some {taxon}`).
- **Missed source-of-truth**: despite a PR comment claiming the `taxa.py` rules were regenerated, the diff does not modify `src/scripts/taxa.py` or `config/taxa.yaml` — the actual gold targets — so the durable fix is absent and the comment overstates what was done.
- **Omissions**: no `RO:0002012` import addition; no `unfold_over` → `RO:0002162` config change; no `docs/bridges.md` / `docs/combined_multispecies.md` updates.
- **Over-editing / scope creep**: large hand/regeneration churn across multiple checked-in generated bridge OWL files; touched-file set far broader than the human's five.
