---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 389
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.545
precision: 0.562
recall: 0.529
jaccard: 0.375
outcome: partial_success
failure_modes: [scope_creep]
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "The merged gold PR #3671 reflects post-review refinements by RiveraAndrea83 (salivon: is_a organ subunit + part_of lobule instead of is_a lobule; dentogingival junction is_a anatomical junction instead of tissue; 'approximately 90%' generalised; def refs changed to PMID:30855909). The issue #3657 thread converged on a different negotiated proposal (is_a lobule; dentogingival is_a tissue) that the agent partially reproduced. The 0.545 F1 partly under-represents quality (correct lobule parent + part_of axioms) but is also partly genuine: the agent added intersection_of equivalence axioms, an adjacent_to calcareous tooth relationship, and a disputed in_taxon NCBITaxon:9606 constraint — none of which were in the proposal or gold."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex added all five requested HRA/HuBMAP terms with the correct issue-negotiated parent for the salivon (`is_a UBERON:0009911 lobule` + `part_of UBERON:0001044`) and the correct gland-specific `part_of` axioms, but deviated from the negotiated proposal by adding `intersection_of` equivalence axioms, modeling `dentogingival junction` as `is_a UBERON:0000481 multi-tissue structure` (proposal/gold said `tissue`/`anatomical junction`), adding an `adjacent_to UBERON:0001091 calcareous tooth` relationship, and adding the explicitly-disputed `in_taxon NCBITaxon:9606` constraint. The 0.545 F1 partly under-represents quality (the lobule parent and part_of structure match the negotiated target) but is partly genuine — the extra equivalence/taxon edits are real scope and modeling deviations the proposal did not authorize.

## Strengths

- **Correct generic parent**: `salivary gland ducto-acinar unit` `is_a UBERON:0009911 lobule` + `relationship: part_of UBERON:0001044 saliva-secreting gland`, exactly matching the issue's converged proposal (the gpt-5.4 opencode runs wrongly used `is_a organ subunit`).
- **Correct gland-specific structure**: the three children `is_a UBERON:9900000` with `part_of UBERON:0001831` (parotid), `UBERON:0001832` (sublingual), `UBERON:0001736` (submandibular) — all matching the proposal and gold.
- **Definitions and synonyms** track the negotiated proposal closely (salivon EXACT, `... ducto-acinar` RELATED, the three dentogingival RELATED synonyms, the lobule/acini definition text); submandibular def uses "predominantly serous acini with a minority of mucous acini", aligning with the gold reviewer's preferred generalisation.
- **Honest validation disclosure**: explicitly flagged that `robot convert` reserialization could not be run because ROBOT was absent, and verified terms could be checked back out of the OBO file.

## Issues

- **Disputed taxon constraint (genuine over-edit)**: added `relationship: in_taxon NCBITaxon:9606 ! Homo sapiens` to all five terms. The issue thread explicitly left this open — nicolevasilevsky's final comment states the constraint may be wrong because the structures occur in other mammals/vertebrates. Gold omits it. This is a substantive, requester-flagged over-reach (`scope_creep`).
- **Unrequested `intersection_of` equivalence axioms**: added `intersection_of: UBERON:0009911 lobule` + `intersection_of: part_of ...` (and for dentogingival, `intersection_of: ...` was avoided but `adjacent_to` added). The negotiated proposal and gold used only primitive `is_a` + `relationship: part_of`; auto-asserting full equivalence classes is a stronger logical commitment than authorized and risks reasoner side-effects.
- **`adjacent_to UBERON:0001091 calcareous tooth` on dentogingival junction**: not in the proposal or gold; an unrequested extra relationship (defensible anatomically but out of scope).
- **`dentogingival junction` `is_a UBERON:0000481 multi-tissue structure`**: deviates from the proposal's `is_a UBERON:0000479 tissue`. This is arguably ontologically *better* (a junctional-epithelium + connective + vascular complex is properly multi-tissue, and it is closer to gold's reviewer-chosen `anatomical junction` than literal `tissue`), so a defensible independent judgment — but still a deviation from the negotiated target that lowers metadiff.
- **Extra provenance metadata** (`dc-contributor`, `dcterms-date`, `created_by`): conventional agent provenance; gold carries only `subset` + `term_tracker_item`. Minor.
- **Subset omitted**: the diff carries no `subset: added_by_HRA` line; gold has it on every term. Minor omission relative to gold/proposal.
- **Placeholder ID range** `UBERON:9900000-9900004`: harmless placeholder artifact; follows the `99xxxxx` config convention.
