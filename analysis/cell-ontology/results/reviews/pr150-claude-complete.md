---
ontology: cell-ontology
issue_number: 3588
pr_number: 3589
eval_repo_pr: 150
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.453
precision: 0.632
recall: 0.353
jaccard: 0.293
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-haiku-4.5/claude correctly diagnosed the issue and removed all 9
redundant `rdfs:label` oboInOwl assertions, plus added a working SPARQL
violation check wired into `SPARQL_VALIDATION_CHECKS`. The core task is solved,
but unlike the opus and sonnet attempts it did **not** delete the
`# Annotation Property: ...` comment headers — instead it rewrote each header
to a stripped form (e.g. `# Annotation Property: oboInOwl:SubsetProperty`),
leaving editorial cruft and producing extra non-gold lines. The F1 of 0.453
under-represents the substantive correctness but the comment-rewrite is a
genuine (if minor) quality defect that distinguishes this attempt from the
cleaner opus run.

## Strengths

- Correct diagnosis and clear PR write-up: explained the redundant-label and
  conflicting-label (`hasDbXref`) rationale accurately, and cited the
  regression history (#3333, #3547, #3522).
- Removed all 9 spurious `AnnotationAssertion(rdfs:label oboInOwl:...)` lines,
  fully addressing the issue's primary ask.
- Idiomatic SPARQL guard: created
  `src/sparql/illegal-oboInOwl-labels-violation.sparql` following the
  `*-violation.sparql` convention and added `illegal-oboInOwl-labels` to
  `SPARQL_VALIDATION_CHECKS`. Uses a robust `STRSTARTS` namespace filter (no
  hardcoded list), the same robust approach as the opus attempt.

## Issues

- **Wrong pattern / editorial cruft**: instead of deleting the comment headers
  along with the assertions (gold's style, opus/sonnet's style), it kept and
  rewrote each header to `# Annotation Property: oboInOwl:<name>` with the
  human-readable parenthetical stripped. This leaves orphan comment blocks for
  properties that no longer have any axiom in the edit file — noise that the
  gold removed. This is the main reason its recall (0.353) sits below opus.
- **Over-editing (scope vs. gold)**: like the other attempts, removed
  `oboInOwl:SubsetProperty`, `consider`, and `inSubset` labels that the gold
  deliberately kept (gold scoped to `oboInOwl:has*`). Very likely correct in
  substance, but broader than the gold and not explicitly verified against the
  merged import.
- **Wrong file for build edit (style/durability)**: added the check to the
  ODK-generated `src/ontology/Makefile` rather than `cl.Makefile` /
  `cl-odk.yaml`; functional but vulnerable to ODK `update_repo` regeneration.
