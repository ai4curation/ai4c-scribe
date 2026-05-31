---
ontology: uberon
issue_number: 3495
pr_number: 3542
eval_repo_pr: 67
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.544
precision: 0.519
recall: 0.571
jaccard: 0.373
outcome: partial_success
failure_modes: [scope_creep, under_editing]
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_reserialization_churn
companion_prs: [3541]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent added all seven required lamina propria terms correctly, but also
re-added four colon **epithelium** terms (UBERON:9900000-3) that belong to
companion PR #3541, not to gold PR #3542's sub-task. The lamina propria terms
themselves are well-formed (correct genus UBERON:0000030, correct part_of
targets, no duplicated `relationship: part_of` per @dosumis's instruction),
but each carries only a single synonym (missing the adjectival forms the gold
includes). F1=0.544 mixes a genuine scope-creep penalty with the usual
placeholder-ID/reserialization artifacts. Identical blob (`9a93c87`) to
attempt #50 — the two are the same run replicated.

## Strengths

- All seven lamina propria terms present with correct part_of targets and
  genus UBERON:0000030 (lamina propria); correct primary label form
  `{segment} lamina propria`.
- Honoured @dosumis's explicit "no need to duplicate `intersection_of:
  part_of` as a relationship" instruction — no redundant asserted part_of.
- Correct definition pattern for the lamina propria terms.
- Reserialized with robot, so it reproduces the gold's `seeAlso`
  reordering hunk at line ~223 — incidental alignment with gold noise rather
  than a quality signal, but shows a faithful edit-workflow round-trip.
- Epithelium terms, while out of scope here, are themselves correctly modelled
  (genus UBERON:0001277 intestinal epithelium + part_of) and were legitimately
  requested in the issue — just in the wrong PR.

## Issues

- **Scope creep**: four epithelium terms (ascending/transverse/descending/
  sigmoid colon) duplicate companion PR #3541's deliverable. The gold PR #3542
  is deliberately scoped to lamina propria only; @cmungall had already filed
  #3541 for the epithelium half before this comment thread. These extra
  stanzas depress precision against the #3542 gold.
- **Under-editing on synonyms**: only one synonym per term ("lamina propria of
  X"); gold also adds the adjectival form ("ascending colonic lamina
  propria", "gastric lamina propria", etc.). Caecum is the only term with the
  fuller synonym set.
- Definition dbxref is the genus ID `[UBERON:0000030]` (self-referential, weak
  provenance) rather than gold's `[https://orcid.org/0000-0003-4389-9821]`
  (the ORCID-dbxref requirement post-dated this run, so partially excusable).
- Placeholder ID range UBERON:9900000-10 vs gold's 8600134-140 — standard
  ID artifact, not a quality defect.
- Adds `created_by` / `term_tracker_item` not in gold — metadiff noise only.
