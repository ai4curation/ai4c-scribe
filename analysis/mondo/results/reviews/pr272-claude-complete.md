---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 272
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes: [missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created a structurally complete new term for reticular pseudodrusen under `MONDO:0006949 retinal drusen` with the three requested synonyms, the SNOMED equivalent xref, creator metadata, and the issue backlink. However, it failed the case's central evidence-evaluation step: it copied all four issue PMIDs verbatim — including `PMID:34752962` ("Monitoring Colonoscopy Quality"), which the curator explicitly flagged as wrong evidence in the issue body — into the definition and into every synonym citation. Metadiff F1 of 0.435 understates the structural correctness but the bad-citation propagation is a genuine quality defect, not just a metadiff artifact.

## Strengths

- **Correct structure and parent**: Term placed under the requested `MONDO:0006949 retinal drusen`; all required fields present (def, three synonyms, xref, creator, tracker item).
- **Correct synonym types**: `subretinal drusenoid deposits` EXACT and `SDD`/`RPD` EXACT ABBREVIATION, matching the requested types and MONDO conventions; no empty citation brackets.
- **Correct xref form**: `SCTID:762533006 {source="MONDO:equivalentTo"}`, matching gold and MONDO convention rather than the raw `SNOMED:` from the issue.
- **Compliant ID**: `MONDO:7770012` is in the config-mandated `MONDO:777xxxx` NTR range; the mismatch vs gold's `MONDO:1060213` is a harness artifact.

## Issues

- **Failed evidence evaluation (the core difficulty of this case)**: Included `PMID:34752962` in the definition and in all three synonym citations. The issue body itself states this is the wrong evidence, and the title resolves to an unrelated gastroenterology letter. Propagating it into the definition and *every* synonym is worse than gold and worse than the codex/Opus attempts that correctly excluded it. This is a `missed_requirement`: the curator's explicit instruction was disregarded.
- **Over-citation of synonyms**: Every synonym carries all four PMIDs (`[PMID:29859199, PMID:34752962, PMID:38386332, PMID:41361163]`). Gold scopes synonym citations narrowly (e.g., `RPD`/`SDD` cite only PMID:29859199). Citing four references — one of them irrelevant — on an abbreviation synonym is poor curation practice.
- **`dcterms:creator` deviates from config template**: Uses requester ORCID `0000-0001-6677-8489`; gold and the config NTR template use curator ORCID `0000-0002-7638-4659`.
- **Definition style**: AMD-risk statement folded into `def:` rather than gold's separate `comment:`; defensible but costs metadiff recall.
- No syntax errors and no scope creep (single stanza), but the unflagged bad-citation propagation is the dominant problem.
