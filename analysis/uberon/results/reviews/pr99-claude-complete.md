---
ontology: uberon
issue_number: 3495
pr_number: 3542
eval_repo_pr: 99
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.354
precision: 0.315
recall: 0.405
jaccard: 0.215
outcome: partial_success
failure_modes: [scope_creep, instruction_violation, under_editing]
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_reserialization_churn
companion_prs: [3541]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent added 11 terms (4 colon epithelium + 7 lamina propria). The seven
lamina propria terms have correct genus and correct part_of targets, but the
attempt violates two explicit instructions: it adds both `is_a` AND a
duplicated `relationship: part_of` alongside the `intersection_of` axioms,
directly contradicting @dosumis's "no need to duplicate `intersection_of:
part_of` as a relationship", and it re-does the epithelium half that belongs
to companion PR #3541. Provenance is also fabricated: every definition uses
the placeholder dbxref `[UBERON:cjm]`. F1=0.354 reflects real defects (scope
creep, instruction violation, missing synonyms/metadata) plus the shared
placeholder-ID artifact.

## Strengths

- All seven lamina propria terms present with correct genus UBERON:0000030
  and correct part_of targets across all segments.
- Correct definition text pattern ("The lamina propria that underlies the
  epithelial lining of the {gut segment}").
- Correct `{segment} lamina propria` primary label form (epithelium terms use
  "epithelium of {region}", which is acceptable for those).
- The (out-of-scope) epithelium terms use the correct genus UBERON:0001277
  (intestinal epithelium).

## Issues

- **Instruction violation**: adds redundant `is_a: UBERON:0000030` AND
  `relationship: part_of {segment}` on top of `intersection_of` — exactly the
  duplication @dosumis told the agent not to add, and inconsistent with the
  canonical UBERON:8600034/8600035 (jejunum/ileum) pattern and the gold.
- **Scope creep**: four epithelium terms duplicate PR #3541's deliverable;
  out of scope for gold PR #3542.
- **Fabricated provenance**: `[UBERON:cjm]` def dbxref on all 11 terms —
  invents an editor-style provenance token rather than using a real source;
  gold uses an ORCID dbxref (later requirement).
- **Missing metadata/synonyms**: no synonyms on any term; no `dc-contributor`,
  no `dcterms-date`. Gold carries both synonym forms plus the requestor
  contributor and date.
- Placeholder ID range UBERON:7700001-11 vs gold 8600134-140 — standard
  artifact (note: it correctly avoided the explicitly disallowed
  UBERON:7770000-7770004 band).
- Net: terms are present and roughly correct but require substantial curator
  rework (strip duplicate axioms, fix provenance, add synonyms/metadata,
  remove epithelium terms).
