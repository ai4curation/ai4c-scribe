---
repo: monarch-initiative/mondo
issue_number: 10149
pr_number: 10156
issue_title: "Request for new term [podocytopathy]"
issue_labels:
  - New term request
issue_created_at: "2026-04-14"
pr_author: sabrinatoro
pr_merged_at: "2026-04-15"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 17
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds a new parent term and reclassifies three existing children under it.
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: kidney-disease
tags:
  - podocytopathy
  - nephrology
  - glomerular-disease
  - hierarchy-grouping
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New grouping term with child reclassification requiring knowledge of renal pathology taxonomy
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_gold_out_of_scope
companion_prs: []
scoring_caveat: "F1 systematically under-represents quality for every attempt. (1) Placeholder-vs-canonical MONDO ID artifact: agents must use the eval-base temp ID MONDO:7770018, but the gold curator assigned canonical MONDO:0700328, so every id:/is_a: line mismatches under metadiff regardless of correctness. (2) The single gold PR #10156 does substantially MORE than issue #10149 asked: it adds a third child not in the issue (MONDO:0005376 membranous glomerulonephritis), an equivalence/genus-differentia axiom (intersection_of MONDO:0019722 + disease_has_location CL:0000653), an SCTID xref, and per-child IAO:0000233 lines. These uncap the gold above the issue request, so even a fully issue-faithful agent solution cannot reach F1=1.0. Judge attempts against issue #10149's explicit asks (new term podocytopathy under MONDO:0019722; two children MONDO:0006835 and MONDO:0100313), not against the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A request was made for a new term "podocytopathy" to serve as a grouping class for diseases caused by podocyte dysfunction. Podocytes are specialized cells in the kidney glomerulus, and podocytopathies include conditions like minimal change disease and focal segmental glomerulosclerosis. The term was needed to provide a clinically meaningful grouping in the disease hierarchy.

This was a collaborative effort with a domain expert (cws99) who helped define the scope and children of the new term.

## Changes Made

Added the new term "podocytopathy" to `src/ontology/mondo-edit.obo` with 17 lines of additions. The PR created the parent term with a definition and also reclassified three existing disease terms as children of the new grouping class. No lines were deleted, indicating clean additions to the hierarchy.

## Resolution

Medium difficulty because it requires understanding renal pathology well enough to determine which existing Mondo terms should be classified as podocytopathies. The curator needed to create a proper definition and identify the correct children, which requires domain knowledge about glomerular disease classification.

## Curation Note (data quality)

Flagged `case_quality: poor` on 2026-05-15 (claude-opus-4.7). Two compounding
reasons make the metadiff F1 a misleading quality signal for **every** attempt:

1. **Placeholder-vs-canonical MONDO ID artifact.** This is a `new_term` case.
   Agents allocate from the eval base's temp ID range and all chose
   `MONDO:7770018`; the gold curator assigned canonical `MONDO:0700328`. The
   agents cannot know the curator-assigned ID, yet every `id:` and `is_a:
   ... ! podocytopathy` line therefore mismatches the gold under whole-file
   metadiff. This alone caps F1 well below 1.0 for a perfectly correct
   solution. F1 differences among attempts here mostly reflect ancillary
   metadata (presence of `subset: disease_grouping`, `dcterms:creator` ORCID,
   PMID sources on child axioms), not core correctness.

2. **The single gold PR exceeds the issue scope.** Issue #10149 explicitly
   requested: a new term `podocytopathy`, parent `MONDO:0019722 glomerular
   disorder`, and exactly **two** children — `MONDO:0006835` lipoid nephrosis
   (minimal change disease) and `MONDO:0100313` focal segmental
   glomerulosclerosis. Gold PR #10156 additionally (a) reparents a **third**
   term not in the issue — `MONDO:0005376 membranous glomerulonephritis`
   (membranous nephropathy); (b) authors a logical/equivalence definition
   (`intersection_of: MONDO:0019722` + `intersection_of: disease_has_location
   CL:0000653`, with matching `relationship`); (c) adds `xref:
   SCTID:1367669003`; (d) adds per-child `property_value: IAO:0000233`. None of
   these were requested. A well-scoped, issue-faithful agent solution is
   therefore structurally unable to reach F1=1.0.

There are **no companion PRs** — the issue was resolved by the single PR
#10156 — but the gold itself is a superset of the issue, which is the relevant
poor-case signature here (Step 3b: "gold has out-of-scope extra edits the issue
never asked for", compounded by the new-term ID artifact).

**Reviewer judgment of the cohort (against the issue, not the metadiff):**
9 of 11 attempts (the gpt-5.5 opencode/codex, gpt-5.4 codex, kimi opencode,
claude sonnet native + copilot, claude opus runs) correctly and faithfully
implemented the issue request: the new term under `MONDO:0019722` with both
requested children added as additional (parent-preserving) subclasses — graded
`success`. The 2 claude-haiku runs (pr478, pr415, identical) created the term
but **omitted both requested children**, a genuine missed requirement — graded
`partial_success`. No attempt reproduced the gold's equivalence axiom or third
child, but neither was requested by the issue, so this is a scope-faithful
divergence rather than a failure. Downstream aggregation should down-weight or
exclude this case's raw F1 and rely on the per-attempt outcome grades.
