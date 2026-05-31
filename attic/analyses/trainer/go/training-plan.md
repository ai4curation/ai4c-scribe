# Training Plan for Dragon-AI-Agent on GO Ontology

## Executive Summary

Analysis of 68 PRs by dragon-ai-agent to geneontology/go-ontology:

| Status | Count | Percentage |
|--------|-------|------------|
| Merged | 45 | 66.2% |
| Closed (not merged) | 13 | 19.1% |
| Open | 10 | 14.7% |
| **Total** | **68** | 100% |

**Success rate of closed PRs:** 45/58 = 77.6%

This training plan addresses all 13 failed PRs. The failure modes below are organized by count; some PRs exhibited multiple issues (noted where applicable).

**Caveat:** One "failure" (PR #30731) was technically correct but superseded by a human PR due to confusion from an earlier wrong PR. Treat this as a process coordination issue rather than a pure content error.

---

## Complete Failure Inventory

All 13 failed PRs are accounted for:

| PR | Primary Failure Mode | Section |
|----|---------------------|---------|
| 30310 | Obsoletion convention errors | §2 |
| 30312 | Duplicate PR + obsoletion errors | §1, §2 |
| 30604 | File format error | §4 |
| 30730 | Content mismatch | §3 |
| 30731 | Scope creep / extraneous changes | §5 |
| 30799 | Permission test (non-training) | §8 |
| 30827 | Approach needed discussion first | §7 |
| 30828 | High-impact changes without discussion | §7 |
| 30985 | New terms needed discussion first | §7 |
| 31004 | Duplicate PR | §1 |
| 31005 | Duplicate PR | §1 |
| 31045 | Term ID conflict | §6 |
| 31244 | Obsoletion needed rework | §2 |

---

## Critical Failure Modes and Training Instructions

### 1. NEVER Create New PRs When Asked to Revise (4 PRs)

**Affected PRs:** 30310→30312, 31004→31005

**The Problem:**
When reviewers requested changes to existing PRs, the agent created entirely new PRs instead of updating the existing branch.

**Training Instructions:**
```
RULE: When a reviewer asks you to modify or fix a PR:
1. ALWAYS push commits to the SAME branch
2. NEVER create a new PR
3. Use `git push` to update the existing PR

Example of correct behavior:
- Reviewer: "Please fix the term name to include 'obsolete'"
- CORRECT: Make change, commit, push to same branch
- WRONG: Create new PR with the fix

If you're unsure whether to create a new PR or update existing:
- Default to updating existing
- Only create new PR if explicitly told to abandon the previous one
```

---

### 2. GO Obsoletion Has Strict Conventions (3 PRs)

**Affected PRs:** 30310, 30312, 31244

**The Problem:**
Multiple failures related to incorrect obsoletion patterns. GO has very specific requirements.

**Training Instructions:**
```
RULE: When obsoleting a GO term, you MUST complete ALL of these steps:

1. PREFIX the term name with "obsolete "
   - CORRECT: name: obsolete D-erythro-sphingosine kinase activity
   - WRONG: name: D-erythro-sphingosine kinase activity

2. PREFIX the definition with "OBSOLETE. "
   - CORRECT: def: "OBSOLETE. The original definition..."
   - WRONG: def: "The original definition..."

3. REMOVE all logical axioms:
   - Remove ALL is_a relationships (superclass)
   - Remove ALL intersection_of
   - Remove ALL relationship: lines
   - Obsolete terms must NOT have parents!

4. Use correct replacement tags:
   - Use replaced_by for direct replacements (1:1 mapping)
   - Use consider ONLY when multiple alternatives exist
   - Do NOT use alt_id unless it's a true merge

5. Handle xrefs properly:
   - Move xrefs from obsolete term to replacement term
   - Apply appropriate SKOS qualifiers (exactMatch, narrowMatch)

6. Add ALL required metadata:
   - is_obsolete: true
   - comment: explaining reason for obsoletion
   - term_tracker_item: linking to GitHub issue

7. Be aware of additional requirements:
   - Some obsoletions require email announcements
   - Annotation review may be needed
   - RHEA reaction participants file may need updating
```

---

### 3. Verify PR Content Matches Objective (2 PRs)

**Affected PRs:** 30730, 30731

**The Problem:**
Some PRs had content completely unrelated to the stated objective. PR 30730 claimed to obsolete 7 terms but actually just added metadata to an unrelated term.

**Training Instructions:**
```
RULE: Before submitting a PR:

1. REVIEW the git diff
2. VERIFY every change relates to the stated objective
3. CHECK commit message matches the actual changes
4. CONFIRM the PR description accurately reflects the diff

Pre-submission checklist:
□ Does the diff only contain changes for this task?
□ Are there any extraneous changes? If yes, remove them.
□ Does the PR title match what the diff shows?
□ Does each commit message accurately describe its changes?
```

---

### 4. Check File Formats Before Modifying (1 PR)

**Affected PRs:** 30604

**The Problem:**
Agent modified a TSV file with incorrect format.

**Training Instructions:**
```
RULE: Before modifying any data/config file:

1. READ the file first to understand the format
2. IDENTIFY column headers and delimiters
3. MATCH the exact format of existing entries
4. VALIDATE changes with any available tools

For TSV files specifically:
- Check column order
- Check if there's a header row
- Check the delimiter (tab, not spaces)
- Ensure proper quoting if needed
```

---

### 5. Avoid Scope Creep and Stay Focused (1 PR)

**Affected PRs:** 30731

**The Problem:**
PR included extraneous changes unrelated to the task—removed `created_by` metadata from many terms while supposedly obsoleting other terms.

**Training Instructions:**
```
RULE: Keep PRs minimal and focused:

1. Only make changes directly requested
2. Do NOT "clean up" or "improve" unrelated code
3. Do NOT remove or add metadata unless asked
4. If you notice issues outside the task scope:
   - Note them in the PR description
   - Create a separate issue for them
   - Do NOT fix them in this PR
```

---

### 6. Check Term ID Availability (1 PR)

**Affected PRs:** 31045

**The Problem:**
Multiple PRs used the same term ID (GO:7770028) for different concepts. PR 31004 proposed GO:7770028 for N-acetyl-D-glucosamine transporter, then PR 31045 reused GO:7770028 for glycoprotein cargo receptor.

**Training Instructions:**
```
RULE: Before creating new GO terms:

1. CHECK if the proposed ID exists in the ontology
2. CHECK recent/pending PRs for the same ID
3. Use sequential IDs in the GO:777xxxx range
4. If unsure, query the current maximum ID first

Example verification:
$ grep "id: GO:7770" src/ontology/go-edit.obo | tail -5
```

---

### 7. Discuss High-Impact or Conceptual Changes First (3 PRs)

**Affected PRs:** 30827, 30828, 30985

**The Problem:**
- PR 30828: Obsoleting high-level terms (organic anion/cation transport) cascaded through hundreds of child terms
- PR 30827: Approach to create broader replacement term needed curator input first
- PR 30985: Added 7 new cell differentiation terms - closed without explanation (likely needed discussion first)

**Training Instructions:**
```
RULE: For changes to high-level/frequently-used terms OR conceptual changes:

1. FIRST analyze the impact:
   - How many terms reference this as a parent?
   - What annotation changes are needed?

2. DISCUSS on the issue before implementing
   - Get curator approval for the approach
   - Confirm new term IDs if creating replacements

3. If proceeding with large changes:
   - May need to break into multiple PRs
   - Ensure all children are properly re-parented
   - Consider if obsoletion is the right approach (vs. renaming/refactoring)

Query to check impact:
$ grep "is_a: GO:XXXXXXX" src/ontology/go-edit.obo | wc -l

RULE: For adding multiple new terms (3+):

1. Propose the terms on the issue BEFORE implementing
2. Get explicit curator approval for:
   - Term names and definitions
   - Logical definitions and relationships
   - Any external ontology imports needed
3. Only create PR after approach is confirmed
```

---

### 8. Permission/Test PRs (1 PR - Non-Training)

**Affected PRs:** 30799

**The Problem:**
This was an intentional permission test PR ("Add blank line to README"). Not a training case.

**Notes:**
- Accounted for completeness
- No training action required
- Agent correctly identified this as a test task

---

## Workflow Best Practices

### Before Starting a Task
1. Read the issue carefully
2. Check for any linked issues or related discussions
3. Verify the proposed term IDs are available
4. Understand the scope—what's in and what's out

### During Implementation
1. Make minimal, focused changes
2. Follow GO conventions exactly
3. Use proper commit messages
4. Review your diff before committing

### Before Submitting PR
1. Verify diff matches objective
2. Run syntax validation if available (`robot convert`)
3. Check for SPARQL violations
4. Write accurate PR description

### After Review Feedback
1. ALWAYS update the existing branch
2. NEVER create new PRs for revisions
3. Address all reviewer comments
4. Re-verify after changes

---

## Quick Reference Card

| Scenario | Required Actions |
|----------|-----------------|
| Reviewer asks for changes | Update existing branch, push. NEVER create new PR. |
| Obsoleting a term | **All of:** (1) prefix name with "obsolete ", (2) prefix def with "OBSOLETE. ", (3) remove ALL is_a/intersection_of/relationship axioms, (4) add is_obsolete:true, (5) add replaced_by or consider, (6) add comment, (7) add term_tracker_item |
| Creating new term | Verify ID is not in use in ontology AND pending PRs |
| Modifying config files | Read file first to understand exact format |
| High-impact changes | Discuss on issue first, get curator approval |
| Unsure about scope | Ask on the issue before implementing |

---

## Success Metrics

**Current state (all 68 PRs):**
- Merged: 45 (66.2%)
- Failed: 13 (19.1%)
- Open: 10 (14.7%)

**Current closed-PR success rate:** 77.6% (45/58)

**Target:** 90%+ success rate on closed PRs

**Improvement breakdown:**
| Fix | PRs Saved | New Success Rate |
|-----|-----------|------------------|
| Eliminate duplicate PR creation | 4 | 84.5% |
| + Perfect obsoletion compliance | 3 | 89.7% |
| + Verify content matches objective | 2 | 93.1% |

---

## Appendix: PR Coverage Matrix

| PR # | §1 Dup | §2 Obs | §3 Match | §4 Fmt | §5 Scope | §6 ID | §7 Discuss | §8 Test |
|------|--------|--------|----------|--------|----------|-------|------------|---------|
| 30310 | | ✓ | | | | | | |
| 30312 | ✓ | ✓ | | | | | | |
| 30604 | | | | ✓ | | | | |
| 30730 | | | ✓ | | | | | |
| 30731 | | | ✓ | | ✓ | | | |
| 30799 | | | | | | | | ✓ |
| 30827 | | | | | | | ✓ | |
| 30828 | | | | | | | ✓ | |
| 30985 | | | | | | | ✓ | |
| 31004 | ✓ | | | | | | | |
| 31005 | ✓ | | | | | | | |
| 31045 | | | | | | ✓ | | |
| 31244 | | ✓ | | | | | | |
