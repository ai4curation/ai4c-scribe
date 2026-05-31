---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 260
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
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
lymphoproliferative immune disorder" but **removed** the ClinGen-attributed
`EXACT` synonym line entirely rather than updating its text to the new label
(human gold PR #10134 renamed the synonym). F1=0.857 (precision 0.75, recall
1.0) fairly represents the outcome: the rename is right; the ClinGen
preferred-label provenance was lost.

## Strengths

- Correct `name:` update, matching gold's primary edit after normalization.
- Old label removed everywhere — the literal reading of the requester's
  comment ("I don't think we'll need to keep that original name as an exact
  synonym") is satisfied; the PR explicitly cites @keparis's confirmation.
- Tight scope: definition, subsets, GARD:0028187 xref, MONDO:0017979
  parentage/equivalence, and gene/predisposition axioms untouched.
- Strong, transparent methodology: `obo-checkout.pl`/`obo-checkin.pl`, ran ODK
  `make NORM`, and re-verified the stanza with `obo-grep.pl` post-edit. The
  validation rigor here exceeds gold's own documented process.

## Issues

- **Missed requirement (provenance loss):** the deleted
  `synonym: "..." EXACT [https://clinicalgenome.org/affiliation/40157/]
  {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` line
  encodes ClinGen's preferred-label attribution, not just the old name. Gold
  updates this line's text to the new label to keep the ClinGen preferred-label
  attribution on the current name. Deleting it discards that provenance — the
  agent should have rewritten the line, not removed it.
- Despite excellent process discipline, the substantive ontological outcome
  needs curator correction, so this is partial success.
