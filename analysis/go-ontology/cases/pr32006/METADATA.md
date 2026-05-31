---
repo: geneontology/go-ontology
issue_number: 31963
pr_number: 32006
issue_title: "Obsolete GO:0045550 geranylgeranyl reductase activity"
issue_created_at: "2026-04-24"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - textual-definition
  - enzymes
  - geranylgeranyl
  - definition-update
case_quality: poor
case_quality_reason: gold_pr_is_partial_and_eval_base_already_contains_gold
companion_prs:
  - 32009
scoring_caveat: "Issue #31963 was resolved by both PR #32006, which updated GO:0102067, and PR #32009, which obsoleted GO:0045550. At least eval PR #124 was run on a base where the #32006 definition/xref update was already present, so its zero metadiff against #32006 reflects base-state leakage as well as failure to complete the issue-level obsoletion."
curated_by: claude-opus-4
curated_at: "2026-05-10"
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
task_type_correction: "Metadata task_type is 'synonym_update' and the issue title says 'Obsolete ...', but the gold PR #32006 is neither: it is a definition_update (rewrites the GO:0102067 def: text and def xrefs, no synonym change, no obsoletion). The obsoletion in the issue title is handled by companion PR #32009. Suggested task_type for the #32006 sub-step: definition_update."
rationale: Follow-up definition refinement based on curator feedback, showing iterative improvement of enzyme term definitions
---

## Context

Issue #31963 primarily requested obsoletion of GO:0045550, but discussion in the issue also identified that GO:0102067 (the replacement term) had an overly complex definition. After the obsoletion was merged in PR #32009, @sjm41 noted that the reaction description in GO:0102067's definition should be simplified to use "phytyl diphosphate" rather than spelling out the full IUPAC substrate name.

## Changes Made

In `src/ontology/go-edit.obo`, the `def:` field of GO:0102067 (geranylgeranyl diphosphate reductase activity) was updated to use simplified substrate naming, making the definition more readable while remaining biochemically accurate.

## Resolution

Merged directly. This single-line definition polish was a direct response to @sjm41's comment in the issue discussion. It demonstrates the common pattern of iterative refinement where obsoletion of one term prompts closer scrutiny of the replacement term's quality.

## Curation Note (data quality)

Issue #31963 is not a clean one-PR evaluation case. The human resolution was split across PR #32006, which updated the `GO:0102067` definition and definition xrefs, and PR #32009, which later obsoleted `GO:0045550` with `replaced_by: GO:0102067`.

This matters for agent scoring because the selected gold PR for this case is only the definition-update sub-step. At least eval PR #124 was run on a base where the #32006 `GO:0102067` definition/xref update was already present while `GO:0045550` was still active. For that attempt, the zero metadiff against #32006 is therefore partly a base-state artifact; the substantive failure is that the agent did not complete the remaining issue-level obsoletion handled by #32009.

### Task-type metadata is wrong (flagged 2026-05-15, claude-opus-4.7)

The frontmatter `task_type: synonym_update` is incorrect, and so is the implied "obsoletion" of the issue title for *this* gold PR. PR #32006 changes only the `def:` text and the bracketed definition xrefs of `GO:0102067` (`[EC:1.3.1.83, GOC:pz]` → `[EC:1.3.1.83, PMID:9492312, RHEA:26229]`). There is no synonym edit and no obsoletion in #32006. The accurate task_type for the #32006 sub-step is **definition_update**; the obsoletion described by the issue title is the separate companion PR #32009.

### Cross-attempt review finding (claude-opus-4.7, 2026-05-15)

All 10 attempts were reviewed. Two clusters explain the score distribution, and the metadiff is misleading in both:

1. **Base `55fadafbd` (gold not pre-applied): #474, #349, #210, #279, #186.** These performed the correct definition rewrite. F1 caps at 0.5 (or 0.4 when a defensible `term_tracker_item` is added) purely because this is a one-line `def:` change and attempts differ from gold only in the bracketed xref set and synonymous phrasing. #186 (gpt-5.4/codex) reproduced the gold xref set `[EC:1.3.1.83, PMID:9492312, RHEA:26229]` exactly and #279 reproduced the gold def text verbatim — both scored only 0.4. The metadiff materially **under-represents** quality for this cluster; these are effectively successes.
2. **Base `8262d5a8a` (gold pre-applied): #157, #140, #124.** F1=0.0 is largely base-state leakage, not a definition-task failure; the real shortfall is the un-done `GO:0045550` obsoletion (companion #32009).
3. **Copilot #442 / #431** are genuine failures unrelated to the case-quality issue: identical off-topic diffs obsoleting `GO:0018581`/`GO:0047074` (hydroxyquinol dioxygenase), never engaging the geranylgeranyl reductase terms.

Recommendation: for aggregate scoring, treat the cluster-1 attempts as successes on the definition sub-step and exclude/down-weight the cluster-2 metadiff; only the two copilot runs are unambiguous failures.
