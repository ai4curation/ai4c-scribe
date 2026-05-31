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
case_quality: poor
case_quality_reason: metadiff_line_atomic_def_xref
companion_prs: []
scoring_caveat: "All 11 attempts score F1=precision=recall=0.000 by construction. Gold PR #3506 added exactly two lines (one def: per term) and folded the contributor ORCID INTO the def xref bracket, also using Uberon's legacy internal identifiers (Wikipedia:INSULA, MESH:D007419) rather than the issue-implied modern ones. The OBO metadiff compares whole normalized def: lines (prose + xref bracket) as atomic set elements, so a definition with even verbatim-correct prose but a differently-formatted xref earns zero credit. pr300 and pr237 reproduced gold's definition prose byte-for-byte and still scored 0. Judge attempts on substance (correct def text + valid OBO formatting + contributor attribution + issue link per the agent config), NOT on the F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3448 identified two Uberon terms lacking text definitions: insular cortex (UBERON:0034891) and Brodmann (1909) area 9 (UBERON:0013540). Definitions were provided by a domain expert (Dana Gabuxda, ORCID:0000-0002-4964-5083) as part of the SCORCH Project's efforts to improve neuroanatomical term quality.

## Changes Made

The PR added two definition lines to src/ontology/uberon-edit.obo, one for each term. The definitions include proper OBO format references and contributor ORCID attribution. Insular cortex was defined based on its location and functional role, and Brodmann area 9 was defined based on its cytoarchitectural characteristics and location in the prefrontal cortex.

## Resolution

Simple difficulty. Adding text definitions to existing terms is a straightforward operation in OBO format. The key requirement is having an accurate, well-sourced definition text. In this case, the definitions were provided by a domain expert in the issue, so an agent would primarily need to format them correctly in OBO syntax with proper attribution.

## Curation Note (data quality)

**Flagged poor (`metadiff_line_atomic_def_xref`) by claude-opus-4.7 on 2026-05-16.**

This is a poor *evaluation* case, not a poor agent cohort. Every one of the
11 attempts scored exactly `f1 = precision = recall = jaccard = 0.000`, and
investigation shows this is a scoring artifact rather than a uniform agent
failure:

- **Gold is correct and complete; not multi-PR.** `gh search prs` confirms
  #3506 is the sole human resolution of issue #3448 (no companion PRs). Its
  parent commit (`595f751`) is byte-identical to the eval base branch
  `eval-base-issue-3448`, so there is **no base contamination and no
  wrong-base** problem. Gold added exactly 2 lines: one `def:` line per term.
- **The zero scores are a line-atomic metadiff artifact.** The OBO metadiff
  (`src/ai4c_scribe/metadiff/api.py`) compares entire normalized added/removed
  lines as set members. A `def:` line is one atomic element including its
  trailing xref bracket. Gold idiosyncratically folded the contributor ORCID
  *inside* the def bracket and used Uberon's legacy internal identifiers:
  - BA9 (UBERON:0013540): `... [Wikipedia:Brodmann_area_9, https://orcid.org/0000-0002-4964-5083]`
  - insular cortex (UBERON:0034891): `... [Wikipedia:INSULA, MESH:D007419, https://orcid.org/0000-0002-4964-5083]`
  None of these xref choices is derivable from issue #3448, which only said
  "References: Wikipedia, MeSH" / "Adapted from Wikipedia". No agent matched
  the exact bracket, so every `def:` line is a non-matching string → 0 true
  positives → F1=0 for all 11, **by construction**.
- **Several attempts are substantively excellent.** pr300 (sonnet-4.5) and
  pr237 (opus-4.7) reproduced gold's definition *prose* byte-for-byte and
  still scored 0.0. pr237 in particular is the model attempt: gold-verbatim
  text, perfect scope, transparent methodology.
- **Gold vs. agent-config mismatch.** The uberon-agent-config CLAUDE.md
  explicitly instructs agents to add `dc-contributor`, `dcterms-date`, and
  `term_tracker_item`. The agents that did so were following instructions;
  the quick human gold commit did none of that. The metadiff ignores those
  keys but cannot reward the (correct) def lines, so instruction-following
  agents are doubly disadvantaged.

**Scoring guidance:** exclude or down-weight this case in aggregate F1.
Judge attempts on substance: (1) accurate definition text faithful to the
expert-supplied issue text, (2) valid OBO xref formatting, (3) contributor
attribution, (4) issue link. On that basis the cohort is largely
successful — best: pr237/pr300 (success); worst: pr150/pr107 (correct text
but malformed `[Wikipedia]` xrefs).
