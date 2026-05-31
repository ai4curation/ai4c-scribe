---
repo: monarch-initiative/mondo
issue_number: 9963
pr_number: 10222
issue_title: "RNU12 - related minor spliceopathy disorder"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-02-20"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - spliceopathy
  - gene-disease
  - RNU12
  - ClinGen
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New gene-disease term requiring correct logical axioms linking RNU12 to a spliceopathy phenotype
case_quality: poor
case_quality_reason: placeholder_id_artifact
companion_prs: []
scoring_caveat: "Gold #10222 is the complete, clean, single-PR human resolution (no companion PRs, no leakage, no repudiation). However the new term's canonical ID MONDO:1060223 is assigned only at merge; all 11 agents necessarily used a placeholder ID (mostly MONDO:7770747), so the gold `id:` line plus both `is_a: MONDO:1060223 ...` child-placement lines and the trailing label comment (~4 of 9 gold additions) are structurally unmatchable for every attempt. This caps recall/F1 across all attempts (best_f1=0.583) even when the substantive curation is correct. Judge attempts on substance vs the issue + gold facts, treating the MONDO ID as a normalizable placeholder; metadiff F1 systematically UNDER-represents quality here."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A new term request was filed for an RNU12-related minor spliceopathy disorder. RNU12 encodes a small nuclear RNA component of the minor spliceosome (U12-type), and mutations disrupt splicing of U12-type introns. The resulting phenotype is a developmental disorder with features overlapping other spliceopathies.

The request was supported by ClinGen curation and required creating a new Mondo term with appropriate gene-disease logical axioms and classification under the spliceopathy hierarchy.

## Changes Made

Added a single new term stanza to `src/ontology/mondo-edit.obo` with 15 lines of additions. The term includes a definition, logical axioms linking to RNU12 via germline mutation, and appropriate classification. This is a straightforward new term addition following established Mondo patterns for gene-disease terms.

## Resolution

Medium difficulty because it requires understanding the spliceopathy disease hierarchy and constructing the correct equivalence axiom linking the disease to RNU12. An agent would need to determine the appropriate parent class and apply the standard gene-disease term pattern with proper provenance attribution.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-15 during eval review of all 11 attempts.

The gold PR (#10222) is itself a good reference: a single human commit by @MeeSiing, tightly scoped to one new term stanza plus two child re-classifications, with no companion PRs, no eval-base contamination, no gold leakage, and no curator repudiation (issue #9963 was approved-first-time).

The data-quality issue is a **structural metadiff artifact**, not a defective gold:

- Mondo assigns the canonical permanent ID for a new term (`MONDO:1060223` in gold) only at merge/ID-mint time. Agents cannot know it in advance and all 11 attempts used a placeholder (10/11 used `MONDO:7770747`).
- Because whole-file OBO metadiff does not normalize the new term's ID, the gold additions `id: MONDO:1060223`, the two `is_a: MONDO:1060223 {...} ! RNU12-related minor spliceopathy disorder` child-placement lines, and their trailing label comments are unmatchable for **every** attempt by construction — roughly 4 of the 9 gold additions.
- Consequently F1 is compressed across the board (best_f1 = 0.583 for gpt-5.5/opencode), even though several attempts (notably eval PRs #86, #67, #50, #442) reproduced the substantive curation correctly: correct ClinGen label, definition, RNU12 `has_material_basis_in_germline_mutation_in HGNC:19380` axiom, both requested children re-parented, and (in the better attempts) the ClinGen EXACT synonym with the `OMO:0002001` source qualifier.

Additional reviewer observations affecting scoring (not poor-case flags, but normal metadiff under-representation):

- The gold parents the new term **only** under `hereditary disease` (MONDO:0003847), despite the issue requesting both `hereditary disease` and `syndromic disease`. Every attempt added both parents — a defensible literal reading of the issue but a divergence from merged curation that lowers recall.
- The gold has **no** `intersection_of` logical definition; many attempts added one (some with incorrect genus, e.g. `syndromic disease` or `human disease`).
- The gold also adds `IAO:0000233` issue provenance and (for SCAR33) the missing RNU12 gene axiom to the two child stanzas; attempts varied in catching these.

Downstream scoring/aggregation should down-weight or exclude raw metadiff F1 for this case and rely on the per-attempt narrative reviews in `analysis/mondo/results/reviews/`, which judge substance against the issue and the gold facts.
