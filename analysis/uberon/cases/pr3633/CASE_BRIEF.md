---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3631
pr_number: 3633
issue_title: 'NTR: occlusal surface of tooth'
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-24'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: dental-anatomy
best_f1: 0.5
best_model: gemma-4-31b
---

# PR #3633 — NTR: occlusal surface of tooth

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3631](https://github.com/obophenotype/uberon/issues/3631) | [PR #3633](https://github.com/obophenotype/uberon/pull/3633) | @dragon-ai-agent | merged 2025-11-24

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3631 requested enhancements to the existing occlusal surface of tooth term (UBERON:8600149), which had been initially added via issue #3602. The term needed additional synonyms and an improved definition to better capture its function in mastication.

## Changes Made

The PR updated UBERON:8600149 with an enhanced definition specifying that the occlusal surface applies to premolar and molar teeth and functions in chewing and grinding food. Two related synonyms were added: "chewing surface" (RELATED) and "masticatory surface" (RELATED). A contributor ORCID and issue tracker link were also added.

## Resolution

Simple difficulty. This is a straightforward metadata enhancement on a single term, adding synonyms and refining a definition. The PR was authored by the dragon-ai-agent and merged same-day. An agent would need basic knowledge of dental anatomy terminology and the OBO synonym syntax with scope qualifiers.

## Curation Note (data quality)

Flagged `case_quality: ok` (not poor — the gold is a single, valid PR resolving the
issue) but the metadiff materially under-represents attempt quality for two reasons:

1. **Gold-repudiated field within the gold PR.** PR #3633 has two commits:
   `f48d88b1` (the edit) and `cd9fb802` ("Remove issue tracker"). The human author
   added a `property_value: term_tracker_item ".../issues/3631"` line and then
   explicitly deleted it before merge. The merged gold diff therefore contains **no**
   `term_tracker_item`. Attempts pr304 (sonnet-4.5) and pr259 (opus-4.7) added that
   line — a defensible, conventional provenance action that the issue's intent
   supports — yet they are scored against a target the gold author themselves
   repudiated. The gold PR body still *claims* it "Added issue tracker", a
   stale claim contradicted by the actual merged diff.

2. **Synonym-scope convention difference.** Gold serialized "chewing surface" and
   "masticatory surface" as `RELATED []`. All three attempts used `EXACT [url]`
   (modeled on the existing `occlusal surface` EXACT synonym / sibling pattern).
   This single qualifier choice is the dominant driver of F1 < 1.0 and is a
   convention difference, not an error (RELATED is the better-justified scope for
   these broader functional descriptors, but EXACT is a reasonable reading).

Companion PRs: #3603 created UBERON:8600149 (resolving #3602); #3632 was a
closed Copilot WIP that added the synonyms as `EXACT []` plus an unrelated
`.gitignore` `tools/` line (not part of the gold).

Substance ranking of attempts: **pr133 (gemma-4-31b)** is strongest — its
definition rewrite is byte-identical to gold and it added no repudiated tracker
line (F1=0.5 under-represents it). **pr259 (opus-4.7)** has the best methodology
but deliberately skipped the issue-supplied definition rewrite (genuine
`missed_requirement`). **pr304 (sonnet-4.5)** skipped the definition rewrite *and*
churned `dcterms-date`/`created_by` provenance (genuine over-editing). F1=0 for
pr259/pr304 over-represents failure relative to the repudiated-field and
synonym-scope artifacts, but both have at least one real defect.

quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 3cbe2c361..875d983a8 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225412,10 +225412,13 @@ property_value: dcterms-date "2025-08-05T09:28:57Z" xsd:dateTime
 [Term]
 id: UBERON:8600149
 name: occlusal surface of tooth
-def: "A tooth surface structure that forms the biting or grinding surface of a molar or premolar." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+def: "A tooth surface structure that forms the chewing edge of premolar or molar tooth. It functions to chew or grind food during biting." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+synonym: "chewing surface" RELATED []
+synonym: "masticatory surface" RELATED []
 synonym: "occlusal surface" EXACT [https://dentaleducationhub.com/surfaces-of-the-teeth/]
 is_a: UBERON:8600148 ! tooth surface structure
 relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+relationship: dc-contributor https://orcid.org/0009-0002-7282-0836
 property_value: dcterms-date "2025-08-29T11:00:00Z" xsd:dateTime
 
 [Term]

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | `8c6afd1` | [#133](https://github.com/ai4curation/eval-ont-agent-uberon/pull/133) | [attempt](attempts/pr133.md) |
| 2 | gpt-5.4 | opencode | 0.222 | 0.250 | 0.200 | `7417832` | [#676](https://github.com/ai4curation/eval-ont-agent-uberon/pull/676) | [attempt](attempts/pr676.md) |
| 3 | gpt-5.4 | opencode | 0.222 | 0.250 | 0.200 | `7417832` | [#616](https://github.com/ai4curation/eval-ont-agent-uberon/pull/616) | [attempt](attempts/pr616.md) |
| 4 | gpt-5.4 | codex | 0.222 | 0.250 | 0.200 | `fcdd440` | [#416](https://github.com/ai4curation/eval-ont-agent-uberon/pull/416) | [attempt](attempts/pr416.md) |
| 5 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `f64666a` | [#638](https://github.com/ai4curation/eval-ont-agent-uberon/pull/638) | [attempt](attempts/pr638.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `f64666a` | [#580](https://github.com/ai4curation/eval-ont-agent-uberon/pull/580) | [attempt](attempts/pr580.md) |
| 7 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `5b1f842` | [#500](https://github.com/ai4curation/eval-ont-agent-uberon/pull/500) | [attempt](attempts/pr500.md) |
| 8 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `c567fda` | [#454](https://github.com/ai4curation/eval-ont-agent-uberon/pull/454) | [attempt](attempts/pr454.md) |
| 9 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `5b1f842` | [#369](https://github.com/ai4curation/eval-ont-agent-uberon/pull/369) | [attempt](attempts/pr369.md) |
| 10 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `3e16bf9` | [#304](https://github.com/ai4curation/eval-ont-agent-uberon/pull/304) | [attempt](attempts/pr304.md) |
| 11 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `b988af7` | [#259](https://github.com/ai4curation/eval-ont-agent-uberon/pull/259) | [attempt](attempts/pr259.md) |
