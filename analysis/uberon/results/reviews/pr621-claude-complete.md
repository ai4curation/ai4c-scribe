---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 621
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.382
precision: 0.406
recall: 0.361
jaccard: 0.236
outcome: partial_success
failure_modes: [over_editing, scope_creep, wrong_pattern]
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "The merged gold PR #3671 reflects post-review refinements by RiveraAndrea83 (salivon: is_a organ subunit + part_of lobule; dentogingival junction is_a anatomical junction; def refs PMID:30855909). The issue #3657 thread converged on a different negotiated proposal (salivon is_a UBERON:0009911 lobule; dentogingival is_a UBERON:0000479 tissue + part_of UBERON:0001828 gingiva). This attempt (diff byte-identical to #683, blob 95b972b) matches NEITHER target: is_a organ subunit but DROPPED part_of lobule, dentogingival part_of UBERON:0001758 periodontium (proposal/gold use part_of gingiva), added intersection_of equivalence axioms, the disputed in_taxon NCBITaxon:9606, and a non-canonical human_reference_atlas subset. The 0.382 F1 is mostly genuine."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode (re-run; diff byte-identical to attempt #683, blob `95b972b`) added all five requested HRA/HuBMAP terms but diverged from both the issue #3657 negotiated proposal and the gold PR. It used `is_a UBERON:0000063 organ subunit` for the salivon *without* the compensating `part_of UBERON:0009911 lobule` (so it matches neither the proposal's `is_a lobule` nor gold's `organ subunit + part_of lobule`), modeled `dentogingival junction` with `part_of UBERON:0001758 periodontium` (both proposal and gold use `part_of UBERON:0001828 gingiva`), and added unrequested `intersection_of` equivalence axioms, the explicitly-disputed `in_taxon NCBITaxon:9606`, and a non-canonical `human_reference_atlas` subset. The 0.382 F1 is mostly genuine — a partial success with real modeling and scope problems, not merely a scoring artifact.

## Strengths

- **All five terms created** with correct labels, the gland-specific `part_of` to the right glands (`UBERON:0001831` parotid, `UBERON:0001832` sublingual, `UBERON:0001736` submandibular) and a coherent generic→specific `is_a` hierarchy.
- **Correct `subset: added_by_HRA`** is present (alongside the spurious extra subset — see Issues).
- **Definitions reasonable** and salivon/`... ducto-acinar` synonyms correctly typed (EXACT/RELATED); dentogingival junction retains the three expected RELATED synonyms.

## Issues

- **Generic parent mismatch with both targets (wrong_pattern)**: `is_a UBERON:0000063 organ subunit` without `part_of UBERON:0009911 lobule`. The proposal said `is_a lobule`; gold's reviewer chose `is_a organ subunit` + `part_of lobule`. Dropping the lobule link loses the relationship both targets preserve.
- **`dentogingival junction` `part_of UBERON:0001758 periodontium` (genuine error)**: proposal and gold both specify `part_of UBERON:0001828 gingiva` (the requester's explicitly requested parent). Periodontium is broader and contradicts the requested placement.
- **Disputed taxon constraint (over-edit)**: `in_taxon NCBITaxon:9606` on all five terms; nicolevasilevsky's final comment left this unresolved and gold omits it. Requester-flagged over-reach (`scope_creep`).
- **Unrequested `intersection_of` equivalence axioms**: full equivalence classes plus `connects calcareous tooth`/`connects gingiva` for dentogingival; proposal/gold used only primitive `is_a` + `relationship: part_of`. Stronger unauthorized logical commitment.
- **Non-canonical extra subset**: `subset: human_reference_atlas` in addition to `added_by_HRA`; gold uses only `added_by_HRA`. Spurious non-established subset.
- **Extra provenance metadata** (`dc-contributor`, `dcterms-date`, `created_by`): conventional agent provenance; minor relative to the substantive issues.
- **No PR/issue comment body captured** in the attempt record (re-run snapshot), so methodology cannot be independently verified; the identical diff to #683 implies the same process.
- **Placeholder ID range** `UBERON:9900000-9900004`: harmless placeholder artifact; follows the `99xxxxx` config convention.
