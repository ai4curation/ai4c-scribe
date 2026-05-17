---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 203
agent: std_claude_sonnet45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.828
precision: 0.800
recall: 0.857
jaccard: 0.706
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent added exactly the two terms requested in issue #3452 — `CL_9900000`
(stem cell memory CD4-positive, alpha-beta T cell, child of `CL_0000897`) and
`CL_9900001` (stem cell memory CD8-positive, alpha-beta T cell, child of
`CL_0000909`) — with the issue's verbatim definitions, all nine requested
synonyms per term as `oboInOwl:hasExactSynonym`, the three definition PMID
xrefs, both contributor ORCIDs, and `terms:creator "GitHub Copilot"`. This is
substantively the same solution as the gold PR. The metadiff F1 of 0.828
under-represents quality: the only divergences from gold are cosmetic/provenance
(en-dash normalization, the `terms:date` value, and Declaration/serialization
placement), not curatorial substance.

## Strengths

- Correct term IDs matching gold exactly (`CL_9900000` = CD4 subset,
  `CL_9900001` = CD8 subset) and correct parents (`SubClassOf CL_0000897`,
  `SubClassOf CL_0000909`).
- Definitions reproduced verbatim from the issue, including the second sentence
  ("This cell acts as a stem-like reservoir capable of regenerating central and
  effector memory T cell subsets") that the haiku attempt dropped.
- All nine synonyms per term added with the correct synonym scope
  (`hasExactSynonym`), exactly as the issue author explicitly classified them
  ("Exact Synonyms:"). This matches gold; it did not over-think the synonym
  scope the way the opus attempt did.
- The three TSCM/abbreviation synonyms correctly carry the
  `Annotation(oboInOwl:hasDbXref "PMID:21926977")` axiom annotation as the issue
  requested.
- Correct scope discipline: it deliberately did **not** add species-specific
  marker axioms (CD95/CD45RA/CD122 etc.) or an `EquivalentClasses` axiom,
  correctly recognizing — as @Caroline-99 instructed in the issue thread — that
  the species-specific marker question raised by @KazuhiroNakagawa belongs in a
  separate ticket. Plain `SubClassOf` of the parent memory T cell matches gold.
- Did not add a `term_tracker_item` — matching gold (the opus and haiku
  attempts both added one, which gold omitted).

## Issues

- Style only: the agent normalized the en-dash in "stem cell–like memory CD4+
  T cell" / "...CD4-positive, alpha-beta T cell" to an ASCII hyphen ("stem
  cell-like ..."). Gold preserved the U+2013 en-dash from the issue text. This
  is a defensible normalization and arguably an improvement, but it costs
  metadiff recall on those two synonym lines per term.
- Provenance: `terms:date` is `2026-05-14T00:00:00Z` vs gold's
  `2026-01-12T12:14:30Z`. This is a normal provenance difference (the agent ran
  on a different date) and is not a quality defect; it depresses F1 without
  reflecting curatorial quality.
- Serialization artifact: the agent did not emit the two `Declaration(Class(...))`
  lines in the dedicated declaration block (gold inserts them after
  `Declaration(Class(obo:UBERON_8910001))`); the agent's term blocks were
  inserted before `CP_0000000` rather than interleaved at `CL_0000898`/
  `CL_0000910` as gold did. Both are valid OWL functional-syntax serializations
  of the same logical content (ROBOT would normalize them), so this is a
  serialization-order artifact, not an error — but it accounts for much of the
  remaining F1 gap.
- No substantive curatorial issues. This PR would be mergeable as-is.
