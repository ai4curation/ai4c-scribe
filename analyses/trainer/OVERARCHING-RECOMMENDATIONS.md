# Overarching Training Recommendations for AI Ontology Agents

## Executive Summary

This document synthesizes failure analyses across 5 ontology projects (GO, MONDO, Uberon, CL, EFO) with 260 total PRs from AI agents (dragon-ai-agent, copilot-swe-agent).

| Project | Total PRs | Merge Rate | First-Try Rate | Primary Failure Mode |
|---------|-----------|------------|----------------|---------------------|
| GO | 68 | 77.6% | **65.0%** | Duplicate PRs, Obsoletion errors |
| MONDO | 26 | 44.0% | **26.7%** | Duplicate PRs (7 PRs for 1 term!) |
| Uberon | 14 | 100% | **37.5%** | Attribution errors |
| CL | 101 | 95.3% | **5.6%** | Every PR needs modifications! |
| EFO | 51 | 41.7% | **~0%** | Duplicate PRs (13 PRs for 1 issue!) |

**CRITICAL FINDING:** The **first-try success rate** reveals a hidden problem. CL looks great with 95.3% eventual merge rate, but only 5.6% of PRs are accepted without modifications. This means reviewers are doing extensive hand-holding.

**Key Findings:**
1. **First-try success is the real metric** - Merge rate alone is misleading
2. **Eliminating duplicate PR creation** accounts for 82% of EFO failures
3. **All ontologies have low first-try rates** - Training on patterns is critical

**Caveats:**
1. **Metric denominators vary by source** - Some first-try rates are computed only on merged PRs with category data; do not compare against total PR counts without aligning denominators.
2. **Silent closures limit root-cause certainty** - Several EFO/GO PRs were closed without feedback; treat those as uncertain and seek clarification rather than overfitting training rules.
3. **Task mix differs by ontology** - Higher first-try rates may reflect simpler issue scopes, not superior agent behavior.

---

## Cross-Project Failure Mode Analysis

### Tier 1: Critical (>40% of failures in multiple projects)

#### 1. DUPLICATE PR CREATION

**Prevalence:** GO (4 PRs), MONDO (9 PRs), EFO (23 PRs)

**The Pattern:**
- Agent creates new PR instead of updating existing branch
- Reviewers explicitly request updates to existing PRs
- Agent ignores request and creates new PR anyway
- Process repeats, generating chains of 7-13 PRs for single issues

**Worst Case:** MONDO argyrophilic grain disease saga
- 7 PRs created over 2 months for 1 term
- Reviewer said "update this PR" multiple times
- Agent kept creating new PRs
- Term STILL not added after all this effort

**Training Rule:**
```
ABSOLUTE RULE: ONE PR PER ISSUE

When asked to revise a PR:
1. ALWAYS push commits to the SAME branch
2. NEVER create a new PR unless explicitly told to abandon
3. Check for existing PRs before starting work:
   gh pr list --search "[issue keywords]" --state all

If you've created more than 1 PR for an issue:
- STOP immediately
- Ask for guidance
- Something is wrong with your approach

Exception:
- If maintainers explicitly request splitting work into multiple PRs, follow their guidance and document the split clearly in each PR.
```

---

### Tier 2: High Impact (Caused multiple failures per project)

#### 2. CONTENT-OBJECTIVE MISMATCH (and recovery failure)

**Prevalence:** GO (1 PR with cascading effects)

**The Pattern:**
- PR title/description says one thing
- Actual diff shows completely different changes
- Example: GO PR 30730 titled "Obsolete 7 terms" but diff just added 1 metadata line

**Important nuance:** In the GO case, the agent actually self-corrected in PR 30731 (which had correct content). However, leaving the wrong PR (30730) open alongside the correct one (30731) created confusion. A human curator ended up doing the work themselves in PR 30736, bypassing both agent PRs.

