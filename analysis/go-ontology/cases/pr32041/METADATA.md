---
repo: geneontology/go-ontology
issue_number: 31902
pr_number: 32041
issue_title: "NTR: [venom-mediated inflammatory response+... leukocyte infiltration+... release of inflammatory mediator]"
issue_created_at: "2026-04-15"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-07"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 13
    deletions: 0
scoping: loosely_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: NTR from the venom biology domain with inter-organism process semantics; only one of the three requested terms was created in this PR
---

## Context

A new term request from a UniProt curator asked for several venom-related biological process terms, including venom-mediated activation of inflammatory response, leukocyte infiltration, and release of inflammatory mediator. These terms are needed to annotate venom toxin proteins that trigger inflammatory cascades in envenomated organisms. The issue referenced PMID:19000915 and PMID:32024243 as supporting literature.

## Changes Made

The PR added GO:7770071 `venom-mediated activation of inflammatory response` as a biological process term. The definition captures the inter-organism nature of envenomation: one organism causes inflammatory response in another organism via venom action. The term includes both a broad synonym (`venom-mediated inflammation`) and an exact synonym using the standard GO inter-organism phrasing (`envenomation resulting in positive regulation of inflammatory response in another organism`).

## Resolution

This PR addressed only one of the three terms requested in the issue, making it partially scoped relative to the full request. The single-term approach is appropriate for incremental ontology development, allowing each term to be reviewed independently. Medium difficulty because the definition required careful framing of inter-organism process semantics, which follow specific GO conventions for processes that span two organisms.
