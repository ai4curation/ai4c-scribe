---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 668
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_requires_source_provenance_investigation
f1: 0.759
precision: 0.611
recall: 1.000
jaccard: 0.611
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

## Summary

Issue #9854 asked to move ORPHANET:2477 ("isolated megalencephaly") from MONDO:0016608
(megalencephaly) to MONDO:0017089 (isolated megalencephaly). This attempt
(gpt-5.5/opencode, blob `97c80df`) is byte-identical to attempt #723 from the same
model: it correctly performed the headline xref + subset move but stopped at the literal
request and did not scrub the co-located Orphanet provenance on the broad term. F1=0.759,
recall=1.000, precision=0.611 — recall=1.0 here means everything the agent did matches
gold while gold did strictly more (an under-edit, not an over-edit). Core ask satisfied;
provenance hygiene incomplete.

## Strengths

- Correctly moved `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from MONDO:0016608
  to MONDO:0017089 — the literal issue request.
- Moved all four ORDO/Orphanet subsets (`{source="Orphanet:2477"}`) to MONDO:0017089,
  matching gold for that block.
- Added `property_value: IAO:0000233 ".../issues/9854"` to MONDO:0017089.
- Tightly scoped, no syntax errors, no spurious edits.

## Issues

- Omission: left `source="Orphanet:2477"`/`Orphanet:2477/e` on `xref: ICD10CM:Q04.5` and
  `xref: icd11.foundation:368780653` on MONDO:0016608 (gold removed these), so the broad
  term still falsely claims Orphanet:2477 support.
- Omission: did not add `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to
  MONDO:0017089 — provenance not fully reconstructed on the correct term.
- Omission: did not address `xref: MedDRA:10050183 {source="Orphanet:2477",
  source="Orphanet:2477/e"}` on MONDO:0016608 (gold re-sourced it to
  `{source="MONDO:equivalentTo"}`).
- Omission: added the `IAO:0000233 ".../issues/9854"` annotation only to MONDO:0017089,
  not also to MONDO:0016608 as gold did on both terms.
- Net: literal task complete and error-free, but residual stale Orphanet provenance would
  require a curator follow-up — partial_success from under-editing the provenance chain.
