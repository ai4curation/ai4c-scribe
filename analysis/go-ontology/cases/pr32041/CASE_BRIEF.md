---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31902
pr_number: 32041
issue_title: 'NTR: [venom-mediated inflammatory response+... leukocyte infiltration+...
  release of inflammatory mediator]'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-07'
task_type: new_term
difficulty: medium
scoping: loosely_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
best_f1: 0.9
best_model: claude-opus-4.7
---

# PR #32041 — NTR: [venom-mediated inflammatory response+... leukocyte infiltration+... release of inflammatory mediator]

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31902](https://github.com/geneontology/go-ontology/issues/31902) | [PR #32041](https://github.com/geneontology/go-ontology/pull/32041) | @dragon-ai-agent | merged 2026-05-07

`new_term` `medium` `loosely_scoped` `approved_first_time`

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

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 7aec1566d..c8728f302 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -617485,6 +617485,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-05-06T17:36:35Z
 
+[Term]
+id: GO:7770071
+name: venom-mediated activation of inflammatory response
+namespace: biological_process
+def: "A process by which an organism causes inflammatory response in another organism via the action of a venom." [PMID:19000915, PMID:32024243]
+synonym: "venom-mediated inflammation" BROAD []
+synonym: "envenomation resulting in positive regulation of inflammatory response in another organism" EXACT []
+intersection_of: GO:0035738 ! venom-mediated perturbation of biological process
+intersection_of: positively_regulates_in_another_organism GO:0006954 ! inflammatory response
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31902" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-07T07:41:13Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.900 | 0.900 | 0.900 | `431c018` | [#332](https://github.com/ai4curation/eval-ont-agent-go/pull/332) | [attempt](attempts/pr332.md) |
| 2 | gpt-5.5 | opencode | 0.842 | 0.800 | 0.889 | `712a235` | [#107](https://github.com/ai4curation/eval-ont-agent-go/pull/107) | [attempt](attempts/pr107.md) |
| 3 | gpt-5.5 | opencode | 0.842 | 0.800 | 0.889 | `712a235` | [#88](https://github.com/ai4curation/eval-ont-agent-go/pull/88) | [attempt](attempts/pr88.md) |
| 4 | gpt-5.5 | codex | 0.842 | 0.800 | 0.889 | `d08b5d9` | [#69](https://github.com/ai4curation/eval-ont-agent-go/pull/69) | [attempt](attempts/pr69.md) |
| 5 | claude-sonnet-4.5 | claude | 0.778 | 0.700 | 0.875 | `1bdc654` | [#468](https://github.com/ai4curation/eval-ont-agent-go/pull/468) | [attempt](attempts/pr468.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.778 | 0.700 | 0.875 | `bf06cbb` | [#384](https://github.com/ai4curation/eval-ont-agent-go/pull/384) | [attempt](attempts/pr384.md) |
| 7 | claude-haiku-4.5 | claude | 0.593 | 0.800 | 0.471 | `7d7fccb` | [#205](https://github.com/ai4curation/eval-ont-agent-go/pull/205) | [attempt](attempts/pr205.md) |
| 8 | kimi-k2.6 | opencode | 0.581 | 0.900 | 0.429 | `f011d7e` | [#287](https://github.com/ai4curation/eval-ont-agent-go/pull/287) | [attempt](attempts/pr287.md) |
| 9 | gpt-5.4 | codex | 0.533 | 0.800 | 0.400 | `6a14820` | [#179](https://github.com/ai4curation/eval-ont-agent-go/pull/179) | [attempt](attempts/pr179.md) |
| 10 | gpt-5.4 | opencode | 0.444 | 0.600 | 0.353 | `2e49a23` | [#673](https://github.com/ai4curation/eval-ont-agent-go/pull/673) | [attempt](attempts/pr673.md) |
| 11 | gpt-5.4 | opencode | 0.444 | 0.600 | 0.353 | `2e49a23` | [#626](https://github.com/ai4curation/eval-ont-agent-go/pull/626) | [attempt](attempts/pr626.md) |
