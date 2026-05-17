---
ontology: cell-ontology
issue_number: 3353
pr_number: 3354
eval_repo_pr: 225
agent: std_claude_sonnet45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: placeholder_id_and_provenance_metadiff_artifact_plus_unstated_gold_side_edits
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is a byte-identical replay of attempt pr283 (same model claude-sonnet-4.5 / claude runtime, same output blob `48f9fd2`). The agent created a well-scoped human-specific term `SubClassOf(CL_9900000 CL_4023036)` with `RO_0002162 some NCBITaxon_9606`, structurally matching the accepted canonical gold `CL_4072046`. F1=0.000 entirely misrepresents quality: it is forced to zero by the instructed placeholder ID vs the gold's canonical `CL_4072046`, metadiff-blind `terms:date` provenance, and the gold PR's unstated parent generalization side-edits.

## Strengths

- Correctly inferred the task from the title alone with an empty issue body.
- Modeling matches the accepted gold `CL_4072046`: subclass of `CL_4023036` + `RO_0002162 some NCBITaxon_9606`.
- Excellent scope discipline — did not over-edit the parent `CL_4023036` (contrast attempt pr80).
- Followed agent config: `CL_99xxxxx` ID, definition with PMID:27477017 + CellxGene xref, `IAO_0000028` symbol, exact synonym, `IAO_0000233` issue link, BDS + cellxgene subsets, `RO_0002175` present-in-taxon, Declaration added.
- Reproducible: identical to pr283, indicating stable behavior for this case.

## Issues

- **Omissions vs gold (not agent fault given empty issue):** no `CLM_1000063` marker set `RO_0015004` axiom, no ILX:0107356 xref, no contributor ORCID; gold also relabeled/reparented `CL_4023036` (drop "cortical", CL_4023018→CL_4023069, +`develops from UBERON_0004024`) and moved the NS-Forest marker comment to the new term — none stated in the issue.
- **Metadiff artifact (case quality, not agent fault):** F1=0 is structural (placeholder-vs-canonical CL ID, provenance fields, gold's out-of-scope parent edits); zero credit for a substantively correct new term.
