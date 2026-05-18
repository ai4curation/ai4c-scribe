---
ontology: cell-ontology
issue_number: 3584
pr_number: 3585
eval_repo_pr: 471
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.249
precision: 0.250
recall: 0.248
jaccard: 0.142
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_renegotiated_plus_placeholder_vs_canonical_cl_id_artifact
companion_prs: []
scoring_caveat: "Byte-identical diff to pr480 (blob cc28a172); difference is runtime only (opencode here, codex for pr480). F1=0.249 is heavily depressed by the placeholder-vs-canonical CL ID artifact (CL_9900000–CL_9900013 off-by-one vs gold's CL_9900001–CL_9900014, both valid in idrange:81), but the attempt also has real substantive deviations (dropped CL_0008015/CL_0000099 parents, SN1/SN2 synonym swap, soma-location collapsed into chemical-grouping subsumption). Judge against the issue spec."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This gpt-5.4/opencode run produces a diff byte-identical to pr480 (blob cc28a172) — the same gpt-5.4 solution under a different runtime. All 14 myenteric-neuron classes from issue #3584 are present with accurate definitions, PMID xrefs, and provenance, on the off-by-one CL_9900000–CL_9900013 scheme, so whole-file metadiff collapses to F1=0.249 (largely the placeholder-vs-canonical artifact, plus real substantive deviations). Outcome `partial_success`: core task done with sound satisfiability reasoning, but several issue-specified axioms were intentionally dropped and SN1/SN2 synonyms swapped.

## Strengths

- **All 14 terms present** with labels, definitions, synonyms, `IAO_0000233` → #3584, `terms:creator`, `terms:date` — provenance satisfied.
- **Reasoning-driven scope discipline:** correctly identified that `CL_0000099` (interneuron) as parent of the myenteric interneuron branch is unsatisfiable under ELK and relaxed that parentage while keeping label/definition — the same defensible judgment gold curators applied to the analogous `CL_0008015` case.
- Both defined grouping classes (cholinergic CL_9900012, nitrergic CL_9900013) correctly encoded as `EquivalentClasses(ObjectIntersectionOf(...))` with the `RO_0002215 some GO_0014055`/`GO_0006809` differentia per Terms 12/13.
- Generic Dogiel type II neuron (CL_9900000) correctly under `CL_0000540`, sibling of CL_4047038, with **no UBERON axiom** per Term 14 ("UBERON Terms: None") — correctly avoiding the out-of-scope `BFO_0000050 some UBERON_0002005` gold added.

## Issues

- **Substantive: SN1/SN2 synonym swap.** Calretinin-**positive** IPAN (CL_9900010) gets `SN2` and calretinin-**negative** (CL_9900011) gets `SN1` — inverse of the issue spec (Term 10 SN1 / Term 11 SN2) and gold. Same source-grounded but contested deviation as pr480; needs curator adjudication, flagged honestly.
- **Omission: requested parents dropped.** Spiny Dogiel I drops the issue-requested `CL_0008015` parent; the interneuron branch drops the requested `CL_0000099`. Defensible for satisfiability but issue requirements (Terms 2, 8) not met as written.
- **Restructured location modelling:** several terms use `SubClassOf` chemical grouping classes (e.g. IPAN CL_9900001 `SubClassOf CL_9900012`) instead of the issue's per-term `RO_0002100 some UBERON_0002439` soma-location axiom, losing the explicit soma-location assertion on some leaves.
- **ID artifact (not an error):** CL_9900000–CL_9900013 off-by-one vs gold; valid within idrange:81 and responsible for a large share of the F1 collapse independent of the substantive issues.
- Label casing "dogiel type II neuron" lowercase vs gold's proper-noun form; cosmetic, metadiff-visible.
- No PR/issue comment captured for this opencode run (pr480's codex run documented the same methodology); the reasoning is inferable from the identical diff.
