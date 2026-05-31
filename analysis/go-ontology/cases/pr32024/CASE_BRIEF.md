---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31916
pr_number: 32024
issue_title: Review of Entner-Doudoroff pathways
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-04'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
best_f1: 0.965
best_model: gpt-5.4
---

# PR #32024 — Review of Entner-Doudoroff pathways

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31916](https://github.com/geneontology/go-ontology/issues/31916) | [PR #32024](https://github.com/geneontology/go-ontology/pull/32024) | @dragon-ai-agent | merged 2026-05-04

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

The Entner-Doudoroff pathway in GO had accumulated five overly specific variant terms (e.g., "through 6-phosphogluconate", "through gluconate", "non-phosphorylative") that were nested under the parent GO:0061678 `Entner-Doudoroff pathway`. A review by sjm41 with agreement from raymond91125 and pgaudet concluded that these variants introduced unnecessary granularity and should be consolidated to the single parent term.

## Changes Made

Five terms were obsoleted with `replaced_by` pointing to GO:0061678: GO:0009255 (through 6-phosphogluconate), GO:0061679 (through gluconate), GO:0061680 (non-phosphorylative), and two additional variants. Each obsoletion involved renaming with the "obsolete" prefix, marking definitions as OBSOLETE, removing logical axioms (is_a, part_of relationships), and adding replaced_by references. The net effect simplified the pathway hierarchy from six terms to one.

## Resolution

Medium difficulty because the decision to collapse pathway variants required understanding the biochemical distinctions between different Entner-Doudoroff pathway routes and whether those distinctions were meaningful for annotation. The prior discussion on issue #29539 provided the biological rationale that the variant pathways were not independently annotatable in practice. The large line changes (37 additions, 47 deletions) reflect the systematic obsoletion of five terms.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1ae42d961..41e9d3f34 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -92094,19 +92094,13 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009255
-name: Entner-Doudoroff pathway through 6-phosphogluconate
+name: obsolete Entner-Doudoroff pathway through 6-phosphogluconate
 namespace: biological_process
-def: "A pathway that converts a carbohydrate to pyruvate and glyceraldehyde-3 phosphate by producing 6-phosphogluconate and then dehydrating it." [GOC:jl, MetaCyc:PWY-8004, PMID:12921356, PMID:12981024]
-xref: MetaCyc:PWY-8004
-is_a: GO:0005975 ! carbohydrate metabolic process
-is_a: GO:0044281 ! small molecule metabolic process
-is_a: GO:0061678 ! Entner-Doudoroff pathway
-intersection_of: GO:0061678 ! Entner-Doudoroff pathway
-intersection_of: ends_with GO:0008675 ! 2-dehydro-3-deoxy-phosphogluconate aldolase activity
-intersection_of: has_intermediate CHEBI:58759 ! 6-phosphonatooxy-D-gluconate
-intersection_of: has_part GO:0004456 ! phosphogluconate dehydratase activity
-intersection_of: has_primary_output CHEBI:15361 ! pyruvate
-intersection_of: has_primary_output CHEBI:58027 ! glyceraldehyde 3-phosphate(2-)
+def: "OBSOLETE. A pathway that converts a carbohydrate to pyruvate and glyceraldehyde-3 phosphate by producing 6-phosphogluconate and then dehydrating it." [GOC:jl, MetaCyc:PWY-8004, PMID:12921356, PMID:12981024]
+comment: This term was obsoleted because the variant Entner-Doudoroff pathways are better represented by the parent term GO:0061678 (Entner-Doudoroff pathway). MetaCyc treats these as 'variant pathways' and such variants are better captured as GO-CAMs rather than as nested ontology terms.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0061678
 
 [Term]
 id: GO:0009256
@@ -369507,7 +369501,10 @@ id: GO:0061678
 name: Entner-Doudoroff pathway
 namespace: biological_process
 def: "A cellular carbohydrate catabolic process that converts a carbohydrate to pyruvate and either glyceraldehyde or glyceraldehyde-3 phosphate by dehydration and aldol cleavage via a gluconate or 6-phosphogluconate intermediate." [GOC:dph, PMID:12921536]
-xref: MetaCyc:Entner-Doudoroff-Pathways
+xref: MetaCyc:ENTNER-DOUDOROFF-PWY {source="skos:narrowMatch"}
+xref: MetaCyc:NPGLUCAT-PWY {source="skos:narrowMatch"}
+xref: MetaCyc:PWY-2221 {source="skos:narrowMatch"}
+xref: MetaCyc:PWY-8004 {source="skos:narrowMatch"}
 is_a: GO:0016052 ! carbohydrate catabolic process
 relationship: has_primary_output CHEBI:15361 ! pyruvate
 created_by: dph
@@ -369515,45 +369512,38 @@ creation_date: 2015-01-16T15:28:25Z
 
 [Term]
 id: GO:0061679
-name: Entner-Doudoroff pathway through gluconate
-namespace: biological_process
-def: "The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate." [GOC:dph, PMID:12921536]
-synonym: "gluconate pathway" RELATED []
-is_a: GO:0061678 ! Entner-Doudoroff pathway
-intersection_of: GO:0061678 ! Entner-Doudoroff pathway
-intersection_of: has_intermediate CHEBI:18391 ! D-gluconate
-intersection_of: has_part GO:0047929 ! gluconate dehydratase activity
-intersection_of: has_part GO:0047935 ! glucose 1-dehydrogenase (NADP+) activity
-intersection_of: has_primary_output CHEBI:15361 ! pyruvate
+name: obsolete Entner-Doudoroff pathway through gluconate
+namespace: biological_process
+def: "OBSOLETE. The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate." [GOC:dph, PMID:12921536]
+comment: This term was obsoleted because the variant Entner-Doudoroff pathways are better represented by the parent term GO:0061678 (Entner-Doudoroff pathway). MetaCyc treats these as 'variant pathways' and such variants are better captured as GO-CAMs rather than as nested ontology terms.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0061678
 created_by: dph
 creation_date: 2015-01-16T15:41:22Z
 
 [Term]
 id: GO:0061680
-name: Entner-Doudoroff pathway through gluconate to D-glyceraldehyde
-namespace: biological_process
-def: "The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate and yields pyruvate and D-glyceraldehyde." [GOC:dph, MetaCyc:NPGLUCAT-PWY, PMID:12921536]
-xref: MetaCyc:NPGLUCAT-PWY
-is_a: GO:0019595 ! non-phosphorylated glucose catabolic process
-is_a: GO:0061679 ! Entner-Doudoroff pathway through gluconate
-intersection_of: GO:0061679 ! Entner-Doudoroff pathway through gluconate
-intersection_of: ends_with GO:0061677 ! 2-dehydro-3-deoxy-D-gluconate aldolase activity
-intersection_of: has_primary_output CHEBI:17378 ! D-glyceraldehyde
+name: obsolete Entner-Doudoroff pathway through gluconate to D-glyceraldehyde
+namespace: biological_process
+def: "OBSOLETE. The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate and yields pyruvate and D-glyceraldehyde." [GOC:dph, MetaCyc:NPGLUCAT-PWY, PMID:12921536]
+comment: This term was obsoleted because the variant Entner-Doudoroff pathways are better represented by the parent term GO:0061678 (Entner-Doudoroff pathway). MetaCyc treats these as 'variant pathways' and such variants are better captured as GO-CAMs rather than as nested ontology terms.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28392" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0061678
 created_by: dph
 creation_date: 2015-01-22T08:51:31Z
 
 [Term]
 id: GO:0061681
-name: Entner-Doudoroff pathway through gluconate to D-glyceraldehyde-3-phosphate
-namespace: biological_process
-def: "The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate and yields pyruvate and D-glyceraldehyde-3-phosphate." [GOC:dph, PMID:12921536]
-xref: MetaCyc:PWY-2221
-is_a: GO:0061679 ! Entner-Doudoroff pathway through gluconate
-intersection_of: GO:0061679 ! Entner-Doudoroff pathway through gluconate
-intersection_of: ends_with GO:0008675 ! 2-dehydro-3-deoxy-phosphogluconate aldolase activity
-intersection_of: has_part GO:0008673 ! 2-dehydro-3-deoxygluconokinase activity
-intersection_of: has_primary_output CHEBI:58027 ! glyceraldehyde 3-phosphate(2-)
+name: obsolete Entner-Doudoroff pathway through gluconate to D-glyceraldehyde-3-phosphate
+namespace: biological_process
+def: "OBSOLETE. The Entner-Doudoroff pathway that proceeds through a D-gluconate intermediate and yields pyruvate and D-glyceraldehyde-3-phosphate." [GOC:dph, PMID:12921536]
+comment: This term was obsoleted because the variant Entner-Doudoroff pathways are better represented by the parent term GO:0061678 (Entner-Doudoroff pathway). MetaCyc treats these as 'variant pathways' and such variants are better captured as GO-CAMs rather than as nested ontology terms.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0061678
 created_by: dph
 creation_date: 2015-01-22T08:55:22Z
 
@@ -369646,13 +369636,13 @@ creation_date: 2015-03-09T09:16:23Z
 
 [Term]
 id: GO:0061688
-name: glycolytic process via Entner-Doudoroff Pathway
+name: obsolete glycolytic process via Entner-Doudoroff Pathway
 namespace: biological_process
-def: "A glycolytic process in which the glucose is catabolized to pyruvate by first entering the Entner-Doudoroff pathway to yield pyruvate and glyceraldehyde-3-phosphate. The glyceraldehyde-3-phosphate is subsequently converted to pyruvate by the core glycolytic enzymes." [GOC:dph, PMID:9657988]
-synonym: "gluconate pathway" RELATED []
-is_a: GO:0006096 ! glycolytic process
-intersection_of: GO:0006096 ! glycolytic process
-intersection_of: starts_with GO:0061678 ! Entner-Doudoroff pathway
+def: "OBSOLETE. A glycolytic process in which the glucose is catabolized to pyruvate by first entering the Entner-Doudoroff pathway to yield pyruvate and glyceraldehyde-3-phosphate. The glyceraldehyde-3-phosphate is subsequently converted to pyruvate by the core glycolytic enzymes." [GOC:dph, PMID:9657988]
+comment: This term was obsoleted because the existing IEA annotations are better captured by the parent term GO:0006096 (glycolytic process); pathway variants are better represented as GO-CAMs rather than as nested ontology terms.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31916" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0006096
 created_by: dph
 creation_date: 2015-03-12T14:39:00Z
 

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.965 | 0.965 | 0.965 | `c0dc80e` | [#180](https://github.com/ai4curation/eval-ont-agent-go/pull/180) | [attempt](attempts/pr180.md) |
| 2 | gpt-5.5 | opencode | 0.965 | 0.965 | 0.965 | `8854823` | [#106](https://github.com/ai4curation/eval-ont-agent-go/pull/106) | [attempt](attempts/pr106.md) |
| 3 | gpt-5.5 | opencode | 0.965 | 0.965 | 0.965 | `8854823` | [#85](https://github.com/ai4curation/eval-ont-agent-go/pull/85) | [attempt](attempts/pr85.md) |
| 4 | gpt-5.5 | codex | 0.965 | 0.965 | 0.965 | `71ddae4` | [#65](https://github.com/ai4curation/eval-ont-agent-go/pull/65) | [attempt](attempts/pr65.md) |
| 5 | kimi-k2.6 | opencode | 0.957 | 0.965 | 0.948 | `b5ed021` | [#276](https://github.com/ai4curation/eval-ont-agent-go/pull/276) | [attempt](attempts/pr276.md) |
| 6 | gpt-5.4 | opencode | 0.948 | 0.965 | 0.932 | `2c6a89c` | [#668](https://github.com/ai4curation/eval-ont-agent-go/pull/668) | [attempt](attempts/pr668.md) |
| 7 | gpt-5.4 | opencode | 0.948 | 0.965 | 0.932 | `2c6a89c` | [#620](https://github.com/ai4curation/eval-ont-agent-go/pull/620) | [attempt](attempts/pr620.md) |
| 8 | claude-opus-4.7 | claude | 0.940 | 0.965 | 0.917 | `bb255a5` | [#337](https://github.com/ai4curation/eval-ont-agent-go/pull/337) | [attempt](attempts/pr337.md) |
| 9 | claude-haiku-4.5 | claude | 0.887 | 0.895 | 0.879 | `c187207` | [#204](https://github.com/ai4curation/eval-ont-agent-go/pull/204) | [attempt](attempts/pr204.md) |
| 10 | claude-sonnet-4.5 | claude | 0.879 | 0.895 | 0.864 | `ad48600` | [#464](https://github.com/ai4curation/eval-ont-agent-go/pull/464) | [attempt](attempts/pr464.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.852 | 0.860 | 0.845 | `a80cb6c` | [#379](https://github.com/ai4curation/eval-ont-agent-go/pull/379) | [attempt](attempts/pr379.md) |
