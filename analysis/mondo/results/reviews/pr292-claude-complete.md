---
ontology: mondo
issue_number: 9493
pr_number: 9726
eval_repo_pr: 292
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
runtime_label: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes: [wrong_pattern, instruction_violation, under_editing]
case_quality: poor
case_quality_reason: gold_has_reviewer_added_pmid_xref
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a genuine failure (independent of the metadiff artifact). The agent added `is_a: MONDO:0005550 {source="https://orcid.org/0000-0003-2955-4640"} ! infectious disease` — i.e. it implemented **Option 1** (the user's literal original request) rather than **Option 3**, which curator @matentzn explicitly instructed in the issue comment ("please implement Option 3"). It also omitted the `IAO:0000233` issue-9493 tracker line. F1=0.0 here correctly reflects substantive divergence from gold, not merely a scoring artifact.

## Strengths

- The edit is syntactically valid and the parent (`MONDO:0005550` infectious disease) is ontologically defensible in isolation — common cold is an infectious disease, so this is not a wrong-term hallucination.
- Included the requested ORCID as source; existing parents preserved; minimal scope.
- PR comment honestly states what it did (added MONDO:0005550) with a plausible rationale from the existing viral-etiology definition.

## Issues

- **Instruction violation / wrong pattern**: the curator gave an explicit directive to implement Option 3 (`is_a: MONDO:0024352` viral respiratory tract infection). The agent implemented Option 1 (`is_a: MONDO:0005550` infectious disease) instead — the less specific classification the curator and issue analysis explicitly recommended against. This is the central failure.
- **Omission**: missing the `property_value: IAO:0000233 ".../issues/9493"` tracker annotation.
- The PR comment claims `make NORM` was run, but the diff is a plain single-line insertion with no normalization side effects — the validation claim is unsubstantiated.
- Net: genuine failure; would need to be redone to the curator's actual instruction. (The case is independently flagged poor for unrelated reasons, but this attempt's F1=0 is deserved.)
