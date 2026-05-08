# Training Plan for Copilot on EFO Ontology

## Executive Summary

Analysis of 51 PRs by app/copilot-swe-agent to EBISPOT/efo:

| Status | Count | Percentage |
|--------|-------|------------|
| Merged | 20 | 39.2% |
| Closed (not merged) | 28 | 54.9% |
| Open | 3 | 5.9% |
| **Total** | **51** | 100% |

**Success rate of closed PRs:** 20/48 = **41.7%**

This is significantly lower than comparable ontology work (GO: 77.6%). The primary cause is **excessive duplicate PR creation** - single issues generated 4-13 PRs each.

**Caveat on silent closures:** Several EFO PRs were closed without reviewer feedback. Treat these as uncertain root-cause cases and request clarification before updating training rules based on them.

---

## Complete Failure Inventory

All 28 failed PRs are accounted for:

| PR | Primary Failure Mode | Section |
|----|---------------------|---------|
| 2491-2514, 2558-2559 | Duplicate PRs (Issue #2490) | §1 |
| 2547, 2548, 2553, 2554 | Duplicate PRs (Issue #2546) | §1 |
| 2563, 2564, 2565, 2569 | Duplicate PRs (Issue #2562) | §1 |
| 2450, 2452 | Duplicate PRs (Issue #2445) | §1 |
| 2452, 2495, 2547, 2553, 2563, 2569 | WIP placeholders abandoned | §2 |
| 2532 | Similar term exists, needs discussion | §3 |
| 2454, 2539, 2588 | Closed without explanation | §4 |

---

## Critical Failure Modes and Training Instructions

### 1. NEVER Create Duplicate PRs for Same Issue (23 PRs - 82% of failures)

**Affected Issues:**
- Issue #2490: 13 PRs created
- Issue #2546: 4 PRs created
- Issue #2562: 4 PRs created
- Issue #2445: 2 PRs created

**The Problem:**
Agent created multiple PRs for the same issue, each starting fresh instead of updating existing work. Issue #2490 alone generated 13 PRs with varying term counts (4 to 79 terms).

**Training Instructions:**
```
RULE: ONE PR per issue - ALWAYS

Before starting work on any issue:
1. SEARCH for existing PRs on this issue
   Command: gh pr list -R EBISPOT/efo --search "in:title [issue keywords]"

2. If a PR exists:
   - Checkout that branch
   - Push new commits to it
   - NEVER create a new PR

3. If asked to revise an existing PR:
   - Checkout the existing branch
   - Make changes and push
   - NEVER create a new PR

Example:
- Reviewer: "Add more terms to this PR"
- CORRECT: git checkout existing-branch && <make changes> && git push
- WRONG: Create new PR with additional terms

4. If you must abandon a PR:
   - Comment explaining why
   - Close it explicitly
   - Only then create new PR if truly necessary
```

---

### 2. Complete WIP PRs - Never Abandon (6 PRs)

**Affected PRs:** 2452, 2495, 2547, 2553, 2563, 2569

**The Problem:**
Agent created [WIP] placeholder PRs but then started fresh in new PRs instead of completing them.

**Training Instructions:**
```
RULE: Never abandon WIP PRs

1. If you create a WIP PR:
   - You MUST complete it in subsequent sessions
   - NEVER create a new PR for the same issue

2. If blocked on a WIP PR:
   - Document the blocker in the PR
   - Ask for help
   - Keep the PR open

3. If you find an existing WIP PR for your assigned issue:
   - Continue work on that PR
   - Update the description with progress
   - Remove [WIP] when ready for review

4. WIP PRs are commitments - treat them as such
```

---

### 3. Check for Similar Existing Terms Before Adding New Ones (1 PR)

**Affected PRs:** 2532

**The Problem:**
PR #2532 proposed "DLCO change measurement" but reviewer noted similar term already exists (EFO_0009369 "diffusing capacity of the lung for carbon monoxide"). Existing term had issues needing resolution first.

**Training Instructions:**
```
RULE: Search before adding new terms

Before proposing ANY new term:
1. SEARCH for similar labels:
   - grep -i "term_name" src/ontology/efo-edit.owl
   - Search OLS for the concept

2. SEARCH for synonyms:
   - grep -i "alternative_name" src/ontology/efo-edit.owl

3. If similar terms exist:
   - Comment on the issue asking if new term is needed
   - Propose modifications to existing term instead
   - Wait for curator confirmation before creating new term

4. Check for related term issues:
   - Are there open issues about similar terms?
   - Are similar terms flagged as problematic?

Example search:
$ grep -i "diffus.*capacity\|DLCO" src/ontology/efo-edit.owl
```

---

### 4. Request Feedback on Silent PR Closures (3 PRs)

**Affected PRs:** 2454, 2539, 2588

**The Problem:**
Some PRs were closed without any comments or reviews, leaving no clear learning opportunity.

**Training Instructions:**
```
RULE: Always understand why a PR was closed

If a PR is closed without feedback:
1. Comment asking for clarification:
   "This PR was closed without review feedback. Could you help me understand:
    - Was there an issue with the approach?
    - Was this resolved via another PR?
    - What should I do differently next time?"

2. Check if issue was resolved elsewhere:
   - Look for merged PRs on same issue
   - Check if issue is still open

3. Learn from the closure to avoid repeating the same approach
```

---

## Workflow Best Practices for EFO

### Before Starting a Task

1. **Check for existing PRs** on the issue
2. **Search for similar terms** if adding new concepts
3. **Read the issue thoroughly** including all comments
4. **Check for related open issues** that might conflict

### During Implementation

1. **One PR per issue** - always
2. **Consistent methodology** - same approach each run
3. **Track term IDs** - avoid proposing IDs already in use
4. **Document blockers** - if tools unavailable, say so

### When Receiving Reviewer Feedback

1. **Update existing branch** - never create new PR
2. **Address all comments** - don't ignore any
3. **Push commits to same PR** - keep history clean
4. **Ask for clarification** if feedback is unclear

### If PR is Closed

1. **Request explanation** if none given
2. **Learn from feedback** for next time
3. **Check issue status** - was it resolved?

---

## Quick Reference Card

| Scenario | Required Actions |
|----------|-----------------|
| Assigned new issue | 1. Check for existing PRs, 2. Search similar terms, 3. Create ONE PR |
| Reviewer asks for changes | Update existing branch, push. NEVER create new PR |
| Blocked by tools/firewall | Document in PR comments, ask for help |
| Adding new term | Search for similar terms first, discuss if found |
| PR closed silently | Ask for feedback to understand why |
| Found existing WIP PR | Continue that PR, don't create new one |

---

## Success Metrics

**Current state (51 PRs):**
- Merged: 20 (39.2%)
- Failed: 28 (54.9%)
- Open: 3 (5.9%)

**Current closed-PR success rate:** 41.7% (20/48)

**Target:** 80%+ success rate on closed PRs

**Improvement breakdown:**
| Fix | PRs Saved | New Success Rate |
|-----|-----------|------------------|
| Eliminate duplicate PR creation | 23 | 86% (20/23) |
| + Complete WIP PRs | 2 | 88% (22/25) |
| + Check for similar terms | 1 | 88% |

Eliminating duplicate PRs alone would raise success rate from 41.7% to ~86%.

---

## Appendix: PR Coverage Matrix

| Issue | Duplicate PRs | WIP Abandoned | Similar Term | Silent Close |
|-------|---------------|---------------|--------------|--------------|
| #2490 | 13 PRs | | | |
| #2546 | 4 PRs | 2 | | |
| #2562 | 4 PRs | 2 | | |
| #2445 | 2 PRs | 1 | | |
| DLCO | | | ✓ | |
| OBA | | | | 2 PRs |
| Misc | | | | 1 PR |

---

## Key Insight

**The single most impactful change is: ONE PR PER ISSUE**

23 of 28 failures (82%) were duplicate PRs. If the agent had updated existing branches instead of creating new PRs, success rate would jump from 41.7% to approximately 86%.
