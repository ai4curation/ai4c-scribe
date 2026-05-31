---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 523
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_metadiff_sensitive_to_new_term_provenance_and_wording
f1: 0.062
precision: 0.067
recall: 0.059
jaccard: 0.032
outcome: partial_success
failure_modes:
  - wrong_term
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added the two requested TSCM terms with correct parents, verbatim
definitions, all nine exact synonyms per term, the three definition PMID xrefs,
and both contributor ORCIDs — substantively the right curation. However, it
minted the **wrong term IDs**: `CL_9900001` (CD4) and `CL_9900002` (CD8) instead
of gold's `CL_9900000` (CD4) and `CL_9900001` (CD8). Because every metadiff line
is keyed to the CL ID, this off-by-one mint collapses F1 to 0.062 even though
the curatorial content is close to gold. The score severely under-represents
quality, but the ID error is a real defect: the agent's `CL_9900001` collides
with the ID gold assigned to the *CD8* term, so this could not be merged
alongside gold without renumbering.

## Strengths

- Correct parentage exactly matching gold: `SubClassOf(CL_9900001 CL_0000897)`
  (CD4 term under CD4-positive, alpha-beta memory T cell) and
  `SubClassOf(CL_9900002 CL_0000909)` (CD8 term under CD8-positive, alpha-beta
  memory T cell).
- Definitions reproduced essentially verbatim from the issue, including the
  second sentence ("This cell acts as a stem-like reservoir capable of
  regenerating central and effector memory T cell subsets").
- All nine synonyms per term added with the correct scope
  (`oboInOwl:hasExactSynonym`), exactly as the issue author classified them
  ("Exact Synonyms:"). Did not demote the TSCM forms to related synonyms the
  way the codex attempt (#324) did.
- The three TSCM/abbreviation synonyms correctly carry the
  `Annotation(oboInOwl:hasDbXref "PMID:21926977")` axiom annotation as the issue
  requested.
- Correct scope discipline: it did not add species-specific marker axioms
  (CD95/CD122/CD45RA) or an `EquivalentClasses` axiom, consistent with
  @Caroline-99's instruction in the issue thread that the species-specific
  marker modeling belongs in a separate ticket. Plain `SubClassOf` matches gold.
- All three definition PMID xrefs (19525962, 21926977, 28060797) and both
  contributor ORCIDs present.

## Issues

- **Wrong term IDs (primary defect)**: minted `CL_9900001`/`CL_9900002` rather
  than gold's `CL_9900000`/`CL_9900001`. This is the dominant cause of the near-
  zero F1. More than a metadiff artifact: the agent's CD4 ID (`CL_9900001`) is
  the ID gold assigned to the CD8 term, an unresolvable collision on a real
  merge. The `CL_99xxxxx` placeholder range is provisional, but the off-by-one
  start is still an error.
- Over-editing: added an unrequested `IAO_0000233` term-tracker annotation
  (`AnnotationAssertion(obo:IAO_0000233 ... "https://github.com/.../issues/3452")`)
  on both terms. Gold deliberately omits `term_tracker_item`; this lowers
  precision against gold.
- Style/normalization: ASCII-hyphenated the two en-dash synonyms
  ("stem cell–like memory ..." → "stem cell-like memory ..."). Defensible and
  arguably an improvement, but diverges from gold's preservation of the issue's
  U+2013 en-dash.
- No substantive ontological errors. With ID renumbering and removal of the
  term-tracker, this would be mergeable. The 0.062 F1 badly under-represents the
  real quality of the curation content.
