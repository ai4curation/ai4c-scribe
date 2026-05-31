---
ontology: go-ontology
issue_number: 31873
pr_number: 32022
eval_repo_pr: 257
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.870
precision: 0.909
recall: 0.833
jaccard: 0.769
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent obsoleted GO:0061817 with correct core mechanics (name/def prefixing, `is_obsolete: true`, axioms and synonym removed, tracker item added), but chose `replaced_by: GO:0160214` for a cross-namespace BP→MF mapping where the human and the issue both call for `consider`. It also reordered the `created_by`/`creation_date` provenance lines, costing recall. F1 = 0.870 fairly reflects a substantively-correct obsoletion with one pattern error and one cosmetic-but-real diff regression.

## Strengths

- Correct obsoletion skeleton: `obsolete`-prefixed name, `OBSOLETE.`-prefixed def, `is_obsolete: true`, both `is_a` axioms and the EXACT synonym removed.
- Added `property_value: term_tracker_item` for issue #31873.
- Kept `consider: GO:0051643` as a candidate, partially matching the human's intent.
- Recognized GO:0160214 as the appropriate migration target.

## Issues

- **Wrong pattern (`replaced_by` for a cross-namespace mapping).** The agent used `replaced_by: GO:0160214`. GO:0160214 is `molecular_function`; GO:0061817 is `biological_process`. `replaced_by` asserts a safe, direct, equivalence-grade substitution and (per the `term-obsoletion` skill) implies the editor should rewire references — inappropriate here. The issue body explicitly leaves "Replace by" blank and says curators "should check that the correct MF term is annotated"; the human used `consider` for both targets. This is the most consequential deviation and is not merely stylistic — `replaced_by` vs `consider` changes downstream annotation-migration semantics.
- **Dropped one `consider`.** Only `consider: GO:0051643` was kept; the human recorded both GO:0051643 and GO:0160214 as `consider`. With GO:0160214 demoted to `replaced_by`, curators lose the dual-target guidance.
- **Provenance line churn.** The agent deleted and re-added `created_by: dph` / `creation_date: 2016-12-05...` (reordering them after the new metadata) instead of leaving them in place as the human did. No semantic effect, but it is unnecessary diff noise and is the main driver of the recall drop to 0.833.
