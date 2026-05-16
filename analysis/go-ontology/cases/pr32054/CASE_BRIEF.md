---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 32044
pr_number: 32054
issue_title: 'NTR: protein O-linked glycosylation via N-acetylglucosamine'
pr_author: sjm41
pr_merged_at: '2026-05-07'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
best_f1: 0.8
best_model: gemma-4-31b
---

# PR #32054 — NTR: protein O-linked glycosylation via N-acetylglucosamine

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #32044](https://github.com/geneontology/go-ontology/issues/32044) | [PR #32054](https://github.com/geneontology/go-ontology/pull/32054) | @sjm41 | merged 2026-05-07

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for "protein O-linked glycosylation via N-acetylglucosamine" (GO:7770074), a biological process term representing the covalent attachment of a single GlcNAc residue to serine or threonine via a beta-glycosidic bond. This modification is distinct from the GalNAc-initiated mucin-type O-glycosylation and plays key roles in cellular signaling. The request originated from earlier issues #29770 and #23575 where the term was discussed but never created.

## Changes Made

The PR added GO:7770074 as a child of `GO:0006493 protein O-linked glycosylation` with a precise definition referencing the beta-glycosidic bond linkage and PMID citations. The definition specifies that this is a monosaccharide addition (not extended chain), distinguishing it from mucin-type glycosylation. As part of the same commit, the sibling term for GalNAc-initiated glycosylation had its spelling harmonized to use consistent nomenclature across the O-linked glycosylation branch.

## Resolution

The PR was merged the same day it was opened, with a single commit modifying `go-edit.obo`. The task required medium difficulty because the definition needed to precisely capture the biochemistry (beta-glycosidic bond, monosaccharide vs. chain extension) and the curator also identified an inconsistency in the sibling term that needed concurrent correction.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index be4a4f262..b3261d154 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -123845,13 +123845,14 @@ consider: GO:0012501
 
 [Term]
 id: GO:0016266
-name: protein O-linked glycosylation via N-acetyl-galactosamine
+name: protein O-linked glycosylation via N-acetylgalactosamine
 namespace: biological_process
 def: "A glycoprotein biosynthetic process starting with the covalent linkage of an N-acetyl-galactosamine via an alpha-glycosidic bond to the oxygen atom of a serine or threonine side chain in a protein, which can be further elongated with the sequential addition of sugar units resulting in the formation of a protein O-linked glycan." [PMID:10580130, PMID:35536936]
 synonym: "core O-glycan biosynthetic process" EXACT []
 synonym: "mucin-type O-glycan synthesis" NARROW []
 synonym: "O-glycan processing" EXACT []
 synonym: "protein O-linked GalNAcylation" RELATED []
+synonym: "protein O-linked glycosylation via N-acetyl-galactosamine" EXACT []
 xref: MetaCyc:PWY-7433 {source="skos:narrowMatch"}
 xref: MetaCyc:PWY-7435 {source="skos:narrowMatch"}
 is_a: GO:0006493 ! protein O-linked glycosylation
@@ -123860,6 +123861,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30362" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30366" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30592" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32044" xsd:anyURI
 
 [Term]
 id: GO:0016267
@@ -617560,6 +617562,18 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-05-07T12:45:27Z
 
+[Term]
+id: GO:7770074
+name: protein O-linked glycosylation via N-acetylglucosamine
+namespace: biological_process
+def: "A glycoprotein biosynthetic process in which a single N-acetylglucosamine is covalently linked via a beta-glycosidic bond to the oxygen atom of a serine or threonine side chain in a protein, resulting in the formation of a protein O-linked glycan. The sugar is not elongated into a larger oligosaccharide chain." [PMID:35536957]
+synonym: "protein O-linked GlcNAcylation" EXACT []
+synonym: "protein O-linked N-acetylglucosaminylation" EXACT []
+is_a: GO:0006493 ! protein O-linked glycosylation
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32044" xsd:anyURI
+created_by: sjm
+creation_date: 2026-05-07T16:32:08Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gemma-4-31b | opencode | 0.800 | 0.667 | 1.000 | [#273](https://github.com/ai4curation/eval-ont-agent-go/pull/273) | [attempt](attempts/pr273.md) |
| 2 | claude-haiku-4.5 | claude | 0.762 | 0.667 | 0.889 | [#408](https://github.com/ai4curation/eval-ont-agent-go/pull/408) | [attempt](attempts/pr408.md) |
| 3 | claude-opus-4.7 | claude | 0.762 | 0.667 | 0.889 | [#357](https://github.com/ai4curation/eval-ont-agent-go/pull/357) | [attempt](attempts/pr357.md) |
| 4 | kimi-k2.6 | opencode | 0.762 | 0.667 | 0.889 | [#288](https://github.com/ai4curation/eval-ont-agent-go/pull/288) | [attempt](attempts/pr288.md) |
| 5 | claude-sonnet-4.5 | claude | 0.727 | 0.667 | 0.800 | [#481](https://github.com/ai4curation/eval-ont-agent-go/pull/481) | [attempt](attempts/pr481.md) |
| 6 | gpt-5.5 | codex | 0.636 | 0.583 | 0.700 | [#539](https://github.com/ai4curation/eval-ont-agent-go/pull/539) | [attempt](attempts/pr539.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.417 | 0.417 | 0.417 | [#501](https://github.com/ai4curation/eval-ont-agent-go/pull/501) | [attempt](attempts/pr501.md) |
| 8 | claude-sonnet-4.5 | copilot | 0.417 | 0.417 | 0.417 | [#449](https://github.com/ai4curation/eval-ont-agent-go/pull/449) | [attempt](attempts/pr449.md) |
