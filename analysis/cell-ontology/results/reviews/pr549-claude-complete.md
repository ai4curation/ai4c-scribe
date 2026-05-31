---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 549
agent: std_opencode_gpt55
model: gpt-5.5
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
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.5 opencode agent added both TSCM terms with correct parents, all nine
synonyms per term as exact synonyms, the contributor ORCIDs, and a clearly
documented methodology (literature review of each PMID, deferral of the
species-specific modeling per the maintainer comment, ROBOT syntax check). It
shares the `f32adb041` blob with eval PR #488. As with the other opencode
attempts it minted the **wrong term IDs** (`CL_9900001`/`CL_9900002` vs gold's
`CL_9900000`/`CL_9900001`), which collapses F1 to 0.062. Two additional
divergences from gold beyond the ID offset: the definitions are **paraphrased**
rather than verbatim, and **every synonym carries a `PMID:21926977` xref** even
the four non-TSCM strings the issue listed without any reference. The score
under-represents quality but the substance has more real divergence from gold
than the #523/#586 pair.

## Strengths

- Correct parentage matching gold: CD4 term `SubClassOf CL_0000897`, CD8 term
  `SubClassOf CL_0000909`.
- All nine synonyms per term added with the correct scope
  (`oboInOwl:hasExactSynonym`) per the issue's "Exact Synonyms:" classification —
  did not demote the TSCM forms to related synonyms like codex #324.
- Correct scope discipline: no species-specific marker axioms, no
  `EquivalentClasses`; consistent with @Caroline-99's separate-ticket
  instruction. Plain `SubClassOf` matches gold.
- Strong, explicit methodology in the PR comment: pre-existing-term search,
  parent-consistency check, per-PMID literature justification, and ROBOT
  syntax validation; correctly recognized and deferred the species-specific
  modeling concern.
- Both contributor ORCIDs present.

## Issues

- **Wrong term IDs (primary defect)**: `CL_9900001`/`CL_9900002` instead of
  gold's `CL_9900000`/`CL_9900001`. Drives the near-zero F1 and collides with
  gold's CD8 ID on a real merge.
- Definitions paraphrased, not verbatim: gold uses the issue's exact two-
  sentence text ("...long-lived, retains a naïve-like phenotype, and exhibits
  self-renewal and multipotent differentiation capacity. This cell acts as a
  stem-like reservoir..."); this attempt compresses it to "...long-lived and
  has the capacity for self-renewal and multipotent differentiation into memory
  and effector T cell subsets." Acceptable in meaning but diverges from the
  requested wording.
- Wrong pattern on synonym evidence: attaches `Annotation(oboInOwl:hasDbXref
  "PMID:21926977")` to **all nine** synonyms, including the four non-TSCM
  strings (e.g. "stem cell memory CD4-positive, alpha-beta T lymphocyte") that
  the issue listed with no reference. Gold puts the PMID only on the three
  TSCM/abbreviation forms and leaves the others unreferenced. Over-attribution
  of evidence.
- Over-editing: added an unrequested `IAO_0000233` term-tracker on both terms;
  gold omits it. Only two definition PMIDs cited (21926977, 28060797) for the
  CD4 term, dropping 19525962 that gold includes.
- Net: a usable start but would need ID renumbering, definition restoration to
  the requested wording, and synonym-evidence cleanup before merge.
