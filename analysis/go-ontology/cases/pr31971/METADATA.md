---
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31971
issue_title: "protoporphyrinogen oxidase activity terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 10
    deletions: 5
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: molecular_function
tags:
  - enzymes
  - EC-alignment
  - RHEA-xref
  - protoporphyrinogen
  - hierarchy-refactor
  - definition-update
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex enzyme hierarchy refactoring requiring reconciliation of EC/RHEA entries with GO term definitions and parent-child relationships
case_quality: ok
case_quality_reason: gold_pr_fully_resolves_issue_as_written; followup_pr_addresses_post_hoc_review
companion_prs: [31979]
scoring_caveat: "metadiff vs #31971 is a FAIR target: #31971 implements all 6 explicit checkboxes in the issue #31965 body exactly (attempt pr122 legitimately scored F1=1.0). Companion PR #31979 ('X as acceptor' renaming of GO:0004729 and GO:0070819) was triggered by a post-hoc reviewer comment from @pgaudet on 2026-04-27 (after issue creation and #31971 merge) and is NOT in the issue body agents were given; do not penalize attempts for not anticipating it. The review_outcome=changes_requested reflects this naming follow-up, not a defect in the agents' or human's resolution of the issue as stated."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #31965 identified that the protoporphyrinogen oxidase activity sub-hierarchy had incorrect mappings: the parent term GO:0070818 and its children did not correctly correspond to their EC and RHEA cross-references. Each term needed its definition, xrefs, and parent relationships realigned to match the actual biochemical reactions catalogued in EC/RHEA.

## Changes Made

In `src/ontology/go-edit.obo`, the protoporphyrinogen oxidase hierarchy was refactored:
- GO:0070818 (parent): Definition updated to include 3x stoichiometry matching RHEA:64720
- Child terms: EC and RHEA xrefs corrected to point to the right reactions
- Definitions rewritten to accurately describe each specific reaction variant
- Parent-child relationships verified against the reaction specificity hierarchy

Net +5 lines reflecting additional xrefs and expanded definitions.

## Resolution

The PR was merged same-day but received review feedback from @pgaudet requesting that child term names follow the standard "X as acceptor" naming pattern. This was addressed in follow-up PR #31979. This case demonstrates how enzyme term refactoring often requires multiple rounds: first the biochemical content is corrected, then naming conventions are applied.

## Curation Note (data quality)

Issue #31965 was resolved by **two** human PRs: the scored gold **#31971** (biochemical content: defs, EC/RHEA xrefs, label change to "quinone-dependent...") and companion **#31979** ("X as acceptor" restyling of GO:0004729 and GO:0070819).

Unlike the classic partial-gold pattern, the gold PR here is a **fair scoring target**. The issue #31965 body contains six explicit checkboxes, and #31971 implements all six exactly — including specifying the literal target label "quinone-dependent protoporphyrinogen oxidase activity". Attempt **pr122** (gpt-5.5/codex) legitimately reproduces #31971 and scores F1=1.0; the attempt F1 spread (1.0 → 0.33) reflects real quality differences, not a misaligned reference.

The `review_outcome: changes_requested` and companion PR **#31979** stem from a **post-hoc reviewer comment** (@pgaudet, 2026-04-27 — three days after the issue was filed and #31971 merged) proposing the "X as acceptor" convention. That naming request is **not present in the issue body the agents were given**, so attempts must **not** be penalized for not anticipating it. None of the 11 attempts attempted the "X as acceptor" rename, which is correct behavior given their inputs.

Practical scoring guidance: judge attempts against issue #31965 + gold PR #31971 only. Do not treat the absence of #31979's renaming as an agent failure, and do not down-weight or exclude this case — the metadiff is reliable here. The single discriminating curation subtlety (which the metadiff does capture) is the GO:0070819 synonym restructuring: demote `protoporphyrinogen-IX:menaquinone oxidoreductase activity` EXACT→NARROW and preserve the old label `menaquinone-dependent protoporphyrinogen oxidase activity` as a NARROW synonym. Flagged by claude-opus-4.7 on 2026-05-15.
