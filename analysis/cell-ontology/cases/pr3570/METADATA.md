---
repo: obophenotype/cell-ontology
issue_number: 3500
pr_number: 3570
issue_title: "Add taxon constraints to DN2a and DN2b thymocytes"
issue_created_at: "2025-12-01"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - taxon-constraint
  - thymocyte
  - DN2
  - mouse
  - Mus-musculus
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple taxon constraint addition restricting DN2a/DN2b thymocyte terms to Mus musculus
case_quality: ok
case_quality_reason: gold_renegotiated_term_tracker_in_pr_comments
companion_prs: []
scoring_caveat: "Gold PR #3570 is the sole and complete human resolution and the F1=1.0 results (#235, #139) are genuine. However the gold was renegotiated in PR comments: the gold agent initially added IAO_0000233/term_tracker_item annotations and curator RiveraAndrea83 explicitly asked to remove them ('please remove term tracker from the edits'), so the merged gold deliberately excludes term-tracker provenance. Attempts that follow the cl-agent-config CLAUDE.md instruction to 'Link back to the issue ... using the term_tracker_item' (#199 separate AnnotationAssertion: F1=0.667; #190 inline IAO_0000233 axiom annotation: F1=0.0) are structurally penalized for instruction-compliant behavior. Judge #199/#190 on substance (both add the correct RO_0002162 some NCBITaxon_10090 constraints) — metadiff materially under-represents their quality."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The DN2a (CL_0002423) and DN2b (CL_0002424) thymocyte subtypes are defined based on mouse thymic development staging that does not directly translate to human T cell development. Issue #3500 requested adding taxon constraints to restrict these terms to Mus musculus, preventing their misuse in annotating human datasets where the DN2a/DN2b distinction is not applicable.

## Changes Made

Added 2 new lines to `cl-edit.owl`, one for each term, adding an `in_taxon some NCBITaxon:10090` (Mus musculus) constraint to CL_0002423 (DN2a thymocyte) and CL_0002424 (DN2b thymocyte). This is the standard CL pattern for species-restricted cell types.

## Resolution

Approved on first review in 4 commits. Simple difficulty because adding taxon constraints follows a well-established pattern in CL, and the biological rationale for restricting these terms to mouse is straightforward -- the DN2a/DN2b distinction is based on mouse-specific developmental staging.

## Curation Note (data quality)

This is a sound evaluation case overall: the ontological target is unambiguous (2 lines), gold PR #3570 is the **sole and complete** human resolution (no companion PRs), there is no base-state contamination or gold leakage, and the F1=1.0 results for attempts #235 (sonnet-4.5/copilot) and #139 (haiku-4.5/claude) are **genuine** — both diffs are byte-identical to the merged gold.

However, the case carries a durable scoring caveat that downstream aggregation should account for. Gold PR #3570 was itself produced by a Copilot agent that *initially added* `IAO_0000233`/`term_tracker_item` annotations on the taxon-constraint axioms. CL curator RiveraAndrea83 then explicitly commented "@copilot please remove term tracker from the edits", and the agent stripped them (commit e544598) before merge. The merged gold therefore deliberately omits term-tracker provenance.

The agents' own configuration (`ai4curation/cl-agent-config` `CLAUDE.md`) instructs: "Link back to the issue you are dealing with using the `term_tracker_item`." Two attempts complied with this standing instruction and were structurally penalized for it:

- **#199** (sonnet-4.5/claude): added the correct two `RO_0002162 some NCBITaxon_10090` constraints **plus** two separate `AnnotationAssertion(oboInOwl:term_tracker_item ... issues/3500)` lines. Precision 1.0, recall 0.5, F1=0.667 — the recall loss is entirely the instruction-compliant term-tracker lines.
- **#190** (opus-4.7/claude): added the correct two constraints but as axioms wrapped with an inline `Annotation(obo:IAO_0000233 ...)`, so every changed line differs from gold and F1 collapses to 0.0 despite the ontology content being correct.

Both #199 and #190 substantively and correctly resolve issue #3500; metadiff materially under-represents their quality because the gold reflects a curator preference (no term tracker) that contradicts the agents' instructions. They should be judged on substance, not the misleading F1. `case_quality: ok` (not `poor`) because the gold is complete and the headline F1=1.0 attempts are genuine; this is a known instruction-vs-curator-preference / gold-renegotiated artifact rather than a broken reference.

