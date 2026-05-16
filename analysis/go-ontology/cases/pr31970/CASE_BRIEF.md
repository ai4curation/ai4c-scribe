---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31962
pr_number: 31970
issue_title: Missing EC/RHEA xrefs to add to oxidoreductase activity GO terms
pr_author: sjm41
pr_merged_at: '2026-04-24'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 1.0
best_model: claude-opus-4.7
---

# PR #31970 — Missing EC/RHEA xrefs to add to oxidoreductase activity GO terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31962](https://github.com/geneontology/go-ontology/issues/31962) | [PR #31970](https://github.com/geneontology/go-ontology/pull/31970) | @sjm41 | merged 2026-04-24

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #31962 identified four oxidoreductase activity GO terms that were missing their EC and/or RHEA cross-references. These mappings are critical for interoperability between GO and enzyme databases and for automated reaction-based reasoning.

## Changes Made

In `src/ontology/go-edit.obo`, cross-references were added to 4 terms:
- GO:0036441 (2-dehydropantolactone reductase activity): Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`
- GO:0070675 (hypoxanthine oxidase activity): Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}` and `xref: RHEA:68012 {source="skos:broadMatch"}`
- Two additional oxidoreductase terms received similar xref additions

The match semantics (`exactMatch` vs `broadMatch`) were chosen based on whether the GO term scope matches the EC entry exactly or represents a subset/superset.

## Resolution

Merged same-day by the author. Adding EC/RHEA cross-references is medium difficulty because it requires biochemical knowledge to determine the correct match type (exact, broad, or narrow) and to verify that the reaction described by the GO term definition actually corresponds to the external database entry.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..35df222a1 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231647,8 +231651,10 @@ namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | [#356](https://github.com/ai4curation/eval-ont-agent-go/pull/356) | [attempt](attempts/pr356.md) |
| 2 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | [#280](https://github.com/ai4curation/eval-ont-agent-go/pull/280) | [attempt](attempts/pr280.md) |
| 3 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | [#187](https://github.com/ai4curation/eval-ont-agent-go/pull/187) | [attempt](attempts/pr187.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.900 | 0.900 | 0.900 | [#392](https://github.com/ai4curation/eval-ont-agent-go/pull/392) | [attempt](attempts/pr392.md) |
| 5 | gemma-4-31b | opencode | 0.842 | 0.800 | 0.889 | [#535](https://github.com/ai4curation/eval-ont-agent-go/pull/535) | [attempt](attempts/pr535.md) |
| 6 | gemma-4-31b | opencode | 0.842 | 0.800 | 0.889 | [#518](https://github.com/ai4curation/eval-ont-agent-go/pull/518) | [attempt](attempts/pr518.md) |
| 7 | gpt-5.5 | opencode | 0.818 | 0.900 | 0.750 | [#154](https://github.com/ai4curation/eval-ont-agent-go/pull/154) | [attempt](attempts/pr154.md) |
| 8 | gpt-5.5 | opencode | 0.818 | 0.900 | 0.750 | [#134](https://github.com/ai4curation/eval-ont-agent-go/pull/134) | [attempt](attempts/pr134.md) |
| 9 | gpt-5.5 | codex | 0.818 | 0.900 | 0.750 | [#126](https://github.com/ai4curation/eval-ont-agent-go/pull/126) | [attempt](attempts/pr126.md) |
| 10 | claude-sonnet-4.5 | claude | 0.778 | 0.700 | 0.875 | [#480](https://github.com/ai4curation/eval-ont-agent-go/pull/480) | [attempt](attempts/pr480.md) |
| 11 | claude-haiku-4.5 | claude | 0.778 | 0.700 | 0.875 | [#214](https://github.com/ai4curation/eval-ont-agent-go/pull/214) | [attempt](attempts/pr214.md) |
