---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 375
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.706
precision: 0.686
recall: 0.727
jaccard: 0.545
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A correct, well-reasoned full **merge** of MONDO:0023243 into MONDO:0011274 (Muenke syndrome) with an exemplary, fully itemized PR writeup (per-item "transferred/dropped" table and a 12-point validation checklist). Obsoleted stanza is reduced exactly per the merge SOP; historical synonyms and the Orphanet:1535 xref are transferred to Muenke with the correct `MONDO:equivalentObsolete` qualifier. This is the curator-endorsed merge approach (PR #10106), not the rejected obsolete-only path (PR #10087). F1=0.706 **under-represents** quality: the divergences are deliberate, defensible curatorial judgments (one of which — dropping the retired SNOMED xref — differs from gold's choice but was explicitly justified).

## Strengths

- Obsoleted stanza is byte-correct: `obsolete glass-chapman-hockley syndrome`, `IAO:0000231 MONDO:TermsMerged`, issue #9798 link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — identical to gold.
- Transferred all four historical synonyms and `synonym: "glass-chapman-hockley syndrome" EXACT [Orphanet:1535]` onto Muenke; transferred `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` and `is_a: MONDO:0000426 ! autosomal dominant disease`; added issue #9798 provenance to Muenke.
- Correctly merged the `is_a: MONDO:0015469 ! craniosynostosis` source qualifiers (`Orphanet:1535/inferred` added to the existing ORCID source) rather than dropping the parent — the most careful handling of that line among all attempts, and consistent with the project guideline against removing parents.
- Used the real `MONDO:equivalentObsolete` qualifier (not the fabricated `MONDO:obsoleteEquivalent` of the kimi/haiku/sonnet attempts), and correctly dropped the owltools-injected `[MONDO:0023243]`-evidenced synonym artifact.
- Outstanding process transparency: explicit "items dropped intentionally" rationale and a QC checklist covering `qc-misused-replaced-by`, `qc-obsoletion-reason`, `qc-deprecated-class-reference`, `qc-xref-without-precision`, etc.

## Issues

- **Deviation from gold (SCTID):** Deliberately dropped `xref: SCTID:720814001`, arguing transferring a retired SNOMED concept as equivalent to Muenke would be inaccurate. Gold instead **retains it as `MONDO:equivalentObsolete`** — the qualifier exists precisely to record obsolete equivalence, so gold's choice is the more idiomatic Mondo handling. This is the one substantive (but defensible and well-argued) miss; it costs recall.
- **Scope/style:** Transferred synonyms kept at `RELATED` scope and "glass-chapman-hockley syndrome" cited as `[Orphanet:1535]`; gold promotes the historical synonyms to `EXACT` and cites `[PMID:20108486]`. Both are reasonable; the agent's are conservative and source-faithful, costing metadiff points without being errors.
- Did not reproduce gold's issue-unrelated incidental cleanups (`MNKES` RELATED→EXACT ABBREVIATION; deletion of "Muenke nonsyndromic coronal craniosynostosis"). Omitting these is correct scope discipline but lowers metadiff recall.