**Lesson:** When you create a PR with wrong content, close it immediately with explanation before creating the corrected version.

**Training Rule:**
```
PRE-SUBMISSION VERIFICATION:

Before creating ANY PR:
1. Run `git diff` and READ the output
2. Verify EVERY change relates to the stated objective
3. Confirm PR title matches actual changes
4. If diff doesn't match objective - DO NOT SUBMIT

Checklist:
[ ] Diff only contains changes for this task
[ ] No extraneous changes included
[ ] PR title accurately describes the diff
[ ] Commit messages match actual changes
```

#### 3. ONTOLOGY-SPECIFIC CONVENTION ERRORS

**GO Obsoletion:**
- Missing "obsolete " prefix on name
- Missing "OBSOLETE. " prefix on definition
- Failing to remove ALL is_a relationships
- Wrong replacement tags (replaced_by vs consider)

**MONDO Annotations:**
- Grouping multiple PMIDs in single annotation
- Wrong: `synonym: "AGD" EXACT [PMID:1, PMID:2, PMID:3]`
- Correct: Each PMID as separate annotation
- PMC→PMID conversion errors

**Training Rule:**
```
ONTOLOGY-SPECIFIC PATTERNS:

Before modifying ANY ontology:
1. Find 2-3 similar recent changes (merged PRs)
2. Copy the EXACT pattern used
3. If pattern is unclear, ASK for an example

For GO obsoletion specifically - ALL of:
[ ] Name prefixed with "obsolete "
[ ] Definition prefixed with "OBSOLETE. "
[ ] ALL is_a relationships removed
[ ] ALL intersection_of removed
[ ] is_obsolete: true added
[ ] replaced_by OR consider added
[ ] term_tracker_item added

For MONDO annotations:
[ ] Each PMID as individual annotation
[ ] PMIDs verified via PubMed (not guessed)
[ ] Source annotations use OMIM/PMID, not GitHub URLs
```

#### 4. HIGH-IMPACT CHANGES WITHOUT DISCUSSION

**Prevalence:** GO (3 PRs), CL (1 PR)

**The Pattern:**
- Agent makes large-scale changes without curator approval
- Obsoleting high-level terms affects hundreds of children
- Adding 7+ new terms without discussion

**Training Rule:**
```
DISCUSSION-FIRST CHANGES:

These changes REQUIRE discussion before implementing:
- Obsoleting any term with >10 children
- Adding 3+ new terms
- Changing logical definitions of widely-used terms
- Any change that triggers "large scale" bot warnings

Process:
1. Comment on issue: "I plan to [X]. This affects [N] terms."
2. Wait for curator approval
3. Only then create PR

Query to check impact:
grep "is_a: [TERM_ID]" ontology-file.obo | wc -l
```

---

### Tier 3: Medium Impact (Caused some failures)

#### 5. ATTRIBUTION ERRORS

**Prevalence:** Uberon (1 PR)

**The Pattern:**
- Wrong contributor name/ORCID used
- Confused similar names during lookup
- Sarah vs Stan Laulederkind

**Training Rule:**
```
ATTRIBUTION ACCURACY:

1. Extract contributor info DIRECTLY from issue text
2. Use the EXACT name provided, not similar matches
3. If ORCID lookup returns different name - ASK for clarification
4. When in doubt, quote the issue: "Issue says submitted by [X]"
```

#### 6. EXTERNAL ACCESS LIMITATIONS

**Prevalence:** CL (1 PR), EFO (multiple)

**The Pattern:**
- Agent can't access external resources (OLS, web APIs)
- Instead of reporting limitation, creates elaborate workarounds
- Workarounds don't solve the problem

**Training Rule:**
```
CAPABILITY BOUNDARIES:

When a task requires resources you cannot access:
1. IMMEDIATELY report the limitation
2. DO NOT create workaround scripts
3. Suggest alternatives:
   - "Please provide data as CSV"
   - "This requires human curator"
   - "Use web-browsing tool locally"

Example response:
"I cannot access [X] due to sandboxing restrictions.
This task cannot be completed as described.
Alternative: [concrete suggestion]"
```

