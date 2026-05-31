---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 421
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.429
precision: 0.429
recall: 0.429
jaccard: 0.273
outcome: partial_success
failure_modes: [syntax_error, missing_metadata]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Claude-Haiku-4.5, second run. The diff is byte-identical to eval PR #475 (same
blob `1ac50b5`): correct `is_a: MONDO:0021074 ! precancerous condition`
classification, paraphrased definition with all four PMIDs, but the same
`IAO:0000233 "...9781" xsd:string` datatype error (gold/MONDO use
`xsd:anyURI`) and the same omission of `is_a` `source=` provenance. Core
classification correct; the reproduced datatype defect plus lower line-overlap
give the cohort-lowest F1 of 0.429. Reproducing the same `xsd:string` typing
across both runs indicates a systematic serialization habit for this model.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition`, matching
  gold and the requester's final preference in issue #9781.
- **Definition** is a faithful paraphrase of the issue's intended concept; all
  four PMIDs cited.
- Clean single term stanza, no spurious synonym, correct ORCID `creator`
  format, no stray edits elsewhere in the file.

## Issues

- **Datatype error (significant, reproduced).** `IAO:0000233 "...9781"
  xsd:string` instead of `xsd:anyURI`. Same defect as PR #475 — systematic, not
  random.
- **`is_a` lacks `source=` annotations** present in the gold (PMIDs + ORCID).
- **Def xref omits requester ORCID.** Minor.
- ID/creator-ORCID differences from gold are sandbox artifacts; the decisive
  issue is the reproduced `xsd:string` typing on the tracker property.
