---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 240
agent: std_opencode_gem4
model: gemma-4-31b
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
`EXACT` synonym line rather than updating its text to the new label (human gold
PR #10134 renamed the synonym). F1=0.857 (precision 0.75, recall 1.0) is a fair
representation: correct rename, lost ClinGen preferred-label provenance.

## Strengths

- Correct `name:` update, matching gold's primary edit after normalization.
- Old label removed everywhere, consistent with the literal reading of the
  requester's instruction.
- Tight scope: definition, subsets, GARD:0028187 xref, MONDO:0017979
  parentage/equivalence, and gene/predisposition axioms untouched.
- Used the `obo-checkout.pl`/`obo-checkin.pl` workflow.

## Issues

- **Missed requirement (provenance loss):** deleted the
  `synonym: "..." EXACT [...clingen...] {OMO:0002001=".../clingen"}` line
  instead of rewriting it to the new label. That entry is ClinGen's
  preferred-label attribution, not just the old name; gold preserves it by
  renaming it. Deleting it discards ClinGen preferred-label provenance.
- Methodology weakness: the PR comment states it "attempted normalization using
  `sh run.sh make NORM`, but since it was a simple name change, I proceeded to
  commit" — i.e., NORM was not actually run. Immaterial for the byte-identical
  outcome here, but weaker validation discipline than the codex/opencode
  attempts that completed `robot convert` or `make NORM`.
- Needs curator correction before merge, hence partial success.
