---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 769
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

This run (gpt-5.4 / opencode) is **byte-identical to eval PR #714** (same blob `28c7285`,
F1=0.273, precision=0.306, recall=0.246) — a duplicate sample of the same agent/config.
The assessment of #714 applies in full: all 8 ClinGen genes addressed with correct
gene-grouping equivalence axioms and (paraphrased) GCEP definitions, but with existing
terms renamed (gold did not rename), definitions mis-provenanced to the issue URL instead
of the ClinGen affiliation, and an unrequested CPOX reframe that deletes a curated GOF
axiom. The metadiff is artifactually deflated by the placeholder-vs-canonical MONDO ID
artifact (MONDO:7770003/7770005 vs gold MONDO:0700382/0700383; see Curation Note), while
also legitimately reflecting these genuine faults. This run's PR comment is the most
thorough of the cohort, explicitly documenting the spreadsheet reconstruction and the
UROD/PCT conservatism decision.

## Strengths

- **All 8 genes addressed**; new groupers `MONDO:7770003` (HMBS), `MONDO:7770004` (AIP
  nonerythroid variant), `MONDO:7770005` (PPOX) — substantive equivalents of gold
  MONDO:0700382/0700384/0700383.
- **Correct lumping**: `is_a: MONDO:7770003` on MONDO:0008294, `is_a: MONDO:7770005` on
  MONDO:0008297, `is_a: MONDO:0100498` on MONDO:0019799, plus reparenting of hereditary
  coproporphyria / harderoporphyria under the CPOX grouper — consistent with the
  curator's gene-centric intent.
- **Best PR documentation in the cohort**: transparently reports recovering the attached
  spreadsheet, the deliberate UROD conservatism (not forcing all PCT under the inherited
  term), and the `make NORM` skip due to missing Docker — strong methodology disclosure.
- GCEP definitions transcribed with `term_tracker_item` IAO:0000233 #9703 on touched
  terms.

## Issues

- **Renamed existing terms** (genuine `wrong_pattern`): same as #714 — `name:` changed on
  MONDO:0008319/0009902/0010420/0013000/0100498 with originals demoted to synonyms; the
  curator preserved all primary labels.
- **Wrong definition provenance**: defs/synonyms cite
  `https://github.com/monarch-initiative/mondo/issues/9703` instead of the gold's
  `https://clinicalgenome.org/affiliation/40097/` definition xref.
- **CPOX mis-reframe + GOF-axiom deletion** (`over_editing`): relabeled MONDO:0800180 to
  `CPOX-related hepatic porphyria` and deleted `relationship: RO:0004001 ... gain of
  function germline mutation in CPOX` from MONDO:0019800 — unrequested removal of a
  curated axiom the gold left intact.
- **Demoted existing ClinGen EXACT synonym to RELATED** on MONDO:0013000
  (`ALAD-related porphyria`) — scope creep on externally-curated content.
- **Placeholder MONDO IDs** (config-mandated, not an agent fault): MONDO:7770003/7770005
  vs gold MONDO:0700382/0700383 — dominant cause of the depressed metadiff (Curation
  Note).
- **Duplicate run** of #714; no additional variability signal.

Overall a partial success with the same profile as #714: correct gene-grouping skeleton,
metadiff artifactually deflated by placeholder IDs, but with genuine renaming,
mis-provenanced definitions, and an unrequested CPOX GOF-axiom deletion needing curator
correction. Methodology reporting is the best in the cohort.
