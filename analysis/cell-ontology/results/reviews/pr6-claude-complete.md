---
ontology: cell-ontology
issue_number: 3519
pr_number: 3520
eval_repo_pr: 6
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v2
case_type: new_term
difficulty: simple
f1: 0.267
precision: 0.333
recall: 0.222
jaccard: 0.154
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent created `CL_9900000` (label `oRGC2`) with the correct definition and both PMID xrefs, and — like the two top attempts — used the **canonical ID `CL_9900000`** matching the merged gold. However it deviated from the explicit NTR instruction in two ways: it changed the requested parent from `CL_0000740` (retinal ganglion cell) to `CL_4023032` (ON retinal ganglion cell), and it rewrote the definition rather than using the verbatim submitted text. The low F1 (0.267) over-states the failure somewhat (the term is real and reasonable), but the parent substitution is a genuine instruction violation, so this is a partial success at best.

## Strengths

- **Correct canonical ID `CL_9900000`,** matching the merged gold.
- Both required references present (`PMID:37066415`, `PMID:31784286`) on the definition.
- Reasonable biological judgement: choosing `ON retinal ganglion cell` (`CL_4023032`) as parent is defensible — the orthotype groups ON parasol / ON-transient α types, and `CL_4023032` is a more specific true superclass. The agent documented this reasoning explicitly.
- Did syntax validation (`robot convert`) and noted the journal version PMID (PMID:38092908) for the Hahn preprint — good diligence.
- Correctly avoided forcing the term under a single species-specific parent.

## Issues

- **Instruction violation / wrong pattern:** the NTR explicitly specified parent `CL_0000740`. The agent overrode this with `CL_4023032`. Biologically defensible, but the issue gave an unambiguous parent and the curator accepted `CL_0000740`; an NTR agent should follow the stated parent or surface the alternative as an open question rather than silently substituting it.
- **Definition rewritten:** the gold (and the NTR) uses the submitter's verbatim text. The agent paraphrased it ("groups together primate foveal and peripheral ON parasol retinal ganglion cells with the molecularly homologous mouse alpha retinal ganglion cell ON-transient subtype, corresponding to transcriptomic cluster C41…"). Semantically equivalent but unnecessary deviation from a curator-supplied definition, and a major metadiff penalty.
- **Scope (over-editing):** added an `hasExactSynonym "ON parasol RGC orthotype"` (xref PMID:37066415) not requested in the NTR and not in gold; added `terms:creator`, `terms:date`, `IAO_0000233`. The invented synonym is the weakest addition — "ON parasol RGC orthotype" is arguably misleading since the orthotype spans parasol *and* α types.
- The new term block was inserted in a different file location (after `CL_4033052`) than gold (after `CL_7770006`); cosmetic, but contributes to metadiff divergence.
