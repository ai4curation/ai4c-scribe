---
repo: geneontology/go-ontology
issue_number: 31967
pr_number: 31968
issue_title: "Reparent 49 EC:1.14.14.x terms from GO:0016709 to GO:0016712 (CYP450 reclassification)"
issue_labels:
  - enzymes
  - parent relationship query
issue_created_at: "2026-04-24"
issue_closed_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-24"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 56
    deletions: 7
scoping: tightly_scoped
scoping_notes: >-
  Every change is a reparent of an EC:1.14.14.x term from GO:0016709 to GO:0016712,
  plus term_tracker_item provenance additions. No unrelated edits.
task_type: reclassification
difficulty: medium
scope: structural_refactor
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - CYP450
  - cytochrome-P450
  - enzyme-classification
  - bulk-reparent
  - EC:1.14.14
  - flavoprotein
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Large-scale structural refactor (49 terms) that is mechanical once the correct parent is identified, good test of bulk editing capability
case_quality: good
case_quality_reason: single_complete_bulk_reclassification_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

All GO terms corresponding to EC:1.14.14.x (cytochrome P450 monooxygenases) were incorrectly classified under GO:0016709 ("oxidoreductase activity, acting on paired donors, with NAD(P)H as one donor"). These enzymes actually use a reduced flavin/flavoprotein as electron donor, so the correct parent is GO:0016712 ("oxidoreductase activity, acting on paired donors, with reduced flavin or flavoprotein as one donor").

The key insight: CYP450 enzymes receive electrons from NADPH *indirectly* via cytochrome P450 reductase (a flavoprotein). The GO hierarchy classifies by the *immediate* electron donor to the catalytic site, which is the flavoprotein, not NADPH itself.

## Changes Made

In `src/ontology/go-edit.obo` (56 additions, 7 deletions):

**Bulk reparent** of 49 terms, each following the same pattern:
```
-is_a: GO:0016709 ! ... NAD(P)H as one donor ...
+is_a: GO:0016712 ! ... reduced flavin or flavoprotein as one donor ...
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31967" xsd:anyURI
```

Example terms affected:
- GO:0004506 (squalene monooxygenase) — EC:1.14.14.17
- GO:0008398 (sterol 14-demethylase) — EC:1.14.14.154
- GO:0010283 (4-coumarate 3-hydroxylase) — EC:1.14.14.91
- GO:0016711 (flavonoid 3'-monooxygenase) — EC:1.14.14.82
- GO:0018664 (benzoate 4-monooxygenase) — EC:1.14.14.93
- Plus ~44 more CYP450-related terms

## Resolution

Medium difficulty: the reasoning (identify correct parent based on electron donor mechanism) requires enzyme biochemistry knowledge, but once determined, the edit is repetitive. An agent would need to:
1. Understand the EC:1.14.14 -> flavoprotein donor mapping
2. Identify all affected terms (those with EC:1.14.14.x xrefs currently under GO:0016709)
3. Apply the bulk reparent mechanically

Same-day turnaround (issue opened and PR merged on 2026-04-24). Approved without changes because the reasoning was clear and the edit was mechanical.
