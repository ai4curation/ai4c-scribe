---
repo: obophenotype/cell-ontology
issue_number: 3332
pr_number: 3333
issue_title: "Re-labelling of imported annotation properties in the -edit file"
issue_created_at: "2025-09-16"
issue_closed_at: "2025-09-17"
pr_author: gouttegd
pr_merged_at: "2025-09-17"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 32
    deletions: 92
scoping: mostly_scoped
scoping_notes: >-
  Primarily removes redundant labels but also adds SPARQL-based annotations to prevent
  future regressions, which goes slightly beyond the original issue scope.
task_type: bulk_edit
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - annotation-properties
  - import-management
  - SPARQL
  - cleanup
  - regression-prevention
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale cleanup with net 60-line reduction plus preventive measures, demonstrating ontology import hygiene
case_quality: poor
case_quality_reason: gold_out_of_scope_reserialization_artifact
companion_prs: []
scoring_caveat: >-
  metadiff vs #3333 is artificially capped at F1 ~0.41-0.43 for all attempts.
  Only ~12 of the gold's 92 deletions (plus their comment headers/blank lines,
  ~36 deletion lines total) implement the actual ask of issue #3332 (removing
  redundant rdfs:label axioms on imported annotation properties). The remaining
  ~56 lines (32 of the additions + ~24 deletions) are a one-time
  re-serialization that relocates the misplaced CL_4072027, CL_7770002, and
  CL_7770005 class blocks and reorders Declaration(Class(...)) lines to
  canonical sorted positions. The PR author states explicitly in the PR body
  that this is a "side-effect ... needed because a previous AI-generated change
  inserted a class at the wrong place" — i.e. cleanup of a PRIOR PR, unrelated
  to #3332 and not inferable from the issue. No agent can or should reproduce
  it. Judge attempts against the issue text + the issue-relevant gold hunk
  only; the metadiff under-represents quality by roughly 2x for the strong
  attempts.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The cell ontology edit file had accumulated many redundant `rdfs:label` annotations for annotation properties that are already labeled in the imported modules (e.g., oboInOwl properties, IAO properties). These redundant labels cause confusion for contributors who may think they need to maintain them, and can mask the canonical labels from imports.

## Changes Made

Removed 92 lines of redundant annotation property labels from `cl-edit.owl` and added 32 lines of replacement content including SPARQL-based annotations to help detect future re-introduction of these labels. The net effect is a 60-line reduction in the edit file.

## Resolution

Approved on first review despite a dismissed review comment. Medium difficulty because the change requires understanding the OWL import chain to identify which labels are redundant versus essential, and adding preventive measures requires knowledge of SPARQL-based quality checking in OBO ontology workflows.

## Curation Note (data quality)

**Flagged poor on 2026-05-16 by claude-opus-4.7 during agent-attempt review.**

Issue #3332 asks for one thing only: remove the redundant `rdfs:label`
AnnotationAssertion axioms that CL locally restates for imported annotation
properties (the maintainer matentzn confirmed: "you are totally right in your
assessment"). The selected gold PR #3333 resolves this issue (no companion PRs;
#3547 and #3589 are unrelated later recurrences), but it **bundles a large
out-of-scope re-serialization**. Quantified from `gh pr diff 3333`:

- Issue-relevant: 12 `AnnotationAssertion(rdfs:label …)` removals on imported
  IAO/oboInOwl/`rdfs:seeAlso` APs, plus their now-empty ROBOT comment
  headers/blank lines (~36 deletion lines).
- Out of scope: ~56 lines that **move** the misplaced `CL_4072027`,
  `CL_7770002`, and `CL_7770005` class blocks and reorder
  `Declaration(Class(...))` lines into canonical OFN sort order. All 32 of the
  gold's *additions* are this churn (relocated class text). The PR body states
  verbatim that this is a "side-effect ... needed because a previous
  AI-generated change inserted a class at the wrong place" — it cleans up a
  *prior* PR and is unrelated to and not inferable from #3332.

Consequence: every one of the 7 agent attempts that correctly and completely
solves #3332 is capped at F1 ≈ 0.41–0.43 (P=0.300) purely because it cannot
reproduce an unrelated, undocumented serialization artifact. The metadiff
**under-represents quality by roughly 2x** for the strong attempts (pr204,
pr177, pr93, pr60, pr42, pr75 — all `success` on the issue). The genuine
quality differentiator is invisible to metadiff: pr20 (gpt-5.5/codex) is the
only attempt with a real defect — it deleted the label axioms but left ~16
orphaned `# Annotation Property:` header comments behind (`partial_success`,
`under_editing`), which would itself reintroduce the spurious-diff problem the
issue targets.

Recommendation for downstream scoring: down-weight or exclude the raw metadiff
for this case; treat pr204/pr177/pr93/pr60/pr42/pr75 as successes and pr20 as
partial. Do not treat the uniform ~0.41 F1 as agent failure.
