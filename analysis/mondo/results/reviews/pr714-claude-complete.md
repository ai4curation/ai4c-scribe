---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 714
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.273
precision: 0.306
recall: 0.246
jaccard: 0.158
outcome: partial_success
failure_modes: [over_editing, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run (gpt-5.4 / opencode) scores in the low tier (F1=0.273, precision=0.306,
recall=0.246) and is **byte-identical to eval PR #769** (same blob `28c7285`) — a
duplicate sample of the same agent/config. It addresses all 8 ClinGen genes with correct
gene-grouping equivalence axioms and faithful GCEP definitions, but provenances the new
definitions/synonyms to the issue URL rather than the ClinGen affiliation, renames the
existing terms (gold did not), and makes the same erroneous CPOX reframe as the rest of
the opencode runs. The metadiff is artifactually deflated by the placeholder-vs-canonical
MONDO ID artifact (MONDO:7770003/7770005 vs gold MONDO:0700382/0700383; see Curation
Note), but the score also legitimately reflects genuine errors.

## Strengths

- **All 8 genes addressed** with new groupers `MONDO:7770003` (HMBS) and `MONDO:7770005`
  (PPOX, plus a `MONDO:7770004` AIP nonerythroid variant per the PR comment), substantive
  equivalents of gold MONDO:0700382/0700383/0700384.
- **Correct lumping**: `is_a: MONDO:7770003` on MONDO:0008294 (acute intermittent),
  `is_a: MONDO:7770005` on MONDO:0008297 (variegate), `is_a: MONDO:0100498` on
  MONDO:0019799 (hepatoerythropoietic) — matching the curator's restructure intent.
- **GCEP definitions** transcribed (in a tighter, paraphrased form) with
  `term_tracker_item` IAO:0000233 #9703 added to every touched term.
- **Defensible UROD conservatism**: the PR comment explains it deliberately did not force
  all porphyria cutanea tarda under the inherited UROD-related term to avoid an
  acquired-vs-inherited conflict — reasonable, reasoner-aware judgment.

## Issues

- **Renamed existing terms** (genuine `wrong_pattern`): changed `name:` on MONDO:0008319
  (→ FECH-related), MONDO:0009902 (→ UROS-related), MONDO:0010420 (→ ALAS2-related),
  MONDO:0013000 (→ ALAD-related), MONDO:0100498 (→ UROD-related porphyria) and demoted the
  originals to synonyms. The curator kept all primary labels and added ClinGen names only
  as EXACT synonyms.
- **Wrong definition provenance**: new defs/synonyms cite
  `https://github.com/monarch-initiative/mondo/issues/9703` instead of the gold's
  `https://clinicalgenome.org/affiliation/40097/` definition xref — a systematic
  attribution error across the run.
- **CPOX mis-reframe + axiom loss** (`over_editing`): relabeled MONDO:0800180 to
  `CPOX-related hepatic porphyria` and **deleted** the existing
  `relationship: RO:0004001 ... ! has material basis in gain of function germline mutation
  in CPOX` from MONDO:0019800 (harderoporphyria) — an unrequested removal of a curated
  GOF axiom the gold did not touch.
- **Demoted an existing ClinGen EXACT synonym to RELATED**: on MONDO:0013000 changed
  `synonym: "ALAD-related porphyria" EXACT [...clingen...]` to RELATED — unrequested
  scope creep on externally-curated content.
- **Placeholder MONDO IDs** (config-mandated, not an agent fault): MONDO:7770003/7770005
  vs gold MONDO:0700382/0700383 — dominant cause of the depressed metadiff (Curation
  Note).
- **Duplicate run** of #769; no additional variability signal.

Overall a partial success: the gene-grouping skeleton is correct and the metadiff is
artifactually deflated by placeholder IDs, but the renaming, mis-provenanced definitions,
CPOX GOF-axiom deletion, and synonym-scope edits are genuine faults requiring curator
correction.
