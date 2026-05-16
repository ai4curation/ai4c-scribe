---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 30894
pr_number: 32011
issue_title: 'NTR: [Ferritin-specific autophagy]'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-29'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new term stanza with no unrelated changes.
domain_area: biological_process
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #32011 — NTR: [Ferritin-specific autophagy]

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #30894](https://github.com/geneontology/go-ontology/issues/30894) | [PR #32011](https://github.com/geneontology/go-ontology/pull/32011) | @dragon-ai-agent | merged 2026-04-29

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request (NTR) was filed for "ferritinophagy" — the selective degradation of ferritin via macroautophagy to release iron. This is a well-characterized selective autophagy pathway (PMID:25327288, PMID:26436293) mediated by NCOA4 as the cargo receptor. The issue was open for ~6 months before resolution.

## Changes Made

Added new term GO:7770069 to `src/ontology/go-edit.obo`:

- **ID**: GO:7770069
- **Name**: ferritinophagy
- **Definition**: "The selective degradation of ferritin to release iron by macroautophagy." [PMID:25327288, PMID:26436293, PMID:38714719]
- **Synonym**: "ferritin-specific autophagy" (EXACT)
- **Parent**: is_a GO:0016236 (macroautophagy)
- **Provenance**: Three PMIDs supporting the term, term_tracker_item linking to issue #30894

## Resolution

The key decisions were:
1. **Hierarchy placement**: Under macroautophagy (GO:0016236) rather than generic autophagy, since ferritinophagy is specifically a macroautophagy process
2. **Definition style**: Genus-differentia pattern — "The selective degradation of [cargo] ... by [mechanism]"
3. **Evidence**: Three supporting publications spanning the discovery and characterization of the pathway

Medium difficulty because it requires knowledge of the selective autophagy hierarchy and the specific mechanism (macroautophagy vs other autophagy types). An agent would need to determine the correct parent by understanding that ferritinophagy operates via the macroautophagy machinery.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 37f74ff37..f6a5e38a4 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -617400,6 +617400,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-28T09:37:41Z
 
+[Term]
+id: GO:7770069
+name: ferritinophagy
+namespace: biological_process
+def: "The selective degradation of ferritin to release iron by macroautophagy." [PMID:25327288, PMID:26436293, PMID:38714719]
+synonym: "ferritin-specific autophagy" EXACT []
+is_a: GO:0016236 ! macroautophagy
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30894" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-04-29T15:27:39Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `91a7e00` | [#467](https://github.com/ai4curation/eval-ont-agent-go/pull/467) | [attempt](attempts/pr467.md) |
| 2 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `48014c9` | [#383](https://github.com/ai4curation/eval-ont-agent-go/pull/383) | [attempt](attempts/pr383.md) |
| 3 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `c7b44c4` | [#335](https://github.com/ai4curation/eval-ont-agent-go/pull/335) | [attempt](attempts/pr335.md) |
| 4 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | `e423c26` | [#255](https://github.com/ai4curation/eval-ont-agent-go/pull/255) | [attempt](attempts/pr255.md) |
| 5 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `3014c59` | [#194](https://github.com/ai4curation/eval-ont-agent-go/pull/194) | [attempt](attempts/pr194.md) |
| 6 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `8686f6f` | [#176](https://github.com/ai4curation/eval-ont-agent-go/pull/176) | [attempt](attempts/pr176.md) |
| 7 | gpt-5.5 | opencode | 0.941 | 1.000 | 0.889 | `fc67f17` | [#102](https://github.com/ai4curation/eval-ont-agent-go/pull/102) | [attempt](attempts/pr102.md) |
| 8 | gpt-5.5 | opencode | 0.941 | 1.000 | 0.889 | `fc67f17` | [#81](https://github.com/ai4curation/eval-ont-agent-go/pull/81) | [attempt](attempts/pr81.md) |
| 9 | gpt-5.5 | codex | 0.941 | 1.000 | 0.889 | `02c093d` | [#55](https://github.com/ai4curation/eval-ont-agent-go/pull/55) | [attempt](attempts/pr55.md) |
