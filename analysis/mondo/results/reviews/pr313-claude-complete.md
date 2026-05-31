---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 313
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes: [wrong_pattern, missed_requirement, instruction_violation, syntax_error]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a second Haiku-4.5 run on issue #9938 and produces a diff byte-identical to pr426 (blob
`3f293b0`). Gold PR #10221 added the ClinGen string as an EXACT synonym (with
`{OMO:0002001=...clingen}` qualifier) plus a `term_tracker_item`, keeping the primary label
`myofibrillar myopathy 4`. The agent **renamed** the term, did not preserve the old label as a
synonym, and added two non-standard property_value lines. F1=0 is accurate; the rename is the
destructive change the curator explicitly avoided. The exact reproduction across pr426/pr313 shows
this failure is deterministic for Haiku-4.5 on this case, not run-to-run noise.

## Strengths

- Identified the correct target term (MONDO:0012277) and the requested string.
- Recognized that attribution and an issue reference were called for (correct intent, wrong
  execution).

## Issues

- **Wrong pattern / instruction violation (primary)**: Renamed the term rather than adding a
  ClinGen-qualified synonym, contrary to the curator's explicit decision and the config's
  "ClinGen Label Handling" guidance.
- **Missed requirement**: Original label "myofibrillar myopathy 4" was not retained as a synonym,
  so the rename destroys the established label; the requested ClinGen synonym was never added.
- **Non-standard / mistyped metadata**: Raw `dcterms:contributor` term-level property instead of
  Mondo nano-attribution convention; `IAO:0000233 ... xsd:string` uses the wrong datatype (gold
  uses `xsd:anyURI`).
- No agent PR/issue comment captured for this run, so methodology cannot be assessed beyond the
  diff — but the diff alone shows the same wrong approach as pr426.
