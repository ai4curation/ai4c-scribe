---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31971
issue_title: protoporphyrinogen oxidase activity terms
pr_author: sjm41
pr_merged_at: '2026-04-24'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 1.0
best_model: gpt-5.5
---

# PR #31971 — protoporphyrinogen oxidase activity terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31965](https://github.com/geneontology/go-ontology/issues/31965) | [PR #31971](https://github.com/geneontology/go-ontology/pull/31971) | @sjm41 | merged 2026-04-24

`reclassification` `hard` `tightly_scoped` `changes_requested`

## Context

Issue #31965 identified that the protoporphyrinogen oxidase activity sub-hierarchy had incorrect mappings: the parent term GO:0070818 and its children did not correctly correspond to their EC and RHEA cross-references. Each term needed its definition, xrefs, and parent relationships realigned to match the actual biochemical reactions catalogued in EC/RHEA.

## Changes Made

In `src/ontology/go-edit.obo`, the protoporphyrinogen oxidase hierarchy was refactored:
- GO:0070818 (parent): Definition updated to include 3x stoichiometry matching RHEA:64720
- Child terms: EC and RHEA xrefs corrected to point to the right reactions
- Definitions rewritten to accurately describe each specific reaction variant
- Parent-child relationships verified against the reaction specificity hierarchy

Net +5 lines reflecting additional xrefs and expanded definitions.

## Resolution

The PR was merged same-day but received review feedback from @pgaudet requesting that child term names follow the standard "X as acceptor" naming pattern. This was addressed in follow-up PR #31979. This case demonstrates how enzyme term refactoring often requires multiple rounds: first the biochemical content is corrected, then naming conventions are applied.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 35df222a1..336a9ade7 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -384002,26 +384002,31 @@ creation_date: 2009-07-13T04:20:17Z
 id: GO:0070818
 name: protoporphyrinogen oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: protoporphyrinogen IX + acceptor = protoporphyrin IX + reduced acceptor." [GOC:mah, PMID:19583219]
+def: "Catalysis of the reaction: protoporphyrinogen IX + 3 acceptor = protoporphyrin IX + 3 reduced acceptor." [RHEA:62000, PMID:19583219]
 synonym: "protoporphyrinogen IX oxidase activity" RELATED [EC:1.3.3.4]
 synonym: "protoporphyrinogen-IX oxidase activity" RELATED [EC:1.3.3.4]
 synonym: "protoporphyrinogenase activity" RELATED [EC:1.3.3.4]
+xref: RHEA:62000 {source="skos:exactMatch"}
 is_a: GO:0016627 ! oxidoreductase activity, acting on the CH-CH group of donors
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28776" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31965" xsd:anyURI
 created_by: mah
 creation_date: 2009-07-20T02:41:12Z
 
 [Term]
 id: GO:0070819
-name: menaquinone-dependent protoporphyrinogen oxidase activity
+name: quinone-dependent protoporphyrinogen oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: protoporphyrinogen IX + menaquinone = protoporphyrin IX + reduced menaquinone." [GOC:mah, PMID:19583219]
-synonym: "protoporphyrinogen-IX:menaquinone oxidoreductase activity" EXACT [GOC:mah]
-xref: EC:1.3.3.4 {source="skos:broadMatch"}
+def: "Catalysis of the reaction: protoporphyrinogen IX + 3 a quinone = protoporphyrin IX + 3 a quinol." [RHEA:65032, PMID:19583219]
+synonym: "protoporphyrinogen-IX:menaquinone oxidoreductase activity" NARROW [GOC:mah]
+synonym: "menaquinone-dependent protoporphyrinogen oxidase activity" NARROW []
+xref: EC:1.3.5.3 {source="skos:exactMatch"}
+xref: RHEA:65032 {source="skos:exactMatch"}
 is_a: GO:0016635 ! oxidoreductase activity, acting on the CH-CH group of donors, quinone or related compound as acceptor
 is_a: GO:0070818 ! protoporphyrinogen oxidase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/24056" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28520" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31965" xsd:anyURI
 created_by: mah
 creation_date: 2009-07-20T02:46:06Z
 

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `b96aae5` | [#122](https://github.com/ai4curation/eval-ont-agent-go/pull/122) | [attempt](attempts/pr122.md) |
| 2 | kimi-k2.6 | opencode | 0.870 | 0.769 | 1.000 | `81dafd6` | [#282](https://github.com/ai4curation/eval-ont-agent-go/pull/282) | [attempt](attempts/pr282.md) |
| 3 | claude-opus-4.7 | claude | 0.846 | 0.846 | 0.846 | `be097c7` | [#347](https://github.com/ai4curation/eval-ont-agent-go/pull/347) | [attempt](attempts/pr347.md) |
| 4 | gpt-5.4 | codex | 0.800 | 0.769 | 0.833 | `577aee2` | [#190](https://github.com/ai4curation/eval-ont-agent-go/pull/190) | [attempt](attempts/pr190.md) |
| 5 | gpt-5.5 | opencode | 0.769 | 0.769 | 0.769 | `1d10e5e` | [#155](https://github.com/ai4curation/eval-ont-agent-go/pull/155) | [attempt](attempts/pr155.md) |
| 6 | gpt-5.5 | opencode | 0.769 | 0.769 | 0.769 | `1d10e5e` | [#136](https://github.com/ai4curation/eval-ont-agent-go/pull/136) | [attempt](attempts/pr136.md) |
| 7 | claude-haiku-4.5 | claude | 0.727 | 0.615 | 0.889 | `6faf7e6` | [#212](https://github.com/ai4curation/eval-ont-agent-go/pull/212) | [attempt](attempts/pr212.md) |
| 8 | claude-sonnet-4.5 | claude | 0.696 | 0.615 | 0.800 | `4f99a6a` | [#475](https://github.com/ai4curation/eval-ont-agent-go/pull/475) | [attempt](attempts/pr475.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.696 | 0.615 | 0.800 | `1471025` | [#391](https://github.com/ai4curation/eval-ont-agent-go/pull/391) | [attempt](attempts/pr391.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.333 | 0.846 | 0.208 | `1be19e9` | [#436](https://github.com/ai4curation/eval-ont-agent-go/pull/436) | [attempt](attempts/pr436.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.333 | 0.846 | 0.208 | `1be19e9` | [#421](https://github.com/ai4curation/eval-ont-agent-go/pull/421) | [attempt](attempts/pr421.md) |
