---
repo: obophenotype/uberon
issue_number: 3509
pr_number: 3515
issue_title: "Definition of common hepatic artery is truncated"
issue_created_at: "2025-04-24"
pr_author: ar-ibrahim
pr_merged_at: "2025-05-08"
pr_num_commits: 3
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: vascular-anatomy
tags:
  - definition-fix
  - truncated-text
  - hepatic-artery
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple text definition fix for a truncated definition on a single vascular term
case_quality: poor
case_quality_reason: issue_underspecified_gold_diverges_from_ask
companion_prs: [3510]
scoring_caveat: "Issue #3509 explicitly asked to 'just shorten this further so it's not trailing'. Gold PR #3515 did the OPPOSITE: it EXPANDED the definition (added 'and gall bladder', enumerated the 3 branches — hepatic artery proper, gastroduodenal artery, right gastric artery — and added an Elsevier source xref). No agent following the issue's literal instruction could reproduce gold. F1=0.500 for every well-formed attempt is a structural single-line def-replacement metadiff artifact (shared deleted line = 1 match; novel rewritten line = 0 match), not a quality signal. The two attempts that added a config-recommended term_tracker_item score F1=0.400 — penalized for a best practice gold omitted. metadiff materially UNDER-represents quality across all 8 attempts; judge against the issue's actual ask (remove the trailing fragment), which every attempt satisfied."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3509 reported that the text definition of the common hepatic artery was truncated, likely due to a data entry or import error. The definition was incomplete and needed to be restored to its full text.

## Changes Made

The PR made a single line change in src/ontology/uberon-edit.obo, replacing the truncated definition with the complete text for the common hepatic artery term. Despite the minimal change, three commits were needed, possibly due to formatting corrections during review.

## Resolution

Simple difficulty. This is a straightforward text correction requiring an agent to identify the truncated definition and supply the complete text. The main challenge is sourcing the correct full definition text, which could be obtained from anatomical references or the term's cross-references to other ontologies.

## Curation Note (data quality)

**Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16.**

This is a poor evaluation reference because the issue's explicit instruction
and the gold PR's actual change point in **opposite directions**:

- **Issue #3509** quotes the truncated definition and says, verbatim:
  *"Just shorten this further so it's not trailing"* — i.e. remove/trim the
  dangling "and has the following branches:." fragment. (Issue has no comments.)
- **Gold PR #3515** (merged 2025-05-08 by ar-ibrahim; verified as current
  canonical text on `master`) did the **opposite**: it *expanded* the
  definition — added "and gall bladder" to the supply list, **enumerated the
  three branches** ("the hepatic artery proper, the gastroduodenal artery and
  the right gastric artery"), and added an Elsevier source xref
  (`https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/common-hepatic-artery/22763`)
  alongside the existing `Wikipedia:Common_hepatic_artery`.

A faithful agent cannot satisfy both the issue text and the gold simultaneously.

**Companion PR #3510** (by cmungall/Claude Code) implemented the literal
issue request (remove the trailing fragment) but was closed unmerged after a
merge conflict; matentzn's comment that it was "implemented elsewhere (#3507)"
is a mistaken cross-reference — PR #3507 is "Added term: medial prefrontal
cortex" (fixes #3446) and does not touch UBERON:0005436. So #3515 is the
genuine, surviving canonical resolution; this is NOT a curator-repudiated or
partial-gold case — it is an underspecified-issue / gold-diverges-from-ask
case.

**Scoring consequence.** This is a single-line `def:` replacement. metadiff
gives every well-formed attempt P=R=F1=0.500 (the deleted line matches gold's
deleted line = 1 TP; the rewritten line is novel prose that cannot match
gold's divergent expansion = 0 TP on the addition). The two opencode/gpt-5.5
attempts (#63, #44) that correctly added a config-recommended
`term_tracker_item` link (which gold omitted) drop to F1=0.400 — penalized
for following uberon-agent-config best practice. The metadiff therefore
materially **under-represents** quality for all 8 attempts.

**Judging guidance.** Score attempts against the issue's actual ask (produce
a complete, non-trailing definition) — which all 8 attempts satisfied with
valid, anatomically accurate, tightly-scoped OBO. Best fidelity to the
surviving canonical text: opus #242 and gemma #113 (byte-identical, blob
`cf7f76d`), which removed *only* the trailing clause and preserved the
original preamble/glosses. Recommend down-weighting or excluding this case
from aggregate metadiff scoring.
