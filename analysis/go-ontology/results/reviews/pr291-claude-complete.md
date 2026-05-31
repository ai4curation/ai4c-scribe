---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 291
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.08
precision: 0.952
recall: 0.042
jaccard: 0.042
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

The agent's actual obsoletion of GO:0009095 is **correct and complete**: name prefixed `obsolete`, def prefixed `OBSOLETE.`, all logical axioms + 5 synonyms + `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, tracker #32005 added (replacing #31091, matching the human gold exactly), and both `consider: GO:0009094` and `consider: GO:0006571` added. The reported F1 of 0.080 grossly under-represents quality: the eval PR's diff also carries ~311 lines of unrelated foreign edits (GO:0000268, GO:0003400, GO:0005048, GO:0008785/8873/8874/8875, exocyst, etc., from other issues #31419/#31922/#31945/#31961/#31989) that appear **identically in all 9 low-scoring attempts** for this case. This is eval base-state contamination, not work the agent did — the harness base `go-edit.obo` (blob `9bfb355`, derived from contaminated base) already contained these changes.

## Strengths

- The GO:0009095 obsoletion is arguably the best of all 12 attempts on the *substance*: it is the only contaminated attempt whose tracker handling exactly matches the human gold (removes #31091, adds #32005), and it correctly removes the MetaCyc xref like the gold.
- Correct dual `consider` targets with sound rationale (PWY-3481 superpathway = PWY-3462 + PWY-3461, already mapped to GO:0009094/GO:0006571).
- Comment accurately states the obsoletion reason (pre-composed superpathway, should be a GO-CAM model) consistent with the issue.
- PR/issue write-ups correctly defer the 4 EXP annotations to the annotation-review process.

## Issues

- The eval PR as scored contains a large block of foreign, unrelated ontology edits. This is **base-state contamination** in the eval harness, not an agent error — the same block is byte-identical across attempts #291, #224, #223, #491, #487, #525, #450, #404, #324. The metadiff (F1 0.080, recall 0.042) is therefore meaningless as a measure of this agent's work; on the in-scope GO:0009095 stanza the agent matches the gold.
- `failure_modes: [over_editing]` is recorded only because the scored diff is dominated by out-of-scope changes; this is an artifact of contamination, not behavior attributable to kimi-k2.6. No genuine omission or error in the agent's obsoletion was found.
- Recommend this attempt be scored on the GO:0009095 stanza only (where it is essentially a gold match) or excluded/down-weighted; see the case-level Curation Note in METADATA.md.
