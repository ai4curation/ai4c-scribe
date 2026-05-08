---
repo: geneontology/go-ontology
issue_number: 27593
pr_number: 31997
issue_title: "NTR ferric iron reductase (for non siderophore)"
issue_created_at: "2024-04-12"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 16
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Long-standing NTR (2+ years open) with a prior failed PR due to GO ID collision, requiring RHEA reaction alignment and careful parent term selection
---

## Context

A new term request for ferric iron reductase activity was filed in April 2024 to support GO-CAM modeling. The existing GO terms for iron reduction were tied to siderophore-mediated processes, but many organisms reduce ferric iron (Fe3+) to ferrous iron (Fe2+) through non-siderophore mechanisms using NADPH as the electron donor. The first attempt at this PR (#31797) was closed due to a GO ID collision where the allocated ID had already been used by a parallel branch.

## Changes Made

The PR added GO:7770068 `ferric iron reductase activity` as a new molecular function term with the reaction `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH` cross-referenced to RHEA:71767 (skos:exactMatch). The term was placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor). The definition referenced PMID:8321236. Additionally, the existing term GO:0000293 was updated to reflect its relationship to the new term.

## Resolution

Hard difficulty due to several factors: the issue was open for over two years, a previous PR attempt failed due to ID collision (requiring careful ID allocation), and the definition needed precise alignment with the RHEA reaction database. The parent term selection required understanding the enzyme classification hierarchy for oxidoreductases acting on metal ion substrates with NAD(P) as acceptor.
