---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 324
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_metadiff_sensitive_to_new_term_provenance_and_wording
f1: 0.375
precision: 0.400
recall: 0.353
jaccard: 0.231
outcome: partial_success
failure_modes:
  - wrong_pattern
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.4 codex agent produced the best-aligned of the five attempts reviewed
here (F1=0.375) because it minted the **correct gold term IDs** —
`CL_9900000` (CD4, child of `CL_0000897`) and `CL_9900001` (CD8, child of
`CL_0000909`) — avoiding the off-by-one ID error that craters the four opencode
attempts. The shape of the edit is right and scope discipline is good (it
explicitly deferred the species-specific modeling per the maintainer comment).
However it diverges from gold on three real curatorial points: paraphrased
definitions, demotion of the four TSCM synonyms to `hasRelatedSynonym` with
`OMO_0003000` abbreviation typing, and use of the GitHub issue URL as a synonym
xref on most synonyms. Partial success: a usable start needing curator cleanup.

## Strengths

- **Correct term IDs matching gold exactly** (`CL_9900000` = CD4 subset,
  `CL_9900001` = CD8 subset) — the only attempt of these five to get the IDs
  right, which is why its F1 is ~6x the opencode attempts'.
- Correct parentage: `SubClassOf(CL_9900000 CL_0000897)` and
  `SubClassOf(CL_9900001 CL_0000909)`, matching gold.
- Correct scope discipline, explicitly reasoned in the PR comment: no
  species-specific taxon/marker restrictions and no `EquivalentClasses`,
  citing @Caroline-99's instruction in the issue thread that species-specific
  modeling should be a separate ticket. Plain `SubClassOf` matches gold.
- All three definition PMID xrefs (19525962, 21926977, 28060797), both
  contributor ORCIDs, and `terms:creator "GitHub Copilot"` present.
- All nine synonym strings per term present; documented, reproducible
  methodology (issue-context read, pre-existing-term check, per-PMID
  justification).

## Issues

- Definitions paraphrased, not verbatim: gold uses the issue's exact wording
  ("...long-lived, retains a naïve-like phenotype, and exhibits self-renewal
  and multipotent differentiation capacity. This cell acts as a stem-like
  reservoir..."); this attempt rewrites it ("...with stem-like properties,
  including longevity, self-renewal, a naive-like phenotype, and multipotent
  differentiation capacity, that can regenerate central and effector memory T
  cell subsets."). Same meaning, but not the requested text.
- Wrong pattern on synonym scope: the four TSCM/abbreviation forms
  (`CD4-positive TSCM cell`, `CD4+ TSCM cell`, `CD8-positive TSCM cell`,
  `CD8+ TSCM cell`) are demoted to `oboInOwl:hasRelatedSynonym` with
  `Annotation(oboInOwl:hasSynonymType obo:OMO_0003000)` abbreviation typing.
  The issue explicitly lists every synonym under "Exact Synonyms:" and gold
  keeps them as `hasExactSynonym`. Note the issue assigns PMID:21926977 to
  three TSCM forms; this attempt also demotes `CD4+ T memory stem cell` /
  `CD8+ T memory stem cell` handling inconsistently (kept exact but with the
  PMID), so the synonym treatment is internally uneven.
- Wrong pattern on synonym evidence: most synonyms receive the GitHub issue
  URL (`<https://github.com/obophenotype/cell-ontology/issues/3452>`) as a
  `hasDbXref` synonym annotation. Gold uses no issue-URL synonym xref; it puts
  PMID:21926977 only on the three TSCM forms and leaves the others unreferenced.
- Over-editing: added an unrequested `IAO_0000233` term-tracker annotation on
  both terms; gold omits `term_tracker_item`. Lowers precision against gold.
- Net: ontologically valid and the closest of these five to gold, but the
  synonym-scope demotion plus issue-URL xrefs plus paraphrased definitions
  would all need curator correction before this matched the accepted pattern.
