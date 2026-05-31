---
repo: monarch-initiative/mondo
issue_number: 9703
pr_number: 9770
issue_title: "Updates to Gene-Disease Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group"
issue_labels:
  - New term request
  - user request
issue_created_at: "2025-10-29"
pr_author: sabrinatoro
pr_merged_at: "2025-11-20"
pr_num_commits: 7
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 60
    deletions: 9
  - path: src/ontology/Makefile
    additions: 1
    deletions: 1
  - path: src/sparql/qc/general/qc-definition-containing-underscore.sparql
    additions: 5
    deletions: 0
scoping: tightly_scoped
scoping_notes: Changes focused on porphyria disease branch with minor supporting infrastructure changes.
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: rare-disease
tags:
  - porphyria
  - ClinGen
  - gene-disease
  - inheritance-pattern
  - reclassification
  - new-terms
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex multi-term restructure of porphyria branch driven by ClinGen expert review requiring new terms, relabeling, and inheritance updates
case_quality: poor
case_quality_reason: placeholder_vs_canonical_mondo_id
companion_prs: []
scoring_caveat: "The gold PR #9770 created three new grouping terms with the registered IDs MONDO:0700382 (HMBS-related hepatic porphyria), MONDO:0700383 (PPOX-related hepatic porphyria) and MONDO:0700384 (porphyria, acute intermittent, nonerythroid variant). The mondo-agent-config CLAUDE.md mandates that agents assign new-term IDs from the MONDO:777xxxx placeholder range, which all four attempts correctly did (MONDO:7770003/7770004/7770005). Metadiff therefore scores every new-term id:/name:/def:/intersection_of: line AND every lumping is_a: axiom that references a new ID as a miss by construction, even when the agent's substance is correct. This caps F1 well below the substantive quality for every attempt (best=0.441). Judge attempts on substance (gene-grouping equivalence axioms, lumping, definitions, provenance) rather than the metadiff. Note a SEPARATE genuine error common to all attempts that is NOT an artifact: every agent renamed the primary name: of ~6 existing terms, whereas the curator kept the original labels and added the ClinGen names only as EXACT synonyms."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

The ClinGen Errors of Inborn Metabolism (EIM) group requested comprehensive updates to porphyria disease entities in Mondo. This included new gene-disease classifications, updated inheritance patterns, new labels, and new child terms. The changes were coordinated via a shared spreadsheet tracking all required updates across the porphyria disease branch.

Porphyrias are a group of metabolic disorders caused by enzyme deficiencies in the heme biosynthesis pathway. Accurate classification requires understanding both the biochemical pathway and the clinical presentations, which differ between acute and cutaneous forms.

## Changes Made

The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`, involving new labels, new terms, updated inheritance annotations, and restructured classification for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting underscores in definitions were also included. The 7 commits reflect an iterative curation process responding to expert review feedback.

## Resolution

Hard difficulty because the porphyria branch restructure required coordinating multiple types of changes (new terms, relabeling, inheritance updates, reclassification) across several related terms while maintaining consistency with ClinGen's expert classifications. An agent would need to interpret the spreadsheet-based requirements and apply domain-specific knowledge about porphyria subtypes.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15.

**Single-PR resolution (no companion PRs).** Issue #9703 was resolved entirely by PR #9770
(`gh search prs "9703"` returns only #9770; the other porphyria PRs — #8394, #8206, #5151,
#2855 — are unrelated older work). Step 3a does not apply.

**Placeholder-vs-canonical MONDO ID artifact (primary reason).** The gold PR created three
new grouping terms with registered IDs:

- `MONDO:0700382` HMBS-related hepatic porphyria
- `MONDO:0700383` PPOX-related hepatic porphyria
- `MONDO:0700384` porphyria, acute intermittent, nonerythroid variant

The `ai4curation/mondo-agent-config` CLAUDE.md explicitly instructs agents: *"New terms
start MONDO:777xxxx"*. All four attempts correctly followed this and used
`MONDO:7770003/7770004/7770005`. OBO metadiff does not normalize new-term ID minting, so
every `id:`, `name:`, `def:`, `intersection_of:` line on the three new terms **and** every
lumping `is_a:` axiom that references a new ID (≈6 lines pointing existing porphyria
entities at the new HMBS/PPOX/UROD groupers) is scored as a miss by construction, in every
attempt — including the strongest run. This systematically caps F1 far below substantive
quality (best observed F1 = 0.441; substance is appreciably better). Downstream
scoring/aggregation should down-weight or exclude this case, and reviewers should judge
attempts on substance (correct gene-grouping equivalence axioms `hepatic porphyria` +
`has_material_basis_in_germline_mutation_in <gene>`, correct lumping targets, faithful
GCEP definitions, ClinGen-attributed synonyms, `term_tracker_item` provenance) rather than
the metadiff.

**Separate genuine error common to all attempts (NOT an artifact).** Every agent renamed
the primary `name:` of ~6 existing terms (MONDO:0008319, 0009902, 0010420, 0013000,
0100498, 0800180), demoting the original labels to synonyms. The curator deliberately did
**not** rename any existing term — the ClinGen names were added only as EXACT synonyms
(with the `OMO:0002001` ClinGen qualifier) while primary labels were preserved. This is a
legitimate quality finding scored in the individual reviews (`wrong_pattern`) and is not
covered by the ID-artifact caveat.

