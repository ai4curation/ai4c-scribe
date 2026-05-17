---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 476
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.5
recall: 0.5
jaccard: 0.333
outcome: partial_success
failure_modes: [under_editing, missed_requirement, syntax_error]
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-haiku-4.5/claude added a STARI term with the correct parent, both synonyms, and both xrefs, but **omitted the `transmitted_by NCBITaxon:6943` vector axiom**, used the non-canonical `SNOMED:` xref prefix, and added a likely-invalid `namespace: infectious_disease` line. Core term created but with several real defects beyond the unmatchable-ID metadiff artifact. F1 0.5 is roughly fair given the genuine substantive issues.

## Strengths

- Correct parent `is_a: MONDO:0025294` (tick-borne infectious disease).
- Both requested synonyms present with correct scopes: `"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`.
- Definition accurate and retained all three PMIDs.
- `xref: NCIT:C128427` correct and qualified `{source="MONDO:equivalentTo"}`.
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873; `is_a` annotated with the submitter ORCID source.

## Issues

- **Error (xref prefix)**: used `xref: SNOMED:444100007` verbatim from the issue. Mondo's repo convention is `SCTID:` for SNOMED CT (the gold uses `SCTID:444100007`; the config CLAUDE.md and ~18k existing `SCTID:` xrefs confirm this). `SNOMED:` is not a recognized prefix in the ontology — a genuine correctness defect.
- **Likely syntax/convention error**: added `namespace: infectious_disease`. The gold and the other strong attempts do not set a per-term `namespace`; Mondo terms inherit the ontology default namespace and a stray `namespace:` line is non-standard for the edit file. Plausible QC failure.
- **Omission (substantive)**: no `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum`, despite the issue/definition naming the lone star tick vector. Same modeling gap as #463 — a `missed_requirement`.
- **ID/locus**: `MONDO:7770018` vs gold `MONDO:1010205` contributes to the metadiff penalty (case flagged poor), but unlike #173 this attempt also has real defects, so 0.5 is not an unfair score.
- The PR/issue comment bodies are essentially empty stubs ("# PR Implementation Summary..." with no content), so methodology cannot be assessed and appears thin relative to the codex/opencode attempts.
