---
ontology: cell-ontology
issue_number: 3588
pr_number: 3589
eval_repo_pr: 594
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
case_quality: ok
case_quality_reason: metadiff_underrepresents_defensible_scope_and_mechanism_difference
f1: 0.585
precision: 0.632
recall: 0.545
jaccard: 0.414
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode correctly diagnosed the root cause and cleanly removed all 9
redundant `AnnotationAssertion(rdfs:label oboInOwl:...)` axioms (with their
`# Annotation Property:` comment headers) from `cl-edit.owl`, but satisfied
the issue's mandatory "must have a check to prevent them from being ever
injected again" requirement only with a prose note in
`docs/annotation_properties.md` rather than an enforced build guard. F1=0.585
(P=0.632, R=0.545) modestly under-represents the cleanup half (the broader
9-label removal vs. gold's `has*`-only scope is the defensible divergence
noted in METADATA), but the metadiff does not penalize the genuinely missing
half: no automated regression guard exists in this attempt.

## Strengths

- Correct root-cause diagnosis matching the issue author's stated rationale:
  recognized the labels are supplied by the merged import module and that
  `oboInOwl:hasDbXref` in particular has conflicting imported labels causing
  unstable serialization-order diffs.
- Clean, idiomatic removal: deleted the comment header + assertion pair for
  each property, matching gold's deletion style. No leftover cruft; the
  `cl-edit.owl` change is byte-clean (blob `5148134` / `ad5669e0a`).
- The broader 9-property removal (including `SubsetProperty`, `consider`,
  `inSubset`) is the defensible/arguably-superior scope described in the
  METADATA scoring caveat — these are standard oboInOwl properties labelled
  in the oboInOwl import, so removing them is very likely correct.
- The agent explicitly reasoned about the eval-repo edit constraints
  (`src/ontology/cl-edit.owl` or `docs/` only) and chose docs accordingly —
  honest about the tradeoff rather than silently skipping the guard.

## Issues

- **Missed requirement (the enforced guard)**: the issue explicitly states
  "we must have a check to prevent them from being ever injected again." The
  gold added an executable `no_relabeling_imported_ap` grep target wired into
  `test` in the hand-maintained `cl.Makefile`. This attempt's only preventive
  measure is a sentence in `docs/annotation_properties.md`, which is not
  machine-enforced and will not fail CI on regression — exactly the failure
  mode (#3333, #3547, #3522) the issue was filed to stop. Sibling attempts
  #557/#497 (gpt-5.5) did add a real `cl.Makefile` grep guard, showing the
  durable approach was achievable under the same constraints. This is the
  decisive gap separating this attempt from `success`.
- Spurious final-newline flip on the last `SubClassOf(...)` line
  (`\ No newline at end of file` → newline added). Harmless and common across
  all attempts, but a minor unintended byte change.
- Scope-vs-gold note (not an error): removed 9 labels where gold removed 6;
  this is the defensible divergence covered by the case scoring caveat and
  does not count against the agent on substance.
