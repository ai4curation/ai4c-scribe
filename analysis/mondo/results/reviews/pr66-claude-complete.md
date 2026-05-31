---
ontology: mondo
issue_number: 9493
pr_number: 9726
eval_repo_pr: 66
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
runtime_label: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: simple
f1: 0.5
precision: 0.5
recall: 0.5
jaccard: 0.333
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_has_reviewer_added_pmid_xref
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Same correct resolution as attempt #87 (same model/runtime, same blob `90dc077`): the agent added `is_a: MONDO:0024352 {source=".../issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! viral respiratory tract infection` and the `IAO:0000233` issue-9493 tracker line, no logical definition. This is a correct, complete, well-scoped implementation of curator @matentzn's Option-3 directive. F1=0.5 under-represents quality due to the reviewer-added `PMID:37426629` on the gold `is_a` line, which is undiscoverable from the issue.

## Strengths

- Solid PR comment with rationale and a checklist: verified stanzas via `obo-grep.pl`, used checkout/checkin, ran `robot convert` for OBO syntax validation, deliberately omitted the logical definition per curator instruction.
- Correct Option-3 classification with ORCID source; correct inheritance reasoning to `MONDO:0005550`.
- Reproduced the `IAO:0000233 ".../issues/9493"` tracker line matching gold; existing parents preserved.
- Honest reporting of the Docker/`make NORM` limitation.

## Issues

- New `is_a` sourced to `{issue URL, ORCID}` vs gold's `{PMID:37426629, ORCID}`; the agent explicitly declined to add a PMID because none was provided for the edit — a defensible reading of the instruction. The F1 penalty is the human-reviewer PMID artifact, not an agent error.
- No substantive issues.
