---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 448
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.75
recall: 1.0
jaccard: 0.75
outcome: partial_success
failure_modes: [missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly renamed MONDO:1060194 to "FAS-related autoimmune
lymphoproliferative immune disorder" but **deleted** the ClinGen-attributed
`EXACT` synonym line entirely instead of updating its text to the new label.
Human gold PR #10134 kept that synonym and renamed it. F1=0.857 (precision 0.75,
recall 1.0) — the score is fair and does not over- or under-represent quality:
the primary rename is right, but the agent lost a real piece of curated
provenance. This is the single most common error in this case (7 of 11
attempts made it).

## Strengths

- Correct `name:` update, matching gold's primary edit after normalization.
- Old label removed everywhere — the literal reading of the requester's "I
  don't think we'll need to keep that original name as an exact synonym" is
  satisfied.
- Tight scope: definition, subsets, GARD:0028187 xref, MONDO:0017979
  parentage/equivalence, and gene/predisposition axioms untouched.
- Methodology: used `obo-checkout.pl`/`obo-checkin.pl` and ran `make NORM` via
  the ODK container; PR rationale correctly summarized the ClinGen discussion.

## Issues

- **Missed requirement (provenance loss):** the deleted line
  `synonym: "FAS-related autoimmune lymphoproliferative syndrome" EXACT
  [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  is not merely the old name as a synonym — it carries ClinGen's
  preferred-label attribution (`OMO:0002001` = preferred label by ClinGen).
  Gold updates this line's text to the new label so the ClinGen preferred-label
  attribution stays attached to the current name. By deleting it, the agent
  silently dropped the ClinGen preferred-label provenance for the term. This is
  an omission, not over-editing: the agent removed a line it should have
  rewritten.
- A curator would need to restore the renamed ClinGen synonym before merge, so
  this is partial success rather than success despite a reasonable literal
  interpretation of an ambiguous instruction.
