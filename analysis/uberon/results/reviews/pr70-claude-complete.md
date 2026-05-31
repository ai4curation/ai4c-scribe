---
ontology: uberon
issue_number: 3572
pr_number: 3573
eval_repo_pr: 70
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.857
precision: 1.000
recall: 0.750
jaccard: 0.750
outcome: success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent made both correct, complete edits: removed `relationship: located_in UBERON:0002224 ! thoracic cavity` from esophagus (UBERON:0001043) and changed `branching_part_of` → `connecting_branch_of` on esophageal artery (UBERON:0035539) → thoracic aorta (UBERON:0001515), `{source="FMA"}` preserved. It additionally added `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3572" xsd:anyURI` provenance to both terms, which the human gold PR did not. F1=0.857 understates quality: the core ontology change is exactly right (precision=1.0) and the extra hunks are valid provenance metadata, not errors.

## Strengths

- Both requested axiom edits exactly correct and complete.
- No `robot convert` reserialization churn (blob `30e675a`) — clean, localized diff.
- Adding `term_tracker_item` linking edits back to the source issue is a defensible, arguably good-practice provenance convention used elsewhere in UBERON.

## Issues

- Scope: the two `term_tracker_item` additions are beyond the issue's explicit ask and not present in the gold PR; this is the sole reason F1 < 1.0 (recall=0.75). It is a defensible, not erroneous, extra — but it does deviate from the human's minimal solution.
- Net assessment: a strong, correct result; the metadiff under-represents it because it penalizes benign provenance metadata.
