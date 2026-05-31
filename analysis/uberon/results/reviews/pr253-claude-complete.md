---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 253
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: failure
failure_modes: [wrong_term, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-opus-4.7 deliberately added a **different batch** than the case target: 6 lung-vasculature terms (left/right superior/inferior pulmonary veins, left/right bronchial veins) rather than the June 24 2025 spleen/esophagus/scrotum/vagina/rectum batch that gold PR #3569 implements. It self-described this as "a single coherent batch ... as a starting point" for the larger tracker. F1=0.000 is partly structural (obo workflow vs gold DOSDP-TSV) but here also reflects a genuine wrong-target choice — the terms it added correspond to the **April 30 2025 comment**, which was already handled in an earlier companion PR.

## Strengths

- Anatomically competent stanzas: pulmonary veins correctly `is_a` left/right pulmonary vein (`UBERON:0009030`/`0009032`), bronchial veins `is_a UBERON:0001592 (bronchial vein)`, with sensible `vessel_drains_blood_from` targets (lobes of lung, main bronchi) and Latin synonyms with `OMO:0003011` synonym-type.
- Honest, well-scoped PR/issue commentary: explicitly flagged that this was only a slice of the tracker and asked maintainers to confirm the ID range and modeling conventions before further batches.
- Correct metadata pattern (term_tracker_item to #3457, dcterms-date, created_by).

## Issues

- Wrong target batch (`wrong_term`): the 6 lung terms (VCCF:1000002/1000001/1000011/1000010/1000834/1000847) are the April 30 2025 tracker batch, not the open June 24 batch the case (and gold #3569) addresses. The case's 7 expected terms (lobar artery of spleen, etc.) are entirely absent. This is a substantive miss, not just a metadiff artifact.
- Contributor attributed to Ellen Quardokus (ORCID 0000-0001-7655-4833); gold/Arwa Ibrahim batches use 0000-0001-6757-4744. Wrong contributor for this issue's terms.
- Base-state contamination / reserialization churn: the diff carries a foreign `airway hillock` (UBERON:8910024) relationship reordering (`part_of`/`has_part` swap) plus blob `aaf65e4` shared with no-op style — unrelated to the issue and a `scope_creep` artifact of the eval base.
- Wrong workflow: hand-authored obo stanzas with `UBERON:99xxxxx` placeholders instead of the DOSDP pattern TSVs used by gold and all prior VCCF batches.
- This is a `case_quality: poor` case (see METADATA.md); however, unlike the other obo attempts, this one's F1=0 is **not** purely structural — it picked the wrong batch, so the failure outcome is warranted on substance.
