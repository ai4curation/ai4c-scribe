---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 540
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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
reviewed_at: '2026-05-15'
---

## Summary

The agent correctly obsoleted GO:0061817 "endoplasmic reticulum-plasma membrane tethering" and, critically, used `consider: GO:0051643` + `consider: GO:0160214` rather than `replaced_by`, exactly matching the human gold PR #32022 and the cross-namespace rationale stated in issue #31873. The structural edit is identical to the human's; F1 = 0.909 is dragged below 1.0 only by a shorter obsoletion `comment`, so the metadiff under-represents the quality — this is effectively a complete, correct solution.

## Strengths

- Prefixed name with `obsolete` and definition with `OBSOLETE.`, added `is_obsolete: true` — textbook obsoletion per the `term-obsoletion` skill.
- Removed both logical axioms (`is_a: GO:0051643`, `is_a: GO:0140056`) and the EXACT synonym, leaving only provenance and obsoletion metadata.
- Correctly chose `consider` over `replaced_by`. The issue proposes GO:0160214 (a `molecular_function`) as the migration target while the obsoleted term is `biological_process`; this is a cross-namespace, non-equivalent mapping, so `replaced_by` would have been wrong. This matches the human PR and the precedent (GO:0000185/0000186/0000187) cited in the issue thread.
- Added `property_value: term_tracker_item` pointing to issue #31873.
- Preserved `created_by`/`creation_date` in place without reordering (avoids spurious diff churn that hurt other attempts).

## Issues

- None substantive. The obsoletion `comment` is terser than the human's ("represents a molecular function rather than a biological process" vs. the human's comment that also names GO:0160214 as the migration target). This is a stylistic/completeness nuance only; the agent's PR/issue comment does spell out the migration target, so curators are not left without guidance. This single differing line is the entire source of the 0.091 F1 gap.
