---
ontology: cell-ontology
issue_number: 3353
pr_number: 3354
eval_repo_pr: 283
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

From a near-empty issue (title only), the agent created a clean, well-scoped human-specific term as `SubClassOf(CL_9900000 CL_4023036)` with `RO_0002162 some NCBITaxon_9606` — structurally identical to the accepted canonical gold term `CL_4072046`. F1=0.000 entirely misrepresents the result: it is forced to zero by the instructed placeholder ID (`CL_9900000` vs canonical `CL_4072046`), metadiff-blind `terms:date` provenance, and the gold PR's unstated parent generalization/reparenting side-edits. This attempt is notable for *not* over-editing the parent (unlike the codex/gpt-5.4 attempt), so it is the most scope-disciplined of the seven; its only substantive gap vs gold is the omission of the marker set / taxon present-in assertion that the empty issue never asked for.

## Strengths

- Correctly inferred the task from the title alone and produced a syntactically valid, minimal, well-formed new term.
- Modeling matches the accepted gold `CL_4072046`: subclass of `CL_4023036` + `RO_0002162 some NCBITaxon_9606`.
- Strong scope discipline — did **not** touch the parent `CL_4023036` definition/label/parentage, avoiding the precision-lowering over-edit seen in attempt pr80.
- Followed agent config: mandated `CL_99xxxxx` ID, definition with PMID:27477017 + CellxGene xref, `IAO_0000028` symbol, exact synonym, `IAO_0000233` issue link, BDS + cellxgene subsets, `RO_0002175` present-in-taxon, and added the Declaration.

## Issues

- **Omissions vs gold (not agent fault given empty issue):** no `CLM_1000063` NS-Forest marker set `RO_0015004` axiom, no ILX:0107356 xref, no contributor ORCID. The gold also generalized/relabeled/reparented the parent (`CL_4023036`: drop "cortical" from label, CL_4023018→CL_4023069, +`RO_0002202 some UBERON_0004024`) and moved the NS-Forest marker comment to the new term. None of this was stated in the issue; it required mining the source term's embedded marker comment.
- **Metadiff artifact (case quality, not agent fault):** F1=0 is structural — placeholder-vs-canonical CL ID for a new_term, plus `terms:date` provenance metadiff ignores/mismatches, plus the gold's out-of-scope parent edits. The score gives zero credit for a correct core term.
- Identical diff to attempt pr225 (same model/runtime, blob `48f9fd2`) — a stable, reproducible output.
