---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 223
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.076
precision: 0.905
recall: 0.04
jaccard: 0.04
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

gpt-5.4/codex produced a **correct** GO:0009095 obsoletion: name/def prefixed, all logical axioms + 5 synonyms + MetaCyc xref removed, `is_obsolete: true`, both `consider: GO:0009094` and `consider: GO:0006571` added, and tracker #32005 added while retaining the historical #31091 (the same defensible choice the 0.927-scoring gpt-5.5 runs made; the human gold replaced #31091). The reported F1 of 0.076 is invalid as a quality measure because the scored eval PR also contains ~311 lines of unrelated foreign edits from other issues — **eval base-state contamination** that is byte-identical across all 9 low-scoring attempts on this case and predates the agent's work.

## Strengths

- In-scope obsoletion substantively matches the human gold; the only intra-stanza deviation (keeping #31091) is identical to the top-scoring gpt-5.5 attempts and is defensible.
- Correct dual `consider` targets; clear rationale citing precedent for obsoleting route-specific amino-acid biosynthesis pathway terms representing GO-CAM-style models.
- Honest reporting: the agent's own checklist explicitly left "PR is created or amended" and the issue/PR comment items **unchecked**, correctly noting they belong to a downstream handoff flow — good calibration rather than over-claiming.
- PMIDs validated locally with `linkml-reference-validator`; per-PMID annotation-impact assessment provided and correctly deferred to annotation review.

## Issues

- Scored eval PR dominated by foreign, unrelated edits — **base-state contamination**, not an agent error. Same block appears in #291, #224, #223, #491, #487, #525, #450, #404, #324.
- `failure_modes: [over_editing]` is purely an artifact of the contaminated scored diff; no genuine over-editing or omission by gpt-5.4 was found in its actual obsoletion.
- Recommend scoring on the GO:0009095 stanza only, or excluding/down-weighting; see Curation Note in METADATA.md.
