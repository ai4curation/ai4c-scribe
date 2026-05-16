---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31945
pr_number: 32013
issue_title: 'Obsoletion request: GO:0003400 regulation of COPII vesicle coating'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-29'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
best_f1: 0.9
best_model: claude-opus-4.7
---

# PR #32013 — Obsoletion request: GO:0003400 regulation of COPII vesicle coating

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31945](https://github.com/geneontology/go-ontology/issues/31945) | [PR #32013](https://github.com/geneontology/go-ontology/pull/32013) | @dragon-ai-agent | merged 2026-04-29

`reclassification` `medium` `tightly_scoped` `approved_first_time`

## Context

GO:0003400 `regulation of COPII vesicle coating` was identified as biologically inappropriate because the proteins annotated to it are actually participants in the COPII vesicle coating process itself, not upstream regulators. The issue also identified that the primary COPII term (GO:0048208) had a misleading name and that GO:0006901 needed a label update.

## Changes Made

Three terms were modified in `go-edit.obo`: GO:0003400 was obsoleted with `replaced_by GO:0048208`, since annotated proteins are part of the coating process rather than regulators. GO:0048208 was renamed from `COPII vesicle coating` to `COPII vesicle coat assembly`, promoting the previous exact synonym to the primary label. GO:0006901 also received a label update. The old names were retained as synonyms to preserve searchability.

## Resolution

Medium difficulty because the changes required understanding the biological distinction between regulation of a process and participation in that process. In vesicle biology, COPII coat proteins like Sec23/Sec24 are components of the coating machinery, not regulators of it. The obsoletion of the regulation term and simultaneous renaming of the target term ensured that annotation migration would be semantically correct.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 6e6af3307..05f772421 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -29440,11 +29440,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -69216,10 +69218,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -123047,7 +123049,7 @@ name: synaptic vesicle coating
 namespace: biological_process
 def: "The formation of clathrin coated pits in the presynaptic membrane endocytic zone, triggered by the presence of high concentrations of synaptic vesicle components. This process leads to, but does not include budding of the membrane to form new vesicles." [GOC:curators, PMID:10099709, PMID:20448150]
 subset: goslim_synapse
-is_a: GO:0006901 ! vesicle coating
+is_a: GO:0006901 ! vesicle coat assembly
 relationship: part_of GO:0016185 ! synaptic vesicle budding from presynaptic endocytic zone membrane
 
 [Term]
@@ -307906,7 +307908,7 @@ name: Golgi transport vesicle coating
 namespace: biological_process
 def: "The addition of specific coat proteins to Golgi membranes during the formation of transport vesicles." [GOC:jid, GOC:mah, ISBN:0716731363, PMID:10219233]
 synonym: "dictyosome transport vesicle coating" NARROW []
-is_a: GO:0006901 ! vesicle coating
+is_a: GO:0006901 ! vesicle coat assembly
 relationship: part_of GO:0048194 ! Golgi vesicle budding
 relationship: part_of GO:0048199 ! vesicle targeting, to, from or within Golgi
 
@@ -307982,13 +307984,13 @@ relationship: part_of GO:0006888 ! endoplasmic reticulum to Golgi vesicle-mediat
 
 [Term]
 id: GO:0048208
-name: COPII vesicle coating
+name: COPII vesicle coat assembly
 namespace: biological_process
 def: "The addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jid, GOC:mah, GOC:tb, ISBN:0716731363, PMID:10219233]
 synonym: "COPII coating of ER-derived vesicle" EXACT [GOC:tb]
-synonym: "COPII vesicle coat assembly" EXACT [GOC:ascb_2009, GOC:dph, GOC:tb]
 synonym: "COPII vesicle coat formation" EXACT [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-is_a: GO:0006901 ! vesicle coating
+synonym: "COPII vesicle coating" EXACT [GOC:ascb_2009, GOC:dph, GOC:tb]
+is_a: GO:0006901 ! vesicle coat assembly
 intersection_of: GO:0022607 ! cellular component assembly
 intersection_of: results_in_assembly_of GO:0030127 ! COPII vesicle coat
 relationship: part_of GO:0048207 ! vesicle targeting, rough ER to cis-Golgi

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.900 | 0.900 | 0.900 | `aa743a8` | [#344](https://github.com/ai4curation/eval-ont-agent-go/pull/344) | [attempt](attempts/pr344.md) |
| 2 | kimi-k2.6 | opencode | 0.900 | 0.900 | 0.900 | `8660123` | [#278](https://github.com/ai4curation/eval-ont-agent-go/pull/278) | [attempt](attempts/pr278.md) |
| 3 | claude-sonnet-4.5 | claude | 0.895 | 0.850 | 0.944 | `b83c095` | [#489](https://github.com/ai4curation/eval-ont-agent-go/pull/489) | [attempt](attempts/pr489.md) |
| 4 | claude-sonnet-4.5 | claude | 0.895 | 0.850 | 0.944 | `b83c095` | [#465](https://github.com/ai4curation/eval-ont-agent-go/pull/465) | [attempt](attempts/pr465.md) |
| 5 | claude-haiku-4.5 | claude | 0.895 | 0.850 | 0.944 | `3b5eea6` | [#211](https://github.com/ai4curation/eval-ont-agent-go/pull/211) | [attempt](attempts/pr211.md) |
| 6 | gpt-5.4 | codex | 0.864 | 0.950 | 0.792 | `086b308` | [#183](https://github.com/ai4curation/eval-ont-agent-go/pull/183) | [attempt](attempts/pr183.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.842 | 0.800 | 0.889 | `4e8dc49` | [#381](https://github.com/ai4curation/eval-ont-agent-go/pull/381) | [attempt](attempts/pr381.md) |
| 8 | gemma-4-31b | opencode | 0.833 | 0.750 | 0.938 | `830593e` | [#247](https://github.com/ai4curation/eval-ont-agent-go/pull/247) | [attempt](attempts/pr247.md) |
| 9 | gpt-5.5 | codex | 0.826 | 0.950 | 0.731 | `2cb1ca3` | [#61](https://github.com/ai4curation/eval-ont-agent-go/pull/61) | [attempt](attempts/pr61.md) |
| 10 | gpt-5.5 | opencode | 0.818 | 0.900 | 0.750 | `8b01af9` | [#104](https://github.com/ai4curation/eval-ont-agent-go/pull/104) | [attempt](attempts/pr104.md) |
| 11 | gpt-5.5 | opencode | 0.818 | 0.900 | 0.750 | `8b01af9` | [#83](https://github.com/ai4curation/eval-ont-agent-go/pull/83) | [attempt](attempts/pr83.md) |
