---
ontology: mondo
issue_number: 9909
pr_number: 10208
eval_repo_pr: 301
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.111
precision: 0.062
recall: 0.5
jaccard: 0.059
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a repeat run of the same model (claude-haiku-4.5 / claude) and produces a diff
**byte-identical** to attempt #416 (blob `b025ce2`): the single edit `synonym: "MYH9-related
disease" EXACT []` → `[Orphanet:182050]`. The reproducibility is itself a finding — the Haiku
behavior on this case is stable. As in #416, the one edit is substantively correct (matches
gold's intent of sourcing this synonym, differing only in the source token vs gold's curator
ORCID) but the run **omits the headline `MATINS` addition** and the term tracker. F1=0.111
fairly reflects a real omission.

## Strengths

- Correctly identified and fixed the policy-violating empty `[]` citation on `MYH9-related
  disease`, using `Orphanet:182050` consistently with the sibling MYH9-related synonyms.
- Tightly scoped, no spurious or incorrect edits, no improper deletions of the historical
  syndrome synonyms.
- Deterministic with #416 — same model, same single correct edit; useful evidence of stable
  (if incomplete) behavior.

## Issues

- Missed requirement: did **not** add `synonym: "MATINS"`, the issue's primary ask and the
  change present in the gold PR and in the Opus/Kimi/Codex attempts.
- Did not add the `property_value: IAO:0000233 ".../issues/9909"` term tracker.
- Under-editing: missed the six RELATED→EXACT scope promotions the gold also made (cohort-wide
  gap; defensible as not literally requested).
- No PR/issue comment captured for this run, so methodology cannot be assessed; the diff shows
  the same under-delivery as #416.
