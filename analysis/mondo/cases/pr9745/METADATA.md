---
repo: monarch-initiative/mondo
issue_number: 9707
pr_number: 9745
issue_title: "Mondo request for SCN5A disease entity for ClinGen"
issue_labels:
  - New term request
  - user request
issue_created_at: "2025-10-30"
pr_author: katiermullen
pr_merged_at: "2025-11-12"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 40
    deletions: 1
scoping: tightly_scoped
scoping_notes: Adds two new terms and reclassifies a related existing term.
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: cardiac-disease
tags:
  - gene-disease
  - SCN5A
  - cardiac
  - ClinGen
  - cardiac-conduction
  - reclassification
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term addition with reclassification requiring cardiac disease domain knowledge and ClinGen coordination
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_artifact
companion_prs: []
scoring_caveat: "The gold PR #9745 allocated canonical IDs MONDO:1010180 (cardiogenetic rhythm disorder) and MONDO:1010181 (SCN5A-related cardiac rhythm disorder). Every agent instead used the eval base's auto-allocated placeholder NTR range MONDO:7770003/MONDO:7770004. Because the bulk of both the gold and agent diffs are `is_a:` lines referencing these new-term IDs, OBO metadiff scores nearly every conceptually-correct reparenting as a miss, structurally capping F1 well below the true quality for all 11 attempts. Additionally the gold includes an out-of-scope cleanup (atrioventricular dissociation MONDO:0000465 reclassified from MONDO:0003847 hereditary disease to MONDO:0100042 cardiac conduction defect, plus excluded_subClassOf and two excluded_from_qc_check relationships) that the issue never requested, further depressing recall for well-scoped agents. Judge attempts against the issue text and the gold's term-creation/reparenting substance, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

ClinGen requested new SCN5A-related disease entities for their gene curation workflow. SCN5A encodes a sodium channel subunit critical for cardiac conduction, and mutations cause a spectrum of cardiac rhythm disorders including Brugada syndrome, long QT syndrome type 3, and conduction defects. The request required creating two new gene-disease terms and adding child terms as specified in the detailed issue discussion.

Additionally, the existing term "atrioventricular dissociation" needed reclassification from its hereditary parent to "cardiac conduction defect" because the condition is not necessarily hereditary.

## Changes Made

Added two new SCN5A-related disease terms to `src/ontology/mondo-edit.obo` with associated child terms (40 additions), and reclassified "atrioventricular dissociation" by updating its parent (1 deletion to remove the old parent). The 2 commits reflect the new term additions and the parent reclassification as separate logical changes.

## Resolution

Hard difficulty because the PR involves multiple coordinated changes: creating two new gene-disease terms, adding their children, and correcting the classification of an existing term. An agent would need to understand the SCN5A channelopathy spectrum, determine correct parent classes for each new term, and recognize that the existing atrioventricular dissociation term was incorrectly classified as hereditary.

## Curation Note (data quality)

Flagged `case_quality: poor` after reviewing all 11 attempts (claude-opus-4.7, 2026-05-15).

Two factors make the metadiff F1 a poor proxy for quality on this case:

1. **Placeholder-vs-canonical MONDO ID artifact.** The merged gold PR #9745 uses canonical IDs `MONDO:1010180` (cardiogenetic rhythm disorder) and `MONDO:1010181` (SCN5A-related cardiac rhythm disorder). Every agent used the eval base's auto-allocated placeholder range `MONDO:7770003`/`MONDO:7770004`. Since most of both diffs are `is_a:` lines that reference these IDs, OBO metadiff scores nearly every correct reparenting as a miss. F1 is structurally compressed (best 0.615, most ~0.31, lowest 0.216) even where agents attached the right child to the conceptually right parent.

2. **Out-of-scope gold cleanup.** The gold also reclassified `atrioventricular dissociation` (MONDO:0000465) from `MONDO:0003847` (hereditary disease) to `MONDO:0100042` (cardiac conduction defect) and added `excluded_subClassOf` plus two `excluded_from_qc_check` relationships. The issue (#9707) never requested this; it is incidental curator cleanup that no well-scoped agent would reproduce, accounting for the gold's single deletion and several additions and further depressing recall.

This issue was resolved by a single PR (#9745); no companion PRs exist. Recommended handling: down-weight or exclude this case from line-level F1 aggregation and judge attempts against the issue text and the gold's term-creation/reparenting substance. On that basis the best attempts (#261 kimi-k2.6/opencode F1=0.615; #407 claude-opus-4.7/claude F1=0.311; #89/#68 gpt-5.5/opencode F1=0.311) are substantively strong partial successes, far better than their raw F1 suggests.
