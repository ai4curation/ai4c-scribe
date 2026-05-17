---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 265
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.781
precision: 0.781
recall: 0.781
jaccard: 0.641
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "The merged gold PR #3671 reflects post-review refinements by RiveraAndrea83 (is_a organ subunit + part_of lobule instead of is_a lobule; dentogingival junction is_a anatomical junction instead of tissue; removed 'approximately 90%'; def refs changed to PMID:30855909). The issue thread, however, converged on a different negotiated proposal (is_a lobule; dentogingival is_a tissue; 'approximately 90%'; NBK538325 ref) that the agent faithfully and correctly reproduced. The 0.781 F1 substantially under-represents quality because it penalizes the agent for not anticipating reviewer-driven changes made after the issue discussion closed. A follow-up PR (#3673) added subset tags / logical definitions."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Opus added all five requested HRA/HuBMAP terms (salivary gland ducto-acinar unit + three gland-specific children + dentogingival junction) faithfully reproducing the final negotiated proposal in issue #3657's discussion thread. The F1 of 0.781 under-represents quality: the merged gold PR diverges from the issue's negotiated proposal because reviewer RiveraAndrea83 requested structural changes *after* the issue discussion closed (changing the salivon parent to `organ subunit` + `part_of lobule`, changing dentogingival junction to `is_a anatomical junction`, dropping the "approximately 90%" wording, and switching def references). Judged against the issue's actual instructions and the converged proposal, this is a strong, correct, well-scoped result.

## Strengths

- **Faithfully reproduced the negotiated proposal**: definitions, synonyms (`salivon` EXACT, `salivary gland ducto-acinar` RELATED), `part_of UBERON:0001044 saliva-secreting gland`, gland-specific `part_of` to UBERON:0001831/0001832/0001736, and the dentogingival `part_of UBERON:0001828 gingiva` all match the dragon-ai-agent ↔ zhengj2007 converged proposal verbatim.
- **Independently improved on the proposal for dentogingival junction**: used `is_a UBERON:0000481 multi-tissue structure` rather than the proposal's `is_a tissue`, with a sound rationale (UBERON's `tissue` is restricted to one/few cell types in a single ECM; a junctional-epithelium + connective-tissue + vascular complex is properly a multi-tissue structure). This is the closest of the three attempts to gold's reviewer-chosen `anatomical junction` and is ontologically defensible on its own terms.
- **Correct subset**: used `subset: added_by_HRA`, matching the gold PR exactly (Sonnet used `human_reference_atlas`; Haiku omitted the subset entirely).
- **Strong methodology and transparency**: cited the mammary gland lobule (UBERON:0001912) as a design template, reviewed and explicitly excluded overlapping terms (UBERON:0035149 gingival epithelial attachment, UBERON:0001949 gingival epithelium, UBERON:0001758 periodontium), and surfaced the unresolved taxon-constraint question (raised by nicolevasilevsky in the issue) instead of guessing — correctly declining to add `in_taxon NCBITaxon:9606`, matching gold.
- **Valid OBO syntax** throughout: `relationship: part_of`, modern `synonym: "..." EXACT []` form.

## Issues

- **Parent of the generic ducto-acinar unit** (`is_a UBERON:0009911 lobule`): this matches the issue's negotiated proposal exactly, but the gold PR's reviewer changed it to `is_a UBERON:0000063 organ subunit` + `relationship: part_of UBERON:0009911 lobule` (reviewer comment: "I believe that the lobule contains the ducto-acinar unit"). The agent could not have anticipated this post-discussion review decision; not a true defect.
- **Submandibular definition** retains "approximately 90% serous": again matches the proposal but the gold reviewer asked for it to be generalised to "predominantly". Reviewer-driven, not foreseeable.
- **Extra provenance metadata** (`dc-contributor`, `dcterms-date`, `created_by: dragon-ai-agent`): gold carries only `subset: added_by_HRA` and `property_value: term_tracker_item`. These extras are normalized/down-weighted by metadiff and are conventional agent provenance, not substantive errors (minor scope, defensible).
- **Placeholder ID range**: used `UBERON:1200004-1200008`; gold used `UBERON:8000010-8000014` and the agent config documents `99xxxxx` for new terms. This is a harmless placeholder-ID artifact (real IDs are minted at merge), but it does not follow the config's stated `99xxxxx` convention (Sonnet/Haiku did).
- **`robot convert` reserialization not run** (no `robot` in environment) — flagged honestly by the agent; cosmetic.
