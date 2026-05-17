---
repo: obophenotype/cell-ontology
issue_number: 3259
pr_number: 3450
issue_title: "[NTR] tPC-IC cell"
issue_created_at: "2025-08-21"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-11-21"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 1
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: renal
tags:
  - NTR
  - kidney
  - collecting-duct
  - transitional-cell
  - intercalated-cell
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for a transitional cell type in kidney collecting duct requiring understanding of principal-intercalated cell plasticity
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact_plus_gold_out_of_scope_serialization_edit
companion_prs: []
scoring_caveat: "Single-PR resolution (no companion PRs). All 7 attempts produced ontologically correct/equivalent tPC-IC terms. The placeholder CL ID is unknowable to a blinded agent: gold used CL_9900001; attempts that coincidentally matched it (#91, #65, #46, #27) score F1 0.636-0.706, while attempts choosing an equally valid temp-range ID (#272/#200 CL_9900000; #82 CL_9903259) score F1=0.000 despite equivalent content. Gold also carries an out-of-scope serialization-order edit (hasDbXref comment text 'has cross-reference' -> 'database_cross_reference') the issue never requested and no agent should reproduce, which caps recall on the matching-ID attempts. Judge attempts on substance against the issue, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term request was filed for the transitional principal-intercalated cell (tPC-IC), a recently described cell type in the kidney collecting duct that exhibits characteristics of both principal cells and intercalated cells. This cell type represents an intermediate state in the plasticity between these two well-established collecting duct cell populations. The issue had been open since August 2025 as part of ongoing kidney cell type curation.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the tPC-IC term with a class declaration, rdfs:label, textual definition with literature references, appropriate parentage, and logical axioms linking the cell to UBERON kidney collecting duct structures via part_of relations. One existing line was modified to accommodate the new term in the class hierarchy.

## Resolution

The PR required changes during review before approval and merge, going through 7 commits total. Medium difficulty because modeling a transitional cell state between two existing cell types requires careful consideration of the ontological relationship -- it is not simply a subclass of either parent type but represents a hybrid phenotype that needed appropriate axiomatization.

## Curation Note (data quality)

`case_quality: poor` (flagged by claude-opus-4.7, 2026-05-16). Step 3a confirms this is a **single-PR resolution** of issue #3259 — PR #3450 fully resolves it; there are no companion PRs, so the union-of-PRs concern does not apply.

The case is poor for two Step 3b reasons:

1. **Placeholder-vs-canonical CL ID artifact (decisive).** The cl-agent-config instructs agents to mint new terms with an ID from the `CL_99xxxxx` temporary range (`9900000-9999999`). The blinded gold human PR landed on `CL_9900001`. Every line of a new-term diff embeds the subject IRI, so an attempt's metadiff score is determined by whether it coincidentally picked the same placeholder:
   - **ID = CL_9900001** → #91 (haiku-4.5, F1 0.706), #65 / #46 (gpt-5.5/opencode, F1 0.696, duplicate runs), #27 (gpt-5.5/codex, F1 0.636)
   - **ID = CL_9900000** → #272 (opus-4.7) and #200 (sonnet-4.5), F1 **0.000**
   - **ID = CL_9903259** (derived from issue #3259) → #82 (gpt-5.4/codex), F1 **0.000**
   All seven attempts produced an ontologically correct and essentially equivalent term (correct parent `CL_1000454`, `part_of UBERON_0001232`, both requested synonyms with correct types, both contributor ORCIDs, PMID-xref'd definition). The three F1=0 results reflect ID luck only, **not** a content failure. All seven are graded `outcome: success`.

2. **Gold has an out-of-scope serialization-order edit.** PR #3450's diff also flips an annotation-property comment from `# Annotation Property: oboInOwl:hasDbXref (has cross-reference)` to `(database_cross_reference)` — a ROBOT/serialization artifact the issue never requested and that no agent could or should reproduce. This depresses recall (and hence F1) on even the ID-matching attempts, so the metadiff under-represents their quality too.

Downstream scoring/aggregation should exclude or down-weight this case's metadiff and treat all attempts as substantive successes. Note also that #46 is a byte-identical duplicate of #65 (same run/blob) and should count once.
