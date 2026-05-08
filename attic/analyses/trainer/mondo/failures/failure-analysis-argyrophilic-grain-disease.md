# Failure Analysis: Argyrophilic Grain Disease Saga

## Overview

This analysis covers **7 failed PRs** all attempting to add the same term for argyrophilic grain disease:

| PR | Title | Created | Closed |
|----|-------|---------|--------|
| [#9311](https://github.com/monarch-initiative/mondo/pull/9311) | Add argyrophilic grain disease (MONDO:7770001) | 2025-07-11 | 2025-07-28 |
| [#9351](https://github.com/monarch-initiative/mondo/pull/9351) | Update argyrophilic grain disease term annotations | 2025-07-21 | 2025-07-28 |
| [#9376](https://github.com/monarch-initiative/mondo/pull/9376) | Add new term for argyrophilic grain disease (MONDO:7770001) | 2025-07-28 | 2025-08-14 |
| [#9427](https://github.com/monarch-initiative/mondo/pull/9427) | Add MONDO:7770002 argyrophilic grain disease | 2025-08-05 | 2025-08-14 |
| [#9455](https://github.com/monarch-initiative/mondo/pull/9455) | Add MONDO:7770002 argyrophilic grain disease | 2025-08-12 | 2025-08-14 |
| [#9456](https://github.com/monarch-initiative/mondo/pull/9456) | Add MONDO:7770002 argyrophilic grain disease | 2025-08-12 | 2025-08-14 |
| [#9482](https://github.com/monarch-initiative/mondo/pull/9482) | Add new term MONDO:7770002 for argyrophilic grain disease | 2025-08-19 | 2025-09-30 |

**Related Issues**: #9279, #9426

## The Failure Pattern

### Phase 1: Initial Attempt (#9311)

The agent created a reasonable first attempt. Reviewer @sabrinatoro requested specific changes:
- Use PMID format instead of PMC/DOI references
- Add database cross-reference for synonym
- Add source annotation for is_a relationships
- Add issue tracker annotation
- Remove namespace annotation

**Critical Error**: Instead of updating PR #9311, the agent created a NEW PR #9351.

### Phase 2: First Revision Attempt (#9351)

Reviewer explicitly said: "please update this PR instead of creating a new one"

The agent still had issues:
- Wrong PMID lookup (PMC5618985 ≠ PMID:29045946, correct is PMID:29213935)
- Grouped all PMIDs in one annotation instead of individual entries

**Reviewer feedback**: "Do not group all the PMIDs in one single annotation: every PMID should be entered as an individual database cross reference or source annotation."

The agent attempted fixes but still got it wrong. Reviewer: "Closing, starting over."

### Phase 3: Repeated Failures (#9376 through #9482)

Despite the reviewer closing PRs and asking to "start over," the agent created 5 more PRs, each with similar issues:
- Still not understanding the individual PMID annotation pattern
- ID confusion (switching between MONDO:7770001 and MONDO:7770002)
- Not learning from previous feedback

## Root Cause Analysis

### 1. Failure to Update Existing PRs

The reviewer explicitly asked multiple times to "update this PR instead of creating a new one." The agent ignored this and created new PRs each time.

### 2. Misunderstanding Annotation Patterns

The agent never correctly implemented individual PMID annotations. Example of what was needed:

```
# WRONG (grouped):
synonym: "AGD" EXACT [PMID:29213935, PMID:16319301, PMID:18234698]

# CORRECT (individual):
synonym: "AGD" EXACT [PMID:29213935]
synonym: "AGD" EXACT [PMID:16319301]
synonym: "AGD" EXACT [PMID:18234698]
```

### 3. PMC to PMID Conversion Errors

The agent consistently got PMID lookups wrong:
- PMC5618985 → Agent said PMID:29045946, correct is PMID:29213935
- Failed to convert DOIs to PMIDs correctly

### 4. No Learning Between Attempts

Each new PR repeated the same mistakes. The agent didn't incorporate feedback from previous failures into subsequent attempts.

## Failure Modes

1. **Creating new PRs instead of updating**: Direct violation of reviewer instructions (9 instances)
2. **Wrong reference format**: PMC/DOI not converted to PMID correctly
3. **Grouped annotations**: Not understanding MONDO's individual annotation pattern
4. **No learning loop**: Same mistakes repeated across 7 PRs
5. **ID instability**: Switching between MONDO:7770001 and MONDO:7770002

## Cost of Failure

- **7 PRs** created and closed
- **2+ months** of back-and-forth (July 11 to September 30)
- **Reviewer time** wasted on repeated reviews
- **Term still not added** after all this effort

## Lessons Learned

1. **ALWAYS update existing PRs when requested**: This was the #1 issue
2. **Learn MONDO annotation patterns**: Each PMID must be a separate annotation
3. **Verify PMID lookups**: Use PubMed directly to convert PMC IDs to PMIDs
4. **Learn from previous failures**: Before creating a new attempt, review why the last one failed
5. **Ask for clarification**: If the pattern isn't clear, ask for a specific example

## Counterfactual: What Should Have Happened

1. Create #9311 with best effort
2. Receive feedback from @sabrinatoro
3. **Update #9311** (not create new PR) with fixes
4. If unsure about annotation pattern, ask: "Could you show me an example of how individual PMIDs should be annotated?"
5. Verify PMID lookups using PubMed before committing
6. Iterate on same PR until merged or explicitly told to close
