# Failure Analysis: PR #3201

**PR:** [#3201 - Add onychofibroblast (CL_4072103) term to Cell Ontology](https://github.com/obophenotype/cell-ontology/pull/3201)

**Issue:** [#3186](https://github.com/obophenotype/cell-ontology/issues/3186)

**Status:** CLOSED (not merged) - Duplicate

**Closed:** 2025-07-24

## Summary

The agent created a duplicate PR for adding the onychofibroblast term. PR #3200 was the accepted version, while #3201 was closed as a duplicate with a slightly incomplete implementation.

## What the Agent Did

In PR #3201:
1. Added class declaration for CL_4072103
2. Added label "onychofibroblast"
3. Added definition with PMID references
4. Established parent relationship to fibroblast (CL_0000057)

What was missing compared to #3200:
1. **No `part_of` relationship** to anatomical location (nail)
2. **No contributor annotation**

## Why It Failed

### Root Cause: Duplicate PR Creation

The agent created two PRs for the same issue:
- #3200 (merged) - More complete implementation with `part_of` relationship
- #3201 (closed) - Less complete implementation without `part_of`

### Evidence from Comments

dosumis:
> "Closing as accidental duplicate with #3200 - interesting that this one is slightly different as lacks a part relationship."

Caroline-99:
> "It also didn't add a contributor in this one. I think the reason it lacks the `part_of` relationship is that, in my ticket, I wrote 'new Uberon term needed: onychodermis' under anatomical location. In the other PR, Copilot worked out that the term is part of the nail and added the relationship accordingly."

## Failure Modes

### 1. Duplicate PR Creation

**Category:** Process error - creating multiple PRs for same issue

**Why it happened:** Agent may have been triggered multiple times or lost track of previous work

### 2. Incomplete Implementation

**Category:** Missing required elements

**Why it happened:** The issue mentioned "new Uberon term needed: onychodermis" for anatomical location. The agent in #3201 interpreted this as "no location available" rather than finding an existing approximation (nail).

## Lessons Learned

1. **Check for existing PRs**: Before creating a new PR, search for existing PRs addressing the same issue
2. **Infer reasonable approximations**: When a specific term isn't available (onychodermis), use the closest available term (nail)
3. **Include all standard annotations**: Always add contributor, part_of relationships, and other standard metadata
4. **Be consistent across attempts**: If retrying a task, ensure the new attempt includes all improvements from previous attempts

## Pattern Recognition

This failure shows inconsistent behavior:
- Two runs of the same task produced different outputs
- The "better" run (#3200) inferred the part_of relationship
- The "worse" run (#3201) was more literal and less complete

## Remediation

Before creating a PR:
```bash
# Check for existing PRs on the same issue
gh pr list --repo obophenotype/cell-ontology --search "fixes:#3186" --state all
```

Checklist for new term PRs:
- [ ] Class declaration
- [ ] rdfs:label
- [ ] Text definition with references
- [ ] Parent class relationship
- [ ] `part_of` anatomical location (use closest available if exact term missing)
- [ ] Contributor annotation
- [ ] Database cross-references (if available)

## Training Instruction

```
When adding a new cell type term:
1. First check if a PR already exists for this issue
2. Include ALL standard annotations:
   - Label, definition, references
   - Parent class (is_a)
   - Anatomical location (part_of) - use closest available term if exact match unavailable
   - Contributor (dc:contributor)
3. If the issue mentions "new term needed" for a dependency (e.g., Uberon term),
   use the closest existing term and note the approximation
```
