---
repo: obophenotype/uberon
issue_number: 3454
pr_number: 3455
issue_title: "Newly introduced crab and lobster terms violate taxon constraints"
issue_created_at: "2024-12-23"
pr_author: gouttegd
pr_merged_at: "2024-12-24"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 39
    deletions: 54
  - path: src/ontology/imports/ncbitaxon_terms.txt
    additions: 1
    deletions: 0
  - path: src/ontology/imports/merged_import.owl
    additions: 42
    deletions: 3
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: invertebrate-anatomy
tags:
  - taxon-constraint
  - crustacean
  - Pleocyemata
  - cross-reference-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Taxon constraint violation fix requiring taxonomic knowledge to find the correct common ancestor taxon for crab and lobster terms
case_quality: poor
case_quality_reason: gold_reserialization_and_odk_import_domination
companion_prs: []
scoring_caveat: "Single gold PR #3455, but its diff is dominated by ODK build-regenerated src/ontology/imports/merged_import.owl (42 add / 3 del) and a whole-file robot reserialization of uberon-edit.obo (xref normalization e.g. 'PMID: 17009928'->'PMID:17009928', tag/relationship reordering, trailing-whitespace trims, a 'has_part ! unipolar brush cell' label fill-in, and an EXACT->RELATED OMO:0003000 synonym change). The substantive curation the issue actually demanded is the ~15x 'in_taxon NCBITaxon:6712 + 6752' -> 'in_taxon NCBITaxon:6692 ! Pleocyemata' replacement. Metadiff scores attempts against the full noisy gold diff, so F1 severely under-represents quality. Judge attempts on the substantive in_taxon fix and the genuine import-membership requirement (adding NCBITaxon:6692 to ncbitaxon_terms.txt / merged_import.owl), not against reserialization noise."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3454 reported that newly introduced nerve terms for crabs and lobsters (from PR #3445) were causing taxon constraint violations. The terms had separate in_taxon restrictions to Astacidea (lobsters) and Brachyura (crabs), but this pattern conflicted with Uberon's taxon constraint checking system. Additionally, several cross-references had formatting errors (spurious spaces after colons, e.g., "PMID: 17009928").

## Changes Made

The PR replaced the separate in_taxon restrictions to Astacidea (NCBITaxon:6712) and Brachyura (NCBITaxon:6752) with a single restriction to their common ancestor Pleocyemata (NCBITaxon:6692). The Pleocyemata term was explicitly imported into the NCBITaxon import (ncbitaxon_terms.txt and merged_import.owl). Cross-reference formatting errors were also corrected across multiple term stanzas, resulting in 39 additions and 54 deletions.

## Resolution

Hard difficulty. An agent would need to understand Uberon's taxon constraint system, look up the NCBI taxonomy to find the appropriate common ancestor for Astacidea and Brachyura (Pleocyemata), update the import configuration to include the new taxon term, and fix the cross-reference formatting issues. The multi-file changes and taxonomic reasoning make this significantly more complex than a simple axiom edit. Same-day merge reflects the urgency of fixing constraint violations.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.** This is a single-PR resolution (verified: only PR #3455 references issue #3454; no companion PRs), so it is *not* a multi-PR partial-gold case. However, the gold PR's diff is a poor scoring reference for the following reasons:

- **ODK build-regenerated file domination.** `src/ontology/imports/merged_import.owl` contributes 42 additions / 3 deletions — version-string bumps (`2024-12-17` → `2024-12-23`), bulk `Declaration(Class(...))` lines, NCBITaxon stanza imports, disjointness GCIs, and a dropped `dcterms:title` annotation-property declaration. These are mechanically produced by the ODK import-refresh pipeline once Pleocyemata is added to `ncbitaxon_terms.txt`; they are not independent curator decisions and no agent reproduces them faithfully.
- **OWL/OBO serialization-order artifacts.** The gold `uberon-edit.obo` change (39 add / 54 del) is largely a whole-file `robot` reserialization commit: xref normalization (`[PMID: 17009928]` → `[PMID:17009928]`, sorted xref lists), `is_a`/`relationship` line reordering, trailing-whitespace trimming, a `has_part CL:4023161 ! unipolar brush cell` label fill-in, and a separate commit changing the STG/abbreviation synonyms from `EXACT` to `RELATED ... OMO:0003000`. Only ~15 line-pairs are the substantive curation the issue demanded.

**Substantive task** (what the issue #3454 author explicitly asked for): replace the contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship: in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon NCBITaxon:6692` (Pleocyemata) on the ~15 affected stomatogastric terms, and add NCBITaxon:6692 to the NCBITaxon import so the build stays complete.

**Scoring impact:**

- All 4 `claude` attempts (pr309, pr233, pr178, pr92; blob `c8688e4`) produced a byte-identical, perfectly-scoped minimal diff whose 15 `in_taxon ... ! Pleocyemata` lines are **byte-identical to gold's substantive lines**, yet score F1=0.073 (recall=1.000, precision=0.038) purely because they did not reproduce the ODK/reserialization noise. F1 grossly under-represents quality here.
- The `codex`/`opencode` attempts (pr17, pr12, pr53, pr35; F1≈0.47) ran `robot convert` and so partially reproduced the reserialization hunks (recall ≈0.82–0.84), but did not regenerate `merged_import.owl`; their F1 also under-represents the correctness of the core fix.
- **Genuine shared defect (not a scoring artifact):** none of the 8 attempts added `NCBITaxon:6692` to `ncbitaxon_terms.txt` / refreshed `merged_import.owl`, so all leave the import membership incomplete. This is a real `missed_requirement`, distinct from the reserialization noise.

Recommendation for downstream aggregation: down-weight or exclude this case's raw F1; score attempts on the substantive `in_taxon` replacement plus the import-membership requirement rather than the full gold diff.
