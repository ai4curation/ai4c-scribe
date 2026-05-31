# Failure Analysis: PR #9199

## PR Details

- **Title**: Make MONDO:0970994 a subclass of MONDO:0800145
- **URL**: https://github.com/monarch-initiative/mondo/pull/9199
- **Created**: 2025-06-12
- **Closed**: 2025-06-13
- **Status**: CLOSED (not merged)

## What the Agent Did

The agent attempted to address issue #8082 by establishing a hierarchical relationship for immunodeficiency 120. The agent modified the is_a relationship, changing from one parent to another.

## Why It Failed

**Reviewer (@sabrinatoro) feedback (first comment):**
> "what you did is not correct. Please update with the following changes:
> - do not remove or update existing SubClassOf annotation, add another one (even if the one you are adding is more specific)
> - the source for the SubClassOf should be OMIM:620836 (NOT the Github issue tracker)"

**Second comment:**
> "please also add a 'excluded from QC' annotation for single child. look at other terms for examples"

## Root Cause Analysis

### Primary Failure: Destructive Edit

The agent **removed** the existing is_a relationship instead of **adding** a new one alongside it. In MONDO, you typically don't remove existing classifications; you add additional ones.

### Secondary Failure: Wrong Source Annotation

The agent used the GitHub issue as the source instead of the proper OMIM reference.

### Tertiary Failure: Created New PR Instead of Updating

After receiving feedback, the agent created PR #9209 instead of updating #9199 as requested.

**Agent response:**
> "The changes have been implemented on branch `issue-9199` and submitted as PR #9209 for your review."

## Failure Modes

1. **Destructive Edit**: Removed existing relationship instead of adding new one
2. **Wrong Source**: Used GitHub issue tracker instead of OMIM
3. **Created New PR**: Didn't update existing PR as expected
4. **Incomplete Changes**: Missed the QC exclusion annotation

## Lessons Learned

1. **Additive, not Destructive**: In MONDO, ADD new relationships; don't REMOVE existing ones unless explicitly told to
2. **Use Proper Sources**: OMIM, PMID, or other authoritative references, not GitHub issues
3. **Study Examples**: When told to "look at other terms for examples," actually do that before implementing
4. **Update Existing PRs**: Don't create new PRs when asked to fix issues in an existing one

## Counterfactual: What Should Have Happened

1. Receive the task to add a SubClassOf relationship
2. **Study existing patterns** in MONDO for similar terms
3. **Add** the new is_a relationship without removing the existing one
4. Use OMIM:620836 as the source
5. Check for QC exclusion patterns and add the annotation
6. When receiving feedback, **update the same PR**, not create a new one

## Positive Note

The follow-up PR #9209 was eventually merged, so the agent did learn to some extent. But the initial destructive approach and creating a new PR wasted reviewer time.
