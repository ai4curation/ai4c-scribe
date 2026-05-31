---
repo: obophenotype/uberon
issue_number: 3473
pr_number: 3494
issue_title: "Not all epithelia with squamous cells are squamous epithelium"
issue_created_at: "2025-02-04"
pr_author: dosumis
pr_merged_at: "2025-03-19"
pr_num_commits: 3
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 15
    deletions: 18
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: epithelial-tissue
tags:
  - definition-refinement
  - squamous-epithelium
  - cell-type
  - classification-logic
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definitional correction requiring nuanced histological understanding of epithelial classification criteria
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "Issue #3473 asks for exactly one substantive change (squamous epithelium has_part→composed_primarily_of, plus 'test/align' downstream). Gold PR #3494's 33-line diff mixes: (a) the in-scope core fix on UBERON:0006914/0000487/0006915/0005099 (~4 lines); (b) reasoner-driven removal of dubious epithelial is_a assertions on endocardium of ventricle (UBERON:0001081), right atrium endocardium (UBERON:0009129) and synovial membrane (UBERON:0002018) (~3 lines) — edits that emerged ONLY from curator histology research and were negotiated in the PR comment thread, not derivable from the issue; and (c) ~11 lines of pure out-of-scope churn: CL label-comment refreshes from upstream term renames (CL:1000271 lung ciliated→lung multiciliated epithelial cell, CL:0002145, CL:0002332, CL:1000223, CL:0000150 glandular epithelial→glandular secretory epithelial cell) and a synonym reordering in hindlimb skin UBERON:0003532, all introduced by a `Merge branch 'master'` commit + ROBOT reserialization. Whole-file metadiff therefore caps F1 at ~0.19 for even a perfectly correct, well-scoped agent. Judge attempts against the issue intent (the has_part→composed_primarily_of repair across the squamous branch), not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3473 identified that the definition of squamous epithelium in Uberon was too broad: not all epithelia containing squamous cells qualify as squamous epithelium. The distinction is histologically significant because transitional epithelium and stratified epithelia may contain squamous cells in their superficial layers without being classified as squamous epithelium proper.

## Changes Made

The PR modified 15 lines and removed 18 lines in uberon-edit.obo, refining the definition and logical axioms for squamous epithelium and related terms. The changes tightened the classification criteria so that the presence of squamous cells alone is insufficient for classification as squamous epithelium, requiring instead that the epithelium be predominantly composed of squamous cells or classified as such by standard histological criteria.

## Resolution

Hard difficulty. An agent would need deep histological knowledge to understand why the original definition was too permissive, distinguish between squamous epithelium proper and epithelia that merely contain squamous cells, and craft logical axioms that correctly capture this distinction without breaking existing classification hierarchies. The three commits over six weeks suggest careful deliberation.

## Curation Note (data quality)

**Flagged poor: `gold_has_out_of_scope_extra_edits` (claude-opus-4.7, 2026-05-16).**

Issue #3473 (no comments; single reporter ask) requests exactly one substantive change: redefine `squamous epithelium` so its differentia uses `composed_primarily_of` instead of `has_part some 'squamous epithelial cell'`, and "test results of change and fix/align". The single resolving PR is #3494 (verified: `gh search prs --repo obophenotype/uberon "3473"` returns only #3494; no companion PRs).

Gold PR #3494's 33-line diff is **not** a clean reflection of the issue. It is a union of three very different kinds of change:

1. **In-scope core fix (~4 lines, predictable from issue):** `has_part CL:0000076` → `composed_primarily_of CL:0000076` on `squamous epithelium` (UBERON:0006914), `simple squamous epithelium` (UBERON:0000487), `stratified squamous epithelium` (UBERON:0006915), and the downstream `short descending thin limb` (UBERON:0005099).
2. **Reasoner-driven curator cleanup (~3 lines, NOT predictable from issue):** removal of `is_a` epithelial assertions on endocardium of ventricle (UBERON:0001081), right atrium endocardium (UBERON:0009129) and synovial membrane (UBERON:0002018). These arose only after the curator ran the reasoner, found "missing autoclassifications", researched synovial/endocardial histology, and negotiated the decision in the PR comment thread (commit "removed epithelia assertions on synovial membrane and endocardium", added the day before merge). No agent working from the issue alone could be expected to produce these.
3. **Pure out-of-scope churn (~11 lines, issue-irrelevant):** CL label-comment refreshes from upstream term renames (CL:1000271 `lung ciliated cell`→`lung multiciliated epithelial cell`; CL:0002145 `ciliated columnar cell`→`multiciliated columnar cell of tracheobronchial tree`; CL:0002332 `ciliated cell of the bronchus`→`multiciliated epithelial cell of the bronchus`; CL:1000223 `lung neuroendocrine cell`→`pulmonary neuroendocrine cell`; CL:0000150 `glandular epithelial cell`→`glandular secretory epithelial cell`) plus a `synonym:` line reordering in hindlimb skin (UBERON:0003532). These entered via the PR's `Merge branch 'master'` commit and ROBOT reserialization — serialization/label-refresh artifacts, not issue work.

Consequently whole-file OBO metadiff caps F1 at ~0.19 even for a perfectly correct, well-scoped agent. Best cohort attempts (codex #80/#73, gpt-5.4/5.5) correctly repaired all three squamous classes and ran ELK validation — substantively near-complete on the issue — yet score F1≈0.18. **All nine attempts should be judged against the issue's actual intent (the `composed_primarily_of` repair across the squamous branch + reasoner testing), not the misleading metadiff.** Downstream scoring/aggregation should down-weight or exclude this case.
