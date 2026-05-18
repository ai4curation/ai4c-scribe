---
ontology: cell-ontology
issue_number: 3584
pr_number: 3585
eval_repo_pr: 480
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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
scoring_caveat: "F1=0.249 is heavily depressed by the placeholder-vs-canonical CL ID artifact: the attempt numbers terms CL_9900000–CL_9900013 (prerequisite Dogiel II = CL_9900000) vs gold's CL_9900001–CL_9900014, so every axiom line is offset by one and fails whole-file metadiff despite substantive equivalence for most terms. Both schemes are valid within idrange:81. However, unlike pr195/pr214 this attempt also has genuine substantive deviations (deliberately dropped CL_0008015 and CL_0000099 parents, SN1/SN2 synonym swap, soma-location collapsed into chemical grouping subsumption), so the low score is part artifact, part real partial-completion. Judge against the issue spec."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created all 14 myenteric-neuron classes from issue #3584 with accurate definitions, PMID xrefs, and provenance, but on the off-by-one CL_9900000–CL_9900013 ID scheme (prerequisite generic Dogiel II = CL_9900000), so the whole-file metadiff collapses to F1=0.249 — largely the placeholder-vs-canonical artifact, but here also reflecting real substantive deviations (dropped requested parents, a deliberate SN1/SN2 synonym swap, and restructured location modelling). Outcome `partial_success`: the core 14-term task is done and the satisfiability reasoning is sound, but several issue-specified axioms were intentionally not asserted. Diff is byte-identical to pr471 (blob cc28a172); the only difference is runtime (codex here, opencode for pr471).

## Strengths

- **All 14 terms present** with labels, definitions, synonyms, `IAO_0000233` → #3584, `terms:creator`, and `terms:date` on every class — provenance instruction satisfied.
- **Genuine reasoning-driven scope discipline, documented in the PR comment:** the agent ran `robot reason --reasoner ELK` and discovered that asserting `CL_0000099` (interneuron) as parent of the myenteric interneuron branch makes it unsatisfiable; it correctly kept the label/definition but relaxed the formal parentage. This is a defensible, well-explained ontological judgment that mirrors what gold curators independently did for the analogous `CL_0008015` case.
- Both defined grouping classes (cholinergic CL_9900012, nitrergic CL_9900013) encoded with correct `EquivalentClasses(ObjectIntersectionOf(...))` and the `RO_0002215 some GO_0014055`/`GO_0006809` differentia per Terms 12/13.
- Generic Dogiel type II neuron (CL_9900000) correctly placed under `CL_0000540` as a sibling of CL_4047038, per Term 14, and correctly given no UBERON axiom (Term 14 says "UBERON Terms: None") — the agent correctly avoided the unrequested `BFO_0000050 some UBERON_0002005` that gold added out-of-scope.
- The agent verified literature: it noted PMID:40954253 did not resolve in its environment and conservatively omitted that xref rather than fabricating it — honest methodology.

## Issues

- **Substantive: SN1/SN2 synonym swap.** The agent assigned `SN2` to calretinin-**positive** IPAN (CL_9900010) and `SN1` to calretinin-**negative** (CL_9900011) — the inverse of both the issue spec (Term 10 = calretinin-positive = SN1; Term 11 = calretinin-negative = SN2) and gold. The agent explicitly justifies this from PMID:37355216 in both the PR and issue comments ("PMID:37355216 supports SN1 as the calretinin-negative ... class"). This is a contested, source-grounded judgment, not a careless error, but it diverges from the agreed issue spec and gold and would need curator adjudication; flagged honestly as a deviation rather than a clean success.
- **Omission: requested parents dropped.** Beyond the satisfiability-motivated `CL_0000099` relaxation, the spiny Dogiel I class also drops the issue-requested `CL_0008015` parent (placed under `CL_9900013` nitrergic grouping instead). Defensible for satisfiability, but it is an issue requirement not met (Term 8 explicitly asks for CL:0008015).
- **Restructured location modelling:** rather than asserting `RO_0002100 some UBERON_0002439` soma-location uniformly as the issue specifies and gold does, several terms are instead made `SubClassOf` the chemical grouping classes (e.g. CL_9900001 IPAN `SubClassOf CL_9900012` cholinergic grouping). This loses the explicit soma-location axiom on some leaf terms and is a different (less faithful) modelling than the issue's per-term UBERON soma-location instruction.
- **ID artifact (not an error):** CL_9900000–CL_9900013 vs gold's CL_9900001–CL_9900014. Valid within idrange:81; responsible for a large share of the F1 collapse independent of the substantive issues above.
- Label casing "dogiel type II neuron" lowercase vs gold's proper-noun form; metadiff-visible cosmetic.