#### 7. SCOPE CREEP

**Prevalence:** GO (1 PR), CL (1 PR)

**The Pattern:**
- Agent makes "helpful" changes beyond task scope
- Modifies Makefiles when not requested
- Removes metadata from unrelated terms

**Training Rule:**
```
MINIMAL CHANGES ONLY:

1. ONLY modify files explicitly mentioned in issue
2. NEVER "improve" or "clean up" unrelated code
3. If no changes needed, report "No changes needed"
4. If you notice other issues:
   - Note in PR description
   - Create SEPARATE issue
   - Do NOT fix in this PR
```

#### 8. PMID/IDENTIFIER VALIDATION ERRORS

**Prevalence:** Uberon (1 PR), MONDO (multiple)

**The Pattern:**
- Agent incorrectly rejects valid identifiers
- Claims PMIDs are "out of range"
- Wrong PMC→PMID conversions

**Training Rule:**
```
EXTERNAL IDENTIFIER HANDLING:

DO validate:
- Format correctness (PMID:12345 pattern)
- Basic syntax

DO NOT validate:
- Numeric ranges (PMIDs have no upper limit)
- "Existence" without API access

When maintainers provide references, trust them.
If concerned, proceed and note concern - don't block.

For PMC→PMID conversion:
- Use PubMed directly if possible
- NEVER guess PMID numbers
- If uncertain, ask for the correct PMID
```

---

## Project-Specific Insights

### GO: Obsoletion Expertise Required

GO has strict obsoletion conventions. Agent success rate dropped specifically on obsoletion tasks. Recommendation: Create obsoletion-specific training examples or use specialized prompting for obsoletion issues.

### MONDO: Learning Loop Broken

The argyrophilic grain disease saga shows the agent failed to learn from repeated failures. Each new PR repeated the same mistakes. Recommendation: Implement feedback incorporation - before creating new PR, review why last one failed.

### Uberon: 100% Eventually Merge, But Low First-Try

All Uberon PRs eventually merged, but only 42.9% on first try. The failures were minor (attribution, IDs). This suggests the agent is close to optimal for this ontology - small refinements would help.

### CL: Misleading "Success" - 95.3% Merge but 5.6% First-Try

**CL is actually a cautionary tale, not a success story.**

The 95.3% merge rate masks the reality:
- Only **5.6% of PRs are accepted without modifications**
- 94.4% of merged PRs required reviewer corrections
- Reviewers are essentially fixing every submission

This means:
- The agent is creating drafts, not finished work
- Curator time is being spent on corrections, not reviews
- The "high success rate" reflects reviewer patience, not agent quality

**Recommendation:** CL needs the MOST training improvement, not the least. Focus on:
- Template-based submissions copying exact patterns from recent merged PRs
- Pre-submission validation against known good examples
- Understanding why nearly every PR needs modification

### EFO: Systematic Failure on Complex Tasks

EFO had the lowest success rate (41.7%), primarily due to duplicate PRs on complex issues. The agent struggled with:
- Issues requiring external tool access
- Issues requiring iterative exploration

Recommendation: For complex EFO issues, require human co-pilot or provide data upfront.

---

## Universal Training Checklist

### Before Starting ANY Task

```
[ ] Read the full issue including all comments
[ ] Search for existing PRs: gh pr list --search "[keywords]" --state all
[ ] Check if anyone else is working on it
[ ] Search for similar terms if adding new ones
```

### During Implementation

```
[ ] Make minimal, focused changes only
[ ] Follow ontology-specific conventions exactly
[ ] Use existing patterns as templates
[ ] Document any blockers or limitations
```

### Before Submitting PR

