---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 592
agent: std_opencode_g54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.500
precision: 0.375
recall: 0.750
jaccard: 0.333
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: ok
case_quality_reason: gold_pr_genuine_but_metadiff_under_represents_top_attempts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt produces a diff byte-identical to pr649 (same blob `d70acc6`, same
gpt-5.4/opencode runtime): both taxon restrictions on `neurula stage`
(UBERON:0000110) and `pharyngula stage` (UBERON:0004707) are tightened from
Eumetazoa (NCBITaxon:6072) to Chordata (NCBITaxon:7711), and the unconditional
`late embryonic stage` (UBERON:0007220) `preceded_by` UBERON:0004707 axiom is
converted to a taxon-scoped GCI. The metadiff F1 of 0.500 over-states the GCI
modeling: the differentia is `gci_relation="in_taxon"`, a genuinely weaker model
than the issue's proposed `occurs in` some Chordata. Otherwise tightly scoped, with
the same benign EOF whitespace reserialization artifact as pr649.

## Strengths

- Both taxon-restriction edits are byte-identical to the gold PR:
  `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata` on
  UBERON:0000110 and UBERON:0004707, fully satisfying proposal item (1).
- The GCI conversion correctly removes the unconditional global
  `preceded_by UBERON:0004707` and replaces it with a taxon-qualified GCI
  (`gci_filler="NCBITaxon:7711"`, Chordata), decoupling the broad
  `late embryo`/`late embryonic stage` classes from the chordate-specific
  pharyngula stage — the structural fix the issue requested.
- Tight scope discipline: only the three issue-relevant term stanzas plus a single
  trailing-newline change; no `term_tracker_item` over-editing, no unrelated
  CL/import reserialization churn (verified the diff is confined to
  uberon-edit.obo and matches pr649 exactly).

## Issues

- Wrong pattern (GCI differentia): identical to pr649 — the GCI uses
  `{gci_relation="in_taxon", gci_filler="NCBITaxon:7711"}` rather than the issue's
  proposed `occurs in` (gold: `gci_relation="BFO:0000066"`). `in_taxon` as the GCI
  antecedent differentia is semantically a weaker/different model than `occurs in`;
  this is a fair penalty distinct from the surface-only label-vs-IRI difference in
  the stronger pr336/pr279 attempts. The decoupling goal is met but the axiom shape
  does not match the stated model.
- Omission: did not reword the `neurula stage` / `pharyngula stage` textual
  definitions to "A chordate developmental stage ...". Defensible (not in issue
  proposal items 1–2; only in the PR author's narrative) but the main recall loss.
- Minor cosmetic: trailing blank line removed at EOF (`vessel_supplies_blood_to`
  stanza, ~line 226040) — a `robot convert` reserialization whitespace artifact,
  harmless, localized, not contamination.
- Net: equivalent to pr649 in substance; issue's explicit asks resolved
  structurally but with a weaker GCI model than the issue specified, so F1=0.500 is
  roughly accurate and this sits below the `occurs_in`-using top tier on substance.
