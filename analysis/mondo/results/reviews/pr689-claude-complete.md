---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 689
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_requires_source_provenance_investigation
f1: 0.944
precision: 0.944
recall: 0.944
jaccard: 0.895
outcome: success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

## Summary

Issue #9854 asked to move ORPHANET:2477 ("isolated megalencephaly") from MONDO:0016608
(megalencephaly) to MONDO:0017089 (isolated megalencephaly). This attempt
(gpt-5.4/opencode, blob `aee5774`) is byte-identical to attempt #743 from the same model
and reproduces essentially the full gold diff, including the non-trivial provenance
scrub on the broad term, scoring F1=0.944. The only residual difference is the same as
in #743: `xref: MedDRA:10050183` was left bare instead of re-sourced to
`{source="MONDO:equivalentTo"}`. The 0.944 score accurately represents quality — this is
a near-complete, mergeable resolution.

## Strengths

- Correctly relocated `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from
  MONDO:0016608 to MONDO:0017089, satisfying the literal issue request.
- Moved all four ORDO/Orphanet subsets (`{source="Orphanet:2477"}`) to MONDO:0017089,
  preserving provenance consistency — a step beyond the explicit ask.
- Performed the harder cleanup: removed `source="Orphanet:2477"` /`Orphanet:2477/e`
  from `xref: ICD10CM:Q04.5` and `xref: icd11.foundation:368780653` on MONDO:0016608,
  and added `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to
  MONDO:0017089 — both matching gold.
- Added `property_value: IAO:0000233 ".../issues/9854"` to both terms, matching the
  gold issue-tracking convention.

## Issues

- Omission (minor): the gold third commit re-sourced
  `xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}` to
  `{source="MONDO:equivalentTo"}` on MONDO:0016608; this attempt left it bare
  (`xref: MedDRA:10050183`). Stripping the invalid Orphanet provenance is correct, but
  dropping the source entirely is slightly inferior to the curator's choice. The gold
  commit history shows the curator was itself uncertain here, so this is a
  defensible-but-imperfect judgment, not an error. It is the only line affecting the
  score.
- No scope creep, no syntax issues. (This attempt file carries no PR/issue comment body,
  only the diff; the agent rationale visible in the twin run #743 indicates the same
  sound methodology.)
