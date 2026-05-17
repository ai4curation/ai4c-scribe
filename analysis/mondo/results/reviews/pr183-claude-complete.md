---
ontology: mondo
issue_number: 9749
pr_number: 10134
eval_repo_pr: 183
agent: std_claude_hai45
model: claude-haiku-4.5
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
`EXACT` synonym line entirely instead of updating its text to the new label
(human gold PR #10134 renamed the synonym). F1=0.857 (precision 0.75, recall
1.0) is a fair reflection: the rename is right; ClinGen preferred-label
provenance was dropped.

## Strengths

- Correct `name:` update, matching gold's primary edit after normalization.
- Old label removed everywhere, consistent with the literal reading of the
  requester's confirmation that the original name need not be kept as a synonym.
- Tight scope, and an unusually thorough PR comment that explicitly enumerated
  the preserved metadata: definition, MONDO:0017979 parentage, FAS gene
  relationship (HGNC:11920), Hodgkin/non-Hodgkin predisposition, subsets
  (gard_rare, rare), creator ORCID, and issue link — all genuinely left intact.
- Methodology: `obo-checkout.pl`/`obo-checkin.pl` workflow; transparently noted
  Docker/NORM unavailable (immaterial for a text swap).

## Issues

- **Missed requirement (provenance loss):** the removed
  `synonym: "FAS-related autoimmune lymphoproliferative syndrome" EXACT
  [https://clinicalgenome.org/affiliation/40157/]
  {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` line
  is ClinGen's preferred-label attribution entry, not just a copy of the old
  name. Gold updates its text to the new label so the ClinGen preferred-label
  attribution remains attached to the current name; deleting it loses that
  provenance. The agent's own "removed the exact synonym for the original term
  name" framing shows it treated the line as disposable rather than recognizing
  the `OMO:0002001` attribution it carries.
- Needs curator correction before merge, hence partial success.
