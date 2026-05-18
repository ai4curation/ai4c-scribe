---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31876
pr_number: 31953
issue_title: 'Obsoletion request: GO:0140057 vacuole-mitochondria membrane tethering'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-23'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: biological_process
best_f1: 1.0
best_model: gpt-5.4
---

# PR #31953 — Obsoletion request: GO:0140057 vacuole-mitochondria membrane tethering

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31876](https://github.com/geneontology/go-ontology/issues/31876) | [PR #31953](https://github.com/geneontology/go-ontology/pull/31953) | @dragon-ai-agent | merged 2026-04-23

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31876 requested obsoletion of GO:0140057 "vacuole-mitochondria membrane tethering" as part of the broader MF_in_BP cleanup initiative. Unlike some other membrane tethering terms in this series, this one was flagged as having been "added in error" with no replacement term needed -- the specific vacuole-mitochondria tethering concept was not judged to warrant its own MF term.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0140057 was obsoleted:
- Marked `is_obsolete: true`
- No `replaced_by` tag (term added in error, no replacement warranted)
- Removed logical axioms
- Impact analysis confirmed no internal ontology references or external annotations existed

## Resolution

Merged after 2 commits (likely a minor formatting fix in the second commit). The key distinction from other membrane tethering obsoletions is that no replacement MF term was created. Per @raymond91125's assessment, the vacuole-mitochondria tethering concept at this granularity does not need representation in GO.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index e7328841b..4aa8b2aca 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -461971,12 +461971,14 @@ creation_date: 2017-06-27T09:58:51Z
 
 [Term]
 id: GO:0140057
-name: vacuole-mitochondria membrane tethering
+name: obsolete vacuole-mitochondria membrane tethering
 namespace: biological_process
-def: "The attachment of a mitochondrial membrane to a vacuolar membrane via molecular tethers that physically bridge their respective membranes and attach them to each other. The tethering may facilitate exchange of metabolites between the organelles." [PMID:27875684]
-is_a: GO:0140056 ! organelle localization by membrane tethering
+def: "OBSOLETE. The attachment of a mitochondrial membrane to a vacuolar membrane via molecular tethers that physically bridge their respective membranes and attach them to each other. The tethering may facilitate exchange of metabolites between the organelles." [PMID:27875684]
+comment: The reason for obsoletion is that this term was added in error.
 created_by: pg
 creation_date: 2017-06-27T10:31:12Z
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31876" xsd:anyURI
+is_obsolete: true
 
 [Term]
 id: GO:0140058

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `8664710` | [#647](https://github.com/ai4curation/eval-ont-agent-go/pull/647) | [attempt](attempts/pr647.md) |
| 2 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `8664710` | [#598](https://github.com/ai4curation/eval-ont-agent-go/pull/598) | [attempt](attempts/pr598.md) |
| 3 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `8664710` | [#456](https://github.com/ai4curation/eval-ont-agent-go/pull/456) | [attempt](attempts/pr456.md) |
| 4 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `8664710` | [#376](https://github.com/ai4curation/eval-ont-agent-go/pull/376) | [attempt](attempts/pr376.md) |
| 5 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `bb3b5b7` | [#333](https://github.com/ai4curation/eval-ont-agent-go/pull/333) | [attempt](attempts/pr333.md) |
| 6 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | `8664710` | [#256](https://github.com/ai4curation/eval-ont-agent-go/pull/256) | [attempt](attempts/pr256.md) |
| 7 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `bb3b5b7` | [#198](https://github.com/ai4curation/eval-ont-agent-go/pull/198) | [attempt](attempts/pr198.md) |
| 8 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `8664710` | [#175](https://github.com/ai4curation/eval-ont-agent-go/pull/175) | [attempt](attempts/pr175.md) |
| 9 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `8664710` | [#150](https://github.com/ai4curation/eval-ont-agent-go/pull/150) | [attempt](attempts/pr150.md) |
| 10 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `8664710` | [#129](https://github.com/ai4curation/eval-ont-agent-go/pull/129) | [attempt](attempts/pr129.md) |
| 11 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `8664710` | [#116](https://github.com/ai4curation/eval-ont-agent-go/pull/116) | [attempt](attempts/pr116.md) |
