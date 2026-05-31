---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 197
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.143
precision: 0.25
recall: 0.1
jaccard: 0.077
outcome: failure
failure_modes: [over_editing, wrong_pattern, instruction_violation, wrong_term]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Second haiku/claude run; the committed diff (`8a11b73`) is byte-identical to
attempt #305. It renamed MONDO:0957382 to "GCSH-related glycine encephalopathy",
**deleted** the existing parent `is_a: MONDO:0017338` and replaced it with
`is_a: MONDO:0011612`, demoted the original label to a `RELATED` synonym with a
mis-applied ClinGen qualifier, fabricated a guessed MalaCards URL, and rewrote
the definition. The curator explicitly declined to rename and kept both parents,
adding the ClinGen label only as an EXACT synonym. F1=0.143 fairly reflects
that only the issue-tracker property aligns with gold.

## Strengths

- Added `property_value: IAO:0000233 ".../issues/9896"` issue tracker matching gold.
- Definition uses the standard gene-disease template phrasing (but wrong genus
  and wrong sources — see Issues).

## Issues

- Instruction violation: removed `is_a: MONDO:0017338` and replaced it with
  `is_a: MONDO:0011612`. The agent config explicitly forbids removing existing
  parents unless explicitly instructed; the curator kept both parents.
- Wrong approach: renamed the primary label, the change the curator examined
  and rejected in the issue thread.
- Wrong synonym handling: the requested "GCSH-related glycine encephalopathy"
  string was made the primary label rather than added as a synonym; the
  original OMIM label was demoted to `RELATED` and incorrectly given the
  `{OMO:0002001=.../clingen}` preferred-label qualifier that belongs only on
  the ClinGen string.
- Fabricated metadata: changed the MalaCards URL to a guessed
  `gcsh_related_glycine_encephalopathy` slug; gold left the original untouched.
- Wrong def genus/sources vs gold (MMDS genus, curator ORCID 0000-0002-7638-4659).
- Net: failure — identical destructive reparent + fabricated URL as #305.
