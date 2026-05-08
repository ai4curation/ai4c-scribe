# Failure Analysis: Issue #2546 Bronchiectasis Series (4 PRs)

## Issue Title
[NTR] Request for new endotypes of bronchiectasis terms

## PRs in Series
- PR #2547, #2548, #2553, #2554 (all closed)
- PR #2582 (eventually merged)

## Failure Mode
**Multiple duplicate PRs with WIP placeholders**

## What Happened

1. Issue #2546 requested bronchiectasis endotype terms from PMID:30215383
2. Agent created **4 PRs** before one was finally merged as #2582
3. Two PRs were WIP placeholders (#2547, #2553) that were never completed
4. Two PRs had actual content (#2548, #2554) but were closed in favor of later attempts

### Timeline
| PR | Title | Status | Notes |
|----|-------|--------|-------|
| 2547 | [WIP] Add new endotypes... | Closed | Never completed |
| 2548 | Add bronchiectasis endotype terms | Closed | Had content |
| 2553 | [WIP] Add new endotypes... | Closed | Never completed |
| 2554 | Add bronchiectasis inflammatory endotype terms | Closed | Had content |
| 2582 | Add bronchiectasis inflammatory endotype terms | **Merged** | Final success |

## Root Causes

1. **WIP PRs not completed** - Agent created placeholder PRs but started fresh instead of continuing
2. **Branch abandonment** - Instead of finishing #2547, agent created #2548
3. **No memory of previous attempts** - Each session started from scratch
4. **Inconsistent term IDs** - PR #2554 used EFO_0920016-0920018, but these IDs were later used for other terms

## ID Collision Issue

PR #2554 proposed:
- EFO_0920016: neutrophilic bronchiectasis
- EFO_0920017: eosinophilic bronchiectasis
- EFO_0920018: paucigranulocytic bronchiectasis

But the successfully merged PR #2582 used different IDs:
- EFO_0920034 onwards for the same concepts

This shows the agent was not tracking which IDs had been proposed/used.

## Correct Approach

1. **Never abandon WIP PRs** - Complete them or update with progress
2. **Check existing PRs** before creating new ones for same issue
3. **Track proposed term IDs** across sessions
4. **Push to existing branch** rather than creating new PRs

## Lessons Learned

- WIP PRs should be completed, not abandoned
- If you've started work on an issue, continue that work in the same PR
- Term IDs need central tracking to avoid collisions
