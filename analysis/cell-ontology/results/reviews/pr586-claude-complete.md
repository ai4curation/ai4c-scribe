---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 586
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

This attempt is byte-identical to eval PR #523 (same `e0d217073` blob): the
agent added both TSCM terms with correct parents, verbatim issue definitions,
all nine exact synonyms per term, the three definition PMIDs, and both
contributor ORCIDs. As with #523 it minted the **wrong IDs** — `CL_9900001`
(CD4) and `CL_9900002` (CD8) instead of gold's `CL_9900000`/`CL_9900001` — which
is what drives the F1 down to 0.062. The PR comment documents sound methodology
(checked for pre-existing terms, verified parents, ran `robot convert` syntax
validation, deferred the species-specific modeling per the maintainer comment).
The score badly under-represents the curatorial substance, which is close to
gold modulo the ID offset and an unrequested term-tracker.

## Strengths

- Correct parentage matching gold: CD4 term `SubClassOf CL_0000897`, CD8 term
  `SubClassOf CL_0000909`.
- Definitions reproduced verbatim from the issue including the second sentence,
  unlike the codex attempt (#324) which paraphrased.
- All nine synonyms per term added as `oboInOwl:hasExactSynonym`, matching the
  issue's explicit "Exact Synonyms:" classification; the three TSCM forms carry
  the `PMID:21926977` xref annotation as requested.
- Correct scope discipline: no species-specific marker axioms and no
  `EquivalentClasses` — consistent with @Caroline-99's instruction to defer
  species-specific modeling to a separate ticket; plain `SubClassOf` matches
  gold.
- Documented, reproducible methodology in the PR comment: pre-existing-term
  check, parent verification, literature support for each PMID, and a ROBOT
  syntax-conversion validation step.
- All three definition PMID xrefs and both contributor ORCIDs present.

## Issues

- **Wrong term IDs (primary defect)**: `CL_9900001`/`CL_9900002` rather than
  gold's `CL_9900000`/`CL_9900001`. Drives the near-zero F1 and creates an ID
  collision with gold's CD8 term on a real merge.
- Over-editing: added an unrequested `IAO_0000233` term-tracker annotation on
  both terms; gold omits it. Lowers precision against gold.
- Style: ASCII-hyphenated the two en-dash "stem cell–like ..." synonyms
  (defensible normalization, diverges from gold's en-dash preservation).
- No substantive ontological errors. With ID renumbering and removal of the
  term-tracker this would be mergeable; the 0.062 F1 substantially under-
  represents quality.
