---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31969
pr_number: 31988
issue_title: Parentage issues within 'oxidoreductase activity' branch
pr_author: sjm41
pr_merged_at: '2026-04-27'
task_type: reclassification
difficulty: hard
scoping: mostly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 14
generated_at: '2026-05-17'
scoping_notes: Primary changes are reparenting oxidoreductase terms per the issue,
  but also includes definition updates to align with RHEA reaction descriptions where
  the old definitions were inaccurate (e.g. GO:0008762, GO:0018525).
domain_area: molecular_function
best_f1: 0.956
best_model: gpt-5.4
---

# PR #31988 — Parentage issues within 'oxidoreductase activity' branch

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31969](https://github.com/geneontology/go-ontology/issues/31969) | [PR #31988](https://github.com/geneontology/go-ontology/pull/31988) | @sjm41 | merged 2026-04-27

`reclassification` `hard` `mostly_scoped` `approved_first_time`

## Context

Issue #31969 identified multiple parentage errors in the oxidoreductase activity branch of GO. Several terms were classified under the wrong oxidoreductase subclass based on their EC number assignments. For example, terms classified under "acting on the CH-OH group" (GO:0016616) that should have been under "acting on the CH-CH group" (GO:0016628) based on their actual reaction chemistry.

## Changes Made

In `src/ontology/go-edit.obo` (66 additions, 38 deletions across multiple term stanzas):

**Reparented terms** (examples):
- GO:0004498 (calcidiol 1-monooxygenase): moved from GO:0016709 (NAD(P)H donor) to GO:0016713 (iron-sulfur protein donor) — the enzyme uses ferredoxin, not NAD(P)H
- GO:0008762 (UDP-N-acetylmuramate dehydrogenase): moved from GO:0016616 (CH-OH group) to GO:0016628 (CH-CH group) — reaction acts on a double bond, not a hydroxyl
- GO:0008867 (formate dehydrogenase): moved from GO:0016620 (aldehyde/oxo group) to GO:0016726 (CH or CH2 groups)
- GO:0010277 (chlorophyllide a oxygenase): moved from GO:0016703 (internal monooxygenases) to GO:0016709 (paired donors, NAD(P)H)

**Definition updates**:
- GO:0008762: updated substrate names to use correct alpha-D- stereochemistry, changed xref from EC to RHEA:12248
- GO:0018525 (4-hydroxybenzoyl-CoA reductase): updated reaction equation to use explicit oxidized/reduced ferredoxin notation from RHEA:29603

**Added provenance**: term_tracker_item linking to #31969 on all modified terms.

## Resolution

This required deep understanding of:
1. The oxidoreductase hierarchy in GO (which subclass maps to which donor/acceptor chemistry)
2. EC number classification scheme and how EC numbers map to GO parents
3. RHEA reaction equations to determine the actual chemistry

Hard difficulty because: (a) affects 25+ terms, (b) each reclassification requires verifying the reaction mechanism against EC/RHEA, (c) some definitions needed updating alongside the reparenting to maintain consistency.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1c96f5771..152c54a64 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -43069,9 +43069,10 @@ xref: EC:1.14.15.18 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03610
 xref: MetaCyc:CALCIDIOL-1-MONOOXYGENASE-RXN
 xref: RHEA:20573 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016713 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced iron-sulfur protein as one donor, and incorporation of one atom of oxygen
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0004499
@@ -85179,7 +85180,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0008762
 name: UDP-N-acetylmuramate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: UDP-N-acetylmuramate + NADP+ = UDP-N-acetyl-3-O-(1-carboxyvinyl)-D-glucosamine + NADPH + H+." [EC:1.3.1.98]
+def: "Catalysis of the reaction: UDP-N-acetyl-alpha-D-muramate + NADP+ = UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine + NADPH + H+." [RHEA:12248]
 synonym: "MurB reductase" RELATED [EC:1.3.1.98]
 synonym: "UDP-GlcNAc-enoylpyruvate reductase activity" RELATED [EC:1.3.1.98]
 synonym: "UDP-N-acetylenolpyruvoylglucosamine reductase activity" RELATED [EC:1.3.1.98]
@@ -85191,8 +85192,9 @@ synonym: "uridine-5'-diphospho-N-acetyl-2-amino-2-deoxy-3-O-lactylglucose:NADP-o
 xref: EC:1.3.1.98 {source="skos:exactMatch"}
 xref: MetaCyc:UDPNACETYLMURAMATEDEHYDROG-RXN
 xref: RHEA:12248 {source="skos:exactMatch"}
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+is_a: GO:0016628 ! oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0008763
@@ -86465,8 +86467,9 @@ xref: EC:1.17.1.8 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-14014
 xref: RHEA:35323 {source="skos:narrowMatch"}
 xref: RHEA:35331 {source="skos:narrowMatch"}
-is_a: GO:0016628 ! oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
+is_a: GO:0016726 ! oxidoreductase activity, acting on CH or CH2 groups, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27695" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0008840
@@ -86762,9 +86765,10 @@ xref: KEGG_REACTION:R00519
 xref: MetaCyc:1.2.1.2-RXN
 xref: RHEA:15985 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0103
-is_a: GO:0016620 ! oxidoreductase activity, acting on the aldehyde or oxo group of donors, NAD or NADP as acceptor
+is_a: GO:0016726 ! oxidoreductase activity, acting on CH or CH2 groups, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28183" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0008864
@@ -102386,10 +102390,11 @@ synonym: "chlorophyllide a:oxygen 7-oxidoreduction activity" RELATED [EC:1.14.13
 synonym: "chlorophyllide-a oxygenation activity" RELATED [EC:1.14.13.122]
 xref: EC:1.14.13.122 {source="skos:exactMatch"}
 xref: RHEA:30359 {source="skos:exactMatch"}
-is_a: GO:0016703 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of one atom of oxygen (internal monooxygenases or internal mixed function oxidases)
+is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27410" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27676" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0010278
@@ -137720,7 +137725,7 @@ is_obsolete: true
 id: GO:0018525
 name: 4-hydroxybenzoyl-CoA reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzoyl-CoA + oxidized ferredoxin + H2O = 4-hydroxybenzoyl-CoA + reduced ferredoxin." [RHEA:29603]
+def: "Catalysis of the reaction: oxidized 2[4Fe-4S]-[ferredoxin] + benzoyl-CoA + H2O = 4-hydroxybenzoyl-CoA + reduced 2[4Fe-4S]-[ferredoxin] + 2 H+." [RHEA:29603]
 synonym: "4-hydroxybenzoyl-coA reductase (dehydroxylating) activity" RELATED []
 synonym: "4-hydroxybenzoyl-coA:(acceptor) oxidoreductase activity" RELATED []
 xref: EC:1.1.7.1 {source="skos:exactMatch"}
@@ -137728,8 +137733,9 @@ xref: KEGG_REACTION:R05316
 xref: MetaCyc:OHBENZCOARED-RXN
 xref: RHEA:29603 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0158
-is_a: GO:0016636 ! oxidoreductase activity, acting on the CH-CH group of donors, iron-sulfur protein as acceptor
+is_a: GO:0016614 ! oxidoreductase activity, acting on CH-OH group of donors
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0018526
@@ -138189,8 +138195,9 @@ xref: EC:1.14.12.25 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-664
 xref: RHEA:42344 {source="skos:exactMatch"}
 xref: UM-BBD_reactionID:r0395
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+is_a: GO:0016708 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of two atoms of oxygen into one donor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0018571
@@ -186783,12 +186790,13 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0032441
 name: pheophorbide a oxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: pheophorbide a + reduced ferredoxin + 2 O2 = red chlorophyll catabolite + oxidized ferredoxin + H2O." [PMID:14657372]
+def: "Catalysis of the reaction: pheophorbide a + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = red chlorophyll catabolite + 2 oxidized [2Fe-2S]-[ferredoxin]." [PMID:14657372, RHEA:48140]
 xref: EC:1.14.15.17 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-7740
 xref: RHEA:48140 {source="skos:exactMatch"}
-is_a: GO:0016730 ! oxidoreductase activity, acting on iron-sulfur proteins as donors
+is_a: GO:0016713 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced iron-sulfur protein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0032442
@@ -200972,8 +200980,9 @@ synonym: "gluconic dehydrogenase activity" RELATED [EC:1.1.99.3]
 xref: EC:1.1.99.3 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-2-DEHYDROGENASE-RXN
 xref: RHEA:12769 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016614 ! oxidoreductase activity, acting on CH-OH group of donors
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0033718
@@ -201598,9 +201607,10 @@ xref: EC:1.14.20.5 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-8000
 xref: RHEA:10448 {source="skos:exactMatch"}
 xref: RHEA:32755 {source="skos:narrowMatch"}
-is_a: GO:0016706 ! 2-oxoglutarate-dependent dioxygenase activity
+is_a: GO:0050498 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, with 2-oxoglutarate as one donor, and the other dehydrogenated
 relationship: part_of GO:0051553 ! flavone biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0033760
@@ -228728,8 +228738,9 @@ def: "Catalysis of the reaction: cholest-4-en-3-one + NADH + H+ + O2 = 26-hydrox
 xref: EC:1.14.15.29 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R09859
 xref: RHEA:51564 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+is_a: GO:0016713 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced iron-sulfur protein as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 created_by: bf
 creation_date: 2012-04-20T02:03:05Z
 
@@ -266774,12 +266785,13 @@ creation_date: 2012-08-15T11:41:24Z
 id: GO:0044684
 name: dihydromethanopterin reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 7,8-dihydromethanopterin + NADPH = 5,6,7,8-tetrahydromethanopterin + NADP." [GOC:mengo_curators, PMID:15028691]
+def: "Catalysis of the reaction: 5,6,7,8-tetrahydromethanopterin + acceptor = 7,8-dihydromethanopterin + reduced acceptor." [PMID:15028691, RHEA:42804]
 xref: EC:1.5.99.15 {source="skos:exactMatch"}
 xref: RHEA:42804 {source="skos:exactMatch"}
-is_a: GO:0016646 ! oxidoreductase activity, acting on the CH-NH group of donors, NAD or NADP as acceptor
+is_a: GO:0016645 ! oxidoreductase activity, acting on the CH-NH group of donors
 relationship: part_of GO:2001118 ! tetrahydromethanopterin biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 created_by: jl
 creation_date: 2012-08-15T13:57:55Z
 
@@ -272387,9 +272399,10 @@ xref: RHEA:21088 {source="skos:exactMatch"}
 xref: RHEA:61132 {source="skos:narrowMatch"}
 xref: RHEA:61136 {source="skos:narrowMatch"}
 xref: RHEA:61140 {source="skos:narrowMatch"}
-is_a: GO:0016706 ! 2-oxoglutarate-dependent dioxygenase activity
+is_a: GO:0050498 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, with 2-oxoglutarate as one donor, and the other dehydrogenated
 relationship: part_of GO:0051555 ! flavonol biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31969" xsd:anyURI
 
 [Term]
 id: GO:0045433
@@ -291828,20 +291841,22 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047081
-name: 3-hydroxy-2-methylpyridinecarboxylate dioxygenase [NAD(P)H] activity
+name: 3-hydroxy-2-methylpyridine-5-carboxylate monooxygenase [NAD(P)H] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: O2 + NAD(P)H + H+ + 3-hydroxy-2-methylpyridine-5-carboxylate = NAD(P)+ + 2-(acetamidomethylene)succinate." [EC:1.14.13.242]
+def: "Catalysis of the reaction: 3-hydroxy-2-methylpyridine-5-carboxylate + NAD(P)H + O2 = 2-(acetamidomethylene)succinate + NAD(P)+." [EC:1.14.13.242]
 synonym: "2-methyl-3-hydroxypyridine 5-carboxylic acid dioxygenase activity" RELATED [EC:1.14.13.242]
 synonym: "3-hydroxy-2-methylpyridine-5-carboxylate,NADPH:oxygen oxidoreductase (decyclizing)" RELATED [EC:1.14.13.242]
 synonym: "3-hydroxy-3-methylpyridinecarboxylate dioxygenase activity" RELATED [EC:1.14.13.242]
 synonym: "methylhydroxypyridine carboxylate dioxygenase activity" RELATED [EC:1.14.13.242]
 synonym: "methylhydroxypyridinecarboxylate oxidase activity" RELATED [EC:1.14.13.242]
+synonym: "3-hydroxy-2-methylpyridinecarboxylate dioxygenase [NAD(P)H] activity" RELATED []
 xref: EC:1.14.13.242 {source="skos:exactMatch"}
 xref: MetaCyc:1.14.12.4-RXN
 xref: RHEA:10860 {source="skos:narrowMatch"}
 xref: RHEA:10864 {source="skos:narrowMatch"}
... (170 more lines truncated)
```

## Agent Attempts (14)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.956 | 0.931 | 0.982 | `51a9917` | [#655](https://github.com/ai4curation/eval-ont-agent-go/pull/655) | [attempt](attempts/pr655.md) |
| 2 | gpt-5.5 | codex | 0.956 | 0.931 | 0.982 | `d755611` | [#63](https://github.com/ai4curation/eval-ont-agent-go/pull/63) | [attempt](attempts/pr63.md) |
| 3 | claude-opus-4.7 | claude | 0.948 | 0.948 | 0.948 | `fd57150` | [#353](https://github.com/ai4curation/eval-ont-agent-go/pull/353) | [attempt](attempts/pr353.md) |
| 4 | kimi-k2.6 | opencode | 0.938 | 0.914 | 0.964 | `611ef98` | [#290](https://github.com/ai4curation/eval-ont-agent-go/pull/290) | [attempt](attempts/pr290.md) |
| 5 | gpt-5.5 | opencode | 0.938 | 0.914 | 0.964 | `611ef98` | [#100](https://github.com/ai4curation/eval-ont-agent-go/pull/100) | [attempt](attempts/pr100.md) |
| 6 | gpt-5.5 | opencode | 0.938 | 0.914 | 0.964 | `611ef98` | [#82](https://github.com/ai4curation/eval-ont-agent-go/pull/82) | [attempt](attempts/pr82.md) |
| 7 | claude-sonnet-4.5 | claude | 0.929 | 0.897 | 0.963 | `767edff` | [#484](https://github.com/ai4curation/eval-ont-agent-go/pull/484) | [attempt](attempts/pr484.md) |
| 8 | gpt-5.4 | opencode | 0.920 | 0.897 | 0.945 | `f15e702` | [#685](https://github.com/ai4curation/eval-ont-agent-go/pull/685) | [attempt](attempts/pr685.md) |
| 9 | gpt-5.4 | opencode | 0.920 | 0.897 | 0.945 | `f15e702` | [#684](https://github.com/ai4curation/eval-ont-agent-go/pull/684) | [attempt](attempts/pr684.md) |
| 10 | gpt-5.4 | codex | 0.920 | 0.897 | 0.945 | `25e223f` | [#192](https://github.com/ai4curation/eval-ont-agent-go/pull/192) | [attempt](attempts/pr192.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.919 | 0.879 | 0.962 | `b682ea1` | [#504](https://github.com/ai4curation/eval-ont-agent-go/pull/504) | [attempt](attempts/pr504.md) |
| 12 | claude-sonnet-4.5 | copilot | 0.919 | 0.879 | 0.962 | `b682ea1` | [#425](https://github.com/ai4curation/eval-ont-agent-go/pull/425) | [attempt](attempts/pr425.md) |
| 13 | gemma-4-31b | opencode | 0.867 | 0.845 | 0.891 | `09ddebb` | [#266](https://github.com/ai4curation/eval-ont-agent-go/pull/266) | [attempt](attempts/pr266.md) |
| 14 | claude-haiku-4.5 | claude | 0.768 | 0.741 | 0.796 | `594789a` | [#219](https://github.com/ai4curation/eval-ont-agent-go/pull/219) | [attempt](attempts/pr219.md) |
