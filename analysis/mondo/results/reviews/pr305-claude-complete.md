---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 305
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

Issue #9896 asked for the ClinGen label; the curator declined to rename and
added it only as an EXACT synonym, keeping both the MMDS7 label and the
MONDO:0017338 parent. This haiku attempt renamed the term, **deleted** the
existing parent `is_a: MONDO:0017338` and replaced it with `is_a: MONDO:0011612`,
demoted the original primary label to a `RELATED` synonym, fabricated a
non-verifiable MalaCards URL, and rewrote the definition. F1=0.143 is roughly
fair and arguably slightly generous — the only gold-aligned element is the
issue-tracker property; nearly everything else is a destructive or unsupported
change.

## Strengths

- Added `property_value: IAO:0000233 ".../issues/9896"` issue tracker matching gold.
- Added a `def:` following the `"Any [parent] in which the cause of the disease
  is a mutation in the [GENE] gene"` template form (though the wrong genus and
  wrong sources — see Issues).

## Issues

- Instruction violation: deleted `is_a: MONDO:0017338 {source="OMIM:620423"}`
  and replaced it with `is_a: MONDO:0011612`. The agent config explicitly
  states: "do not remove existing parents unless _explicitly instructed_ to do
  so." The issue gave no such instruction; the curator in fact kept both
  parents.
- Wrong approach: renamed the primary label — the curator examined and
  rejected this in the issue thread.
- Wrong synonym scope: demoted "multiple mitochondrial dysfunctions syndrome 7"
  to `RELATED` and incorrectly attached the `{OMO:0002001=.../clingen}`
  ClinGen-preferred qualifier to it. The OMIM label is an EXACT synonym, and
  the ClinGen qualifier belongs only on the ClinGen-preferred string. The
  agent never added the requested "GCSH-related glycine encephalopathy"
  synonym at all (it became the primary label), so the actual requested
  synonym string is absent in synonym position.
- Fabricated metadata: changed the MalaCards URL to
  `.../card/gcsh_related_glycine_encephalopathy`, an unverified slug derived
  from the new name. Gold left the original MalaCards URL untouched. Editing an
  external resource URL to a guessed value risks a dead link.
- Wrong def genus/sources: "Any glycine encephalopathy..." sourced to
  `[https://orcid.org/0000-0002-7437-8060, OMIM:620423]` vs gold's MMDS genus
  and curator ORCID `0000-0002-7638-4659`.
- Net: failure — destructive reparent against an explicit config rule plus a
  fabricated external URL.
