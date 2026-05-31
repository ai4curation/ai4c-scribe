---
ontology: cell-ontology
issue_number: 3588
pr_number: 3589
eval_repo_pr: 557
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

gpt-5.5/opencode fully resolved the issue: it removed all 9 redundant
`AnnotationAssertion(rdfs:label oboInOwl:...)` axioms (with comment headers)
from `cl-edit.owl` and added an executable `test_no_oboInOwl_labels` grep
guard to the **hand-maintained** `src/ontology/cl.Makefile`, wired into the
custom `test` target — mechanically and locationally the closest of any
attempt to the gold's `no_relabeling_imported_ap` guard. F1=0.583 (P=0.737,
R=0.483) substantially **under-represents** quality: this is the same
mechanism in the same durable file as gold; the recall shortfall is purely
the defensible 9-vs-6 label scope and the slightly different (and broader)
grep regex, both of which are robustness improvements, not errors.

## Strengths

- Correct root-cause diagnosis matching the issue author's rationale (imported
  labels; `oboInOwl:hasDbXref` conflicting labels → unstable serialization).
- Clean removal of all 9 comment-header + assertion pairs; byte-clean
  `cl-edit.owl` (blob `ad5669e`).
- **Enforced, durable guard placed correctly**: added the check to
  `src/ontology/cl.Makefile` — the same hand-maintained file the gold edited,
  surviving ODK regeneration — and wired it into `test` exactly as gold wired
  `no_relabeling_imported_ap`. This is the decisive thing #594/#534/#293
  failed to do.
- Guard is more robust than gold's: `grep -n 'AnnotationAssertion(rdfs:label
  oboInOwl:'` catches *all* `oboInOwl:*` relabelling (not just `has*`),
  prints offending lines, emits a clear error message, and `exit 1`s; marked
  `.PHONY`. This generalizes the protection to exactly the broader set the
  agent (defensibly) removed.
- Highest precision in the cohort (0.737), reflecting tightly scoped,
  on-target edits with no extraneous files.

## Issues

- No substantive issues. The 9-vs-6 label scope and the broader grep pattern
  are the defensible/arguably-superior divergence documented in the METADATA
  scoring caveat, not errors — the agent's guard correctly matches its own
  (broader) removal scope, which is internally consistent and more future-proof
  than gold's `has*`-only grep that the author called "admittedly very crude."
- Minor: spurious trailing-newline flip on the last `SubClassOf(...)` line
  (present across all attempts); cosmetic only.
