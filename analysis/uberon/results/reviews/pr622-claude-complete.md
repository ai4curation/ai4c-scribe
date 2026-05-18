---
ontology: uberon
issue_number: 3672
pr_number: 3673
eval_repo_pr: 622
agent: std_opencode_gpt54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: other
difficulty: simple
case_quality: ok
case_quality_reason: gold_id_revised_away_from_verbatim_issue_text
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4 (opencode) added a single `subsetdef:` to the `uberon-edit.obo` header
in the correct location with valid OBO syntax, but used the issue-verbatim
camelCase ID `addedByHRA` instead of the curator-revised snake_case
`added_by_HRA`. The produced diff is byte-identical to pr681 (same blob
`1994ec1`, same gpt-5.4/opencode agent) and, unlike pr390, carries no trailing
whitespace churn. F1=0.0 over-represents severity: functional, in-scope,
matches the issue's literal request. Established gold-verbatim-issue-text
inversion.

## Strengths

- Correct file, correct header placement next to `added_for_HCA`, correct
  `subsetdef:` syntax, single-line in-scope change with no term-stanza edits.
- ID `addedByHRA` is exactly the string the issue requested — defensible
  literal reading, not a hallucination.
- Clean diff: no ODK reserialization or trailing-newline churn artifact
  (contrast pr390 from the same gpt-5.4 model under codex).

## Issues

- Wrong pattern: `addedByHRA` violates Uberon's universal snake_case subsetdef
  convention; gold and master use `added_by_HRA`. Snake_case exemplars sat one
  line above the insertion point and were not followed.
- Weak description: "...added by HRA and HuBMAP team members." is terse, omits
  the canonical "Classes tagged with this subset property were added..."
  pattern, and drops the HuBMAP/Human Reference Atlas provenance framing of the
  gold.
- Net: valid, functional, in-scope subsetdef; partial_success rather than
  success despite F1=0.0. (Only an Agent Diff section is present in this
  attempt file; the diff alone is sufficient to assess this minimal metadata
  change.)
