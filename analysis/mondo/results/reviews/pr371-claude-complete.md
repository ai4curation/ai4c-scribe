---
ontology: mondo
issue_number: 9862
pr_number: 10103
eval_repo_pr: 371
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
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

The agent correctly identified the target term MONDO:0859152 by label (no
guessed IDs), added the two requested exact synonyms, and added the
`IAO:0000233` term-tracker link back to issue #9862 — which exactly matches
one line of the human gold. The reported F1 of 0.182 substantially
**under-represents** the quality of the core work: the issue asked only for
the two exact synonyms, and the agent delivered exactly that, scoped
cleanly. The low score is driven by the human curator's out-of-scope
enrichment (definition, comment, logical definition, NEDCAM abbreviation
synonym) that issue #9862 never requested, plus a plural/singular surface
difference in the synonym strings.

## Strengths

- Resolved the explicit issue ask correctly: both synonyms added as `EXACT`
  scope on MONDO:0859152, matching the requester's stated need ("we aim to
  have all the synonyms in the gene-related conditions").
- Methodologically careful: states it located the term via `obo-grep.pl` on
  `name`, used `obo-checkout.pl`/`obo-checkin.pl`, and confirmed via
  `git diff` that only the intended lines changed. Diff is clean and
  minimal — no collateral edits.
- Added `property_value: IAO:0000233 ".../issues/9862"` — this is the single
  line that matches the human gold byte-for-byte and is good Mondo practice
  for an untracked term.
- Honest, well-reasoned provenance handling: rather than fabricate PMIDs
  (CLAUDE.md forbids guessing identifiers; `aurelian`/network were
  unavailable), it cited the issue URL as a non-empty source, which is a
  defensible fallback consistent with the requirement that every synonym
  carry a citation.
- Cited prior Mondo gene-related naming precedent (e.g. MEF2C-related,
  CHD4-related neurodevelopmental disorder) to justify the synonym pattern.

## Issues

- **Omission (under-editing relative to gold):** Did not add the definition
  or logical definition. The human added a `def:` with xrefs
  `[OMIM:619333, PMID:33963192, PMID:38773790]`, a `comment:`, and an
  `intersection_of:` genus-differentia logical definition
  (`MONDO:0700092` and `has_material_basis_in_germline_mutation_in HGNC:20043`).
  The agent config's CLAUDE.md explicitly states "All terms should have
  definitions, with at least one definition xref, ideally a PMID" and
  prescribes genus-differentia logical definitions, so a maximally-aligned
  agent would have proactively enriched this under-annotated term. This is a
  legitimate quality gap, but it is *beyond the literal issue request*.
- **Surface mismatch:** Used plural forms ("GEMIN5-related neurodevelopmental
  disorders", "GEMIN5 disorders") as written in the issue; the human
  normalized to singular ("GEMIN5-related neurodevelopmental disorder",
  "GEMIN5 disorder"), consistent with Mondo's singular-label convention.
  Minor but it lowers metadiff match and is the more correct curatorial form.
- Did not add the `NEDCAM EXACT ABBREVIATION` synonym the human included
  (derivable from OMIM:619333); not requested by the issue, so a defensible
  omission.
- Could not run ODK `make NORM` (Docker unavailable) — transparently
  disclosed; not the agent's fault, but the diff is therefore unnormalized.

Net: a correct, well-scoped resolution of the stated request that misses the
human's discretionary enrichment. F1=0.182 under-represents actual quality;
this is a metadiff under-representation case, not a poor evaluation case.
