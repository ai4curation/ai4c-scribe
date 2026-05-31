---
repo: obophenotype/cell-ontology
issue_number: 3252
pr_number: 3253
issue_title: "[NTR] quiescent fibroblast"
issue_created_at: "2025-08-13"
issue_closed_at: "2025-09-04"
pr_author: Caroline-99
pr_merged_at: "2025-09-04"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 11
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: connective-tissue
tags:
  - fibroblast
  - quiescence
  - NTR
  - cell-state
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request requiring reasoning about cell state vs cell type and proper placement in the fibroblast hierarchy
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact_zeroes_all_attempts
companion_prs: []
scoring_caveat: "All 8 attempts score exactly F1=0.000 because the cl-agent-config CLAUDE.md mandates placeholder IDs (CL_99xxxxx, idrange:81) while the gold PR #3253 used the curator's live-assigned canonical ID CL_4052071. The new term's whole stanza plus its Declaration line are ID-anchored, so an ID-naive line metadiff craters to zero even when the agent's label/definition/xrefs/synonym/parentage match gold. Judge attempts on substance vs the issue spec and gold content, not on the F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term request was filed for "quiescent fibroblast" as part of a broader effort to improve the fibroblast branch of the cell ontology (tracked in issue #2097). Quiescent fibroblasts are fibroblasts in a reversible G0 cell cycle arrest state, distinct from senescent fibroblasts. This is part of a larger initiative to add cell-state-qualified fibroblast subtypes.

## Changes Made

Added 11 new lines to `cl-edit.owl` defining the quiescent fibroblast term. This includes the class declaration, label, textual definition with literature references, parentage under fibroblast, and any relevant logical axioms linking the cell to its quiescent state via Gene Ontology biological process terms.

## Resolution

Approved on first review. Medium difficulty because creating a cell-state-qualified term requires understanding the distinction between cell states and cell types in ontology modeling, choosing appropriate GO terms for the quiescent state, and correctly structuring the logical definition.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.**

This is a clean, fully-specified single-PR NTR. Step 3a does not apply: PR #3253 is the *complete and only* human resolution (no companion PRs; `gh search prs` for "3252" and "quiescent fibroblast" returns only #3253; the related #2097 is a parent tracking issue, not a separate resolving PR; approved first time by RiveraAndrea83).

The case is nonetheless a **poor evaluation reference** due to the **placeholder-vs-canonical ID artifact**:

- The `ai4curation/cl-agent-config` CLAUDE.md *explicitly mandates*: "New term IDs MUST start with CL_99xxxxx (as specified in Datatype: idrange:81 in src/ontology/cl-idranges.owl)". All 8 attempts complied, using `CL_9900001` or `CL_4072103`.
- The gold PR #3253 used the curator's live-assigned canonical ID **`CL_4052071`** (from a real curator idrange, with `terms:contributor` ORCID 0009-0000-8480-9277).
- The new term's entire stanza, plus its `Declaration(Class(...))` line, is ID-anchored, and the term sorts to a different file location depending on its ID. An ID-naive line-level metadiff therefore yields **exactly F1=0.000 / P=0 / R=0 for all 8 attempts**, regardless of content correctness.

Substantively, the agents performed well. The gold definition is *verbatim* the issue-requested definition; pr281 (sonnet-4.5) and pr90 (haiku-4.5) reproduced it byte-for-byte, and pr90/pr14 even matched gold's `hasExactSynonym` scope. Several attempts added value beyond gold (pr57/pr41 cross-reference `circulating fibrocyte` CL:0000135; pr14 verified and correctly dropped the unrelated DOI; pr26 added a defensible `participates in GO:0044838` logical definition).

Config-driven divergences from gold that also depress metadiff but are **not agent errors**: agents add `IAO_0000233` term-tracker links and `dc:creator "GitHub Copilot"` because cl-agent-config instructs it, whereas the human gold used `terms:contributor` ORCID and no tracker item.

**Downstream guidance:** exclude or down-weight this case in F1 aggregation; judge attempts on substance against the issue spec and gold content. Best substantive outcomes: pr281, pr273, pr57/pr41, pr14, pr10 (success); pr26 (success, mild over-modeling); pr90 (partial — dropped xrefs/comment).
