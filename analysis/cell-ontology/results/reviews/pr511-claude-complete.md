---
ontology: cell-ontology
issue_number: 3259
pr_number: 3450
eval_repo_pr: 511
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: success
failure_modes:
  - under_editing
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact_plus_gold_out_of_scope_serialization_edit
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced a substantively **correct** `transitional principal-intercalated cell of kidney collecting duct` term — accurate PMID-xref'd definition, both requested synonyms with correct types, both contributor ORCIDs, the correct parent `CL_1000454`, and a structured issue-tracker link. This attempt is **byte-identical to #573** (same opencode/gpt-5.4 blob `00f884a27`, same `CL_9900000`) and should be counted once with it. The reported F1 of **0.000 is overwhelmingly a placeholder-vs-canonical CL ID artifact**: the agent used `CL_9900000` from the config-mandated `CL_99xxxxx` temp range while the blinded gold PR landed on `CL_9900001`, so the entire diff differs only by the subject IRI and metadiff matches zero lines. Graded **success** under the established `case_quality: poor` flag; the one genuine (metadiff-independent) shortfall is the omission of the requested `part_of UBERON_0001232` location axiom.

## Strengths

- **Correct parentage**: `SubClassOf(obo:CL_9900000 obo:CL_1000454)` — exactly the requested parent (kidney collecting duct epithelial cell); a sound conservative placement for a transitional/hybrid cell rather than committing it to the principal- or intercalated-cell lineage.
- **Both synonyms correct**: `tPC-IC cell` related synonym with abbreviation type (`OMO_0003000`, PMID:37468583) and `hybrid principal-intercalated cell` broad synonym (PMID:33893305) — matches the issue's requested synonym/type/reference triples.
- **Both contributor ORCIDs** present via `terms:contributor` (`0000-0002-2999-0103`, `0009-0000-8480-9277`).
- **Definition accurate and PMID-xref'd** (PMID:33893305, PMID:37468583): co-expression of principal- and intercalated-cell markers, CKD enrichment — same content as the issue/gold text, defensibly paraphrased.
- **Issue link** recorded as a proper `IAO_0000233` term-tracker annotation; clean single-term scope with no gratuitous edits and no reproduction of gold's out-of-scope `hasDbXref` comment-text serialization artifact.

## Issues

- **Omission of the requested anatomical-location axiom (genuine, metadiff-independent)**: the issue explicitly requests location in `UBERON_0001232` (collecting duct of renal tubule); gold encodes `SubClassOf(... ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))`. This attempt omits the `part_of UBERON_0001232` axiom, a real under-editing gap versus the issue's stated requirements and independent of the ID artifact (distinguishes it from #272/#200, which included the location axiom).
- **Placeholder ID differs from gold (artifact, not error)**: `CL_9900000` vs gold's `CL_9900001`. Both are valid temp-range placeholders; a blinded agent cannot predict the gold ID. This single difference zeroes the metadiff. Established poor-case flag applies.
- **Duplicate run**: identical blob to eval-PR #573 (same workflow output); should be de-duplicated in aggregation.
- **Definition paraphrased rather than verbatim** from the issue; faithful in content, minor style difference from gold, metadiff-irrelevant given the ID artifact.
- **`IAO_0000233` as a plain string literal** rather than an IRI literal, and an extra harmless `terms:date` provenance assertion not in gold; both minor and defensible.
