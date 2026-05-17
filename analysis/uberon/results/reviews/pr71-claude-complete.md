---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 71
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [wrong_pattern, wrong_term, scope_creep]
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

gpt-5.5/opencode added the correct June 24 2025 batch of 7 terms as OBO stanzas in `src/ontology/uberon-edit.obo` (obo edit-file workflow per CLAUDE.md, `UBERON:99xxxxx` range). F1=0.000 is **structural**: gold PR #3569 uses the DOSDP pattern-TSV workflow with `UBERON:89200xx` IDs, so a faithful obo-route attempt cannot line-match. The anatomical content is correct and consistent; the main real defect is one wrong arterial source plus base-state reserialization contamination in the diff. This run is byte-identical (blob `7e174bf`) to opencode attempt #54.

## Strengths

- Correct batch and complete coverage: all 7 June 24 terms with their VCCF xrefs (VCCF:1000203, 1000195, 1000348, 1000362, 1000750, 1000708, 1000709), each with definition + source xref, parent (`UBERON:0001637` artery / `UBERON:0001638` vein), vascular relations (`connecting_branch_of`, `vessel_supplies_blood_to`, `tributary_of`, `vessel_drains_blood_from`), `term_tracker_item` to #3457, contributor + dcterms-date.
- Sound anatomy: lobar artery of spleen → splenic artery + spleen; superior rectal vein → inferior mesenteric vein + rectum; inferior/posterior scrotal veins → internal pudendal vein — all agree with gold's drains/source targets.
- Reported `robot convert` syntax validation and `robot reason` (ELK) consistency check; reasonable methodology.

## Issues

- Wrong arterial source for posterior scrotal artery: `connecting_branch_of UBERON:0001358 (perineal artery)`; gold sources it from `internal pudendal artery (UBERON:0007315)`.
- Contributor attributed to Aleix Puig-Barbé (ORCID 0000-0001-6677-8489); the gold #3569 batch is attributed to Arwa Ibrahim (0000-0001-6757-4744). Wrong contributor for this issue.
- Base-state contamination (`scope_creep`): the diff carries a large foreign hunk of `seeAlso`/`source` annotation reordering on unrelated terms (flying-fish wing, hyoid bone, spinal accessory nerve, manual digits, spleen marginal sinus, lateral malleolus) and an `airway hillock` (UBERON:8910024) relationship reorder — robot-reserialization churn from the eval base, not issue work.
- Wrong workflow (`wrong_pattern`): hand-authored stanzas with placeholder 99xxxxx IDs instead of the artery/vein DOSDP pattern TSVs used by gold and all prior VCCF batches.
- This is a `case_quality: poor` case (see METADATA.md): F1=0 is dominated by the workflow/ID mismatch and base contamination; on substance the term content is largely correct (one parent error).
