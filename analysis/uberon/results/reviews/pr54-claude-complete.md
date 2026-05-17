---
ontology: uberon
issue_number: 3457
pr_number: 3569
eval_repo_pr: 54
agent: std_opencode_g55
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

gpt-5.5/opencode (second run) added the correct June 24 2025 batch of 7 terms as OBO stanzas in `src/ontology/uberon-edit.obo`. The agent diff is **byte-identical** to opencode attempt #71 (same blob `7e174bf`, same content, same `dragon-ai-agent` / Aleix Puig-Barbé attribution, same posterior-scrotal-artery error). The PR write-up differs (it claims `UBERON:89200xx` IDs and ELK reasoning), but the committed stanzas are `UBERON:99000xx`. F1=0.000 is **structural** — gold PR #3569 uses the DOSDP pattern-TSV workflow with `UBERON:89200xx` IDs.

## Strengths

- Correct batch and full coverage: all 7 June 24 terms with VCCF xrefs, definitions + source xrefs, artery/vein parents, vascular relations (`connecting_branch_of`/`vessel_supplies_blood_to`/`tributary_of`/`vessel_drains_blood_from`), `term_tracker_item` to #3457, contributor + dcterms-date.
- Sound anatomy matching gold's drains/source targets for the splenic, rectal, and scrotal vessels.
- Reported `robot convert` and `robot reason` (ELK) validation.

## Issues

- Wrong arterial source for posterior scrotal artery: `connecting_branch_of UBERON:0001358 (perineal artery)`; gold uses `internal pudendal artery (UBERON:0007315)`.
- Contributor attributed to Aleix Puig-Barbé (ORCID 0000-0001-6677-8489); gold #3569 batch is Arwa Ibrahim (0000-0001-6757-4744). The PR comment's claim of verifying "Arwa Ibrahim ORCID" contradicts the committed `dc-contributor`, and its claim of `UBERON:89200xx` IDs contradicts the committed `UBERON:99000xx` — a write-up/diff mismatch.
- Base-state contamination (`scope_creep`): same foreign `seeAlso`/`source` reordering hunk on unrelated terms (flying-fish wing, hyoid, spinal accessory nerve, manual digits, spleen marginal sinus, lateral malleolus) and `airway hillock` relationship reorder — robot-reserialization churn from the eval base, not issue work.
- Wrong workflow (`wrong_pattern`): hand-authored stanzas with placeholder 99xxxxx IDs instead of the artery/vein DOSDP pattern TSVs used by gold and all prior VCCF batches.
- This is a `case_quality: poor` case (see METADATA.md): F1=0 is dominated by workflow/ID mismatch and base contamination; substance is largely correct (one parent error, wrong contributor).
