---
repo: monarch-initiative/mondo
issue_number: 5726
pr_number: 10155
issue_title: "Add non-human animal diseases from VeNom"
issue_created_at: "2022-12-12"
pr_author: katiermullen
pr_merged_at: "2026-04-16"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9006
    deletions: 0
scoping: loosely_scoped
scoping_notes: Bulk addition of hundreds of non-human animal disease terms from the VeNom coding system.
task_type: new_term
difficulty: hard
scope: structural_refactor
review_outcome: approved_first_time
domain_area: veterinary-disease
tags:
  - VeNom
  - non-human-animal
  - bulk-addition
  - veterinary
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale batch import of veterinary disease terms requiring cross-reference alignment and classification decisions across multiple animal groups
case_quality: poor
case_quality_reason: gold_leakage_base_contamination
companion_prs: [10145, 10231, 10232, 10234, 10235, 10233]
scoring_caveat: "The three F1=1.0 attempts (#71, #90, #263) are gold-leakage artifacts: in each, the substantive 9006-line change is a github-actions[bot] commit byte-identical to gold PR #10155 (all 724 curator-minted MONDO IDs, ORCIDs, NCBITaxon assignments), while the actual eval-agent commit is empty (0/0). The agent could not have independently minted 724 canonical MONDO IDs — the curated VeNom source TSVs were never committed to the repo (gold #10155 only touches mondo-edit.obo) and the agent comments confirm they were unavailable. Additionally the gold is only Template 2 of a multi-PR resolution of issue #5726 (#10145 Template 1 xrefs is the eval base; #10231/#10232/#10234/#10235/#10233 are later body-system tranches). The codex attempts (#153/#47 F1=0.002, #158 F1=0.0) ran without the leak and reflect the true difficulty. Do NOT count #71/#90/#263 as three independent perfect successes; exclude or heavily down-weight this case in aggregation."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #5726 was a long-running initiative (opened December 2022) to incorporate non-human animal diseases from the VeNom (Veterinary Nomenclature) coding system into Mondo. VeNom contains over 6,000 diagnosis entries spanning large animals, small animals, farm animals, equines, and exotics. This PR represents one tranche of that effort, adding curated veterinary disease terms with appropriate VeNom cross-references and classifications.

## Changes Made

The PR added 9,006 lines to `src/ontology/mondo-edit.obo` across 3 commits, with zero deletions. Each new term stanza includes a label, definition, VeNom cross-reference, and classification under the non-human animal disease hierarchy. The scale of this change required careful curation to map VeNom diagnoses to appropriate Mondo parent classes and to exclude entries that are phenotypes rather than diseases.

## Resolution

Complex difficulty due to the sheer volume of terms and the need for systematic curation decisions. Each VeNom entry required evaluation of whether it represents a true disease (vs. a phenotype or procedure), selection of an appropriate parent class, and construction of valid cross-references. This task is not well-suited to a single agent pass and instead required iterative human curation across multiple PRs addressing the same long-running issue.

## Curation Note (data quality)

Flagged `case_quality: poor` on 2026-05-15 by claude-opus-4.7 after reviewing all 6 attempts.

**Two compounding problems make this an unreliable evaluation case:**

1. **Gold-leakage / eval base-state contamination (primary).** The three attempts reporting F1=1.0 (eval PRs #71, #90, #263) did not produce the scored work. In each eval PR the substantive change is a `github-actions[bot]` commit whose content is **byte-identical to gold PR #10155** — all 724 curator-minted MONDO IDs in the same sequence (MONDO:1010206, MONDO:1013000–1013014, …), identical ORCID provenance, identical `disease_has_infectious_agent NCBITaxon:*` assignments, even mirrored commit messages ("update due to qc failure" / "Add VeNom non-human animal disease analogs"). The actual `eval-agent` commit in every one of these PRs is **empty (0 additions / 0 deletions)**. Independently minting 724 brand-new canonical MONDO IDs is impossible without the gold; gold PR #10155 only modifies `mondo-edit.obo` (the curated VeNom TSVs were never committed to the repo) and the agent comments themselves state those TSVs were unavailable. The perfect scores are pure contamination artifacts and the true outcome for #71/#90/#263 is **no_output**.

2. **Multi-PR partial gold (Step 3a, secondary).** Issue #5726 (opened Dec 2022) was a long-running VeNom import resolved across at least six human PRs. The eval base branch `eval-base-issue-5726` is pinned at `7fe96d42e` = the merge of **#10145** ("add venom xrefs", Template 1, 229 NHA exact-match xrefs). The gold for this case is **#10155** ("Add non-human animal diseases from VeNom", Template 2, 728 new cross-species-analog terms) only. Later body-system tranches (**#10231** infectious diseases, **#10232** reproductive, **#10234** hematopoietic, plus open **#10233** masses, **#10235** endocrine) further resolve the same issue. Scoring any single-pass attempt against #10155 alone never captures the full issue resolution.

**Companion PRs:** #10145 (eval base / Template 1), #10231, #10232, #10234, #10235, #10233.

**Scoring guidance:** Exclude or heavily down-weight this case in aggregation. The three opencode "1.0" runs must not be counted as three independent perfect successes (they share the same leaked diff). The codex runs (#153/#47 = small correct scoped 4-line edit; #158 = unrelated off-target axiom change) are the only attempts reflecting genuine model behavior, and their near-zero metadiff under-represents (#153/#47) the quality of their honest, in-scope reasoning under genuinely missing curated inputs.
