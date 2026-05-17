---
ontology: cell-ontology
issue_number: 3408
pr_number: 3522
eval_repo_pr: 51
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: other
difficulty: hard
f1: 0.614
precision: 0.558
recall: 0.683
jaccard: 0.443
outcome: success
failure_modes: [scope_creep]
case_quality: poor
case_quality_reason: gold_dominated_by_odk_serialization_artifact_and_unrequested_style
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is the same gpt-5.5/opencode configuration as eval PR #69 and produces a byte-identical diff (blob `a493391`, identical F1/P/R). The agent fully implemented every explicit instruction in issue #3408 for all five terms (CL_0002666–CL_0002670): relabel to "type I–V spiral ligament fibrocyte", old labels as broad synonyms, updated definitions with added (not replaced) PMID xrefs, `part of some spiral ligament` (UBERON_0006725), `adjacent to some stria vascularis of cochlear duct` (UBERON_0002282) for type I, `tension fibroblast` exact synonym for type III, and `term_tracker_item` provenance. F1=0.614 **under-represents** quality because the gold PR is dominated by an ODK/ROBOT-regenerated annotation-property-label block and UBERON `Declaration` housekeeping (serialization artifacts), gold-only stylistic synonyms, and a CL_0020005 reasoner-equivalence refactor never requested by the issue. The one genuine over-edit is the unrequested `adjacent to bony otic capsule` axiom on type III.

## Strengths

- All issue-mandated edits present and correct, including the per-type PMID additions (not replacements) exactly per the issue's bolded instruction.
- Resolved `stria vascularis of cochlear duct` to UBERON_0002282 via OLS rather than guessing; type-I-only `adjacent to` axiom matches gold.
- Reparented all five to CL_0020005 with explicit `part of spiral ligament` — a defensible asserted-hierarchy alternative to gold's `EquivalentClasses` refactor; equivalent after reasoning.
- Explicit validation log: `robot convert`, `robot reason -r ELK`, `git diff --check`; transparently noted `aurelian` was unavailable.

## Issues

- **Scope creep**: added `SubClassOf(CL_0002669 'adjacent to' some UBERON_0005411)` (bony otic capsule) for type III — not requested by the issue and not in gold. Defensible (definition mentions lining the bony otic capsule) but an unrequested logical axiom that lowers precision.
- Dropped MP:0004487–MP:0004490 xrefs (same as gold; minor, not a divergence).
- Style divergence (not an error): asserted `SubClassOf CL_0020005` vs. gold's `EquivalentClasses` defined class, and omitted gold's unrequested "type N SLF" OMO related synonyms / Arabic exact synonyms. Drives much of the metadiff gap but not a quality defect.
- Duplicate run of the same configuration as #69 (identical output); no independent signal.
