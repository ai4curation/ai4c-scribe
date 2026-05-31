---
repo: obophenotype/uberon
issue_number: 3631
pr_number: 3633
issue_title: "NTR: occlusal surface of tooth"
issue_created_at: "2025-11-24"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-24"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 4
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: dental-anatomy
tags:
  - AI-agent
  - synonym-addition
  - definition-update
  - dental
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: AI agent-authored synonym and definition update on a single dental term, demonstrating automated ontology curation
case_quality: ok
case_quality_reason: metadiff_underrepresents_synonym_scope_and_gold_repudiated_field
companion_prs: [3603, 3632]
scoring_caveat: "Gold PR #3633 itself contains a 'Remove issue tracker' commit (the human author added then deleted term_tracker_item before merge), so attempts that add term_tracker_item are penalized for reproducing a field the gold author repudiated. The gold also serializes the two new synonyms as RELATED [] while a defensible reading is EXACT [url]; all three attempts chose EXACT, costing F1. Judge attempts on substance: term-identity recognition, definition rewrite, synonyms, and the second contributor ORCID."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

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
