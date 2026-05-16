---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31882
pr_number: 32036
issue_title: 'Obsolete: GO:0097711 ciliary basal body-plasma membrane docking Biological
  Process'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-05'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
best_f1: 1.0
best_model: gpt-5.5
---

# PR #32036 — Obsolete: GO:0097711 ciliary basal body-plasma membrane docking Biological Process

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31882](https://github.com/geneontology/go-ontology/issues/31882) | [PR #32036](https://github.com/geneontology/go-ontology/pull/32036) | @dragon-ai-agent | merged 2026-05-05

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

Two terms in the cilium assembly branch were identified as redundant with `GO:1905349 ciliary transition zone assembly`. GO:1905353 `ciliary transition fiber assembly` and GO:0097711 `ciliary basal body-plasma membrane docking` both described aspects of the same biological process already captured by the replacement term. The obsoletion was discussed and confirmed by curators ValWood, hattrill, pgaudet, and raymond91125.

## Changes Made

Both GO:1905353 and GO:0097711 were obsoleted in `go-edit.obo` with `replaced_by` pointing to GO:1905349 `ciliary transition zone assembly`. The obsoletion involved removing logical axioms (is_a relationships, intersection_of definitions), adding the "OBSOLETE." prefix to definitions, and renaming terms with the "obsolete" prefix. The net change removed 36 lines (axioms and active term stanzas) and added 13 lines (obsoletion markers and replaced_by references).

## Resolution

This was a straightforward obsoletion with pre-existing curator consensus. Easy difficulty because the replacement term was already identified, multiple curators had agreed on the action, and no annotation migration complexity was involved. The large line deletion count reflects the removal of logical definitions and axioms from both terms.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index a85b5cc9a..455454c0f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -353921,7 +353921,6 @@ relationship: has_part GO:0035735 ! intraciliary transport involved in cilium as
 relationship: has_part GO:0061512 ! protein localization to cilium
 relationship: has_part GO:0097712 ! trans-Golgi to periciliary membrane compartment transport
 relationship: has_part GO:1905349 ! ciliary transition zone assembly
-relationship: starts_with GO:0097711 ! ciliary basal body-plasma membrane docking
 
 [Term]
 id: GO:0060272
@@ -428970,16 +428969,13 @@ creation_date: 2016-06-07T12:45:00Z
 
 [Term]
 id: GO:0097711
-name: ciliary basal body-plasma membrane docking
+name: obsolete ciliary basal body-plasma membrane docking
 namespace: biological_process
-def: "The docking of a cytosolic centriole/basal body to the plasma membrane via the ciliary transition fibers. In some species this may happen via an intermediate step, by first docking to the ciliary vesicle via the ciliary transition fibers. The basal body-ciliary vesicle then relocates to the plasma membrane, followed by the ciliary vesicle fusing with the plasma membrane, effectively attaching the basal body to the plasma membrane." [GOC:cilia, PMID:13978319, PMID:23348840, PMID:23530209, PMID:25686250, PMID:26981235]
-comment: Basal bodies in jawed vertebrates appear to first attach to a ciliary vesicle. It is unclear how specific this is to jawed vertebrates or if other organisms also employ this sequence. Some species like Giardia intestinalis do not relocate their basal bodies to the plasma membrane, but have their axonemes extend through the cytosol to then protrude out of the cell to form flagella.
-synonym: "anchoring of the basal body to the plasma membrane" RELATED []
-synonym: "ciliary basal body docking" EXACT []
-is_a: GO:0140056 ! organelle localization by membrane tethering
-relationship: part_of GO:0060271 ! cilium assembly
-created_by: pr
-creation_date: 2016-08-05T16:12:33Z
+def: "OBSOLETE. The docking of a cytosolic centriole/basal body to the plasma membrane via the ciliary transition fibers. In some species this may happen via an intermediate step, by first docking to the ciliary vesicle via the ciliary transition fibers. The basal body-ciliary vesicle then relocates to the plasma membrane, followed by the ciliary vesicle fusing with the plasma membrane, effectively attaching the basal body to the plasma membrane." [GOC:cilia, PMID:13978319, PMID:23348840, PMID:23530209, PMID:25686250, PMID:26981235]
+comment: The reason for obsoletion is that this term is redundant with GO:1905349 ciliary transition zone assembly. Per PMID:27646273, transition zone assembly is a complex process that begins with docking of the mother centriole to cytoplasmic vesicles, so the docking step is encompassed by transition zone assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31882" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:1905349
 
 [Term]
 id: GO:0097712
@@ -578482,32 +578478,13 @@ creation_date: 2016-08-05T14:01:23Z
 
 [Term]
 id: GO:1905353
-name: ciliary transition fiber assembly
-namespace: biological_process
-def: "The aggregation, arrangement and bonding together of a set of components to form a ciliary transition fiber." [GO_REF:0000079, GOC:cilia, GOC:TermGenie, PMID:24189274]
-synonym: "centriolar distal appendage assembly" RELATED [GOC:TermGenie]
-synonym: "centriolar distal appendage formation" RELATED [GOC:TermGenie]
-synonym: "cilial transition fiber assembly" EXACT [GOC:TermGenie]
-synonym: "cilial transition fiber formation" EXACT [GOC:TermGenie]
-synonym: "cilial transition fibre assembly" EXACT [GOC:TermGenie]
-synonym: "cilial transition fibre formation" EXACT [GOC:TermGenie]
-synonym: "ciliary transition fiber formation" EXACT [GOC:TermGenie]
-synonym: "ciliary transition fibre assembly" EXACT [GOC:TermGenie]
-synonym: "ciliary transition fibre formation" EXACT [GOC:TermGenie]
-synonym: "cilium transition fiber assembly" EXACT [GOC:TermGenie]
-synonym: "cilium transition fiber formation" EXACT [GOC:TermGenie]
-synonym: "cilium transition fibre assembly" EXACT [GOC:TermGenie]
-synonym: "cilium transition fibre formation" EXACT [GOC:TermGenie]
-synonym: "distal appendage of basal body assembly" RELATED [GOC:TermGenie]
-synonym: "distal appendage of basal body formation" RELATED [GOC:TermGenie]
-synonym: "distal appendage of centriole assembly" RELATED [GOC:TermGenie]
-synonym: "distal appendage of centriole formation" RELATED [GOC:TermGenie]
-synonym: "distal appendage of mother centriole assembly" RELATED [GOC:TermGenie]
-synonym: "distal appendage of mother centriole formation" RELATED [GOC:TermGenie]
-intersection_of: GO:0022607 ! cellular component assembly
-intersection_of: results_in_assembly_of GO:0097539 ! ciliary transition fiber
-created_by: pr
-creation_date: 2016-08-05T14:01:32Z
+name: obsolete ciliary transition fiber assembly
+namespace: biological_process
+def: "OBSOLETE. The aggregation, arrangement and bonding together of a set of components to form a ciliary transition fiber." [GO_REF:0000079, GOC:cilia, GOC:TermGenie, PMID:24189274]
+comment: The reason for obsoletion is that this term is redundant with GO:1905349 ciliary transition zone assembly. Ciliary transition fiber assembly is part of transition zone assembly and the term had no annotations.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31882" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:1905349
 
 [Term]
 id: GO:1905354

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `455454c` | [#170](https://github.com/ai4curation/eval-ont-agent-go/pull/170) | [attempt](attempts/pr170.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `455454c` | [#158](https://github.com/ai4curation/eval-ont-agent-go/pull/158) | [attempt](attempts/pr158.md) |
| 3 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `455454c` | [#131](https://github.com/ai4curation/eval-ont-agent-go/pull/131) | [attempt](attempts/pr131.md) |
| 4 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `455454c` | [#101](https://github.com/ai4curation/eval-ont-agent-go/pull/101) | [attempt](attempts/pr101.md) |
| 5 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `455454c` | [#68](https://github.com/ai4curation/eval-ont-agent-go/pull/68) | [attempt](attempts/pr68.md) |
| 6 | claude-sonnet-4.5 | claude | 0.964 | 0.952 | 0.976 | `c56de82` | [#463](https://github.com/ai4curation/eval-ont-agent-go/pull/463) | [attempt](attempts/pr463.md) |
| 7 | kimi-k2.6 | opencode | 0.964 | 0.952 | 0.976 | `75615e0` | [#265](https://github.com/ai4curation/eval-ont-agent-go/pull/265) | [attempt](attempts/pr265.md) |
| 8 | gpt-5.5 | opencode | 0.964 | 0.952 | 0.976 | `6d5ded1` | [#86](https://github.com/ai4curation/eval-ont-agent-go/pull/86) | [attempt](attempts/pr86.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.952 | 0.952 | 0.952 | `8ff7469` | [#382](https://github.com/ai4curation/eval-ont-agent-go/pull/382) | [attempt](attempts/pr382.md) |
| 10 | claude-opus-4.7 | claude | 0.952 | 0.952 | 0.952 | `12d7182` | [#334](https://github.com/ai4curation/eval-ont-agent-go/pull/334) | [attempt](attempts/pr334.md) |
| 11 | claude-haiku-4.5 | claude | 0.952 | 0.952 | 0.952 | `a887d5e` | [#202](https://github.com/ai4curation/eval-ont-agent-go/pull/202) | [attempt](attempts/pr202.md) |
| 12 | gpt-5.4 | codex | 0.952 | 0.952 | 0.952 | `d99825a` | [#178](https://github.com/ai4curation/eval-ont-agent-go/pull/178) | [attempt](attempts/pr178.md) |
