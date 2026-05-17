---
ontology: mondo
issue_number: 9892
pr_number: 10206
eval_repo_pr: 520
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.769
precision: 0.667
recall: 0.909
jaccard: 0.625
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9892 asked for one thing: relabel MONDO:0011996 to "chronic myeloid leukemia"
(the preferred NCI/NIH/ACS name) while retaining the precise "chronic myelogenous
leukemia, BCR-ABL1 positive" as a synonym. This attempt did exactly that: it renamed
the term, updated all three `is_a` referrer label comments (lines ~133431, ~262021,
~512034), preserved the prior label as an EXACT synonym, and added the
`IAO:0000233 .../issues/9892` term-tracker item. F1=0.769 **under-represents** the
quality of this run: the metadiff is capped because gold PR #10206 also performed
unrequested OMIM/QC churn (repointing the `chronic myeloid leukemia` synonym xref list,
deleting three `leukemia, ...` synonyms, and adding the typo-bearing
`synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]` produced by its
"fix failed qc of double genes" commit) that the issue never requested and no agent
could derive. Against the issue's actual asks, this is a correct, complete, tightly
scoped solution.

## Strengths

- Correctly renamed `MONDO:0011996` `name:` to `chronic myeloid leukemia`, matching
  the issue request and the gold label exactly.
- Updated all three external `is_a: MONDO:0011996` referrer comments (`{source="NCIT:C9110"}`,
  `{source="DOID:0060761"}`, `{source="UMLS:C0023472"}`) so displayed labels stay
  consistent — matching gold exactly on these three lines.
- Preserved the prior precise label by adding `synonym: "chronic myelogenous leukemia,
  BCR-ABL1 positive" EXACT [DOID:0081088, NCIT:C3174]`, faithfully honoring the issue's
  explicit "should be kept as a synonym" instruction. The xref list mirrors the
  pre-existing capital-P sibling synonym, a sensible provenance choice.
- Added the `property_value: IAO:0000233 ".../issues/9892"` term-tracker item, matching
  gold and Mondo convention.
- Tight scope: no edits outside the issue's intent; no broken OBO syntax.

## Issues

- Did not reproduce gold's unrequested synonym churn (repointed `chronic myeloid
  leukemia` synonym xrefs; deleted `leukemia, chronic myeloid` RELATED and two
  `leukemia, ... somatic` EXACT synonyms; added `"leukimia, chronic myeloid" EXACT
  [OMIM:608232]`). This is the sole reason F1 < 1.0, but these changes are out of
  scope for issue #9892 and are an artifact of gold's OMIM-alignment/QC pipeline, not
  a curation requirement. Not counted against the agent.
- Minor style note: the new precise-label synonym duplicates the pre-existing
  capital-P `"chronic myelogenous leukemia, BCR-ABL1 Positive"` synonym at near-identical
  string value; a curator might dedupe by case. This is the same redundancy the gold
  curator chose not to introduce (gold relied on the existing capital-P synonym), so it
  is a defensible-but-different choice, not an error.
