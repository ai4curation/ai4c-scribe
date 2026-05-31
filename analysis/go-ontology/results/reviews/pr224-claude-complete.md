---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 224
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
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

claude-haiku-4.5 produced a **correct and complete** GO:0009095 obsoletion: name/def prefixed, all logical axioms (`is_a: GO:0009073`, three `intersection_of`) + 5 synonyms + `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, `consider: GO:0009094` and `consider: GO:0006571` added, tracker #32005 added (and #31091 removed, matching the human gold). The reported F1 of 0.080 is an artifact of **eval base-state contamination**: the scored diff also contains ~311 lines of unrelated foreign edits (GO:0000268/0003400/0005048/0008785/0008873-5 etc.) that are byte-identical across all 9 low-scoring attempts on this case and were present in the harness base before the agent ran. They are not the agent's work.

## Strengths

- GO:0009095 stanza is a substantive gold match, including tracker handling (removes #31091, adds #32005) — equal to the human PR.
- Excellent write-up: a detailed annotation-impact table for all 4 EXP annotations (UniProt PMID:21102469 ×2, TAIR PMID:20883697, MTBBASE PMID:18727669) with per-annotation migrate/remove recommendations matching the issue author's analysis, while correctly leaving annotation changes to the annotation-review process.
- Correct dual `consider` targets with accurate MetaCyc-decomposition rationale.
- Methodology evidence: pre/post `make travis_build` reported passing, internal references to GO:0009095 checked (none), `obo-checkout.pl`/`obo-checkin.pl` workflow used.

## Issues

- The scored eval PR is dominated by foreign, unrelated ontology edits — **base-state contamination**, not an agent error. Identical block appears in attempts #291, #224, #223, #491, #487, #525, #450, #404, #324. F1/recall are therefore not a valid measure of this run.
- `failure_modes: [over_editing]` is recorded only as an artifact of the contaminated scored diff; no genuine over-editing or omission by claude-haiku-4.5 was found. The agent's own claimed scope ("Single change: obsolete GO:0009095 term") is accurate for the work it actually performed.
- Recommend scoring on the GO:0009095 stanza only, or excluding/down-weighting; see Curation Note in METADATA.md.
