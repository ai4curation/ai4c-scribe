---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 16
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.538
precision: 0.583
recall: 0.5
jaccard: 0.368
outcome: success
failure_modes: [missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Same gpt-5.4/codex agent, identical diff (blob `653b5d4`) to attempt #21: a correctly modeled TSEN2-related NDD term with correct logical definition, asserted gene relationship to `HGNC:28422`, the ClinGen-qualified EXACT synonym, a `comment:` disambiguating from `MONDO:0012890`, and TRACK-syndrome synonyms from `PMID:34964109`. The PR write-up here additionally claims `is_a: MONDO:0100500` was asserted, but the actual diff matches #21 (single parent `MONDO:0700092` only) — a minor discrepancy between narrative and diff. F1=0.538 understates the modeling quality; the ceiling is the new_term canonical-ID artifact plus a leaner-than-gold definition xref list.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition, asserted `relationship`, correct parent `MONDO:0700092`, tracker → issue #9956.
- Reproduced gold's ClinGen-qualified EXACT synonym verbatim with `{OMO:0002001=...}`.
- Strong disambiguation: explicit `comment:` distinguishing the new term from the existing TSEN2 PCH-type-2B term `MONDO:0012890`.
- Defensible `TRACK syndrome` synonyms sourced from the correct primary paper (`PMID:34964109`).
- Honest about environment limits (NORM not runnable without docker; `robot convert` passed).

## Issues

- **Narrative/diff mismatch**: the PR comment states the term was placed under `MONDO:0100500` (Mendelian neurodevelopmental disorder) "and also asserted `MONDO:0700092`", but the diff only contains `is_a: MONDO:0700092`. The agent's self-report overstates the parentage actually committed.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **Scope creep / under-citation**: definition xrefs reduced to `[ClinGen, PMID:34964109, PMID:38347586]`, dropping 6 of the 7 issue PMIDs gold retained, while adding the out-of-list `PMID:34964109`.
- Creator `doi:10.1186/s13326-024-00320-3` differs from human ORCID (unavoidable).
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
