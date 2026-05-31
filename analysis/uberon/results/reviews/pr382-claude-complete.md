---
ontology: uberon
issue_number: 3629
pr_number: 3630
eval_repo_pr: 382
agent: codex
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.609
precision: 0.636
recall: 0.583
jaccard: 0.438
outcome: partial_success
failure_modes:
  - wrong_term
  - over_editing
case_quality: ok
case_quality_reason: gold_verbatim_issue_text_with_metadiff_scoring_artifacts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added `UBERON:9900000 carotid artery intima–media region` with the canonical ID, correct definition, synonym, disjointness, and provenance, but **substituted the issue-specified differentia with different terms**: it used artery-specific layer classes `UBERON:0005740` (tunica intima of artery) and `UBERON:0007239` (tunica media of artery) instead of the explicitly requested `UBERON:0002523` (tunica intima) / `UBERON:0002522` (tunica media), and added an unrequested `part_of UBERON:0000415` (artery wall). The F1=0.609 is roughly fair here — these are genuine `wrong_term` and `over_editing` divergences from a near-verbatim issue spec, not metadiff artifacts.

## Strengths

- Canonical ID `UBERON:9900000` matches gold (not the `9900001` placeholder).
- Definition verbatim-correct with single `[PMID:39416432]` xref; synonym `"carotid intima-media" EXACT [PMID:39416432]` correct.
- Correct genus `is_a: UBERON:0000481` (multi-tissue structure).
- Included `disjoint_from: UBERON:0005734 ! tunica adventitia of blood vessel` as the issue requested (semantically equivalent to gold's reciprocal placement).
- Retained `relationship: part_of UBERON:0005396` (carotid artery segment) as specified.
- Full metadata: `dc-contributor` ORCID, `dcterms-date`, `term_tracker_item` (`xsd:anyURI`), `created_by: dragon-ai-agent`. PR comment honestly notes `robot` was unavailable so reserialization could not run.

## Issues

- **`wrong_term` — differentia substitution:** the issue is exceptionally prescriptive and explicitly dictates `has part` some `tunica intima` (`UBERON:0002523`) and `has part` some `tunica media` (`UBERON:0002522`). The agent instead used `has_part UBERON:0005740` (tunica intima *of artery*) and `has_part UBERON:0007239` (tunica media *of artery*). These are anatomically plausible (arguably more precise for a carotid context) but they change the modeled differentia away from the requested axiom pattern and from the gold. On a verbatim-spec issue this is a substantive deviation, not a serialization artifact.
- **`over_editing` — unrequested relation:** added `relationship: part_of UBERON:0000415 ! artery wall`, which the issue never asked for. Defensible anatomy but it is scope creep on a tightly-scoped NTR and reduces precision.
- **Truncated contributor label:** `dc-contributor ... ! Aleix Puig` drops the full ` ! Aleix Puig-Barbé` surname. The ORCID is correct, so this is cosmetic, but it is a label inaccuracy.
- **Single hunk only:** the disjointness sits on the new-term side and there is no reciprocal `disjoint_from: UBERON:9900000` on the `UBERON:0005734` stanza, so a strict whole-file metadiff sees only one of the two gold hunks (semantically equivalent, but contributes to the lower recall alongside the real differentia divergence).

Net: correct ID, definition, synonym, genus, and disjointness, but the issue-specified `tunica intima`/`tunica media` differentia was replaced with artery-specific variants plus an extra `artery wall` partonomy. On a near-verbatim issue these are real deviations; F1=0.609 is approximately fair. Graded `partial_success`, consistent with the prior codex review of this PR.
