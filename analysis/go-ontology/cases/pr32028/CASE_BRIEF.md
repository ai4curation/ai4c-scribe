---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31114
pr_number: 32028
issue_title: 'NTR: Terreic acid biosynthetic process'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-05'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 18
generated_at: '2026-05-17'
domain_area: biological_process
best_f1: 0.0
best_model: gpt-5.4
---

# PR #32028 — NTR: Terreic acid biosynthetic process

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31114](https://github.com/geneontology/go-ontology/issues/31114) | [PR #32028](https://github.com/geneontology/go-ontology/pull/32028) | @dragon-ai-agent | merged 2026-05-05

`axiom_repair` `simple` `tightly_scoped` `changes_requested`

## Context

Issue #31114 originally requested new terms for terreic acid biosynthetic processes. During implementation, it was noticed that three terms had `created_by: PomBase:vw` instead of the expected GO convention. This PR attempted to fix them by changing to `GOC:vw`.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was changed from `PomBase:vw` to `GOC:vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

## Resolution

While the PR was merged, @pgaudet subsequently clarified that the correct format uses bare initials (`vw`) without any prefix. This prompted a follow-up PR (#32032) to make the final correction. This case demonstrates the importance of verifying metadata conventions with experienced curators rather than guessing at the pattern.

## Curation Note (data quality)

This is a poor scoring reference for agent evaluation. PR #32028 is an interim fix that changed `created_by: PomBase:vw` to `created_by: GOC:vw`, but issue discussion immediately clarified that `created_by` should use bare initials and follow-up PR #32032 changed the same fields to `created_by: vw`.

The metadiff score is also misleading because the OBO comparison ignores `created_by` metadata fields. Attempts that reproduce PR #32028 exactly, or that make the final-correct `vw` change, can still receive F1=0.0. Reviews for this case should judge attempts against the issue discussion and final convention, not the raw score alone.

Three additional findings from the 2026-05-15 review pass (claude-opus-4.7):

1. **The gold PR bundles an unrelated term.** The middle hunk of PR #32028 changes `created_by` on **GO:0180068 `negative regulation of carbohydrate utilization`**, whose `term_tracker_item` points to issue **#31261** — a carbohydrate-utilization request, not terreic acid. An agent given only issue #31114 has no signal to locate or edit GO:0180068. The gold PR's batch is an artifact of the human curator running `grep PomBase:vw` across the file and fixing every hit at once. Codex reviews for this case loosely describe the third term as a missed "terreic-acid" target; that is imprecise — it is a different term from a different issue.

2. **The literal `created_by` instruction in the issue was itself wrong.** ValWood explicitly asked the agent to use `GOC:vw`; @pgaudet then corrected this to bare `vw` (#32032). Attempts that produced bare `vw` (haiku #411, copilot #375, kimi #267) are *closer to the final-correct state* than the gold PR, yet score identically (0.0).

3. **The label/synonym swap is in-scope, not scope creep.** The issue thread (ValWood 2026-05-05 07:31, pgaudet 2026-05-04) explicitly requested swapping the primary label `terreate biosynthetic process` ↔ synonym `terreic acid biosynthetic process` for GO:0180067 and its regulation children. Attempts that did this (most of them) were following the issue, not over-editing. This sub-task was carried in the separate human PR #32014 (still open), not #32028. The case should be judged against the **union of the issue asks + #32028 + #32032 + #32014**, not #32028 alone.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..eaa8ef407 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483087,7 +483087,7 @@ is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483097,7 +483097,7 @@ namespace: biological_process
 def: "Any process that  that stops, prevents, or reduces the frequency, rate or extent of carbohydrate utilization." [GOC:vw]
 is_a: GO:0043610 ! regulation of carbohydrate utilization
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31261" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-01-19T11:52:03Z
 
 [Term]
@@ -483109,7 +483109,7 @@ is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

## Agent Attempts (18)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `194cbde` | [#671](https://github.com/ai4curation/eval-ont-agent-go/pull/671) | [attempt](attempts/pr671.md) |
| 2 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `194cbde` | [#669](https://github.com/ai4curation/eval-ont-agent-go/pull/669) | [attempt](attempts/pr669.md) |
| 3 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `d3e085b` | [#644](https://github.com/ai4curation/eval-ont-agent-go/pull/644) | [attempt](attempts/pr644.md) |
| 4 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `d3e085b` | [#641](https://github.com/ai4curation/eval-ont-agent-go/pull/641) | [attempt](attempts/pr641.md) |
| 5 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#631](https://github.com/ai4curation/eval-ont-agent-go/pull/631) | [attempt](attempts/pr631.md) |
| 6 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#621](https://github.com/ai4curation/eval-ont-agent-go/pull/621) | [attempt](attempts/pr621.md) |
| 7 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#594](https://github.com/ai4curation/eval-ont-agent-go/pull/594) | [attempt](attempts/pr594.md) |
| 8 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#591](https://github.com/ai4curation/eval-ont-agent-go/pull/591) | [attempt](attempts/pr591.md) |
| 9 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `388ac2a` | [#549](https://github.com/ai4curation/eval-ont-agent-go/pull/549) | [attempt](attempts/pr549.md) |
| 10 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `274e543` | [#543](https://github.com/ai4curation/eval-ont-agent-go/pull/543) | [attempt](attempts/pr543.md) |
| 11 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `ffd9273` | [#452](https://github.com/ai4curation/eval-ont-agent-go/pull/452) | [attempt](attempts/pr452.md) |
| 12 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#451](https://github.com/ai4curation/eval-ont-agent-go/pull/451) | [attempt](attempts/pr451.md) |
| 13 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `eaa8ef4` | [#441](https://github.com/ai4curation/eval-ont-agent-go/pull/441) | [attempt](attempts/pr441.md) |
| 14 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `d3e085b` | [#411](https://github.com/ai4curation/eval-ont-agent-go/pull/411) | [attempt](attempts/pr411.md) |
| 15 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `2cc4923` | [#375](https://github.com/ai4curation/eval-ont-agent-go/pull/375) | [attempt](attempts/pr375.md) |
| 16 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `ff761b5` | [#336](https://github.com/ai4curation/eval-ont-agent-go/pull/336) | [attempt](attempts/pr336.md) |
| 17 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `54cbaee` | [#267](https://github.com/ai4curation/eval-ont-agent-go/pull/267) | [attempt](attempts/pr267.md) |
| 18 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `274e543` | [#242](https://github.com/ai4curation/eval-ont-agent-go/pull/242) | [attempt](attempts/pr242.md) |
