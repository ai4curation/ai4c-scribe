# Dragon-AI-Agent PR Analysis: Mondo Repository

## Overview

**Date**: 2025-12-20
**Repository**: monarch-initiative/mondo
**Agent Account**: dragon-ai-agent

## Statistics

| Metric | Count | Percentage |
|--------|-------|------------|
| Total PRs | 26 | 100% |
| Merged | 11 | 42% |
| Closed (unmerged) | 14 | 54% |
| Open | 1 | 4% |

**Success Rate**: 11/25 completed PRs = **44%**

## First-Try Success Rate

Of the merged PRs (from extracted data with category info):

| Category | Count | Percentage |
|----------|-------|------------|
| Merged without modifications | 4 | 26.7% |
| Merged with modifications | 11 | 73.3% |
| **Total merged (in dataset)** | **15** | 100% |

**First-try success rate:** 4/15 = **26.7%**

This is critically low - nearly 3 out of 4 merged PRs required modifications. The agent struggles to get submissions right on the first attempt.

## Merged PRs (Success)

| PR | Title | Merged Date |
|----|-------|-------------|
| [#9726](https://github.com/monarch-initiative/mondo/pull/9726) | Add viral respiratory tract infection as parent to common cold | 2025-12-01 |
| [#9724](https://github.com/monarch-initiative/mondo/pull/9724) | Add logical definition to renal infectious disease | 2025-11-03 |
| [#9717](https://github.com/monarch-initiative/mondo/pull/9717) | Add infectious disease as parent to renal infectious disease | 2025-11-03 |
| [#9652](https://github.com/monarch-initiative/mondo/pull/9652) | Add skin basal cell carcinoma as parent | 2025-10-14 |
| [#9409](https://github.com/monarch-initiative/mondo/pull/9409) | Add new term avoidant/restrictive food intake disorder | 2025-11-03 |
| [#9363](https://github.com/monarch-initiative/mondo/pull/9363) | Refactor Addison's disease classification | 2025-08-07 |
| [#9283](https://github.com/monarch-initiative/mondo/pull/9283) | Add HP:0003002 xref to breast carcinoma | 2025-07-03 |
| [#9261](https://github.com/monarch-initiative/mondo/pull/9261) | Fix CDC URLs | 2025-10-10 |
| [#9209](https://github.com/monarch-initiative/mondo/pull/9209) | Add SubClassOf relationship for immunodeficiency 120 | 2025-06-13 |
| [#9198](https://github.com/monarch-initiative/mondo/pull/9198) | Add cutaneous solitary mastocytoma as subclass | 2025-06-13 |
| [#8843](https://github.com/monarch-initiative/mondo/pull/8843) | Update synonyms of FATWO | 2025-05-28 |

## Failed PRs Checklist

Each PR below was closed without merging and requires analysis:

- [ ] [#9734](https://github.com/monarch-initiative/mondo/pull/9734) - Simplify ochronosis disorder - **Work already done by another contributor**
- [ ] [#9482](https://github.com/monarch-initiative/mondo/pull/9482) - Add argyrophilic grain disease - **Duplicate attempt #7**
- [ ] [#9456](https://github.com/monarch-initiative/mondo/pull/9456) - Add argyrophilic grain disease - **Duplicate attempt #6**
- [ ] [#9455](https://github.com/monarch-initiative/mondo/pull/9455) - Add argyrophilic grain disease - **Duplicate attempt #5**
- [ ] [#9427](https://github.com/monarch-initiative/mondo/pull/9427) - Add argyrophilic grain disease - **Duplicate attempt #4**
- [ ] [#9376](https://github.com/monarch-initiative/mondo/pull/9376) - Add argyrophilic grain disease - **Duplicate attempt #3**
- [ ] [#9351](https://github.com/monarch-initiative/mondo/pull/9351) - Update argyrophilic grain disease annotations - **Duplicate attempt #2, failed to follow instructions**
- [ ] [#9311](https://github.com/monarch-initiative/mondo/pull/9311) - Add argyrophilic grain disease - **Initial attempt, wrong annotation format**
- [ ] [#9330](https://github.com/monarch-initiative/mondo/pull/9330) - Fix Lynch syndrome subtypes - **Duplicate of existing work**
- [ ] [#9199](https://github.com/monarch-initiative/mondo/pull/9199) - Make immunodeficiency 120 a subclass - **Destructive edit; created new PR instead of updating**
- [ ] [#9173](https://github.com/monarch-initiative/mondo/pull/9173) - Obsolete cone-rod dystrophy 12 - **Replacement PR, still not merged**
- [ ] [#9172](https://github.com/monarch-initiative/mondo/pull/9172) - Obsolete cone-rod dystrophy 12 - **Wrong obsoletion reason, replaced by #9173**
- [ ] [#9167](https://github.com/monarch-initiative/mondo/pull/9167) - Add equine spinocerebellar ataxia - **OWL structure error (Class and Individual)**
- [ ] [#8868](https://github.com/monarch-initiative/mondo/pull/8868) - Add CLAUDE.md - **Duplicate of #9019**

## Open PRs (Pending)

- [ ] [#9725](https://github.com/monarch-initiative/mondo/pull/9725) - Add tuberculous pneumothorax as child of tuberculosis

## Failure Mode Summary

| Failure Mode | Count | PRs |
|--------------|-------|-----|
| Created new PR instead of updating existing | 9 | #9482, #9456, #9455, #9427, #9376, #9351, #9173, #9172, #9199 |
| Wrong annotation/reference format | 7 | #9311, #9351, #9456, #9455, #9427, #9376, #9482 |
| Duplicate of existing work | 3 | #9734, #9330, #8868 |
| Destructive edit (removed instead of added) | 2 | #9734, #9199 |
| Technical OWL/OBO structure error | 1 | #9167 |
| Failed to follow reviewer instructions precisely | 5 | #9311, #9351, #9199, #9172, #9173 |

## Critical Issues Identified

### 1. The Argyrophilic Grain Disease Saga (7 PRs for 1 term!)

This single term request (#9279/#9426) resulted in **7 separate PRs** over 2 months:
- #9311 → #9351 → #9376 → #9427 → #9455 → #9456 → #9482

All were closed. The reviewer repeatedly asked to "update this PR instead of creating a new one" but the agent kept creating new PRs.

### 2. Annotation Format Misunderstanding

The agent consistently failed to understand MONDO's annotation patterns:
- Grouped multiple PMIDs in one annotation instead of separate entries
- Confused PMC IDs with PMIDs
- Used wrong source annotations for SubClassOf relationships

### 3. Not Checking for Existing Work

Multiple PRs were closed because the work was already done or in progress by human contributors.
