---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 476
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.615
precision: 0.667
recall: 0.571
jaccard: 0.444
outcome: partial_success
failure_modes:
  - wrong_pattern
case_quality: poor
case_quality_reason: scoring_artifact_placeholder_id_and_xref_placement_plus_gold_term_tracker_misattribution
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Opus-4.7/claude produced the strongest attempt in this case: it broadened
`CL_0002496` (intraepithelial lymphocyte) with the issue's verbatim "Improved
textual definition" (correcting the source typo "ntegrin"→"integrin" and
flagging it for reviewers), performed the core axiom repair
`RO_0001025 some UBERON_0001277` → `RO_0001025 some UBERON_0000483` exactly as
gold, embedded `PMID:29674648` and `Wikipedia:Intraepithelial_lymphocyte` as
axiom-annotations *inside* the IAO_0000115 definition (the same serialization
shape as gold, unlike the sonnet/gpt attempts which used top-level lines), kept
`GOC:tfm`/`MP:0008894`, added the requested ORCID contributor to both terms,
and minted `CL_9900000` (matching gold's ID) with the original narrow
definition and `UBERON_0001277` equivalent class. The single real defect is a
`wrong_pattern` modeling error: the new asserted parent edge is written
`SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_9900000
obo:CL_0002496)`. F1=0.615 under-represents quality (placeholder/xref-order/
provenance artifacts dominate the penalty) but the is_inferred error is genuine,
so partial_success rather than success.

## Strengths

- **Definition broadening verbatim-correct**: `CL_0002496` IAO_0000115 replaced
  with exactly the issue's requested text (tissue-resident lymphocyte ... GI,
  respiratory, reproductive tracts ... CD103/E-cadherin ... granzyme B, perforin,
  NKG2D), matching gold; the "ntegrin → integrin" typo fix is correct and was
  transparently disclosed for reviewer sign-off.
- **Core axiom repair exact**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — identical to gold.
- **Xref placement matches gold**: PMID:29674648 and
  Wikipedia:Intraepithelial_lymphocyte added as axiom-annotations embedded in
  the definition (not separate top-level `hasDbXref` lines), so this attempt
  avoids the serialization-convention penalty that hit sonnet/gpt; existing
  GOC:tfm and MP:0008894 preserved per the "DO NOT replace" instruction.
- **Contributor metadata correct on both terms**: `terms:contributor
  <https://orcid.org/0009-0000-8480-9277>` added to `CL_0002496` (alongside the
  pre-existing 0000-0003-1980-3228) and to the new subclass.
- **Subclass logically correct**: `CL_9900000` carries the original narrow
  definition, `EquivalentClasses(... RO_0001025 some UBERON_0001277 ...)`,
  `terms:creator "GitHub Copilot"`, the ORCID, and parents under `CL_0002496` —
  the placeholder ID also coincides with gold's `CL_9900000`.
- **Provenance more correct than gold**: `IAO_0000233` points to the actual
  issue #3346; gold mis-targets #3455 (an unrelated issue), so the agent's
  term-tracker value is arguably more accurate than the reference.

## Issues

- **Modeling error (wrong_pattern) — asserted parent marked inferred**: the new
  edge is `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_9900000
  CL_0002496)`. A hand-asserted superclass on a freshly minted term must be a
  plain `SubClassOf(CL_9900000 CL_0002496)` (as in gold); the `is_inferred
  "true"` annotation falsely claims the reasoner derived the edge and risks it
  being stripped on the next pipeline pass. This looks cargo-culted from the
  adjacent `SubClassOf(Annotation(oboInOwl:is_inferred "true") CL_0002496
  CL_0002419)` line.
- **Unrequested embellishments (minor scope drift)**: an extra exact synonym
  "intestinal IEL" on the new term and a `terms:date` stamp on `CL_0002496`,
  neither in gold; defensible but not requested.
- **Provenance fields unscoreable**: `terms:date "2026-05-16..."` vs gold's
  date — normal metadiff noise, not a quality defect.
- No other ontological errors, no scope creep, no missed requirement; the
  detailed definition content the gpt/codex attempts dropped is present here.

## Curation Note (for METADATA, not this file)

F1 under-represents: placeholder-ID coincidence aside, the definition, axiom
repair, xref placement, and contributor metadata all match gold substantively.
The one genuine defect is the `is_inferred="true"` annotation on the new
asserted subclass edge (same wrong_pattern haiku-4.5/#144 made). Net assessment:
partial_success — strongest attempt, marred only by the asserted-edge modeling
error.
