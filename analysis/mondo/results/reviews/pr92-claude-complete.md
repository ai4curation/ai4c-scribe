---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 92
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.522
precision: 0.500
recall: 0.545
jaccard: 0.353
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created a substantively correct new term for reticular pseudodrusen under the requested parent `MONDO:0006949 retinal drusen`, with a literature-backed definition, the three requested synonyms (`subretinal drusenoid deposits` EXACT, `SDD`/`RPD` EXACT ABBREVIATION), the SNOMED equivalent xref, creator metadata, and the issue tracker backlink. Critically, it correctly identified and excluded `PMID:34752962` ("Monitoring Colonoscopy Quality") as wrong evidence — the exact evidence-evaluation step the curator performed. The metadiff F1 of 0.522 (the best of all 10 attempts) substantially under-represents quality: it is depressed almost entirely by the placeholder ID (`MONDO:7770012` vs the curator's post-merge canonical `MONDO:1060213`), which the agent config explicitly instructs agents to use, plus stylistic differences in the def/comment split and synonym pluralization.

## Strengths

- **Correct evidence evaluation**: Independently verified the PMIDs and excluded `PMID:34752962` because it "resolves to an unrelated colonoscopy-quality letter," matching the curator's own determination in the issue body. This is the hardest part of the case and the agent nailed it without being told the answer.
- **Correct parent placement**: Retained `MONDO:0006949 retinal drusen` as the requester specified, with an explicit rationale citing existing MONDO drusen-subtype structure and the literature distinguishing RPD by its location internal to the RPE.
- **Correct synonym scoping**: `subretinal drusenoid deposits` as EXACT and `SDD`/`RPD` as EXACT ABBREVIATION — matches the requested synonym types and MONDO's ABBREVIATION qualifier convention. No empty `[]` brackets; all synonyms carry PMID citations.
- **Correct xref form**: Used the MONDO-standard `SCTID:762533006 {source="MONDO:equivalentTo"}` form, exactly matching gold, rather than the raw `SNOMED:` prefix from the issue.
- **Compliant ID allocation**: `MONDO:7770012` is in the `MONDO:777xxxx` NTR range that the agent config (`CLAUDE.md`: "New terms start MONDO:777xxxx") explicitly mandates; collision-checked via grep. The mismatch against gold's `MONDO:1060213` is a harness artifact, not an agent error.
- **Sound methodology**: Documented checklist (existing-term search, parent check, SNOMED verification via NCBI/MedGen, robot convert syntax check, NORM normalization attempt with a clear note that Docker was unavailable).

## Issues

- **`dcterms:creator` deviates from config template**: The agent set `dcterms:creator` to the requester's ORCID `https://orcid.org/0000-0001-6677-8489`. Both the gold PR and the agent config's own NTR template example use the curator ORCID `https://orcid.org/0000-0002-7638-4659` for `dcterms:creator` (requester ORCID belongs in `[...]` source brackets and `is_a` source). Minor convention deviation; quality-neutral for ontology semantics but a metadiff and provenance mismatch.
- **Definition style differs from gold (stylistic, not wrong)**: The agent folded the AMD-risk statement into `def:` whereas gold split it into a separate `comment:` field and rewrote the genus into Aristotelian "A retinal drusen characterized by..." form. The agent's definition is accurate and well-cited; this is a defensible alternative, not an error, but it costs metadiff recall.
- **Synonym pluralization**: Used plural "subretinal drusenoid deposits" vs gold's singular "subretinal drusenoid deposit". Trivial; matches the issue's wording.
- No syntax, scope, or correctness errors. No over-editing — the diff is exactly one new stanza.
