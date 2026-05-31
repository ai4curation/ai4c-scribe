---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 694
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.750
recall: 1.0
jaccard: 0.75
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly renamed MONDO:1060194 from "FAS-related autoimmune
lymphoproliferative syndrome" to "FAS-related autoimmune lymphoproliferative
immune disorder" per ClinGen's request in issue #9749, but deleted the
ClinGen-attributed `EXACT` synonym line entirely instead of updating its text
to the new label as human gold PR #10134 did. The diff is byte-identical to
sibling attempt #748 (same `9a6d3aa16` blob). F1=0.857 (P=0.750, R=1.000)
accurately reflects the substance: correct rename, one gold-retained line
dropped along with its `OMO:0002001` community-preferred-label provenance.
This is the documented ambiguous-instruction interpretation split, not a case
quality defect (METADATA `case_quality: good` stands).

## Strengths

- Correct `name:` update to "FAS-related autoimmune lymphoproliferative immune
  disorder", matching gold after normalization (recall=1.000).
- Tight scope: definition, `subset` lines, `xref: GARD:0028187`,
  `is_a`/`intersection_of: MONDO:0017979`, and FAS predisposition axioms all
  untouched — no scope creep, no spurious identifiers.
- Defensible reading of the issue thread: keparis stated "I don't think we'll
  need to keep that original name as an exact synonym," so removing the old
  synonym string is a literal, good-faith interpretation of an ambiguous
  curator instruction.

## Issues

- Omission (the factor separating this from F1=1.0 attempts such as #37): gold
  did not delete the synonym — it repointed the `synonym: "..." EXACT
  [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  line to the new label, keeping the ClinGen source and the
  preferred-label-by-community annotation. The requester declined to retain the
  *old* label as a synonym; they did not ask to drop ClinGen's preferred-label
  provenance for the *new* label. The agent's full-line deletion loses it.
  Diff is -2/+1 vs. gold's -2/+2.
- Classified as `missed_requirement` (provenance retention), not
  `over_editing`: precision=0.750 / recall=1.000 indicates the agent did less
  than gold on the synonym line (removed where gold replaced).
- No syntax or term errors; OBO remains valid. No PR/issue comment captured in
  the attempt file, so methodology beyond the diff could not be assessed.
