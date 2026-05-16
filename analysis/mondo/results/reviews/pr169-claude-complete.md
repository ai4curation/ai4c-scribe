---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 169
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.417
precision: 0.417
recall: 0.417
jaccard: 0.263
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created a correct, well-scoped new term under `MONDO:0006949 retinal drusen` with the requested synonyms, the SNOMED equivalent xref, creator and tracker metadata, and correctly excluded the bogus `PMID:34752962` with a clear rationale ("resolves to an unrelated gastroenterology publication"). It rewrote the definition into a more concise genus-differentia form ("A retinal drusen characterized by...") and cited `PMID:29859199` plus `PMID:30298528` ("Reticular pseudodrusen: current understanding", Clin Exp Optom 2019) — a real, on-topic review it located itself. Metadiff F1 of 0.417 understates quality: the substance is correct and the definition style is actually closer to gold's genus-differentia phrasing than most other attempts; the score is depressed by the placeholder ID and the differing PMID set.

## Strengths

- **Correct evidence evaluation**: Excluded `PMID:34752962` as an unrelated gastroenterology publication, matching the curator's judgment.
- **Genus-differentia definition style closest to gold**: "A retinal drusen characterized by..." mirrors gold's "A retinal drusen characterized by subretinal deposits...". This is good ontology authoring practice (definition starts with the genus) and better aligned with MONDO style than the attempts that pasted the raw issue text.
- **Independent literature sourcing**: Added `PMID:30298528` (Clin Exp Optom 2019, "Reticular pseudodrusen: current understanding") — a valid, directly on-topic review the issue did not list, demonstrating genuine research rather than verbatim copying.
- **Correct structure**: Requested synonym types, `SCTID:762533006 {source="MONDO:equivalentTo"}` xref form, `is_a` with PMID source, creator and tracker metadata; no empty citation brackets.
- **Sound methodology**: Used `obo-grep.pl` / `obo-checkin.pl` workflow, ran `make NORM`, robot convert syntax check; documented checklist.

## Issues

- **`namespace: mondo` line included**: Per the config this field is required, but gold (post-NORM) does not carry it because `make NORM` normalizes it away. Harmless — robot/NORM strips it — but it is a metadiff line that gold lacks. Not an error.
- **`dcterms:creator` deviates from config template**: Requester ORCID `0000-0001-6677-8489` instead of the curator ORCID `0000-0002-7638-4659` used by gold and the config NTR template.
- **Definition omits the imaging/biomicroscopy detail and AMD-risk statement**: The agent's definition is more concise than gold's; it drops the "bluish-white appearance by biomicroscopy / hyperreflective on OCT" clause and the AMD-risk statement (gold keeps the imaging detail in def and the AMD-risk as a `comment:`). Defensible as a tighter definition but slightly less complete than gold.
- **Different PMID set than gold** (29859199+30298528 vs gold's 29859199+38386332+41361163): all agent-cited PMIDs are valid and on-topic, so this is a defensible curatorial choice, not an error; it does cost metadiff recall.
- Compliant `MONDO:777xxxx` ID; no syntax errors, no scope creep (single stanza).
