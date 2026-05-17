---
ontology: uberon
issue_number: 3495
pr_number: 3542
eval_repo_pr: 82
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.432
precision: 0.352
recall: 0.559
jaccard: 0.275
outcome: partial_success
failure_modes: [under_editing, instruction_violation]
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_reserialization_churn
companion_prs: [3541]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Correctly scoped to the seven lamina propria terms only (no epithelium scope
creep, unlike the gpt-5.5 runs), with correct genus-differentia logical
definitions and no duplicated asserted `relationship: part_of` per @dosumis.
The headline problem is the definition/synonym provenance: every term cites a
distinct **guessed PMID** (PMID:25349585, PMID:7106744, PMID:31988593,
PMID:36595919, PMID:10026315, PMID:31114440, PMID:7021601) as both the
`def` xref and the synonym xref. The project CLAUDE.md explicitly prohibits
guessing PMIDs; these are almost certainly unverified/hallucinated citations
for generic "lamina propria of X" definitions and constitute an instruction
violation. F1=0.432 partly reflects this and the single-synonym shortfall, on
top of the shared placeholder-ID/reserialization artifacts.

## Strengths

- Tight scope: only the seven requested lamina propria terms, no spurious
  epithelium terms.
- Correct genus UBERON:0000030 (lamina propria) and correct part_of targets
  for all seven segments; correct `{segment} lamina propria` label form.
- Honoured @dosumis's instruction: no duplicate `relationship: part_of`.
- Correct definition text pattern; reserialized with robot (reproduces the
  gold `seeAlso` churn hunk incidentally).
- Used a fresh canonical-range placeholder (UBERON:8600051-57) and self-
  reported correcting an ID collision before commit.

## Issues

- **Instruction violation**: guessed PMIDs as def and synonym xrefs in direct
  contradiction of the CLAUDE.md no-guessing-PMIDs rule. The PMIDs are not
  tied to verified segment-specific lamina-propria sources; this introduces
  unreliable provenance. Gold uses an ORCID dbxref (a later requirement) with
  empty synonym xrefs.
- **Under-editing on synonyms**: only one synonym per term; gold includes both
  the "lamina propria of X" and the adjectival form.
- Placeholder ID range UBERON:8600051-57 vs gold 8600134-140 — standard
  artifact; harmless but contributes to metadiff gap.
- Extra `created_by` / `term_tracker_item` vs gold — metadiff noise only.
- Net: ontologically the seven terms are usable and correctly axiomatised, but
  the fabricated citations would require a curator to strip/replace every
  xref before merge.
