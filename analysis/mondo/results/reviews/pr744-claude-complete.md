---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 744
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 0.889
jaccard: 0.002
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff compares a correct ~10-line single-term fix against the 5,103-line ontology-wide bulk sweep selected as gold (#10117); F1=0.003 is meaningless here. Judge against the literal ask of issue #10030."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent removed all 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium" and added the `IAO:0000233` issue-tracker provenance annotation for #10030 (blob `a9a6bf8`, byte-identical to attempt #690). This is a complete and correct resolution of the literal ask of issue #10030. Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge, so a correctly scoped single-term fix is structurally unscoreable against it.

## Strengths

- Correct core fix: all 8 mis-imported DOID:13074 "cellulitis and abscess..." synonyms removed (these are bacterial soft-tissue infections at unrelated body sites, clearly wrong on a fungal nail infection).
- Preserved the valid nail-dermatophytosis synonyms (`dermatophytic onychia`, `dermatophytic onychomycosis`, `dermatophytosis of nail`) and all logical axioms (`is_a`/`intersection_of`/`disease_has_location UBERON:0001705`/`disease_has_infectious_agent`).
- Added the `IAO:0000233` term-tracker provenance annotation per the mondo-agent-config convention.
- Strong, transparent process reporting: read issue context, inspected full stanza, confirmed bad synonyms present in live edit file, reviewed final diff for scope, committed only `mondo-edit.obo`, and was honest about being unable to run Docker-backed ODK validation.

## Issues

- Minor cosmetic side-effect: the diff also removes a single trailing blank line at end of file (`@@ -666091,4 +666084,3 @@` ... `transmitted by` block). This is a benign whitespace normalization artifact, not a content error, and would not affect ontology semantics.
- Unlike the codex/gpt-5.5 variants, this run did not also remove the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}` (ICD-9 681.9 = cellulitis/abscess of unspecified digit, same erroneous cluster). This is a defensible omission, not an error — the issue did not explicitly ask for it — but the xref removal would have been a more thorough cleanup.
- recall=0.889 in the metadiff is a scoring artifact of the broken gold comparison, not a real omission relative to the issue.
