---
ontology: uberon
issue_number: 3414
pr_number: 3499
eval_repo_pr: 596
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.226
precision: 0.231
recall: 0.222
jaccard: 0.128
outcome: partial_success
failure_modes: [wrong_pattern]
case_quality: poor
case_quality_reason: gold_renegotiated_outside_issue
companion_prs: [3420]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is a sibling run of eval PR #656 (same model gpt-5.4/opencode, identical
blob `cecb942`, identical F1 0.226 — tied for highest in the 13-attempt case).
The agent added all 8 terms from the issue's authoritative 2025-02-13 spec
(`UBERON:8600124`–`8600131`), with the expert-mandated layer placement and
logically defined epithelium/muscularis terms. The byte-identical diff to #656
means the assessment is the same: a solid, issue-compliant submission whose
top-of-case F1 still **under-represents** quality because gold PR #3499
renegotiated labels and structure outside the issue thread (METADATA.md).

## Strengths

- **Complete, correctly enumerated term set:** all 8 terms
  (`UBERON:8600124`–`8600131`) match @aleixpuigb's explicit 2025-02-13 list.
- **Followed expert layer placement** (2024-11-26 forwarded SME guidance):
  epithelium terms `part_of UBERON:0005048 ! mucosa of fallopian tube`;
  muscularis terms `intersection_of UBERON:0006642 ! muscle layer of oviduct`.
- **Logical definitions for every term** (`intersection_of UBERON:0000483 !
  epithelium` + `part_of UBERON:0005048`; `intersection_of UBERON:0006642` +
  `part_of UBERON:0003889`) — good ontological practice.
- **Honored the polarity constraint semantically:** no erroneous `part_of
  mesosalpinx`/`part_of antimesosalpinx`; definitions correctly frame these as
  regional designations.
- Disambiguated bare issue labels with EXACT synonyms (e.g. `superior
  epithelium of fallopian tube` / `superior epithelium`); complete metadata
  (dc-contributor Ellen Quardokus, term_tracker_item, dcterms-date,
  created_by).

## Issues

- **No explicit `adjacent_to` (or other) relation** linking the
  mesosalpinx/antimesosalpinx terms to UBERON:0012331 / UBERON:8600117;
  polarity is encoded only in free text — the same modeling gap as #656.
  Correctly avoids the wrong `part_of` but leaves the spatial relationship
  unaxiomatized (`wrong_pattern`).
- **Generic epithelial genus** (`UBERON:0000483 ! epithelium`) rather than the
  more specific `UBERON:0004804 ! oviduct epithelium`.
- **Muscularis `part_of UBERON:0003889 ! fallopian tube`** is broader than the
  expert-named `muscle layer of oviduct`; partly mitigated by the
  `intersection_of UBERON:0006642` genus.
- Deletes one trailing blank line at end of file — cosmetic, harmless.
- Divergence from gold labels/intermediate parent is a gold-renegotiation
  artifact, not an agent failing (METADATA.md). Duplicate of #656 — no
  independent signal.
