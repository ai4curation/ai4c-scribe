---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 373
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.348
precision: 0.333
recall: 0.364
jaccard: 0.211
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created a correct, well-scoped new term under `MONDO:0006949 retinal drusen` with the three requested synonyms, the SNOMED equivalent xref (in MONDO `SCTID:` form), creator and tracker metadata, and excluded the bogus `PMID:34752962` — additionally posting a constructive issue comment asking the requester whether a different PMID was intended (transparent, curator-grade handling). It cited the three valid PMIDs (29859199, 38386332, 41361163), exactly matching gold's PMID set for the definition. Despite a low metadiff F1 of 0.348, this is one of the best substantive resolutions in the cohort; the score is almost entirely an artifact of the placeholder ID and gold's def/comment split.

## Strengths

- **Best-in-cohort evidence handling**: Verified all four issue PMIDs by title, excluded only `PMID:34752962` (correctly identified as Thiruvengadam 2022 "Monitoring Colonoscopy Quality"), and retained exactly the three valid PMIDs (29859199, 38386332, 41361163) that gold uses — without ever seeing gold. Also raised the discrepancy with the requester in an issue comment, mirroring real curator practice.
- **Per-synonym citation scoping**: Cited `subretinal drusenoid deposits`/`SDD` to PMID:29859199 and `RPD` to PMID:38386332 — discriminating citations rather than dumping all PMIDs on every synonym (closer to gold's careful scoping than most attempts).
- **Correct synonym types and parent**: EXACT / EXACT ABBREVIATION as requested; retained the requester-specified parent with an explicit, well-reasoned note about the above-vs-below-RPE tension and the requester's deliberate choice.
- **Correct xref convention**: Recognized the issue's `SNOMED:` should be MONDO's `SCTID:` prefix and applied it, citing the ~18.5k existing `SCTID:` xrefs as justification.
- **Transparent limitations**: Explicitly flagged that `make NORM` (Docker/ODK) and reasoner checks could not run locally and should be run before merge — accurate and honest.

## Issues

- **`xref` source attribution differs from gold**: Used `xref: SCTID:762533006 {source="https://orcid.org/0000-0001-6677-8489"}` whereas gold uses `{source="MONDO:equivalentTo"}`. The `MONDO:equivalentTo` value is the MONDO convention for an equivalent SNOMED mapping; attributing the xref to the requester ORCID instead is a minor convention miss (the only real, if small, defect in this attempt).
- **`dcterms:creator` deviates from config template**: Requester ORCID `0000-0001-6677-8489` rather than the curator ORCID `0000-0002-7638-4659` used by gold and the config NTR template.
- **Definition style (stylistic, not wrong)**: Folded the AMD-risk statement into `def:` rather than gold's separate `comment:` and did not adopt gold's "A retinal drusen characterized by..." genus opener. The definition is accurate and well-cited; this is a defensible alternative that costs metadiff recall.
- Compliant `MONDO:777xxxx` ID; no syntax errors, no scope creep (single stanza). Metadiff F1 materially under-represents this attempt's quality.
