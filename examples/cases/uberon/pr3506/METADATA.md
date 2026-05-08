---
repo: obophenotype/uberon
issue_number: 3448
pr_number: 3506
issue_title: "two new defs for undefined terms"
issue_created_at: "2024-12-13"
pr_author: cmungall
pr_merged_at: "2025-04-23"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - definition-addition
  - insular-cortex
  - Brodmann-area
  - SCORCH
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Adding missing text definitions to two existing neuroanatomical terms, sourced from domain expert
---

## Context

Issue #3448 identified two Uberon terms lacking text definitions: insular cortex (UBERON:0034891) and Brodmann (1909) area 9 (UBERON:0013540). Definitions were provided by a domain expert (Dana Gabuxda, ORCID:0000-0002-4964-5083) as part of the SCORCH Project's efforts to improve neuroanatomical term quality.

## Changes Made

The PR added two definition lines to src/ontology/uberon-edit.obo, one for each term. The definitions include proper OBO format references and contributor ORCID attribution. Insular cortex was defined based on its location and functional role, and Brodmann area 9 was defined based on its cytoarchitectural characteristics and location in the prefrontal cortex.

## Resolution

Simple difficulty. Adding text definitions to existing terms is a straightforward operation in OBO format. The key requirement is having an accurate, well-sourced definition text. In this case, the definitions were provided by a domain expert in the issue, so an agent would primarily need to format them correctly in OBO syntax with proper attribution.
