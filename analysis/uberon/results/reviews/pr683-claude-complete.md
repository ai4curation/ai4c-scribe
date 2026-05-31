---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 683
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
scoring_caveat: "The merged gold PR #3671 reflects post-review refinements by RiveraAndrea83 (salivon: is_a organ subunit + part_of lobule; dentogingival junction is_a anatomical junction; def refs PMID:30855909). The issue #3657 thread converged on a different negotiated proposal (salivon is_a UBERON:0009911 lobule; dentogingival is_a UBERON:0000479 tissue + part_of UBERON:0001828 gingiva). This attempt matches NEITHER target on key axes: it used is_a organ subunit but DROPPED part_of lobule (so it does not match gold's reviewer choice either), modeled dentogingival junction with part_of UBERON:0001758 periodontium (neither proposal nor gold, which both use part_of gingiva), added intersection_of equivalence axioms, added the explicitly-disputed in_taxon NCBITaxon:9606, and added a non-canonical human_reference_atlas subset. The 0.382 F1 is mostly genuine, not a scoring artifact."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode added all five requested HRA/HuBMAP terms but diverged from both the issue #3657 negotiated proposal *and* the gold PR on several substantive axes. Unlike its gpt-5.5 siblings (#644/#585) that reproduced the proposal's `is_a UBERON:0009911 lobule`, this run used `is_a UBERON:0000063 organ subunit` *without* the compensating `part_of UBERON:0009911 lobule` that gold's reviewer added — so it matches neither the proposal nor gold's final state. It further modeled `dentogingival junction` with `part_of UBERON:0001758 periodontium` (both proposal and gold use `part_of UBERON:0001828 gingiva`), added unrequested `intersection_of` equivalence axioms, the explicitly-disputed `in_taxon NCBITaxon:9606`, and a non-canonical `human_reference_atlas` subset. The 0.382 F1 is mostly genuine — this is a partial success with real modeling and scope problems, not merely a scoring artifact.

## Strengths

- **All five terms created** with correct labels, the gland-specific `part_of` to the right glands (`UBERON:0001831` parotid, `UBERON:0001832` sublingual, `UBERON:0001736` submandibular) and a coherent generic→specific `is_a` hierarchy.
- **Correct `subset: added_by_HRA`** is present (alongside the spurious extra subset — see Issues).
- **Definitions are reasonable** and the salivon/`... ducto-acinar` synonyms are correctly typed (EXACT/RELATED); dentogingival junction retains the three expected RELATED synonyms.
- **Reasonable design rationale articulated** (modeled the FTU as `organ subunit` per the issue's "not epithelial-only multicellular unit" framing) and validation steps documented (existing-term check, ROBOT convert).

## Issues

- **Generic parent mismatch with both targets (wrong_pattern)**: used `is_a UBERON:0000063 organ subunit` but omitted `part_of UBERON:0009911 lobule`. The issue proposal said `is_a lobule`; the gold reviewer chose `is_a organ subunit` + `part_of lobule`. By dropping the lobule link entirely this attempt loses the lobule relationship that *both* the proposal (as genus) and gold (as part_of) preserve.
- **`dentogingival junction` `part_of UBERON:0001758 periodontium` (genuine error)**: the negotiated proposal and the gold PR both specify `part_of UBERON:0001828 gingiva` (the requester's explicitly requested parent). Periodontium is broader than gingiva and contradicts the requester's stated parent term; this is a substantive misplacement.
- **Disputed taxon constraint (over-edit)**: added `relationship: in_taxon NCBITaxon:9606` to all five terms. nicolevasilevsky's final issue comment explicitly left this unresolved (may occur in other mammals/vertebrates); gold omits it. Requester-flagged over-reach (`scope_creep`).
- **Unrequested `intersection_of` equivalence axioms**: added full equivalence-class axioms (`intersection_of: ... part_of ...`; for dentogingival, `intersection_of: connects calcareous tooth` + `connects gingiva`). The proposal and gold used only primitive `is_a` + `relationship: part_of`. Asserting equivalence and `connects` axioms is a stronger, unauthorized logical commitment.
- **Non-canonical extra subset**: added `subset: human_reference_atlas` in addition to `added_by_HRA`. Gold uses only `added_by_HRA`; the extra subset is not an established UBERON subset and is spurious.
- **Extra provenance metadata** (`dc-contributor`, `dcterms-date`, `created_by`): conventional agent provenance; gold carries only `subset` + `term_tracker_item`. Minor relative to the substantive issues above.
- **Placeholder ID range** `UBERON:9900000-9900004`: harmless placeholder artifact; follows the `99xxxxx` config convention.
