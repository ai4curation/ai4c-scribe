---
ontology: cell-ontology
issue_number: 3588
pr_number: 3589
eval_repo_pr: 497
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
case_quality: ok
case_quality_reason: metadiff_underrepresents_defensible_scope_and_mechanism_difference
f1: 0.583
precision: 0.737
recall: 0.483
jaccard: 0.412
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode produced a diff byte-identical to its sibling attempt #557
(blob `ad5669e`): all 9 redundant `AnnotationAssertion(rdfs:label
oboInOwl:...)` axioms (plus comment headers) removed from `cl-edit.owl`, and
an executable `test_no_oboInOwl_labels` grep guard added to the
hand-maintained `src/ontology/cl.Makefile` and wired into the custom `test`
target. This fully resolves the issue's two explicit asks (remove the labels;
have a check to prevent re-injection). F1=0.583 (P=0.737, R=0.483)
substantially **under-represents** quality — same guard mechanism, same
durable file as gold; the recall gap is only the defensible 9-vs-6 scope and
the broader grep pattern, both robustness improvements.

## Strengths

- Correct root-cause diagnosis aligned with the issue author's rationale
  (imported labels; `oboInOwl:hasDbXref` conflicting labels → unstable
  serialization diffs).
- Clean removal of all 9 comment-header + assertion pairs; byte-clean
  `cl-edit.owl`.
- **Enforced, durable guard in the right place**: check added to the
  hand-maintained `src/ontology/cl.Makefile` (survives ODK regen) and wired
  into `test`, directly paralleling gold's `no_relabeling_imported_ap`
  target. This is precisely what #594/#534/#293 missed.
- Guard more robust than gold's: matches all `oboInOwl:*` relabelling, prints
  offending lines, emits a clear error, `exit 1`s, `.PHONY`-declared —
  consistent with the agent's broader (defensible) removal scope.
- Highest-precision tier in the cohort (0.737); tightly scoped, no extraneous
  files.
- Deterministic/reproducible: identical to #557, indicating a well-grounded
  rather than lucky solution.

## Issues

- No substantive issues. The 9-vs-6 scope and broader grep are the
  defensible/arguably-superior divergence in the METADATA scoring caveat, not
  errors; the guard correctly matches the agent's own removal scope and is
  more future-proof than gold's `has*`-only grep.
- Minor cosmetic trailing-newline flip on the final `SubClassOf(...)` line
  (present in all attempts).
