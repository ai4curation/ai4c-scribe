---
ontology: uberon
issue_number: 3657
pr_number: 3671
eval_repo_pr: 644
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.762
precision: 0.750
recall: 0.774
jaccard: 0.615
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "The merged gold PR #3671 reflects post-review refinements by RiveraAndrea83 (salivon: is_a organ subunit + part_of lobule instead of is_a lobule; dentogingival junction is_a anatomical junction instead of tissue; 'approximately 90%' generalised to 'predominantly'; def refs changed to PMID:30855909). The issue #3657 thread, however, converged on a different negotiated proposal (is_a lobule; dentogingival is_a tissue; 'predominantly serous'; NBK538325/ISBN refs) that this attempt faithfully reproduced. The 0.762 F1 substantially under-represents quality because it penalizes the agent for not anticipating reviewer-driven changes made after the issue discussion closed. A follow-up companion PR (#3673) added subset tags / logical definitions."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode added all five requested HRA/HuBMAP terms (salivary gland ducto-acinar unit + parotid/sublingual/submandibular children + dentogingival junction), reproducing the issue #3657 converged proposal almost verbatim — including the exact negotiated parents `is_a UBERON:0009911 lobule` and `is_a UBERON:0000479 tissue`, the `part_of` axioms, all synonyms, and the proposed definitions. The 0.762 F1 under-represents quality: the merged gold diverges only because reviewer RiveraAndrea83 made structural changes (organ subunit + part_of lobule; anatomical junction; "predominantly" wording; PMID:30855909) *after* the issue thread closed. Judged against the issue's actual negotiated target this is a strong, correct, well-scoped result.

## Strengths

- **Faithfully reproduced the negotiated proposal**: `salivary gland ducto-acinar unit` `is_a UBERON:0009911 lobule` + `part_of UBERON:0001044 saliva-secreting gland`; the three children `is_a` the generic term with `part_of UBERON:0001831` (parotid), `UBERON:0001832` (sublingual), `UBERON:0001736` (submandibular); `dentogingival junction` `is_a UBERON:0000479 tissue` + `part_of UBERON:0001828 gingiva`. Every parent/part_of matches the dragon-ai-agent ↔ zhengj2007 converged proposal exactly.
- **Definitions and synonyms verbatim from the proposal**: salivon EXACT, `salivary gland ducto-acinar` RELATED, the lobule/acini/striated-duct definition with the classical-physiology comment, and the dentogingival junction's three RELATED synonyms (`dentogingival complex`, `gingival attachment`, `supracrestal tissue attachment`) all match the negotiated text.
- **Correct subset**: used `subset: added_by_HRA`, matching gold exactly (the gpt-5.4 opencode runs added an extra non-canonical `human_reference_atlas` subset).
- **Correctly omitted the disputed taxon constraint**: did not add `in_taxon NCBITaxon:9606`, matching gold and respecting nicolevasilevsky's explicit final comment that the constraint was unresolved (the species may occur in other mammals). The gpt-5.4 codex/opencode attempts wrongly added it.
- **Sound submandibular wording**: used "predominantly serous acini with a minority of mucous acini" — closer to the gold reviewer's requested generalisation than the proposal's literal "approximately 90%", an independent improvement.
- **Strong, transparent methodology**: documented checking for existing `ducto-acinar`/`salivon`/`dentogingival` terms (none found), verifying all parents with `obo-grep.pl`, reviewing PMIDs, ROBOT convert + ELK reasoning, and honestly noting `aurelian` was unavailable.
- **Valid OBO syntax** throughout (`relationship: part_of`, modern `synonym: "..." EXACT []`); no `intersection_of` axioms added (matches gold's simpler relational modeling).

## Issues

- **Generic parent `is_a UBERON:0009911 lobule`**: matches the issue proposal exactly but the gold reviewer changed it to `is_a UBERON:0000063 organ subunit` + `part_of UBERON:0009911 lobule` ("the lobule contains the ducto-acinar unit"). Not foreseeable from the issue thread; not a true defect.
- **`dentogingival junction` `is_a UBERON:0000479 tissue`**: matches the proposal but gold's reviewer changed it to `is_a UBERON:0007651 anatomical junction`. Reviewer-driven, not foreseeable. (Opus's independent choice of `multi-tissue structure` was arguably closer to gold here; this attempt followed the literal proposal instead — defensible.)
- **Extra provenance metadata** (`dc-contributor`, `dcterms-date`, `created_by: dragon-ai-agent`): gold carries only `subset: added_by_HRA` and `property_value: term_tracker_item`. Conventional agent provenance, normalized/down-weighted by metadiff; minor scope, not substantive.
- **Placeholder ID range** `UBERON:9900001-9900005`: gold used `UBERON:8000010-8000014`. Harmless placeholder artifact (real IDs minted at merge); the `99xxxxx` form follows the config convention.
