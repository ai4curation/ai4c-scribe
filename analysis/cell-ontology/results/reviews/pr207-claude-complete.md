---
ontology: cell-ontology
issue_number: 3346
pr_number: 3549
eval_repo_pr: 207
agent: std_claude_sonnet45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.615
precision: 0.667
recall: 0.571
jaccard: 0.444
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: scoring_artifact_xref_placement_and_provenance_plus_gold_term_tracker_misattribution
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Sonnet-4.5/claude produced a substantively complete and correct resolution of issue
#3346: it broadened `CL_0002496` (intraepithelial lymphocyte) to the issue's exact
requested definition text, switched the genus-differentia from `RO_0001025 some
UBERON_0001277` (intestinal epithelium) to `RO_0001025 some UBERON_0000483`
(epithelium) — identical to gold — added PMID:29674648 and the ORCID contributor
0009-0000-8480-9277, and minted the new `intestinal intraepithelial lymphocyte`
subclass with the original narrow definition, the `UBERON_0001277` equivalent class,
and `SubClassOf CL_0002496`. The metadiff F1=0.615 substantially **under-represents**
quality: the only material divergences from gold are xref *placement* convention
(top-level `hasDbXref` line vs. embedding `WIKIPEDIA:` inside the definition's xref
annotation) and unscoreable provenance fields (date stamp, term-tracker target). This
is effectively a near-correct run scored down by serialization/convention artifacts,
compounded by a misattribution in the gold PR itself (gold's `IAO_0000233` points to
issue #3455, not #3346).

## Strengths

- **Definition broadening verbatim-correct**: `CL_0002496` IAO_0000115 was replaced
  with exactly the issue's "Improved textual definition" (tissue-resident lymphocyte
  ... gastrointestinal, respiratory, and reproductive tracts ... CD103/E-cadherin ...
  granzyme B, perforin, NKG2D), byte-identical to the gold definition.
- **Logical axiom repair correct**: `EquivalentClasses(CL_0002496
  ObjectIntersectionOf(CL_0002419 ObjectSomeValuesFrom(RO_0001025 UBERON_0000483)
  ObjectSomeValuesFrom(RO_0002215 GO_0002385)))` — exactly matches gold's broadened
  axiom; the intestinal→epithelium genus-differentia change is the core ask and is
  precisely right.
- **References added, not replaced**: PMID:29674648 was added to the definition's
  xref annotation set while preserving `GOC:tfm` and `MP:0008894`, honoring the
  issue's explicit "DO NOT replace existing ones" instruction.
- **Contributor metadata correct**: added `terms:contributor CL_0002496
  <https://orcid.org/0009-0000-8480-9277>` (the ORCID from the issue) alongside the
  pre-existing 0000-0003-1980-3228 contributor — matches gold.
- **Subclass created correctly**: new `CL_9900000` with the original narrow
  definition text, `EquivalentClasses(... RO_0001025 some UBERON_0001277 ...)`, and
  `SubClassOf(CL_9900000 CL_0002496)`. The placeholder ID happens to coincide with
  the gold's minted ID, but more importantly the term's logical content is exactly
  the gold's. `terms:creator "GitHub Copilot"` and the ORCID contributor are present.
- **Provenance more correct than gold**: the agent's `IAO_0000233` points to the
  actual issue #3346; the gold PR mis-targets #3455 (an unrelated issue), so the
  agent's term-tracker value is arguably *more* accurate than the reference.

## Issues

- **Xref placement style divergence (precision penalty, not an error)**: the issue
  asked to add `WIKIPEDIA:Intraepithelial_lymphocyte`. The agent added it as a
  separate top-level `AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002496
  "WIKIPEDIA:Intraepithelial_lymphocyte")` plus a top-level `IAO_0000233 ... #3346`,
  whereas gold embedded `WIKIPEDIA:` as an axiom-annotation on the definition. The
  requested content is present and ontologically valid; only the OWL serialization
  shape differs, which the line-oriented metadiff penalizes.
- **WIKIPEDIA xref on the subclass placed as a top-level line** rather than inside
  the definition annotation (same convention difference as above). Substantively the
  xref the issue asked for is present.
- **Provenance fields unscoreable**: `terms:date "2026-05-14..."` vs gold's
  "2026-01-05..."; these never match across runs and are normal metadiff noise, not
  quality defects.
- No ontological errors, no scope creep, no missed requirement. The agent did not
  reproduce gold's (incorrect) `#3455` term-tracker value — a divergence in the
  agent's favor.

## Curation Note (for METADATA, not this file)

F1/precision/recall here are artifacts of xref-placement convention and provenance,
plus a misattributed term-tracker URL *in the gold PR*. The substantive ontology
edit (broadened definition, UBERON_0001277→UBERON_0000483 axiom repair, faithful
narrow subclass) is essentially correct and complete. Treat as `success`.
