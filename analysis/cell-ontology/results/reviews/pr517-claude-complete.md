---
ontology: cell-ontology
issue_number: 3408
pr_number: 3522
eval_repo_pr: 517
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: other
difficulty: hard
f1: 0.357
precision: 0.299
recall: 0.442
jaccard: 0.217
outcome: partial_success
failure_modes: [over_editing, scope_creep]
case_quality: poor
case_quality_reason: gold_dominated_by_odk_serialization_artifact_and_unrequested_style
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This attempt produces a diff **byte-identical** to #580 (same blob `2b77ae5`, same F1=0.357 / P=0.299 / R=0.442) — a replicate run of the same gpt-5.4/opencode configuration. The agent correctly implemented the core of issue #3408 across all five terms (CL_0002666–CL_0002670): relabel to "type I–V spiral ligament fibrocyte", definitions rewritten with the issue-supplied text, per-type PMIDs **added** (not replaced) to the existing `GOC:tfm`/`PMID:18353863` xrefs, reparenting to CL_0020005, `part of some spiral ligament` (UBERON_0006725) on all five, type-I `adjacent to some stria vascularis` (UBERON_0002282), and the `tension fibroblast` exact synonym for type III. As in #580 it **over-edited the logical axioms** with three unrequested `adjacent to` axioms, one of them (type V → stria vascularis) anatomically dubious. F1=0.357 is the lowest of the nine attempts; the gold-padding caveat under-represents the correct portions, but the low score also reflects genuine scope creep plus retained old exact synonyms and extra provenance lines.

## Strengths

- Relabelling correct for all five terms; old Arabic labels added as `hasBroadSynonym` (per the issue), though with an extra unrequested PMID:33193034 xref on the broad synonym.
- Definitions rewritten with the issue text; new PMIDs appended to (not replacing) the existing `GOC:tfm`/`PMID:18353863` definition xrefs, honoring the issue's bolded "DO NOT replace references" instruction.
- `part of some UBERON_0006725` (spiral ligament, verified) added to all five and reparented to CL_0020005 — correct anatomy, unlike the UBERON_0001863 wrong-target defect in #211.
- `adjacent to (RO_0002220) UBERON_0002282` (stria vascularis of cochlear duct) correctly added for type I (CL_0002670).
- `tension fibroblast` exact synonym (xref PMID:33193034) added to type III (CL_0002669), as requested.
- Added `IAO_0000233` issue-provenance links to all five terms. (No PR/issue narrative captured for this run; assessment is from the diff, which is identical to #580.)

## Issues

- **Scope creep / over-editing (genuine defect):** added three `adjacent to (RO_0002220)` axioms the issue never asked for — CL_0002666 (type II) → UBERON_0028194 (spiral prominence of cochlear duct), CL_0002669 (type III) → UBERON_0004637 (otic capsule), and CL_0002667 (type V) → UBERON_0002282 (stria vascularis of cochlear duct). The issue requests an `adjacent to` axiom for **type I only**. The type V → stria vascularis assertion is questionable: the type V definition places it *suprastrial / above* the stria, not adjacent. These unrequested axioms reduce precision and risk imprecise anatomy.
- Did not demote the pre-existing Roman-numeral exact synonyms ("type II otic fibrocyte", etc.) — left them as `hasExactSynonym` rather than converting to broad synonyms, inconsistent with the relabel intent (gold demotes these).
- Style divergence (not an error) plus the gold's serialization artifacts (annotation-property label block, UBERON declarations, "type N SLF" OMO synonyms, Arabic exact synonyms, `EquivalentClasses` refactor) account for the remainder of the large metadiff gap and are not quality defects in this attempt.
