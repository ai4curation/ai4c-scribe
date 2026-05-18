---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 488
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

This attempt is byte-identical to eval PR #549 (same `f32adb041` blob, same
gpt-5.5 opencode agent): both TSCM terms added with correct parents, all nine
exact synonyms per term, and both contributor ORCIDs. It shares #549's three
divergences from gold: **wrong term IDs** (`CL_9900001`/`CL_9900002` vs gold's
`CL_9900000`/`CL_9900001`, the dominant cause of the 0.062 F1), **paraphrased
definitions** rather than the issue's verbatim text, and a **`PMID:21926977`
xref attached to all nine synonyms** including the four the issue listed
unreferenced. The metadiff score under-represents the curatorial substance but
this attempt has more real divergence from gold than the #523/#586 pair.

## Strengths

- Correct parentage matching gold: CD4 term `SubClassOf CL_0000897`, CD8 term
  `SubClassOf CL_0000909`.
- All nine synonyms per term added as `oboInOwl:hasExactSynonym`, matching the
  issue's explicit "Exact Synonyms:" classification — not demoted to related
  synonyms like codex #324.
- Correct scope discipline: no species-specific marker axioms and no
  `EquivalentClasses`, consistent with @Caroline-99's separate-ticket
  instruction; plain `SubClassOf` matches gold.
- Both contributor ORCIDs present; the CD8 term cites all three definition
  PMIDs.

## Issues

- **Wrong term IDs (primary defect)**: `CL_9900001`/`CL_9900002` instead of
  gold's `CL_9900000`/`CL_9900001`; drives the near-zero F1 and collides with
  gold's CD8 ID on a real merge.
- Definitions paraphrased rather than reproduced verbatim from the issue
  (loses the requested two-sentence wording gold preserves).
- Wrong pattern on synonym evidence: `Annotation(oboInOwl:hasDbXref
  "PMID:21926977")` attached to all nine synonyms, including the four non-TSCM
  strings the issue listed without any reference. Gold scopes the PMID to the
  three TSCM/abbreviation forms only.
- Over-editing: unrequested `IAO_0000233` term-tracker on both terms; gold
  omits it. CD4 term cites only two definition PMIDs (21926977, 28060797),
  dropping 19525962 that gold includes.
- No PR comment block was captured for this run (diff-only), so methodology
  cannot be assessed here; the identical-blob sibling #549 documents a sound
  process. Would need ID renumbering, definition restoration, and synonym-
  evidence cleanup before merge.
