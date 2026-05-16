---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31966
pr_number: 32003
issue_title: Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 1.0
best_model: gpt-5.4
---

# PR #32003 — Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31966](https://github.com/geneontology/go-ontology/issues/31966) | [PR #32003](https://github.com/geneontology/go-ontology/pull/32003) | @dragon-ai-agent | merged 2026-04-28

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #31966 requested obsoletion of GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity". Per @sjm41's analysis, this term had no direct EC cross-reference, but "(R)-2-hydroxyisocaproate dehydrogenase" is listed as a synonym of EC:1.1.1.345, which corresponds to GO:0140175 "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity". The specific substrate (isocaproate) is just one instance of the broader (2R)-2-hydroxyacid class.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0043713 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0140175` for annotation migration
- Removed logical axioms
- The replacement points annotators to the correct broader activity term

## Resolution

Merged directly. The biochemical reasoning was clearly laid out in the issue: the specific substrate term (isocaproate) is subsumed by the generic substrate class term ((2R)-2-hydroxyacid). This is a typical enzyme term consolidation where overly specific terms are replaced by appropriately general ones that match EC classification granularity.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..55fadafbd 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. "(R)-2-hydroxyisocaproate dehydrogenase" is a synonym of EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase (NAD+)), which is the exact match xref of GO:0140175. The reaction catalyzed (involving (R)-2-hydroxy-4-methylpentanoate / 2-oxoisocaproate, RHEA:10052) is a narrowMatch instance of the more general reaction in GO:0140175.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | [#189](https://github.com/ai4curation/eval-ont-agent-go/pull/189) | [attempt](attempts/pr189.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.889 | 0.889 | 0.889 | [#502](https://github.com/ai4curation/eval-ont-agent-go/pull/502) | [attempt](attempts/pr502.md) |
| 3 | claude-sonnet-4.5 | claude | 0.889 | 0.889 | 0.889 | [#477](https://github.com/ai4curation/eval-ont-agent-go/pull/477) | [attempt](attempts/pr477.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.889 | 0.889 | 0.889 | [#430](https://github.com/ai4curation/eval-ont-agent-go/pull/430) | [attempt](attempts/pr430.md) |
| 5 | claude-opus-4.7 | claude | 0.889 | 0.889 | 0.889 | [#340](https://github.com/ai4curation/eval-ont-agent-go/pull/340) | [attempt](attempts/pr340.md) |
| 6 | kimi-k2.6 | opencode | 0.889 | 0.889 | 0.889 | [#275](https://github.com/ai4curation/eval-ont-agent-go/pull/275) | [attempt](attempts/pr275.md) |
| 7 | gemma-4-31b | opencode | 0.889 | 0.889 | 0.889 | [#246](https://github.com/ai4curation/eval-ont-agent-go/pull/246) | [attempt](attempts/pr246.md) |
| 8 | claude-haiku-4.5 | claude | 0.889 | 0.889 | 0.889 | [#213](https://github.com/ai4curation/eval-ont-agent-go/pull/213) | [attempt](attempts/pr213.md) |
| 9 | gpt-5.5 | opencode | 0.889 | 0.889 | 0.889 | [#161](https://github.com/ai4curation/eval-ont-agent-go/pull/161) | [attempt](attempts/pr161.md) |
| 10 | gpt-5.5 | opencode | 0.889 | 0.889 | 0.889 | [#141](https://github.com/ai4curation/eval-ont-agent-go/pull/141) | [attempt](attempts/pr141.md) |
| 11 | gpt-5.5 | codex | 0.889 | 0.889 | 0.889 | [#125](https://github.com/ai4curation/eval-ont-agent-go/pull/125) | [attempt](attempts/pr125.md) |
