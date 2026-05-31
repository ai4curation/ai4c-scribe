---
ontology: cell-ontology
issue_number: 3533
pr_number: 3571
eval_repo_pr: 593
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.009
precision: 0.004
recall: 0.926
jaccard: 0.004
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: odk_regenerated_file_domination
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt (gpt-5.4 / opencode) is the strongest of this five-PR batch: it added the four zonal articular chondrocyte terms `CL_9900000`–`CL_9900003` as `SubClassOf CL_1001607`, with definitions, PMID definition xrefs, a related synonym on the middle and deep terms, contributor ORCID and date, editing only `cl-edit.owl` — and it is the only attempt here that also reproduced gold's `RO_0002292` (expresses) marker axioms (`PR_000013208` on superficial, `PR_000005693` on deep and calcified). The reported F1 of 0.009 is an **ODK build-regenerated-file domination** artifact (gold PR #3571 bundles ~9000 lines of pipeline-regenerated `merged_import.owl` +920/-5186, `hra_subset.owl` +898/-20, `cellxgene_subset.tsv` +959/-959, and six version-date bumps onto a ~46-line genuine `cl-edit.owl` hand edit), so whole-file metadiff cannot represent the actual work. On substance this is the closest match to gold of any attempt — the term-block diff is near-identical to gold's `cl-edit.owl` block (definitions are gold-verbatim).

## Strengths

- Correctly resolved the issue's erroneous parent ID `CL:0002557` ("fibroblast of pulmonary artery") to `CL_1001607` (articular chondrocyte), documented the correction in the PR/issue comments — matching gold and the curator @RiveraAndrea83's explicit confirmation.
- Allocated `CL_9900000`–`CL_9900003` from the temporary range, exactly matching gold's IDs and labels, so the term block aligns line-for-line with gold's `cl-edit.owl` content.
- Reproduced gold's `RO_0002292` expresses axioms precisely: `PR_000013208` (PRG4/lubricin) on the superficial term, `PR_000005693` (collagen X) on the deep and calcified terms — the only attempt in this batch to include the marker modeling gold has.
- Definitions are gold-verbatim (the same flattened-morphology / lubricin, transitional-zone, radial-zone / collagen-X, calcified-matrix phrasing), with the same PMID definition xref set (23015907, 23124445, 41226342; 18455690 on calcified).
- Added `hasRelatedSynonym` "transitional zone articular chondrocyte" (middle) and "radial zone articular chondrocyte" (deep) with PMID:23015907 xrefs, matching gold's referenced-synonym style.
- Tightly scoped to `cl-edit.owl`; validated with `robot convert`; clean provenance.

## Issues

- No `term_tracker_item` / `IAO_0000233` issue back-link on the new terms (gold also omits this, so not a deviation from gold, but it is a minor provenance gap vs project convention).
- Slightly thinner synonym coverage than the issue offered: only middle and deep terms received a synonym; superficial ("superficial zone chondrocyte") and calcified ("calcified zone chondrocyte") alternative labels from the issue were not added. Gold also omitted superficial/calcified synonyms, so this is parity with gold rather than a regression.
- `terms:date "2026-05-17"` (run date) vs gold's `2026-02-18` — expected eval-harness artifact, not a fault.
