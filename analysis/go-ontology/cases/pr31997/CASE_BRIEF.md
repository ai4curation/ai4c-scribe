---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 27593
pr_number: 31997
issue_title: NTR ferric iron reductase (for non siderophore)
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: new_term
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
best_f1: 1.0
best_model: gpt-5.5
---

# PR #31997 — NTR ferric iron reductase (for non siderophore)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #27593](https://github.com/geneontology/go-ontology/issues/27593) | [PR #31997](https://github.com/geneontology/go-ontology/pull/31997) | @dragon-ai-agent | merged 2026-04-28

`new_term` `hard` `tightly_scoped` `approved_first_time`

## Context

A new term request for ferric iron reductase activity was filed in April 2024 to support GO-CAM modeling. The existing GO terms for iron reduction were tied to siderophore-mediated processes, but many organisms reduce ferric iron (Fe3+) to ferrous iron (Fe2+) through non-siderophore mechanisms using NADPH as the electron donor. The first attempt at this PR (#31797) was closed due to a GO ID collision where the allocated ID had already been used by a parallel branch.

## Changes Made

The PR added GO:7770068 `ferric iron reductase activity` as a new molecular function term with the reaction `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH` cross-referenced to RHEA:71767 (skos:exactMatch). The term was placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor). The definition referenced PMID:8321236. Additionally, the existing term GO:0000293 was updated to reflect its relationship to the new term.

## Resolution

Hard difficulty due to several factors: the issue was open for over two years, a previous PR attempt failed due to ID collision (requiring careful ID allocation), and the definition needed precise alignment with the RHEA reaction database. The parent term selection required understanding the enzyme classification hierarchy for oxidoreductases acting on metal ion substrates with NAD(P) as acceptor.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 5b4d6c89f..8ab446b18 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -3208,12 +3208,13 @@ intersection_of: has_primary_input SO:0000587 ! group_I_intron
 id: GO:0000293
 name: ferric-chelate reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2 Fe3+-siderophore + electron donor = 2 Fe2+-siderophore + electron acceptor." [PMID:33559753]
+def: "Catalysis of the reaction: 2 Fe3+-chelate + electron donor = 2 Fe2+-chelate + electron acceptor." [PMID:33559753]
 synonym: "ferric chelate reductase activity" EXACT []
 synonym: "iron chelate reductase activity" EXACT []
-is_a: GO:0016722 ! oxidoreductase activity, acting on metal ions
+is_a: GO:7770068 ! ferric iron reductase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/21029" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/26726" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30815" xsd:anyURI
 
 [Term]
@@ -617387,6 +617388,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-04-21T19:33:16Z
 
+[Term]
+id: GO:7770068
+name: ferric iron reductase activity
+namespace: molecular_function
+def: "Catalysis of the reaction: 2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH." [PMID:8321236, PMID:34614242, PMID:39940646, RHEA:71767]
+synonym: "ferric reductase activity" EXACT []
+synonym: "Fe3+ reductase activity" EXACT []
+xref: RHEA:71767 {source="skos:exactMatch"}
+is_a: GO:0016723 ! oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/27593" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-04-28T09:37:41Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `f73e876` | [#73](https://github.com/ai4curation/eval-ont-agent-go/pull/73) | [attempt](attempts/pr73.md) |
| 2 | kimi-k2.6 | opencode | 0.889 | 0.857 | 0.923 | `fc2dabe` | [#269](https://github.com/ai4curation/eval-ont-agent-go/pull/269) | [attempt](attempts/pr269.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.880 | 0.786 | 1.000 | `80160d1` | [#386](https://github.com/ai4curation/eval-ont-agent-go/pull/386) | [attempt](attempts/pr386.md) |
| 4 | gpt-5.5 | opencode | 0.786 | 0.786 | 0.786 | `7b1cce1` | [#110](https://github.com/ai4curation/eval-ont-agent-go/pull/110) | [attempt](attempts/pr110.md) |
| 5 | gpt-5.5 | opencode | 0.786 | 0.786 | 0.786 | `7b1cce1` | [#91](https://github.com/ai4curation/eval-ont-agent-go/pull/91) | [attempt](attempts/pr91.md) |
| 6 | claude-opus-4.7 | claude | 0.667 | 0.643 | 0.692 | `2e3bd15` | [#338](https://github.com/ai4curation/eval-ont-agent-go/pull/338) | [attempt](attempts/pr338.md) |
| 7 | claude-sonnet-4.5 | claude | 0.643 | 0.643 | 0.643 | `a76bf69` | [#472](https://github.com/ai4curation/eval-ont-agent-go/pull/472) | [attempt](attempts/pr472.md) |
| 8 | claude-haiku-4.5 | claude | 0.643 | 0.643 | 0.643 | `69ad86c` | [#195](https://github.com/ai4curation/eval-ont-agent-go/pull/195) | [attempt](attempts/pr195.md) |
| 9 | gpt-5.4 | codex | 0.593 | 0.571 | 0.615 | `78c01e8` | [#174](https://github.com/ai4curation/eval-ont-agent-go/pull/174) | [attempt](attempts/pr174.md) |
