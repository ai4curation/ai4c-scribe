---
repo: obophenotype/uberon
issue_number: 3678
pr_number: 3679
issue_title: "Add bone part terms from HubMap - HRA"
issue_created_at: "2026-03-20"
pr_author: dosumis
pr_merged_at: "2026-03-25"
pr_num_commits: 5
files_changed:
  - path: src/templates/hra-skeleton.template.tsv
    additions: 286
    deletions: 0
  - path: src/ontology/components/hra_skeleton.owl
    additions: 5156
    deletions: 0
  - path: src/templates/hra-skeleton-prefixes.owl
    additions: 15
    deletions: 0
  - path: src/ontology/uberon-odk.yaml
    additions: 4
    deletions: 0
  - path: src/ontology/uberon.Makefile
    additions: 10
    deletions: 0
  - path: src/ontology/Makefile
    additions: 12
    deletions: 4
  - path: src/ontology/catalog-v001.xml
    additions: 1
    deletions: 0
  - path: docs/odk-workflows/RepositoryFileStructure.md
    additions: 1
    deletions: 0
  - path: src/templates/hra-skeleton-reports/corrections_report.md
    additions: 79
    deletions: 0
  - path: src/templates/hra-skeleton-reports/duplicate_candidates_report.md
    additions: 1536
    deletions: 0
  - path: src/templates/hra-skeleton-reports/term_mapping_table.md
    additions: 119
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: skeletal-anatomy
tags:
  - HRA
  - HuBMAP
  - ROBOT-template
  - batch-import
  - component
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale batch import of 386 skeletal terms via ROBOT template component, requiring ODK pipeline integration and prefix management
case_quality: poor
case_quality_reason: gold_artifact_leakage
companion_prs: [3686, 3685]
scoring_caveat: "Two of three attempts (eval #305 sonnet, #175 haiku) checked in hra_skeleton.owl / hra-skeleton.template.tsv that are byte-identical to the already-merged gold (git blobs 9934d34b0 / b10105932 vs gold 9934d34b01 / b10105932c). The 5156-line component and 286-line bespoke-definition template cannot be independently regenerated from the issue CSV; gold PR #3679 merged upstream 2026-03-25, before these eval runs, so the agents reproduced/retrieved the published gold rather than synthesizing it. Metadiff F1 (0.926, 0.894) over-represents quality for the leaking attempts; F1=0.001 for the opus attempt (#267) under-represents the only genuine independent work. Judge attempts on independent reasoning evidenced in reports/PR comments, not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Human Reference Atlas (HRA) / HuBMAP project needed 386 new skeletal anatomical terms integrated into Uberon. These terms cover bone zones, projections, fossae, foramina, and other features of the human skeleton. IDs were assigned in the automation range UBERON:1200004 through UBERON:1200389, each with definitions, part_of axioms, cross-references, and present_in_taxon restrictions to NCBITaxon:9606.

## Changes Made

Rather than editing uberon-edit.obo directly, the PR introduced a ROBOT template-based component (hra_skeleton.owl) built from src/templates/hra-skeleton.template.tsv. The ODK configuration (uberon-odk.yaml) was updated to register the new component, and a custom Makefile rule was added in uberon.Makefile to supply dcterms/dc prefix declarations during the build. Four problematic terms were dropped after quality review, as documented in a corrections report.

## Resolution

This is a complex case requiring understanding of the ODK component pipeline, ROBOT template syntax, prefix management in OWL builds, and batch term quality review. The PR touches 11 files across templates, build configuration, and documentation. An agent would need to generate the ROBOT template TSV, wire it into the build system, and handle edge cases around prefix declarations. Approved after review with no changes requested.

## Curation Note (data quality)

**Flagged `case_quality: poor` — gold-artifact leakage (Step 3b).**

Gold PR #3679 was itself produced "via an agentic workflow" (issue #3678 comment by dosumis) followed by substantial human curation: the `parents_as` column was discarded as unreliable and parents re-derived from term labels, ~9 mismatch corrections were applied (see `corrections_report.md`), and four likely-duplicate terms were dropped before merge. It was merged upstream on 2026-03-25.

The eval runs occurred after that merge. Inspection of git blob hashes shows:

- eval #305 (sonnet): `hra_skeleton.owl` blob `9934d34b0` and `hra-skeleton.template.tsv` blob `b10105932` — **byte-identical** to gold blobs `9934d34b01` / `b10105932c`.
- eval #175 (haiku): `hra_skeleton.owl` blob `9934d34b0` — **byte-identical** to gold.

A 5156-line ROBOT-template-generated OWL component (with a fixed `releases/2026-03-20` version IRI and deterministic declaration ordering) and a 286-line template in which every row carries a unique 150–250-word genus-differentia definition plus corrections-report-driven parent fixes cannot be independently regenerated bit-for-bit from the issue CSV. The byte-identity indicates the leaking attempts retrieved/reproduced the already-published gold artifact rather than synthesizing it. The eval-base branch `eval-base-issue-3678` does **not** contain these files (404), but the eval repo's default branch and upstream `obophenotype/uberon` both do — the most plausible leakage path.

Consequence for scoring:

- Metadiff F1 for #305 (0.926) and #175 (0.894) **over-represents** capability; it rewards copying a merged answer.
- Metadiff F1 for #267 (opus, 0.001) **under-represents** quality: it is the only attempt that did genuine independent work — a conservative 129-row draft template plus a data-quality report that independently rediscovered the same CSV defects the gold's own corrections report documents (non-bone `parents_as` IDs, row-shifted rib/vertebra parents, ASCTB-TEMP/FMA URIs). Its main genuine shortfall is over-aggressive duplicate exclusion (~102 qualified "... of <bone>" terms the gold kept as new terms).

Downstream aggregation should exclude or heavily down-weight the metadiff for this case and judge attempts on the independent reasoning in their reports/PR comments. Companion PRs #3686 (template/prefix refinement) and #3685 (release integration) are post-merge follow-ups, not separate sub-steps — gold #3679 is the complete substantive resolution of the issue, so this is a leakage case, not a partial-gold case.
