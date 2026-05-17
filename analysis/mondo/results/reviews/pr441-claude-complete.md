---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 441
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.1
precision: 0.25
recall: 0.062
jaccard: 0.053
outcome: failure
failure_modes: [over_editing, scope_creep, wrong_pattern, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The curator declined to rename MONDO:0957382 and added the ClinGen label only
as an EXACT synonym, keeping the MMDS7 label and both parents. This sonnet
attempt is the most heavily over-edited of the ten: it renamed the term, added
five synonyms, replaced the parent (MONDO:0017338 deleted, MONDO:0011612 added)
with an `excluded_subClassOf` axiom documenting the removal, added an
`intersection_of` equivalence definition, a `clingen` subset, and a
`dc:creator` property. F1=0.100 is roughly fair — almost nothing aligns with
the conservative gold beyond the issue tracker.

## Strengths

- Strong, well-documented research: the PR comment correctly identifies the
  glycine-cleavage-system mechanism, cites sibling gene-specific terms
  (MONDO:0958179 GLDC, MONDO:0958192 AMT, MONDO:0015010 SLC6A9), and explains
  the reparenting rationale coherently.
- Added `property_value: IAO:0000233 ".../issues/9896"` matching gold.
- The ClinGen synonym is present with the correct `{OMO:0002001=.../clingen}`
  preferred-label qualifier.

## Issues

- Instruction violation: removed `is_a: MONDO:0017338` (replacing it with
  MONDO:0011612 and an `excluded_subClassOf MONDO:0017338` axiom). The config
  explicitly forbids removing existing parents unless explicitly instructed;
  the curator kept both parents. The `excluded_subClassOf` axiom actively
  asserts the original classification is *wrong* — a strong claim the curator
  did not make and which is contradicted by gold retaining MONDO:0017338.
- Wrong approach: renamed the primary label, the change the curator rejected.
- Scope creep / over-editing: five synonyms, an `intersection_of` equivalence
  axiom, and a `clingen` subset — none requested, none in gold. Some synonym
  citations are weak (`MONDO:patterns/disease_series_by_gene` as a source for a
  free-text synonym is a pattern reference, not evidence).
- ClinGen synonym sources are empty `[]`; gold cites the ClinGen affiliation
  and requester ORCID.
- Wrong def genus/sources: "Any glycine encephalopathy..." cited
  `[MONDO:patterns/disease_series_by_gene, OMIM:620423]` vs gold's MMDS genus
  and curator ORCID 0000-0002-7638-4659.
- Net: failure — the most aggressive over-edit of the set, including an
  explicit `excluded_subClassOf` repudiation of the parent the curator kept.
