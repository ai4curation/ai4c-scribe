---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 295
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes: [wrong_pattern, missed_requirement, syntax_error, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Gold PR #10221 added the ClinGen string as an EXACT synonym (with `{OMO:0002001=...clingen}`
qualifier and ORCID/affiliation attribution) plus a `term_tracker_item`, keeping the primary label
`myofibrillar myopathy 4`. This Gemma attempt **renamed** the term, added the old label back as a
synonym with the *wrong* source (the GitHub issue URL instead of OMIM or ClinGen attribution), and
crucially **inserted the synonym line in the wrong position** — between `name:` and `def:` rather
than in the synonym block. F1=0 is accurate; the result is both the destructive rename the curator
avoided and structurally malformed.

## Strengths

- Identified the correct term (MONDO:0012277) and attempted to preserve the old label rather than
  destroy it (better than the Haiku attempts on that one point).

## Issues

- **Stanza-ordering / syntax error**: The new `synonym:` line was placed immediately after `name:`
  and before `def:`. While OBO is technically tag-order-tolerant, this violates Mondo's serialized
  ordering convention; after `make NORM` the line would move, and as written the diff is not the
  shape any Mondo curator or the normalizer would produce. The agent's checklist claims
  "Normalized and committed changes" — this is false; the diff is unnormalized.
- **Wrong pattern / instruction violation**: Renamed the term, contrary to the curator's explicit
  decision to add the string as a ClinGen Preferred synonym, and contrary to the config's
  "ClinGen Label Handling" section.
- **Missed requirement / wrong source**: The requested synonym
  `"LDB3-related myofibrillar myopathy"` with ClinGen qualifier + ORCID was never added. The old
  label was preserved but cited to the issue URL
  (`synonym: "myofibrillar myopathy 4" EXACT [https://github.com/.../issues/9938]`), which is not a
  valid synonym source — issue URLs belong in `term_tracker_item`, not synonym brackets.
- No `term_tracker_item` (IAO:0000233) added at all.
- Self-reported validation checklist ("Checked for label clashes", "Normalized") does not match
  the actual diff.
