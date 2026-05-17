---
ontology: cell-ontology
issue_number: 3353
pr_number: 3354
eval_repo_pr: 43
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: placeholder_id_and_provenance_metadiff_artifact_plus_unstated_gold_side_edits
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Byte-identical replay of attempt pr62 (same model gpt-5.5 / opencode runtime, same output blob `ea297b4`). The agent created human-specific term `CL_9900000` under **both** `CL_4023036` and `CL_4072029` plus `RO_0002162 some NCBITaxon_9606`. The core term is substantively reasonable; the dual-parent choice is defensible but deviates from the accepted canonical gold `CL_4072046` (single parent `CL_4023036`) and the local CL pattern. F1=0.000 is a metadiff artifact (placeholder-vs-canonical CL ID, provenance fields, gold's unstated parent side-edits), with the extra `CL_4072029` parent being a real modeling deviation.

## Strengths

- Correctly inferred the task from the title alone with an empty issue body; documented a clear checklist and ran `robot convert` validation.
- New term modeled as a subclass of `CL_4023036` + `RO_0002162 some NCBITaxon_9606` — the core of the accepted gold structure.
- Followed agent config: `CL_99xxxxx` ID, definition with PMID:27477017 + PMID:37824655 + CellxGene xref, `IAO_0000028` symbol, exact synonym, `IAO_0000233` issue link, BDS + cellxgene subsets, `RO_0002175` present-in-taxon, Declaration added.
- Reproducible: identical to pr62.

## Issues

- **Wrong/extra pattern:** second parent `SubClassOf(CL_9900000 CL_4072029)` — not used by the accepted canonical gold `CL_4072046` (which asserts only `CL_4023036`); `CL_4072029` is itself an equivalence-defined class so the direct subclass assertion is redundant/non-idiomatic for this cluster.
- **Omissions vs gold (not agent fault given empty issue):** no `CLM_1000063` marker set, no ILX xref, no contributor ORCID; gold also relabeled/reparented `CL_4023036` and moved the NS-Forest marker comment — none stated in the issue.
- **Metadiff artifact (case quality, not agent fault):** F1=0 is structural (placeholder-vs-canonical CL ID, provenance fields, gold's out-of-scope parent edits).
