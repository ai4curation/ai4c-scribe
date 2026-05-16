---
ontology: mondo
issue_number: 9862
pr_number: 10103
eval_repo_pr: 132
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: synonym_update
difficulty: simple
f1: 0.182
precision: 0.125
recall: 0.333
jaccard: 0.100
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added both requested exact synonyms to MONDO:0859152 with
`PMID:38773790` citations and added the `IAO:0000233` issue-tracker link,
yielding a clean minimal diff identical (blob `50c891a`) to attempt #111.
F1=0.182 **under-represents** the core quality: the issue requested only the
two exact synonyms and the agent delivered exactly that, scoped cleanly; the
low score reflects the human's out-of-scope enrichment (definition, comment,
logical definition, NEDCAM synonym), not an agent error.

## Strengths

- Correctly resolved the explicit ask: both synonyms added as `EXACT` on the
  correct term, located by label.
- Used a real literature citation, `PMID:38773790` (the Brain and Behavior
  GEMIN5 disorders paper), which matches the gold's source for the "GEMIN5
  disorder" synonym.
- Added `property_value: IAO:0000233`, the line matching gold exactly.
- Claims it ran `make NORM` and `robot convert` syntax validation; minimal,
  scoped diff with no collateral edits.

## Issues

- **Provenance over-application:** Applied `PMID:38773790` to *both*
  synonyms. The gold cites `PMID:33963192` (Nature Communications) for the
  "GEMIN5-related neurodevelopmental disorder" synonym; using only
  PMID:38773790 for that synonym is a weaker/less precise citation, though
  both PMIDs are real GEMIN5 papers.
- **Omission relative to gold:** No `def:`, `comment:`, or `intersection_of:`
  logical definition. CLAUDE.md calls for definitions with a PMID xref and
  genus-differentia logical definitions; proactive enrichment of this
  under-annotated term was missed. Beyond the literal issue request but a
  genuine quality gap and the reason F1 is capped.
- **Surface mismatch:** Plural synonym forms vs the human's singular
  normalization; the singular is the more correct Mondo convention.
- Did not add the `NEDCAM EXACT ABBREVIATION` synonym; defensible as out of
  the issue's scope.

Net: correct, well-scoped resolution of the stated request, slightly weakened
by applying a single PMID to both synonyms and missing the discretionary
enrichment. F1=0.182 under-represents quality; metadiff under-representation,
not a poor evaluation case.
