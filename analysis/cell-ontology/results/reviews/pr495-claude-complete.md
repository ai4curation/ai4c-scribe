---
ontology: cell-ontology
issue_number: 3584
pr_number: 3585
eval_repo_pr: 495
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.639
precision: 0.639
recall: 0.639
jaccard: 0.469
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_plus_placeholder_vs_canonical_cl_id_artifact
companion_prs: []
scoring_caveat: "This attempt uses the canonical CL_9900001–CL_9900014 numbering that matches gold's ID assignment, so it scores higher (F1=0.639) than the ontologically-equivalent off-by-one attempts (pr195/pr214 ~0.26). Remaining F1 gap is driven by metadiff-blind divergences that are not quality defects: term_tracker_item points to issue #3584 vs gold's #3471, terms:date differs, and gold carries review-only/out-of-scope edits (removed CL_0008015 axiom, added CL_0007011 on CL_9900001, edited pre-existing CL_4033160, added BFO_0000050 some UBERON_0002005 on the generic Dogiel II class) that no well-scoped attempt can predict from issue #3584. Judge against the issue spec, not the line-level metadiff vs #3585."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced a complete, well-scoped implementation of all 14 myenteric-neuron terms from issue #3584, using the canonical CL_9900001–CL_9900014 ID scheme that aligns with gold's numbering (prerequisite generic "Dogiel type II neuron" = CL_9900001, matching gold). Its F1 of 0.639 is the highest of the gpt-5.x set and substantively under-represents quality: the residual gap is almost entirely metadiff-blind provenance differences (term_tracker_item → #3584 vs gold's #3471, differing `terms:date`) plus gold's own review-only and out-of-scope edits that the issue never specified. Outcome graded `success` on substance (case is `poor`, see METADATA).

## Strengths

- **All 14 terms present, correctly labelled, and ID-aligned to gold**: CL_9900001 (Dogiel type II neuron) through CL_9900014 (nitrergic neuron of myenteric plexus), one-to-one with the gold numbering — this is why it avoids the off-by-one collapse that hit pr195/pr214.
- Definitions faithfully reproduce the issue text with the prescribed PMID xrefs on `IAO_0000115` (e.g. CL_9900001 carries PMID:34170401; CL_9900002 carries the PMID:34170401/37355216/40954253 triple exactly as specified for Term 1).
- Parentage matches the issue spec: generic Dogiel II under `CL_0000540` (Term 14, sibling of CL_4047038); stubby Dogiel I (CL_9900008) under `CL_0000100` + `CL_0007011` + `CL_4047038` (Term 7); spiny Dogiel I (CL_9900009) retains the requested `CL_0008015` inhibitory-motor-neuron parent (Term 8); Dogiel II of myenteric plexus (CL_9900010) under generic Dogiel II + IPAN (Term 9).
- Both defined grouping classes encoded correctly: `EquivalentClasses(CL_9900013 ObjectIntersectionOf(CL_0007011, RO_0002100 some UBERON_0002439, RO_0002215 some GO_0014055))` for cholinergic, and the GO_0006809 analogue for nitrergic CL_9900014 — exactly the genus-differentia the issue requested.
- Soma-location modelled with `RO_0002100 some UBERON_0002439` consistently; added the intestinofugal axon-target restriction (`RO_0013007` over the union of celiac/superior/inferior mesenteric ganglia UBERON_0002262/0005479/0005480), going beyond gold (which described axon targets in text only) but faithfully encoding the issue's explicit Term 4 UBERON axon-target list.
- `IAO_0000233` term_tracker_item added on every term, satisfying the agent-config provenance instruction (which the top-scoring pr143 missed).

## Issues

- **Provenance divergence (metadiff-penalized, not a defect):** term_tracker_item points to `issues/3584` whereas gold points to `issues/3471` (the broader linked HuBMAP request). The issue body opens "Links #3471"; both targets are defensible. `terms:date` is the run date rather than gold's 2026-03-10. These flatten F1 with no ontological consequence.
- **Synonym scope differs from gold:** the agent demotes several abbreviation synonyms to `hasRelatedSynonym` without the `OMO_0003000` (abbreviation) synonym-type tag that gold and pr195 apply (e.g. "AH neuron", "IPAN" handled as plain related synonyms; "Dogiel II neuron" as exact). Valid, but a house-convention miss that the metadiff penalizes.
- **Ontology risk faithfully inherited from the issue:** spiny Dogiel I (CL_9900009) keeps `SubClassOf CL_0008015`, exactly as Term 8 requests. In gold review, curators removed the analogous axiom because it forced the class to `SubClassOf owl:Nothing` under the taxon-constraint bot. Reproducing the issue here reproduces the latent unsatisfiability — a real caveat, but not an agent fault given the issue text.
- **Label casing:** "dogiel type II neuron" (lowercase d) vs gold's "Dogiel type II neuron". Cosmetic, but inconsistent with the proper-noun convention and metadiff-visible.
- Gold's out-of-scope edit to pre-existing `CL_4033160` and its unrequested `BFO_0000050 some UBERON_0002005` on the generic Dogiel II class are gold-side over-edits the agent correctly avoided; they depress apparent recall through no fault of the agent.
