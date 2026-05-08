---
repo: geneontology/go-ontology
issue_number: 31969
pr_number: 31988
issue_title: "Parentage issues within 'oxidoreductase activity' branch"
issue_labels:
  - enzymes
  - parent relationship query
issue_created_at: "2026-04-24"
issue_closed_at: "2026-04-27"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 66
    deletions: 38
scoping: mostly_scoped
scoping_notes: >-
  Primary changes are reparenting oxidoreductase terms per the issue, but also includes
  definition updates to align with RHEA reaction descriptions where the old definitions
  were inaccurate (e.g. GO:0008762, GO:0018525).
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - oxidoreductase
  - enzyme-classification
  - EC-alignment
  - RHEA
  - hierarchy-repair
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Complex multi-term reclassification requiring cross-referencing EC numbers, RHEA reactions, and GO hierarchy
---

## Context

Issue #31969 identified multiple parentage errors in the oxidoreductase activity branch of GO. Several terms were classified under the wrong oxidoreductase subclass based on their EC number assignments. For example, terms classified under "acting on the CH-OH group" (GO:0016616) that should have been under "acting on the CH-CH group" (GO:0016628) based on their actual reaction chemistry.

## Changes Made

In `src/ontology/go-edit.obo` (66 additions, 38 deletions across multiple term stanzas):

**Reparented terms** (examples):
- GO:0004498 (calcidiol 1-monooxygenase): moved from GO:0016709 (NAD(P)H donor) to GO:0016713 (iron-sulfur protein donor) — the enzyme uses ferredoxin, not NAD(P)H
- GO:0008762 (UDP-N-acetylmuramate dehydrogenase): moved from GO:0016616 (CH-OH group) to GO:0016628 (CH-CH group) — reaction acts on a double bond, not a hydroxyl
- GO:0008867 (formate dehydrogenase): moved from GO:0016620 (aldehyde/oxo group) to GO:0016726 (CH or CH2 groups)
- GO:0010277 (chlorophyllide a oxygenase): moved from GO:0016703 (internal monooxygenases) to GO:0016709 (paired donors, NAD(P)H)

**Definition updates**:
- GO:0008762: updated substrate names to use correct alpha-D- stereochemistry, changed xref from EC to RHEA:12248
- GO:0018525 (4-hydroxybenzoyl-CoA reductase): updated reaction equation to use explicit oxidized/reduced ferredoxin notation from RHEA:29603

**Added provenance**: term_tracker_item linking to #31969 on all modified terms.

## Resolution

This required deep understanding of:
1. The oxidoreductase hierarchy in GO (which subclass maps to which donor/acceptor chemistry)
2. EC number classification scheme and how EC numbers map to GO parents
3. RHEA reaction equations to determine the actual chemistry

Hard difficulty because: (a) affects 25+ terms, (b) each reclassification requires verifying the reaction mechanism against EC/RHEA, (c) some definitions needed updating alongside the reparenting to maintain consistency.
