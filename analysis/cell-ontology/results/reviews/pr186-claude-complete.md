---
ontology: cell-ontology
issue_number: 3452
pr_number: 3554
eval_repo_pr: 186
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.452
precision: 0.467
recall: 0.438
jaccard: 0.292
outcome: partial_success
failure_modes:
  - instruction_violation
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent added the two requested terms with correct IDs (`CL_9900000`,
`CL_9900001`), correct parents (`CL_0000897`, `CL_0000909`), verbatim
definitions, the three definition PMID xrefs, and both contributor ORCIDs. The
core task is done and the terms are ontologically valid. However, the agent
made an unrequested modeling decision that contradicts an explicit instruction
in the issue: it reclassified roughly half of the synonyms from `hasExactSynonym`
to `hasBroadSynonym` and added `OMO_0003000` (abbreviation) synonym typing,
even though the issue author explicitly listed all of them under "Exact
Synonyms". It also added a `term_tracker_item` (`IAO_0000233`) that gold
omitted. The metadiff F1 of 0.452 somewhat over-penalizes a partially correct
result, but the synonym-scope divergence is a genuine substantive deviation.

## Strengths

- Correct term IDs matching gold (`CL_9900000` CD4, `CL_9900001` CD8) and
  correct parent placement via plain `SubClassOf` of `CL_0000897` /
  `CL_0000909`.
- Correctly and explicitly avoided species-specific marker axioms / an
  `EquivalentClasses` axiom, with a well-reasoned justification citing
  @KazuhiroNakagawa's human-vs-mouse marker-panel point and @Caroline-99's
  instruction to defer it to a separate ticket. This scope judgment is correct.
- Both contributor ORCIDs and `terms:creator "GitHub Copilot"` present;
  definition reproduced faithfully (with `naïve`→`naive`, see Issues).
- Transparent PR comment documenting the reasoning, including an honest note
  that `robot reason` could not be run locally and manual checks were
  substituted instead.

## Issues

- Instruction violation / over-editing (synonym scope): the issue author
  explicitly enumerated all synonyms under "**Exact Synonyms:**". The agent
  reclassified `stem cell memory CD4+ T-cell`, `...CD4+ T-lymphocyte`, `stem
  cell-like memory CD4+ T cell`, `CD4+ T memory stem cell`, `CD4-positive TSCM
  cell`, and `CD4+ TSCM cell` (and the CD8 analogues) as `hasBroadSynonym`,
  justified by an asserted sibling pattern at `CL_0000904`. Even if a
  broad/exact distinction is defensible ontology practice in the abstract, the
  requestor and the gold PR both treat these as exact synonyms; overriding an
  explicit, specific instruction without curator sign-off is the wrong call
  here and is the main driver of the low recall.
- Over-editing (extra annotations): added
  `AnnotationAssertion(obo:IAO_0000233 ... "https://github.com/.../issues/3452")`
  (term_tracker_item) on both terms. Gold did not include this. It is harmless
  and arguably good provenance practice, but it is an unrequested addition that
  reduces precision against gold.
- Added `Annotation(oboInOwl:hasSynonymType obo:OMO_0003000)` to the TSCM
  synonyms — again defensible (they are abbreviations) but unrequested and
  divergent from both issue and gold.
- Style: normalized "naïve" → "naive" in the definition; gold retained the
  diacritic from the issue text. Minor and defensible, but contributes to the
  metadiff gap.
- Net: the terms are usable, but a curator would need to revert the
  exact→broad synonym demotion to match the requestor's intent, so this is a
  partial success rather than a clean one.
