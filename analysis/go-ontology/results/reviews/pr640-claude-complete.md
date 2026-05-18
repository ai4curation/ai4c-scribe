---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 640
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.909
precision: 0.909
recall: 0.909
jaccard: 0.833
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The agent correctly obsoleted GO:0061817 "endoplasmic reticulum-plasma membrane tethering" and used `consider: GO:0160214` + `consider: GO:0051643` rather than `replaced_by`, exactly matching the human gold PR #32022 and the cross-namespace (BP→MF) rationale stated in issue #31873 and the dragon-ai-agent resolution comment. The structural edit is identical to the human's; F1 = 0.909 is held below 1.0 only by a terser obsoletion `comment`, so the metadiff under-represents the quality — this is effectively a complete, correct solution.

## Strengths

- Prefixed name with `obsolete` and definition with `OBSOLETE.`, added `is_obsolete: true` — textbook `term-obsoletion` pattern.
- Removed both logical axioms (`is_a: GO:0051643`, `is_a: GO:0140056`) and the EXACT synonym, leaving only provenance and obsoletion metadata.
- Correctly chose `consider` over `replaced_by` for GO:0160214. The issue proposes GO:0160214 (a `molecular_function`) while the obsoleted term is `biological_process`; this is a cross-namespace, non-equivalent mapping where `replaced_by` would be semantically too strong. This matches the human PR and the precedent (GO:0000185/0000186/0000187) cited by the curator-facing agent.
- Retained `consider: GO:0051643` (the BP localization parent), matching the gold's second consider tag.
- Added `property_value: term_tracker_item` pointing to issue #31873; preserved `created_by`/`creation_date` in place without reordering.
- Documented a clean methodology (pre/post `make travis_build`, term-search of GO:0061817/GO:0160214/GO:0051643, checkout/checkin workflow).

## Issues

- None substantive. The obsoletion `comment` ("The reason for obsoletion is that this term represents a molecular function.") is terser than the human's, which also names GO:0160214 as the migration target. This is the entire source of the 0.091 F1 gap; the agent's PR/issue comments do spell out the migration target, so curators are not left without guidance.
