---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 547
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

Gpt-5.5/opencode got the structural repair right but materially under-delivered
on the definition content. It broadened `CL_0002496` (intraepithelial
lymphocyte) with the correct core axiom change `RO_0001025 some UBERON_0001277`
→ `RO_0001025 some UBERON_0000483` (matching gold), added PMID:29674648 +
WIKIPEDIA:Intraepithelial_lymphocyte (preserving GOC:tfm/MP:0008894), added the
ORCID contributor to both terms, and minted `CL_9900000` (matching gold's ID)
with `UBERON_0001277` equivalent class and `SubClassOf CL_0002496`. However it
replaced the IAO_0000115 definition with a thin one-liner ("A mature T cell that
is located in an epithelium and is capable of a mucosal immune response")
instead of the issue's verbatim detailed "Improved textual definition" (CD103/
E-cadherin/granzyme B/perforin/NKG2D/tract list), and tagged the new asserted
parent edge `is_inferred "true"`. F1=0.593 partly reflects the placeholder/
xref-placement artifact but the dropped definition content is a real omission;
this is `partial_success`. (Note: eval PR #487 is a byte-identical run, blob
`2484338`.)

## Strengths

- **Core axiom repair exact**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — identical to gold; the
  intestinal→epithelium genus-differentia broadening is correct.
- **References added, not replaced**: PMID:29674648 and
  WIKIPEDIA:Intraepithelial_lymphocyte added to the definition's xref
  annotation set while keeping GOC:tfm and MP:0008894, honoring the issue's
  explicit instruction.
- **Contributor metadata correct on both terms**: `terms:contributor
  <https://orcid.org/0009-0000-8480-9277>` added to `CL_0002496` (alongside the
  pre-existing 0000-0003-1980-3228) and to the new subclass.
- **Subclass logically correct**: `CL_9900000` (matching gold's minted ID)
  carries the original narrow definition, `EquivalentClasses(... RO_0001025
  some UBERON_0001277 ...)`, `terms:creator "GitHub Copilot"`, the ORCID, and
  `SubClassOf CL_0002496`.
- **Provenance more correct than gold**: `IAO_0000233` points to the actual
  issue #3346 (gold mis-targets #3455).
- **Validated with robot convert**: the agent reports running `robot convert`
  successfully (functional-syntax check), good methodology.

## Issues

- **Missed requirement — definition content dropped**: the issue supplied a
  verbatim "Improved textual definition" with the tissue-resident /
  GI-respiratory-reproductive / CD103-E-cadherin / granzyme B-perforin-NKG2D
  detail. The agent collapsed this to "A mature T cell that is located in an
  epithelium and is capable of a mucosal immune response," discarding all the
  requested phenotypic/anatomical content. Gold uses the full text. This is the
  primary substantive shortfall (real recall loss, not an artifact).
- **Modeling error (wrong_pattern) — asserted parent marked inferred**:
  `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_9900000 CL_0002496)`.
  The hand-asserted superclass on the new term must be a plain `SubClassOf`
  (as in gold); the `is_inferred "true"` annotation is incorrect and risks the
  edge being stripped.
- **New subclass definition also thin**: "A mature T cell that is located in
  the intestinal epithelium ..." — acceptable as the narrow concept but does
  not carry the requested xref-backed content depth; minor relative to the
  parent omission.
- **Xref-placement convention penalty (artifact, not an error)**: WIKIPEDIA
  added as part of the definition annotation set; line-shape differences vs
  gold inflate the metadiff penalty.

## Curation Note (for METADATA, not this file)

The core axiom repair, references, contributor, and subclass structure are
correct, and the placeholder ID coincides with gold. The real defects are the
dropped detailed definition content (missed_requirement) and the
`is_inferred="true"` annotation on the new asserted edge (wrong_pattern).
F1=0.593 mixes the real omission with placeholder/xref artifacts; net
assessment is partial_success.
