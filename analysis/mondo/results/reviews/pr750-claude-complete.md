---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 750
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.951
precision: 0.906
recall: 1.0
jaccard: 0.906
case_quality: good
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 / opencode correctly and completely merged MONDO:0034186 (autosomal
recessive extra-oral halitosis) into MONDO:0029144 (extraoral halitosis due to
methanethiol oxidase deficiency). The obsolete stanza is reduced to the
canonical merge form (`is_obsolete: true`, `replaced_by: MONDO:0029144`,
`property_value: IAO:0000231 MONDO:TermsMerged`, `obsolete `-prefixed name,
issue tracker item), and every meaningful annotation was transferred to the
survivor. Metadiff F1=0.951 **under-represents** quality: recall is a perfect
1.000, and the precision shortfall is driven almost entirely by the gold PR's
cosmetic delete+re-add churn of two unchanged synonyms (`"EHMTO"`,
`"extraoral halitosis due to MTO deficiency"`) which the agent sensibly left in
place, plus one genuine but minor omission (the #9842 tracker item was not
added to the survivor). This is a correct, well-scoped merge.

## Strengths

- Correct, complete merge following Mondo's obsoletion pattern; obsolete stanza
  contains exactly the canonical fields plus the issue-9842 tracker item, and
  the scheduling artifacts (`subset: obsoletion_candidate`,
  `property_value: IAO:0006012 "2026-03-01"`, the scheduled-merge `comment`)
  were correctly removed.
- All transfer targets handled on MONDO:0029144: the 6 rare-disease subsets
  (`gard_rare`, `nord_rare`, `ordo_disorder`, `orphanet`, `orphanet_rare`,
  `rare`), `xref: GARD:0017996 {source="MONDO:GARD"}`,
  `xref: Orphanet:562538 {source="MONDO:equivalentTo"}`,
  `is_a: MONDO:0019222 {source="Orphanet:562538"}`, and
  `relationship: has_characteristic HP:0000007`.
- Correctly re-cited the transferred `autosomal recessive extra-oral halitosis`
  synonym as `EXACT [Orphanet:562538]` rather than leaving stale
  `[MONDO:0034186]` evidence — a common QC trap, handled correctly.
- Conservative, gold-consistent choice to keep
  `is_a: MONDO:0003847 ! hereditary disease` on the survivor alongside the more
  specific transferred parent.
- PR comment documents a sound process (issue-context review, pre-edit stanza
  inspection, dangling-reference check, `git diff` review) and transparently
  reports the docker/`make NORM` environment limitation rather than faking it.

## Issues

- Minor omission: unlike gold (and attempts #43/#62), the agent did **not** add
  `property_value: IAO:0000233 ".../issues/9842"` to the survivor
  MONDO:0029144. The tracker item was added to the obsolete stanza only. This
  is the main genuine contributor to precision=0.906; low impact (provenance
  only, no ontological effect).
- Cosmetic-only divergence from gold: the human re-ordered the survivor's
  synonym block (delete + re-add of two unchanged synonyms); the agent kept
  them in original position. Not an error — the agent's diff is arguably
  cleaner (no churn). This explains most of the apparent metadiff gap and
  matches the established case note for pr10158.
- No substantive ontological errors.
