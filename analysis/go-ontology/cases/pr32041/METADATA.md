---
repo: geneontology/go-ontology
issue_number: 31902
pr_number: 32041
issue_title: "NTR: [venom-mediated inflammatory response+... leukocyte infiltration+... release of inflammatory mediator]"
issue_created_at: "2026-04-15"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-07"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 13
    deletions: 0
scoping: loosely_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: NTR from the venom biology domain with inter-organism process semantics; only one of the three requested terms was created in this PR
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32048, 32049, 32055]
scoring_caveat: "metadiff vs #32041 only covers the deliberately scoped first sub-step (parent term GO:7770071). Issue #31902 requested 4 things; the human resolved it across #32041 (parent, merged) + #32055 (children GO:7770075/GO:7770076, merged; #32048/#32049 superseded), and dropped the GO:0044480 reparenting. Judge attempts against the issue plus the union of #32041+#32055, not against #32041 alone."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A new term request from a UniProt curator asked for several venom-related biological process terms, including venom-mediated activation of inflammatory response, leukocyte infiltration, and release of inflammatory mediator. These terms are needed to annotate venom toxin proteins that trigger inflammatory cascades in envenomated organisms. The issue referenced PMID:19000915 and PMID:32024243 as supporting literature.

## Changes Made

The PR added GO:7770071 `venom-mediated activation of inflammatory response` as a biological process term. The definition captures the inter-organism nature of envenomation: one organism causes inflammatory response in another organism via venom action. The term includes both a broad synonym (`venom-mediated inflammation`) and an exact synonym using the standard GO inter-organism phrasing (`envenomation resulting in positive regulation of inflammatory response in another organism`).

## Resolution

This PR addressed only one of the three terms requested in the issue, making it partially scoped relative to the full request. The single-term approach is appropriate for incremental ontology development, allowing each term to be reviewed independently. Medium difficulty because the definition required careful framing of inter-organism process semantics, which follow specific GO conventions for processes that span two organisms.

## Curation Note (data quality)

`case_quality: poor` — the gold `pr_number` (#32041) is only the **first, deliberately scoped sub-step** of a multi-PR human resolution, so the metadiff F1 systematically penalizes attempts that correctly did more of the issue.

Issue #31902 (verified via `gh issue view`) requested **four** things in its body:
1. parent term `venom-mediated activation of inflammatory response`
2. child `venom-mediated leukocyte infiltration`
3. child `venom-mediated release of inflammatory mediator`
4. add `part_of` the new parent to existing GO:0044480 `venom-mediated mast cell degranulation`

The human resolution was split across PRs, driven by @pgaudet's in-issue comments:
- **#32041** (merged, the gold) — adds only the parent term `GO:7770071`, in response to @pgaudet's first comment that explicitly narrowed scope to just that term.
- **#32048** / **#32049** (closed, superseded) — first attempts at the two child terms (GO:7770072/GO:7770073).
- **#32055** (merged) — the final child terms `GO:7770075 venom-mediated leukocyte infiltration` and `GO:7770076 venom-mediated release of inflammatory mediator`, each with `intersection_of: GO:7770071` + `positively_regulates_in_another_organism` (GO:0002523 / GO:0002532).
- Ask #4 (reparent GO:0044480) was **explicitly dropped** by @pgaudet and never implemented.

Implications for scoring:
- The gold #32041 is a *legitimate, well-scoped* target for the first curator request, and its key differentiator from most attempts is the EXACT synonym `envenomation resulting in positive regulation of inflammatory response in another organism`. Single-term attempts (#332, #107, #88, #69, #468, #384) that scoped to the parent term per the comment are correctly scoped and score reasonably (0.78–0.90).
- Multi-term attempts (#205 kimi-via-haiku-slot, #287 kimi, #179 gpt-5.4) acted on the full original issue body and are penalized to F1 ≈ 0.53–0.59 **despite substantively anticipating the human's eventual companion work (#32055)**. For these, F1 materially under-represents quality; #287 in particular is the most issue-complete and the closest parent-term match yet scores 0.581.
- Eval base state (`eval-base-issue-31902` @ ada3c56) was checked and is **clean** — no GO:7770071 and GO:0044398 still has its original `is_a: GO:0035738`; there is no base-state contamination.

Recommendation: when aggregating, judge attempts against the issue + the union of #32041 and #32055, and down-weight/annotate the raw metadiff for this case. `quality_flagged_by: claude-opus-4.7` on 2026-05-15.
