---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31961
pr_number: 32015
issue_title: obsolete GO:0008785 alkyl hydroperoxide reductase activity
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-29'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 23
generated_at: '2026-05-15'
scoping_notes: All changes directly address the obsoletion of the single term GO:0008785.
domain_area: molecular_function
best_f1: 0.8
best_model: claude-sonnet-4.5
---

# PR #32015 — obsolete GO:0008785 alkyl hydroperoxide reductase activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31961](https://github.com/geneontology/go-ontology/issues/31961) | [PR #32015](https://github.com/geneontology/go-ontology/pull/32015) | @dragon-ai-agent | merged 2026-04-29

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

GO:0008785 "alkyl hydroperoxide reductase activity" was flagged for obsoletion because, despite its generic-sounding name, it represented a substrate-specific activity more specific than any known gene product. The enzyme name "alkyl hydroperoxide reductase" is actually listed as a synonym of EC:1.11.1.26 (NADH-dependent peroxiredoxin activity), which corresponds to GO:0102039.

## Changes Made

In `src/ontology/go-edit.obo`, the term GO:0008785 was modified:

- Name prefixed with "obsolete" -> "obsolete alkyl hydroperoxide reductase activity"
- Definition prefixed with "OBSOLETE."
- Added explanatory comment about why the term was obsoleted (substrate specificity mismatch with EC:1.11.1.26)
- Removed `is_a` relationship to GO:0016668 (oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor)
- Added `is_obsolete: true`
- Added `replaced_by: GO:0102039` (NADH-dependent peroxiredoxin activity)
- Added term_tracker_item linking to issue #31961

## Resolution

Straightforward obsoletion following standard OBO pattern. The key reasoning was identifying that GO:0102039 is the correct replacement based on EC number alignment (EC:1.11.1.26). Approved without changes on first review.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 05f772421..f1ce0ab45 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -85576,12 +85576,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786

```

## Agent Attempts (23)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.800 | 0.889 | 0.727 | `c2f046b` | [#498](https://github.com/ai4curation/eval-ont-agent-go/pull/498) | [attempt](attempts/pr498.md) |
| 2 | claude-sonnet-4.5 | claude | 0.800 | 0.889 | 0.727 | `d02b23b` | [#473](https://github.com/ai4curation/eval-ont-agent-go/pull/473) | [attempt](attempts/pr473.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.800 | 0.889 | 0.727 | `c2f046b` | [#437](https://github.com/ai4curation/eval-ont-agent-go/pull/437) | [attempt](attempts/pr437.md) |
| 4 | claude-sonnet-4.5 | codex | 0.800 | 0.889 | 0.727 | `26cc47b` | [#369](https://github.com/ai4curation/eval-ont-agent-go/pull/369) | [attempt](attempts/pr369.md) |
| 5 | claude-opus-4.7 | claude | 0.800 | 0.889 | 0.727 | `8a2018c` | [#348](https://github.com/ai4curation/eval-ont-agent-go/pull/348) | [attempt](attempts/pr348.md) |
| 6 | kimi-k2.6 | opencode | 0.800 | 0.889 | 0.727 | `bbd4dda` | [#228](https://github.com/ai4curation/eval-ont-agent-go/pull/228) | [attempt](attempts/pr228.md) |
| 7 | kimi-k2.6 | opencode | 0.800 | 0.889 | 0.727 | `bbd4dda` | [#227](https://github.com/ai4curation/eval-ont-agent-go/pull/227) | [attempt](attempts/pr227.md) |
| 8 | gpt-5.5 | codex | 0.800 | 0.889 | 0.727 | `29a680f` | [#66](https://github.com/ai4curation/eval-ont-agent-go/pull/66) | [attempt](attempts/pr66.md) |
| 9 | gpt-5.5 | codex | 0.800 | 0.889 | 0.727 | `29a680f` | [#54](https://github.com/ai4curation/eval-ont-agent-go/pull/54) | [attempt](attempts/pr54.md) |
| 10 | gpt-5.4 | codex | 0.800 | 0.889 | 0.727 | `d9a1e5c` | [#46](https://github.com/ai4curation/eval-ont-agent-go/pull/46) | [attempt](attempts/pr46.md) |
| 11 | gpt-5.4 | codex | 0.800 | 0.889 | 0.727 | `d9a1e5c` | [#40](https://github.com/ai4curation/eval-ont-agent-go/pull/40) | [attempt](attempts/pr40.md) |
| 12 | gpt-5.4 | codex | 0.800 | 0.889 | 0.727 | `7960fbb` | [#37](https://github.com/ai4curation/eval-ont-agent-go/pull/37) | [attempt](attempts/pr37.md) |
| 13 | claude-sonnet-4.5 | claude | 0.800 | 0.889 | 0.727 | `e347ebb` | [#31](https://github.com/ai4curation/eval-ont-agent-go/pull/31) | [attempt](attempts/pr31.md) |
| 14 | claude-haiku-4.5 | claude | 0.800 | 0.889 | 0.727 | `f5c2608` | [#33](https://github.com/ai4curation/eval-ont-agent-go/pull/33) | [attempt](attempts/pr33.md) |
| 15 | gpt-5.4 | codex | 0.800 | 0.889 | 0.727 | `ed8baba` | [#32](https://github.com/ai4curation/eval-ont-agent-go/pull/32) | [attempt](attempts/pr32.md) |
| 16 | claude-sonnet-4.5 | claude | 0.800 | 0.889 | 0.727 | `d02b23b` | [#39](https://github.com/ai4curation/eval-ont-agent-go/pull/39) | [attempt](attempts/pr39.md) |
| 17 | gpt-5.4 | opencode | 0.762 | 0.889 | 0.667 | `e255e07` | [#51](https://github.com/ai4curation/eval-ont-agent-go/pull/51) | [attempt](attempts/pr51.md) |
| 18 | gpt-5.4 | opencode | 0.762 | 0.889 | 0.667 | `e255e07` | [#50](https://github.com/ai4curation/eval-ont-agent-go/pull/50) | [attempt](attempts/pr50.md) |
| 19 | gpt-5.5 | codex | 0.762 | 0.889 | 0.667 | `ae96d5d` | [#38](https://github.com/ai4curation/eval-ont-agent-go/pull/38) | [attempt](attempts/pr38.md) |
| 20 | gemma-4-31b | opencode | 0.727 | 0.889 | 0.615 | `18391a4` | [#225](https://github.com/ai4curation/eval-ont-agent-go/pull/225) | [attempt](attempts/pr225.md) |
| 21 | gpt-5.5 | opencode | 0.696 | 0.889 | 0.571 | `c0ea8ab` | [#103](https://github.com/ai4curation/eval-ont-agent-go/pull/103) | [attempt](attempts/pr103.md) |
| 22 | gpt-5.5 | opencode | 0.696 | 0.889 | 0.571 | `c0ea8ab` | [#84](https://github.com/ai4curation/eval-ont-agent-go/pull/84) | [attempt](attempts/pr84.md) |
| 23 | gemini-2.5-flash | gemini | 0.308 | 0.222 | 0.500 | `dddefb5` | [#362](https://github.com/ai4curation/eval-ont-agent-go/pull/362) | [attempt](attempts/pr362.md) |
