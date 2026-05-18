---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 569
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.342
precision: 0.232
recall: 0.65
jaccard: 0.206
outcome: partial_success
failure_modes: [under_editing, over_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent did the requested core fix on MONDO:0009106 — replaced the over-narrow
`xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}` with
`xref: Orphanet:573278 {source="MONDO:equivalentTo"}` and demoted the SCM type 1 synonyms
to NARROW — but introduced two unjustified extra edits (`subset: disease_grouping` and
`subset: ordo_group_of_disorders`) and dropped Orphanet:1671 from the `diastematomyelia`
EXACT synonym xref list where the human retargeted it to Orphanet:573278. F1=0.342 (lowest
recall, 0.65, of the five) **under-represents** quality because the dominant missing mass
is the established off-issue subtype creation and obsoletion-merge rewrite (METADATA.md
Curation Note), but this attempt also has the weakest in-scope precision of the set.

## Strengths

- Correct primary intent: `xref: Orphanet:573278 {source="MONDO:equivalentTo"}` added and
  the equivalentTo Orphanet:1671 xref removed entirely (cleaner than the #665/#721
  re-qualification approach, and closer to the gold deletion).
- Synonym scope matches the human gold: `synonym: "SCM type 1"` and
  `synonym: "split cord malformation type 1"` demoted EXACT→NARROW `[Orphanet:1671]`;
  `synonym: "split cord malformation"` upgraded to EXACT.
- Promoted `synonym: "split spinal cord malformation"` to EXACT (the human did this too,
  though the human cited `[GARD:0001851, Orphanet:573278]` rather than the agent's
  `[GARD:0001851, MEDGEN:3801]`).
- Added the `IAO:0000233` #9871 term tracker; ran ODK `make NORM` and ROBOT syntax check
  per the PR comment (the only attempt in this set that reports completing normalization).

## Issues

- Over-editing (over_editing): added `subset: disease_grouping` and
  `subset: ordo_group_of_disorders {source="Orphanet:573278"}`, neither of which the human
  added. `disease_grouping` is unjustified — MONDO:0009106 is a disease, not a grouping
  class, and the issue did not request reclassification; this risks introducing an error.
- Provenance regression (missed_requirement): dropped Orphanet:1671 from the
  `diastematomyelia` EXACT synonym xref list entirely
  (`[ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500]`) rather than
  retargeting it to Orphanet:573278 as the human did — losing a citation instead of
  correcting it.
- Incomplete provenance cleanup (under_editing): left stale `source="Orphanet:1671"`
  qualifiers on `xref: ICD10CM:Q06.2`, `xref: MedDRA:10012750`, and `xref: OMIM:222500`
  (with `/e`/`/specific` fragments). The human moved all of these to Orphanet:573278.
- Subset over-collapse: dropped `ordo_disorder`, `ordo_morphological_anomaly`,
  `orphanet_rare`; the human kept all four orphanet subsets retargeted to 573278.
- Did not create MONDO:1060220-1060222 nor run the obsoletion-merge — the dominant F1 gap,
  but the established case-quality artifact, not an agent failure.
