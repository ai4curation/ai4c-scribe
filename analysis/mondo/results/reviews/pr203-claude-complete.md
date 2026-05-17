---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 203
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
`EXACT` synonym line instead of updating its text to the new label (human gold
PR #10134 renamed it). F1=0.857 (precision 0.75, recall 1.0) is a fair score:
correct rename, lost ClinGen preferred-label provenance. This run produced no
PR/issue comment (bare diff only), so methodology cannot be assessed beyond the
diff itself; the diff is byte-identical to the other gemma-4-31b attempt (#240).

## Strengths

- Correct `name:` update, matching gold's primary edit after normalization.
- Old label removed everywhere, consistent with the literal reading of the
  requester's instruction.
- Tight scope: definition, subsets, GARD:0028187 xref, MONDO:0017979
  parentage/equivalence, and gene/predisposition axioms untouched. No
  collateral edits.

## Issues

- **Missed requirement (provenance loss):** deleted the
  `synonym: "..." EXACT [...clingen...] {OMO:0002001=".../clingen"}` line rather
  than rewriting it to the new label. That entry encodes ClinGen's
  preferred-label attribution, not just the old name; gold preserves it by
  renaming it. Deleting it discards ClinGen preferred-label provenance.
- No PR comment or issue comment was generated, so there is no evidence of
  research, validation, or rationale; the workflow steps cannot be verified.
- Needs curator correction before merge, hence partial success.
