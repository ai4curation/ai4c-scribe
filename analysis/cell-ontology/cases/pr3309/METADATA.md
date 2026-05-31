---
repo: obophenotype/cell-ontology
issue_number: 2967
pr_number: 3309
issue_title: "T follicular helper cell logical definition using obsolete term"
issue_created_at: "2025-02-13"
issue_closed_at: "2025-09-09"
pr_author: gouttegd
pr_merged_at: "2025-09-09"
pr_num_commits: 1
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - logical-definition
  - obsolete-term
  - GO-reference
  - T-cell
  - follicular-helper
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal single-line fix replacing an obsolete GO term reference in a logical definition
case_quality: poor
case_quality_reason: metadiff_conjunct_reorder_artifact
companion_prs: []
scoring_caveat: "All 8 attempts made the semantically correct edit (GO:0051024 -> GO:0002639 in the CL:0002038 EquivalentClasses axiom). F1 caps at 0.500 (0.333 for codex runs) purely because the gold serialization sorts the two commutative RO_0002215 conjuncts (GO_0002639 before GO_0045830) while agents do literal text substitution (GO_0045830 first); ObjectIntersectionOf is order-independent so the axioms are logically identical. Codex runs are additionally penalized by an incidental EOF-newline normalization hunk. Judge against semantic equivalence, not line match: every attempt is a success."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
---

## Context

The logical definition of T follicular helper cell referenced a deprecated GO class. When GO obsoletes a term, downstream ontologies that use it in logical axioms must update their references to the replacement term. This is a common maintenance task in the OBO ecosystem.

## Changes Made

Changed a single GO term reference in `cl-edit.owl`, replacing the obsolete GO class with its active replacement in the logical definition of T follicular helper cell. One line added, one line removed.

## Resolution

Approved on first review in a single commit. Simple difficulty because the fix is mechanical: identify the obsolete term, find its replacement, and update the reference. However, this case illustrates an important pattern for agents working with OBO ontologies: they must be able to detect and resolve obsolete cross-ontology references.

## Curation Note (data quality)

`case_quality: poor` — flagged because the metadiff score systematically
under-represents agent quality on this case (a scoring artifact, not a gold
defect; the gold PR #3309 is correct, single, and complete — issue #2967's only
actionable ask was the specific term replacement, with @addiehl twice
recommending `GO:0051024` → `GO:0002639`; the broader release-time
`deprecated_class_reference` check discussed in the thread was never converted
to a CL PR and was explicitly out of scope, exactly as gouttegd scoped #3309).

**The artifact:** The gold `EquivalentClasses(CL:0002038 ...)` axiom serializes
its two `ObjectSomeValuesFrom(obo:RO_0002215 ...)` conjuncts in sorted order —
`GO_0002639` before `GO_0045830` — because the editing tool/ROBOT normalizes
conjunct order. All 8 agents performed a literal in-place text substitution of
`GO_0051024` → `GO_0002639`, leaving the order as `GO_0045830` then
`GO_0002639`. `ObjectIntersectionOf` is commutative, so the agent and gold
axioms are **logically identical**; the line-based metadiff nonetheless scores
the changed line as a mismatch, capping F1 at **0.500** (claude/opencode runs)
and **0.333** (codex runs, additionally hit by an incidental EOF-newline
normalization producing a spurious second hunk).

**Consequence for scoring/aggregation:** All 8 attempts (claude-sonnet-4.5,
claude-opus-4.7, claude-haiku-4.5, gemma-4-31b, gpt-5.5 ×2 opencode, gpt-5.4 &
gpt-5.5 codex) are substantively **success** — every one produced the correct
biological fix with tight scope. The recorded F1 values (`best_f1: 0.5`) should
be treated as a serialization floor, not a quality signal; downstream scoring
should down-weight or exclude this case, or compare on logical/normalized-axiom
equivalence rather than line diff. A ROBOT-normalized comparison would yield
F1 ≈ 1.0 for the 6 non-codex attempts.
