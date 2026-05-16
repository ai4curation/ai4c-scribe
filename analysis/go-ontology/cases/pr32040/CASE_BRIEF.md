---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31295
pr_number: 32040
issue_title: 'NTR: p24 cargo receptor complex'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-06'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
best_f1: 0.75
best_model: claude-opus-4.7
---

# PR #32040 — NTR: p24 cargo receptor complex

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31295](https://github.com/geneontology/go-ontology/issues/31295) | [PR #32040](https://github.com/geneontology/go-ontology/pull/32040) | @dragon-ai-agent | merged 2026-05-06

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for `p24 cargo receptor complex` (GO:7770070), a cellular component term needed for GO-CAM annotation of vesicle-mediated transport pathways. The p24 family forms hetero-oligomeric complexes that cycle between the ER and Golgi, selectively recruiting GPI-anchored proteins and other secretory cargo into COPII vesicles. The issue was tagged "Needed for GO-CAM" and "vesicle-mediated-transport", indicating it was blocking functional annotation work.

## Changes Made

The PR added GO:7770070 as a child of `GO:0062137 cargo receptor complex`. The definition describes the hetero-oligomeric (typically tetrameric) nature of the complex, its cycling between ER and Golgi, and its role in selectively recruiting GPI-anchored proteins into COPII vesicles. The term required two commits, suggesting a minor revision was needed after the initial submission.

## Resolution

Despite the issue being open since January 2026, the PR was created and merged in May, reflecting the backlog of new term requests. The 2-commit history suggests a small correction was needed. Medium difficulty because the definition needed to accurately capture the composition and functional role of p24 complexes in vesicular transport, and the parent term placement under `cargo receptor complex` rather than a more specific transport complex class required domain knowledge.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 7d228a566..7aec1566d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -617470,6 +617470,21 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-29T15:27:39Z
 
+[Term]
+id: GO:7770070
+name: p24 cargo receptor complex
+namespace: cellular_component
+def: "A conserved, hetero-oligomeric (often tetrameric) cycling ER-Golgi protein complex that selectively recruits secretory cargo, especially GPI-anchored proteins, into COPII vesicles and helps maintain early secretory pathway organization. A functional p24 complex typically contains one member of each subfamily of p24 proteins, alpha, beta, gamma and delta." [PMID:19566487, PMID:26224213, PMID:27569046, PMID:32456004, PMID:34647572]
+synonym: "p24 complex" EXACT []
+synonym: "Emp24-Erv25 complex" RELATED []
+synonym: "p24 family complex" RELATED []
+synonym: "TMED complex" RELATED []
+is_a: GO:0062137 ! cargo receptor complex
+relationship: capable_of_part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediated transport
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31295" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-06T17:36:35Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.750 | 0.750 | 0.750 | [#327](https://github.com/ai4curation/eval-ont-agent-go/pull/327) | [attempt](attempts/pr327.md) |
| 2 | claude-sonnet-4.5 | claude | 0.700 | 0.583 | 0.875 | [#466](https://github.com/ai4curation/eval-ont-agent-go/pull/466) | [attempt](attempts/pr466.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.700 | 0.583 | 0.875 | [#389](https://github.com/ai4curation/eval-ont-agent-go/pull/389) | [attempt](attempts/pr389.md) |
| 4 | gpt-5.4 | codex | 0.700 | 0.583 | 0.875 | [#173](https://github.com/ai4curation/eval-ont-agent-go/pull/173) | [attempt](attempts/pr173.md) |
| 5 | gpt-5.5 | opencode | 0.696 | 0.667 | 0.727 | [#93](https://github.com/ai4curation/eval-ont-agent-go/pull/93) | [attempt](attempts/pr93.md) |
| 6 | gpt-5.5 | opencode | 0.696 | 0.667 | 0.727 | [#87](https://github.com/ai4curation/eval-ont-agent-go/pull/87) | [attempt](attempts/pr87.md) |
| 7 | kimi-k2.6 | opencode | 0.636 | 0.583 | 0.700 | [#261](https://github.com/ai4curation/eval-ont-agent-go/pull/261) | [attempt](attempts/pr261.md) |
| 8 | claude-haiku-4.5 | claude | 0.636 | 0.583 | 0.700 | [#196](https://github.com/ai4curation/eval-ont-agent-go/pull/196) | [attempt](attempts/pr196.md) |
| 9 | gpt-5.5 | opencode | 0.636 | 0.583 | 0.700 | [#111](https://github.com/ai4curation/eval-ont-agent-go/pull/111) | [attempt](attempts/pr111.md) |
| 10 | gpt-5.5 | opencode | 0.636 | 0.583 | 0.700 | [#105](https://github.com/ai4curation/eval-ont-agent-go/pull/105) | [attempt](attempts/pr105.md) |
| 11 | gpt-5.5 | codex | 0.636 | 0.583 | 0.700 | [#74](https://github.com/ai4curation/eval-ont-agent-go/pull/74) | [attempt](attempts/pr74.md) |
| 12 | gpt-5.5 | codex | 0.636 | 0.583 | 0.700 | [#70](https://github.com/ai4curation/eval-ont-agent-go/pull/70) | [attempt](attempts/pr70.md) |
