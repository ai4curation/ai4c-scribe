---
ontology: cell-ontology
issue_number: 3408
pr_number: 3522
eval_repo_pr: 184
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: other
difficulty: hard
f1: 0.631
precision: 0.610
recall: 0.653
jaccard: 0.461
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_dominated_by_odk_serialization_artifact_and_unrequested_style
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly and completely implemented every explicit instruction in issue #3408: relabelled all five type 1–5 otic fibrocyte terms (CL_0002666–CL_0002670) to "type I–V spiral ligament fibrocyte", added the old labels as broad synonyms, updated definitions with the issue-supplied text (adding rather than replacing PMIDs), added `part of some spiral ligament` (UBERON_0006725), added `adjacent to some stria vascularis of cochlear duct` (UBERON_0002282) for type I, and added the `tension fibroblast` exact synonym for type III. The metadiff F1 of 0.631 (highest of the 6 attempts) **substantially under-represents** the quality: ~45% of the gold PR's 51 added lines are an ODK/ROBOT-regenerated annotation-property-label-declaration block plus UBERON `Declaration` housekeeping (serialization artifacts no agent should reproduce), plus gold-only stylistic synonyms ("type N SLF" OMO_0003000 related synonyms, Arabic "type N spiral ligament fibrocyte" exact synonyms) and a reasoner-equivalence refactor of CL_0020005 — none of which the issue requested.

## Strengths

- Hit every explicit ask in the issue, including the per-type PMID sets (e.g. type I: PMID:18581144 + PMID:33193034; type III: PMID:22043022 + PMID:22476723 + PMID:33193034) added to, not replacing, the existing `GOC:tfm`/`PMID:18353863` xrefs — exactly as the issue's bolded "DO NOT replace references" instruction demanded.
- Correctly added `adjacent to (RO_0002220) some UBERON_0002282` for type I only, matching the gold exactly (the issue requested this for type I alone).
- Explicit, well-reasoned design rationale: chose `hasBroadSynonym` for the old "otic fibrocyte" names with a correct ontological justification (CL_0002665 otic fibrocyte is the broader genus), and reparented to CL_0020005 (spiral ligament fibrocyte) — a defensible asserted-hierarchy alternative to the gold's `EquivalentClasses` reasoner-driven approach. Both produce the same inferred classification.
- Added `term_tracker_item` (IAO_0000233) provenance to each term; correctly preserved `terms:contributor` and `creation_date`.
- Validated with `robot convert` and `robot reason --reasoner ELK` (no unsatisfiable classes), and surfaced the MP-xref-drop judgement call transparently for curator review.

## Issues

- Dropped the MP cross-references (MP:0004487–MP:0004490) that were previously attached to the "type N spiral ligament fibrocyte" exact synonyms. The gold also dropped these, so this is not a divergence from gold, but it is a minor information loss; the agent flagged it explicitly and offered to re-attach — good practice.
- Style divergence (not an error): the gold keeps `SubClassOf CL_0002665` and instead converts CL_0020005 to a defined class via `EquivalentClasses`, whereas this agent asserted `SubClassOf CL_0020005` directly. The agent's approach is the more conventional/conservative choice and is ontologically equivalent after reasoning; this divergence is a large part of the metadiff penalty but is not a quality defect.
- The gold added "type N SLF" OMO_0003000 related synonyms and Arabic "type N spiral ligament fibrocyte" exact synonyms; the agent did not. These were never requested in the issue, so the omission is reasonable scope discipline, not a real miss — but it depresses recall.
