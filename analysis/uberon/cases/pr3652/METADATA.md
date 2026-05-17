---
repo: obophenotype/uberon
issue_number: 3651
pr_number: 3652
issue_title: "Newly introduced disjointness axioms cause OBO serialisation issue"
issue_created_at: "2026-01-19"
pr_author: aleixpuigb
pr_merged_at: "2026-01-21"
pr_num_commits: 7
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 8
  - path: src/ontology/components/disjoint_union_over.owl
    additions: 1
    deletions: 0
  - path: src/ontology/imports/merged_import.owl
    additions: 7012
    deletions: 6419
scoping: tightly_scoped
task_type: other
difficulty: hard
scope: structural_refactor
review_outcome: approved_first_time
domain_area: ontology-infrastructure
tags:
  - disjointness
  - OBO-serialisation
  - ODK-component
  - refactor
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Structural refactoring moving disjoint axioms between files to fix OBO serialisation, requiring ODK pipeline understanding
case_quality: poor
case_quality_reason: robot_convert_reserialization_churn
companion_prs: []
scoring_caveat: "metadiff F1=0.001 across all 3 attempts is a robot-convert / ODK-pipeline reserialization artifact. The substantive gold change is only 9 lines (8 deletions in uberon-edit.obo, 1 addition in disjoint_union_over.owl); gold also carries ~13,431 lines of unrelated merged_import.owl pipeline churn (chebi#->chebi/ prefix migration, RO import refresh, version-date bump 2026-01-12->2026-01-20) that no agent should reproduce. Additionally the gold is imperfect: it re-adds only DisjointClasses(UBERON_0000001 GO_0110165) and silently drops the GO:0005623 disjointness. Judge attempts against issue #3651 solution (B), not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3651 reported that newly introduced disjointness axioms in uberon-edit.obo were causing OBO serialisation problems. The OBO format has limited support for certain OWL axiom patterns, and disjoint union axioms needed to be housed in a dedicated OWL component file rather than in the OBO edit file.

## Changes Made

The PR removed eight lines of disjoint axioms from src/ontology/uberon-edit.obo and relocated them to the OWL component file src/ontology/components/disjoint_union_over.owl. The merged_import.owl file was regenerated with significant churn (7012 additions, 6419 deletions) as a side effect of the pipeline rebuild. Seven commits indicate iterative refinement during the migration.

## Resolution

Hard difficulty. An agent would need to understand the limitations of OBO format serialisation for disjoint union axioms, know that the ODK pipeline supports component-based OWL files for axioms that cannot be represented in OBO, and correctly move the axioms while ensuring the build pipeline picks them up. The large diff in merged_import.owl is a pipeline artifact, not manual editing. Two-day turnaround from issue to merge.

## Curation Note (data quality)

**Flagged `case_quality: poor` (robot_convert_reserialization_churn) by claude-opus-4.7 on 2026-05-16.**

The reported metadiff F1=0.001 (P=0.000) for all three attempts (#292 sonnet-4.5, #261 opus-4.7, #165 haiku-4.5) is an evaluation artifact, not a quality signal:

1. **Pipeline reserialization churn dominates the gold diff.** The substantive human change in PR #3652 is only ~9 lines: 8 deletions in `src/ontology/uberon-edit.obo` (the two orphan label-less `[Term] id: GO:0005623` / `[Term] id: GO:0110165` frames) plus **one** added `DisjointClasses` line in `src/ontology/components/disjoint_union_over.owl`. The remaining ~13,431 changed lines are entirely in `src/ontology/imports/merged_import.owl` and are pure ODK release-pipeline reserialization: `chebi#…` → `chebi/…` annotation/object-property prefix migration, RO import refresh (new RO_0018xxx chemical-relationship properties), CHEBI/GO declaration additions, and a version-date bump (`2026-01-12` → `2026-01-20`). An agent neither would nor should hand-author this regenerated import file; whole-file metadiff therefore craters recall/precision to ~0 for every attempt regardless of correctness.

2. **Single-PR resolution (Step 3a N/A).** Issue #3651 was resolved entirely by PR #3652; the only cross-reference on the issue is #3652 itself. `companion_prs: []`.

3. **The gold itself is imperfect.** Gold #3652 re-adds only `DisjointClasses(UBERON_0000001 GO_0110165)` to the component and silently **drops the `GO:0005623` disjointness axiom** (GO:0005623 was "obsolete cell" by then). All three agents preserved *both* the GO_0005623 and GO_0110165 disjointness axioms, which is a more faithful reading of the issue's intent ("move the disjointness axioms"). A strict line-match thus penalizes the agents for being more semantically complete than the gold.

**Adjudication:** Judge attempts against issue #3651's solution (B) (curator-endorsed: move the axioms to an imported OWL Functional Syntax component) and the issue's explicit ask, not the metadiff. On that basis all three attempts are substantive successes: #261 (opus) is the cleanest minimal implementation; #292 (sonnet) is correct but adds a defensible extra duplicate into `external-disjoints.obo`; #165 (haiku) is correct but with a thin/stub PR writeup. Downstream scoring/aggregation should exclude or down-weight the F1 for this case.
