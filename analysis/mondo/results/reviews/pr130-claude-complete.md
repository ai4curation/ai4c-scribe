---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 130
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.348
precision: 0.333
recall: 0.364
jaccard: 0.211
outcome: partial_success
failure_modes: [missed_requirement, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent (gpt-5.5 via opencode/"pi" runtime) created a structurally complete new term under `MONDO:0006949 retinal drusen` with all required fields. However — and in direct contradiction to the PR comment claiming care — it copied all four issue PMIDs including the curator-flagged bogus `PMID:34752962` into the definition, every synonym citation, the `is_a` source, and the `xref` source. It also over-attributed the `is_a` and `xref` axioms with a five-source block (four PMIDs + ORCID). This diff is byte-identical to attempt #110 (same blob `f5b1ef9`). Metadiff F1 of 0.348 reflects the bad-citation propagation plus the expected ID/style mismatches.

## Strengths

- **Correct structure and parent**: Term under the requested `MONDO:0006949 retinal drusen`; all required fields present (def, three synonyms with EXACT/EXACT ABBREVIATION types, xref, creator, tracker item); no empty citation brackets.
- **Correct xref concept and form**: `SCTID:762533006` with `MONDO:equivalentTo` among its sources (the issue's `SNOMED:` correctly mapped to the `SCTID:` prefix).
- **Compliant ID**: `MONDO:7770012` in the config-mandated `MONDO:777xxxx` range.

## Issues

- **Failed evidence evaluation (core difficulty)**: Propagated `PMID:34752962` ("Monitoring Colonoscopy Quality") — explicitly flagged as wrong evidence in the issue body — into `def:`, all three synonym citations, the `is_a` source, and the `xref` source. The agent applied the bad citation in *more* places than any other attempt. `missed_requirement`.
- **Over-attributed axioms (`over_editing`)**: `is_a: MONDO:0006949 {source="PMID:29859199", source="PMID:34752962", source="PMID:38386332", source="PMID:41361163", source="https://orcid.org/0000-0001-6677-8489"}` and a two-source `xref`. Gold attributes `is_a` to just one PMID + the ORCID. Dumping four PMIDs (one bogus) onto a subclass axiom is poor curation and reduces precision.
- **Over-citation of every synonym**: All synonyms carry all four PMIDs; gold scopes them narrowly. Poor practice independent of the bogus-PMID issue.
- **`dcterms:creator` deviates from config template**: Requester ORCID instead of curator ORCID `0000-0002-7638-4659`.
- **Thin PR/issue documentation**: The PR comment is a one-line summary with no rationale and no mention of evidence evaluation — contrasting unfavorably with the codex and Opus attempts. No evidence the bogus PMID was even examined.
- **Definition style**: AMD-risk folded into `def:` rather than gold's `comment:`.
- No syntax errors, single stanza, but the unflagged and widely-propagated bad citation is a real quality defect.
