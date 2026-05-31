---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 409
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.441
precision: 0.531
recall: 0.377
jaccard: 0.283
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This run (claude-opus-4.7 / claude) is the strongest of the four attempts and produced a
substantively competent porphyria restructure: all 8 ClinGen genes addressed, correct
gene-grouping equivalence axioms, the GCEP definitions transcribed, ClinGen-attributed
synonyms added, and `term_tracker_item` annotations on every touched term. The reported
F1=0.441 (precision=0.531, recall=0.377) materially **under-represents** the quality:
the new grouping terms were created with the config-mandated placeholder IDs
`MONDO:7770003/7770004/7770005` while the gold used the registered IDs
`MONDO:0700382/0700383/0700384`, so every `id:`/`is_a:` line on the three new terms and
the ~6 lumping axioms that reference them is scored as a miss by construction (the
placeholder-vs-canonical MONDO ID artifact — see Curation Note). The genuine, non-artifact
error is that the agent **renamed** the primary labels of six existing terms, whereas the
curator deliberately kept the original labels and added the ClinGen names only as EXACT
synonyms.

## Strengths

- **Correct gene-grouping construction.** New terms MONDO:7770003 (HMBS-related hepatic
  porphyria) and MONDO:7770005 (PPOX-related hepatic porphyria) were given exactly the
  logical definition the curator used for MONDO:0700382/0700383: `intersection_of:
  MONDO:0002520 ! hepatic porphyria` + `intersection_of:
  has_material_basis_in_germline_mutation_in <hgnc>`, following the
  `disease_series_by_gene` DOSDP pattern. HGNC IDs are correct (HMBS=4982, PPOX=9280).
- **Correct lumping.** Added `is_a MONDO:7770003` to MONDO:0008294 (acute intermittent
  porphyria) and `is_a MONDO:7770005` to MONDO:0008297 (variegate porphyria), matching the
  gold's intent of placing the HMBS/PPOX disease entities under the new gene groupers
  (gold did the same via MONDO:0700382/0700383). Reasoned correctly that
  MONDO:0019799 (hepatoerythropoietic) and MONDO:0957577 inherit transitively.
- **UROD restructure matches gold semantics.** Added `is_a MONDO:0100498` to MONDO:0015104
  (porphyria cutanea tarda) and removed the now-inconsistent `excluded_subClassOf
  MONDO:0019142`; the gold achieved the equivalent end-state on the UROD-related entity
  MONDO:0008295 by replacing its `intersection_of MONDO:0015104 / has_characteristic
  MONDO:0021152` equivalence with `is_a MONDO:0100498`.
- **Definitions transcribed faithfully** from the ClinGen GCEP text with the
  `https://clinicalgenome.org/affiliation/40097/` xref, matching the gold definitions for
  FECH (MONDO:0008319), UROS (MONDO:0009902), ALAS2 (MONDO:0010420), ALAD (MONDO:0013000)
  and UROD (MONDO:0100498) near-verbatim.
- **Disciplined provenance and process.** ClinGen-attributed EXACT synonyms with the
  `OMO:0002001` qualifier, `term_tracker_item` to #9703 on all edited terms, and an
  explicit, well-reasoned PR comment flagging the open "erythropoietic porphyria" question
  raised by @sabrinatoro — the same question the curator and @mtwilke-art resolved in the
  issue thread. The agent handled it conservatively (no new grouping term), which is
  consistent with what the curator ultimately did.

## Issues

- **Renamed existing terms (genuine `wrong_pattern` error, not an artifact).** The agent
  changed `name:` on MONDO:0008319 → "FECH-related erythropoietic protoporphyria",
  MONDO:0009902 → "UROS-related erythropoietic porphyria", MONDO:0010420 →
  "ALAS2-related erythropoietic protoporphyria", MONDO:0013000 → "ALAD-related hepatic
  porphyria", MONDO:0100498 → "UROD-related porphyria", MONDO:0800180 → "CPOX-related
  hepatic porphyria", demoting the original labels to synonyms. The curator did **not**
  rename any existing term — the ClinGen names were added as EXACT synonyms while primary
  labels were preserved. This is a defensible reading of the spreadsheet's "new label"
  column but diverges from Mondo curation practice and from the accepted resolution; it
  accounts for most of the genuine (non-ID-artifact) precision/recall loss.
- **Did not create MONDO:0700384 equivalent correctly.** The agent created
  MONDO:7770004 "acute intermittent porphyria, nonerythroid variant" as a child of
  MONDO:7770003, which corresponds to the gold's MONDO:0700384 "porphyria, acute
  intermittent, nonerythroid variant" (is_a MONDO:0700382). The intent matches but the
  label differs slightly from the curator's chosen form.
- **Placeholder MONDO IDs (config-mandated; not a fault of the agent).** Per
  `mondo-agent-config` CLAUDE.md ("New terms start MONDO:777xxxx"), the agent used
  MONDO:7770003-5. The gold used MONDO:0700382-4. This is correct behavior under the
  agent's instructions but is the dominant cause of the depressed metadiff — see the
  Curation Note added to METADATA.md.
- **Could not run ODK normalization** (no Docker in the runner). Flagged transparently;
  the diff is not normalized, which would need a local NORM pass before merge.

Overall a partial success whose true quality is appreciably higher than F1=0.441 implies:
the substantive ontology engineering (new gene groupers, equivalence axioms, lumping,
definitions, provenance) is largely correct; the only genuine modeling error is the
unrequested renaming of existing terms. The score gap is dominated by the
placeholder-vs-canonical ID artifact, not by agent error.