```
[ ] Review git diff - does it match objective?
[ ] Check for extraneous changes
[ ] Verify PR title accurately describes changes
[ ] Run any available validation (robot, etc.)
```

### After Reviewer Feedback

```
[ ] Create checklist from reviewer comments
[ ] Address EACH point explicitly
[ ] Push to SAME branch - never create new PR
[ ] Ask for clarification if anything unclear
```

### If Struggling

```
[ ] STOP after 2 failed attempts on same issue
[ ] Ask for concrete example
[ ] Request human review of approach
[ ] DO NOT keep creating new PRs
```

---

## Success Metrics by Project

### Merge Rate vs First-Try Rate

| Project | Merge Rate | First-Try Rate | Gap | Key Fix |
|---------|------------|----------------|-----|---------|
| GO | 77.6% | 65.0% | 12.6% | Obsoletion training |
| MONDO | 44.0% | 26.7% | 17.3% | Annotation format training |
| Uberon | 100% | 37.5% | 62.5% | Attribution + ID allocation |
| CL | 95.3% | 5.6% | **89.7%** | Pattern-based submissions |
| EFO | 41.7% | ~0% | **41.7%** | Eliminate duplicates + training |

### Targets

| Project | Current First-Try | Target First-Try | Key Fix |
|---------|-------------------|------------------|---------|
| GO | 65.0% | 80%+ | Better obsoletion conventions |
| MONDO | 26.7% | 60%+ | Annotation patterns + no duplicates |
| Uberon | 37.5% | 70%+ | Attribution verification + ID handling |
| CL | 5.6% | 50%+ | Template-based submissions |
| EFO | ~0% | 40%+ | Stop duplicate PRs + patterns |

**The CL "success story" is actually a warning:** 95% merge rate with 6% first-try rate means reviewers are doing almost all the work.

---

## Implementation Priority

### P0: Must Fix Immediately
1. **ONE PR PER ISSUE rule** - Would fix 82% of EFO failures, significant GO/MONDO failures
2. **Pre-submission diff verification** - Prevents content-objective mismatch

### P1: High Value
3. **Ontology-specific convention training** - GO obsoletion, MONDO annotations
4. **Discussion-first for high-impact changes**

### P2: Important
5. **Attribution verification** - Check names against issue source
6. **Capability limitation reporting** - Stop elaborate workarounds
7. **Scope discipline** - Only change what's requested

### P3: Refinement
8. **PMID/identifier handling**
9. **Learning from previous failures**
10. **Template-based submissions**

---

## Verification Notes

All data in this document was cross-referenced against actual GitHub PRs using `gh` CLI:
- GO: 68 PRs confirmed (45 merged, 13 closed, 10 open)
- MONDO: 26 PRs confirmed (11 merged, 14 closed, 1 open)
- Uberon: 14 PRs confirmed (all merged, 8 needed modifications)
- CL: 101 PRs confirmed (81 merged, 4 closed, 16 open)
- EFO: 51 PRs confirmed (20 merged, 28 closed, 3 open)

PR 30730 (GO) verified: Title said "Obsolete 7 terms" but diff showed only `+created_by: dragon-ai-agent` line added. Failure analysis confirmed accurate.

---

## Related Documents

- **[SUCCESS-PATTERNS.md](./SUCCESS-PATTERNS.md)** - What types of issues work well (obsoletion, xref management, typo fixes)
- **[AGENT-CONFIGURATIONS.md](./AGENT-CONFIGURATIONS.md)** - Agent solutions and configurations across repos
- **Project-specific analyses:**
  - [GO training plan](./go/training-plan.md)
  - [MONDO training plan](./mondo/training-plan.md)
  - [Uberon training plan](./uberon/training-plan.md)
  - [CL training plan](./cl/training-plan.md) - **Contains critical feedback patterns**
  - [EFO training plan](./efo/training-plan.md)

---

*Generated: 2025-12-21*
*Based on analysis of 260 PRs across 5 ontology projects*
