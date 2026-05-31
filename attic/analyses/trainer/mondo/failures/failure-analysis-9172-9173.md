# Failure Analysis: PRs #9172 and #9173

## PR Details

### PR #9172
- **Title**: Obsolete cone-rod dystrophy 12 and replace with PROM1-related retinopathy
- **URL**: https://github.com/monarch-initiative/mondo/pull/9172
- **Created**: 2025-06-06
- **Closed**: 2025-07-04
- **Status**: CLOSED (replaced by #9173)

### PR #9173
- **Title**: Obsolete cone-rod dystrophy 12 and merge with PROM1-related retinopathy
- **URL**: https://github.com/monarch-initiative/mondo/pull/9173
- **Created**: 2025-06-06
- **Closed**: 2025-07-19
- **Status**: CLOSED (not merged)

## What the Agent Did

The agent attempted to address issue #9171 by obsoleting cone-rod dystrophy 12 (MONDO:0012983) and replacing it with PROM1-related retinopathy (MONDO:1040056).

## Why It Failed

### PR #9172 Failure

**Reviewer (@mellybelly) feedback:**
> "please replace the explanation for the term obsoletion because the two terms represented the same concept. If there is a standard code for this please use it."

The agent's original explanation focused on "phenotypic spectrum" which was the wrong reason. The correct reason was that the terms were duplicates/same concept.

**Resolution**: Agent created PR #9173 instead of updating #9172.

### PR #9173 Failure

PR #9173 was eventually closed on 2025-07-19 without being merged. The reasons aren't fully clear from the data, but the PR sat open for over a month after the initial fix.

## Root Cause Analysis

### Primary Failure: Wrong Obsoletion Reason

The agent used the wrong justification for the obsoletion. In MONDO:
- **Wrong**: "broader phenotypic spectrum"
- **Correct**: `MONDO:TermsMerged` (standard IAO code for merged terms)

### Secondary Failure: Created New PR

Instead of updating #9172 with the corrected obsoletion reason, the agent created #9173.

### Tertiary Failure: Obsoletion Pattern Knowledge Gap

The agent didn't know the standard IAO codes used for term obsoletion in MONDO:
- `IAO:0000231 MONDO:TermsMerged` - for merged terms
- `IAO:0000233` - for issue tracker reference

## Failure Modes

1. **Wrong Obsoletion Reason**: Used narrative explanation instead of standard code
2. **Created New PR**: Should have updated existing PR
3. **Incomplete Knowledge**: Didn't know MONDO obsoletion patterns

## Lessons Learned

1. **Learn MONDO Obsoletion Patterns**: Standard IAO codes exist for common reasons:
   - `MONDO:TermsMerged` - terms represent same concept
   - `MONDO:duplicateInMondo` - duplicate entries
   - `MONDO:OutOfScope` - term doesn't belong in MONDO

2. **Study Existing Obsoleted Terms**: Before obsoleting a term, look at how other obsoleted terms are annotated

3. **Update PRs, Don't Replace Them**: When asked to fix something, fix it in place

## Counterfactual: What Should Have Happened

1. Before creating the obsoletion PR, search for examples: "is_obsolete: true" in mondo-edit.obo
2. Identify the standard pattern using IAO codes
3. Apply the correct obsoletion reason from the start
4. When feedback is received, update the same PR
5. Follow up if PR sits without review for extended period
