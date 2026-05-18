---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 487
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.593
precision: 0.667
recall: 0.533
jaccard: 0.421
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
case_quality: poor
case_quality_reason: scoring_artifact_placeholder_id_and_xref_placement_plus_gold_term_tracker_misattribution
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Gpt-5.5/opencode (eval PR #487) is a byte-identical run to eval PR #547 — same
output blob `2484338`, same F1=0.593. The structural repair is correct: the
core axiom change `RO_0001025 some UBERON_0001277` → `RO_0001025 some
UBERON_0000483` on `CL_0002496` matches gold, PMID:29674648 +
WIKIPEDIA:Intraepithelial_lymphocyte were added without replacing GOC:tfm/
MP:0008894, the ORCID contributor is on both terms, and `CL_9900000` (matching
gold's minted ID) was created with the `UBERON_0001277` equivalent class and
`SubClassOf CL_0002496`. The same two real defects as #547 apply: the
IAO_0000115 definition was collapsed to a thin one-liner instead of the issue's
verbatim detailed text (missed_requirement), and the new asserted parent edge is
tagged `is_inferred "true"` (wrong_pattern). F1 mixes the real omission with the
placeholder/xref-placement artifact; this is `partial_success`.

## Strengths

- **Core axiom repair exact**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — identical to gold.
- **References added, not replaced**: PMID:29674648 and
  WIKIPEDIA:Intraepithelial_lymphocyte added while preserving GOC:tfm and
  MP:0008894 per the issue's explicit instruction.
- **Contributor metadata correct on both terms**: `terms:contributor
  <https://orcid.org/0009-0000-8480-9277>` added to `CL_0002496` (alongside the
  pre-existing 0000-0003-1980-3228) and to the new subclass.
- **Subclass logically correct**: `CL_9900000` (matching gold's minted ID)
  carries the original narrow definition, `EquivalentClasses(... RO_0001025
  some UBERON_0001277 ...)`, `terms:creator "GitHub Copilot"`, the ORCID, and
  `SubClassOf CL_0002496`.
- **Provenance more correct than gold**: `IAO_0000233` points to the actual
  issue #3346 (gold mis-targets #3455).

## Issues

- **Missed requirement — definition content dropped**: the IAO_0000115
  definition was collapsed to "A mature T cell that is located in an epithelium
  and is capable of a mucosal immune response," discarding the issue's verbatim
  detailed content (tissue-resident; GI/respiratory/reproductive tracts;
  CD103/E-cadherin; granzyme B/perforin/NKG2D). Gold uses the full text. Primary
  substantive shortfall (real recall loss, not an artifact).
- **Modeling error (wrong_pattern) — asserted parent marked inferred**:
  `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_9900000 CL_0002496)`;
  the hand-asserted superclass must be a plain `SubClassOf` (as in gold).
- **New subclass definition also thin** (same as #547); acceptable as the
  narrow concept but lacks the requested content depth.
- **Reproducibility note**: identical output to eval PR #547 — not a defect,
  but the two runs should be treated as one data point in aggregation.
- **Xref-placement convention penalty (artifact, not an error)**: line-shape
  differences vs gold inflate the metadiff penalty beyond the true defect set.

## Curation Note (for METADATA, not this file)

Identical to eval PR #547 (blob `2484338`). Core axiom repair, references,
contributor, and subclass structure correct; placeholder ID coincides with
gold. Real defects: dropped detailed definition (missed_requirement) and
`is_inferred="true"` on the new asserted edge (wrong_pattern). Net:
partial_success; F1=0.593 over-weights placeholder/xref artifacts relative to
the real omission.
