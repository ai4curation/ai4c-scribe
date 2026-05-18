---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 723
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
(gpt-5.5/opencode, blob `97c80df`) got the headline move and subset relocation correct
but stopped at the literal request: it did not perform the provenance scrub of the
co-located xrefs on the broad term that the gold curator did across commits 1–3. F1=0.759
with recall=1.000 / precision=0.611 — the recall=1.0 is metadiff-misleading: it means
every change the agent made overlaps gold, but the agent made *fewer* changes (the score
is depressed by missed gold lines, i.e. this is an under-edit, not an over-edit). Core
ask satisfied; provenance hygiene incomplete.

## Strengths

- Correctly moved `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from MONDO:0016608
  to MONDO:0017089 — the literal issue request, done correctly.
- Moved all four ORDO/Orphanet subsets (`{source="Orphanet:2477"}`) from the broad term
  to MONDO:0017089, matching gold for that block.
- Added `property_value: IAO:0000233 ".../issues/9854"` to MONDO:0017089.
- Tightly scoped: no spurious edits, no syntax errors. Reported running `make NORM` and
  `robot convert` syntax validation locally (docker unavailable).

## Issues

- Omission: did not strip the `source="Orphanet:2477"` / `Orphanet:2477/e` provenance
  from `xref: ICD10CM:Q04.5` and `xref: icd11.foundation:368780653` on MONDO:0016608.
  These xrefs still falsely assert Orphanet:2477 supports the broad term — exactly the
  inconsistency the issue's underlying intent targets.
- Omission: did not add `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to
  MONDO:0017089, so the moved provenance is incompletely reconstructed on the correct
  term.
- Omission: did not touch `xref: MedDRA:10050183 {source="Orphanet:2477",
  source="Orphanet:2477/e"}` on MONDO:0016608 (gold re-sourced it to
  `{source="MONDO:equivalentTo"}`); the stale Orphanet provenance remains.
- Omission: did not add the `IAO:0000233 ".../issues/9854"` annotation to MONDO:0016608
  (only added to the isolated term). Gold annotated both.
- Net: the visible/literal task is done and would not introduce errors, but a curator
  would still need a follow-up pass to clean residual Orphanet provenance — a
  partial_success driven by under-editing the provenance chain, not by wrong edits.
