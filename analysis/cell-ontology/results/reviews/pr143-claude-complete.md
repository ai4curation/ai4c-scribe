---
ontology: cell-ontology
issue_number: 3584
pr_number: 3585
eval_repo_pr: 143
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.711
precision: 0.667
recall: 0.762
jaccard: 0.552
outcome: success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_renegotiated_and_id_artifact
companion_prs: []
scoring_caveat: "Gold #3585 reflects review-negotiated changes (removed unsatisfiable SubClassOf(CL_9900009 CL_0008015), added SubClassOf(CL_9900001 CL_0007011)) plus an out-of-scope edit to pre-existing CL_4033160 and an unrequested BFO_0000050 some UBERON_0002005 on the generic Dogiel type II class — none of which the issue specified and none an agent could predict from the issue alone. F1=0.711 modestly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent created all 14 requested myenteric-neuron terms (CL_9900001–CL_9900014) with definitions, parentage, soma-location axioms, synonyms, and the two defined grouping classes essentially as specified in issue #3584. It used the same ID-to-term mapping as the gold PR (generic "Dogiel type II neuron" = CL_9900001), which is the main reason it scored highest of the three attempts (F1=0.711). The metadiff modestly **under-represents** quality: most of the residual gap comes from (a) a real omission — the agent dropped the `term_tracker_item` (IAO_0000233) annotation that the issue and agent config both require — and (b) gold-side artifacts an agent could not anticipate (review-negotiated axiom removal, an out-of-scope edit to pre-existing CL_4033160, an unrequested `BFO_0000050 some UBERON_0002005` on the generic Dogiel II class, and synonym-type/abbreviation conventions).

## Strengths

- All 14 terms present with the **same ID assignment as gold** (Dogiel type II neuron = CL_9900001 … nitrergic neuron of myenteric plexus = CL_9900014), correctly placing the prerequisite generic class first.
- Definitions are byte-faithful to the issue's supplied text for every term, with the prescribed PMID xrefs (34170401, 37355216, 40954253, 32888429, 38292899) attached to `IAO_0000115`.
- Parentage matches the issue spec: IPAN of myenteric plexus (CL_9900002) under `CL_0007011` + `CL_0000101`; interneuron (CL_9900003) under `CL_0007011` + `CL_0000099`; stubby Dogiel I (CL_9900008) under `CL_4047038` + `CL_0007011` + `CL_0000100`; ascending/descending interneurons under CL_9900003; calretinin ± IPANs under CL_9900002; Dogiel II of myenteric plexus (CL_9900010) under CL_9900001 + CL_9900002.
- Both defined grouping classes encoded correctly with `EquivalentClasses(... ObjectIntersectionOf(CL_0007011, RO_0002100 some UBERON_0002439, RO_0002215 some GO_0014055 / GO_0006809))`, plus the asserted parent (CL_0000108 cholinergic / CL_0000528 nitrergic) — matching the gold's logical-definition approach.
- `has soma location` (RO_0002100 some UBERON_0002439) applied to every location-specific term; the generic Dogiel II class (CL_9900001) correctly left location-agnostic.

## Issues

- **Omission (real, instruction violation):** No `IAO_0000233` (term_tracker_item) annotation on any term. The agent config explicitly says to "Link back to the issue you are dealing with using the `term_tracker_item`," and the gold links every term to issue #3471. This is a genuine miss and the largest correctable contributor to the F1 gap.
- **Style (metadiff-penalized, defensible):** All synonyms were emitted as `oboInOwl:hasRelatedSynonym` with no `oboInOwl:hasSynonymType obo:OMO_0003000` abbreviation tags. Gold and the issue treat IPAN/PSVN/VFN/SN1/SN2 as abbreviation-typed and several descriptive forms as `hasExactSynonym`. Valid but divergent from the house convention; depresses recall.
- **Scope/ontology (not the agent's fault, gold artifact):** Gold removed `SubClassOf(CL_9900009 CL_0008015)` during review because it forced the spiny Dogiel I term to `SubClassOf owl:Nothing`. This attempt retains `SubClassOf(CL_9900009 obo:CL_0008015)` (inhibitory motor neuron) for its spiny term — which is exactly what the issue's Term 8 asks for, so it is faithful to the issue, but it reproduces the same latent unsatisfiability the curators later fixed. Worth noting as a substantive ontology risk rather than a scoring artifact.
- **Minor:** `terms:date` stamped 2026-05-12 vs gold's 2026-03-10; provenance-only, metadiff-normalized, immaterial.
- The gold's out-of-scope edit to pre-existing `CL_4033160` and the unrequested `BFO_0000050 some UBERON_0002005` on the generic Dogiel II class are gold-side over-edits the agent correctly did not make; they cap achievable F1 and are not agent faults.
