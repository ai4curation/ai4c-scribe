---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 19
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.562
precision: 0.529
recall: 0.600
jaccard: 0.391
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.4/codex obsoleted MONDO:0009327 correctly at the structural level and
rewired the dangling MONDO:0007703, but — like the gemma run — left every xref
source qualifier unchanged (still `MONDO:equivalentTo` /
`MONDO:equivalentObsolete` on an obsolete term) and dropped all subsets. Lowest
F1 (0.562) and second-lowest precision in the set. Partial success.

## Strengths

- Core obsoletion mechanics correct: name → `obsolete heart, malformation of`,
  `is_obsolete: true`, both `is_a` parents removed, `obsoletion_candidate`
  removed, `IAO:0006012` removed, `consider: MONDO:0005267` added (correctly
  used `consider`, not `replaced_by`), obsoletion reason
  `IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}` added.
- Rewired the dangling MONDO:0007703 `replaced_by: MONDO:0009327` →
  `consider: MONDO:0005267`, per the agent config rule; improvement over gold.
- Documented methodology (issue context read, references swept, ROBOT convert).

## Issues

- **Missed requirement**: xref source qualifiers left entirely unchanged —
  `MEDGEN:6748 {source="MONDO:equivalentTo"...}`,
  `OMIM:140500/234750 {source="MONDO:equivalentObsolete"}`,
  `UMLS:C0018798 {source="MONDO:equivalentTo"...}`. The gold retargeted all of
  these to obsolete-aware qualifiers; asserting active equivalence on an
  obsolete term is incorrect. This is the single largest source of the
  recall/precision shortfall and is a genuine omission, not a metadiff
  artifact.
- Over-editing: removed `subset: gard_rare`, `subset: nord_rare`,
  `subset: rare` (plus `obsoletion_candidate`); the gold kept the rare-disease
  subsets.
- Obsoletion comment is terse free text differing from gold;
  normalization-invisible, substantively acceptable.

Net: structurally a valid obsoletion + correct dangling-ref fix, but skipping
the xref-provenance modernization the gold required leaves the obsolete stanza
internally inconsistent. Partial success; the low F1 reflects a real omission
on top of the gold-omission artifact shared by the whole case.
