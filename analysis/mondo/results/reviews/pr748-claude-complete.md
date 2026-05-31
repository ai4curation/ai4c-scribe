---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 748
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
immune disorder" per ClinGen's request in issue #9749, but *deleted* the
ClinGen-attributed `EXACT` synonym line entirely rather than updating its text
to the new label as the human gold PR #10134 did. F1=0.857 (P=0.750, R=1.000)
accurately reflects the substance: the rename is correct, but one line gold
retained was dropped, discarding the `OMO:0002001` community-preferred-label
provenance. This is the documented ambiguous-instruction interpretation split,
not a quality defect in the case (METADATA `case_quality: good` stands).

## Strengths

- Correct `name:` update to "FAS-related autoimmune lymphoproliferative immune
  disorder", matching gold after normalization (recall=1.000).
- Tight scope: definition, `subset` lines, `xref: GARD:0028187`, `is_a`/
  `intersection_of: MONDO:0017979`, and FAS predisposition axioms left
  untouched — no scope creep.
- Reasonable, transparent methodology: read `__issue_context__.json`, verified
  the stanza via the MONDO `obo-checkout.pl`/`obo-checkin.pl` workflow,
  re-queried after check-in, and honestly disclosed that ODK/`robot convert`
  validation could not run (no Docker) — immaterial for a one-line text edit.
- The interpretation is defensible: keparis explicitly said "I don't think
  we'll need to keep that original name as an exact synonym," and the agent
  cited this clarification as its rationale. Deleting the synonym is a literal
  reading of that instruction.

## Issues

- Omission (the deciding factor vs. F1=1.0 attempts like #37): gold did not
  delete the synonym — it *repointed* the `synonym: "..." EXACT
  [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  line to the new label, preserving the ClinGen source and the
  preferred-label-by-community annotation. The requester only declined to keep
  the *old* string as a synonym; they did not ask to strip ClinGen's
  preferred-label provenance for the *new* label. The agent's deletion loses
  that annotation. Diff is -2/+1 vs. gold's -2/+2.
- This is `missed_requirement` (provenance retention), not `over_editing`: the
  agent did less than gold on the synonym line (removed where gold replaced),
  consistent with precision=0.750 / recall=1.000.
- No syntax or term errors; the OBO remains valid.
