# Training Plan: dragon-ai-agent for MONDO Repository

## Executive Summary

Analysis of 26 PRs from dragon-ai-agent revealed a **44% success rate** (11 merged, 14 closed, 1 open). The failures cluster around a few key behavioral patterns that can be addressed through targeted training.

**Caveat:** At least one failure (PR #9167) was likely due to later human edits (Class/Individual conflict). Treat this as a validation/process gap, not solely an agent error.

## Failure Mode Analysis

| Rank | Failure Mode | Occurrences | Impact |
|------|--------------|-------------|--------|
| 1 | Creating new PRs instead of updating existing | 9 | Critical |
| 2 | Wrong annotation/reference format | 7 | High |
| 3 | Duplicate of existing work | 3 | Medium |
| 4 | Destructive edits (removal instead of addition) | 2 | High |
| 5 | Failed to follow reviewer instructions | 5 | High |
| 6 | Technical OWL/OBO structure errors | 1 | Medium |

---

## Training Instructions

### 1. CRITICAL: Always Update Existing PRs

**Problem**: The agent repeatedly created new PRs when asked to fix issues in existing ones. The argyrophilic grain disease saga resulted in 7 PRs for 1 term.

**Training Rule**:
```
WHEN a reviewer requests changes to a PR:
  1. ALWAYS commit changes to the SAME PR branch
  2. NEVER create a new PR unless explicitly told to "close this and start fresh"
  3. If you see "please update this PR" - that means SAME PR, not new one
  4. Push to the existing branch, not a new branch
```

**Verification Step**:
Before creating any new PR, ask yourself:
- Is there an existing PR for this issue?
- Has a reviewer asked for changes to an existing PR?
- If yes to either, UPDATE the existing PR.

---

### 2. Learn MONDO Annotation Patterns

**Problem**: The agent consistently grouped PMIDs together instead of creating individual annotations.

**Training Rule - Individual Annotations**:
```
# WRONG - grouped PMIDs:
synonym: "AGD" EXACT [PMID:29213935, PMID:16319301, PMID:18234698]
is_a: MONDO:0001627 {source="PMID:29213935, PMID:16319301"}

# CORRECT - individual annotations:
synonym: "AGD" EXACT [PMID:29213935]
xref: PMID:16319301
xref: PMID:18234698
is_a: MONDO:0001627 {source="PMID:29213935"}
is_a: MONDO:0001627 {source="PMID:16319301"}
```

**Training Rule - Reference Conversion**:
```
ALWAYS convert references to PMID format:
- PMC5618985 → Look up correct PMID (PMID:29213935)
- DOI:10.1093/brain/awm305 → Look up PMID (PMID:18234698)
- DOI:10.1097/00019442-200512000-00008 → Look up PMID (PMID:16319301)

Use PubMed or the DOI resolver to get accurate PMIDs.
NEVER guess PMID numbers.
```

**Training Rule - Source Annotations**:
```
For SubClassOf/is_a relationships:
- Use authoritative sources: OMIM, PMID, ORPHA
- NOT GitHub issue URLs
- Example: {source="OMIM:620836"} not {source="https://github.com/..."}
```

---

### 3. Check for Existing Work Before Starting

**Problem**: Multiple PRs were closed because work was already done or in progress.

**Training Rule - Pre-Work Checklist**:
```
BEFORE starting any PR:
1. Search for existing PRs:
   gh pr list --search "<keywords>" --repo monarch-initiative/mondo --state all

2. Check issue comments for:
   - Recent activity
   - "Fixed by #XXXX" references
   - Other contributors already assigned

3. Check issue labels:
   - "in progress" or similar
   - "assigned" to someone

4. If in doubt, comment on the issue:
   "Is anyone currently working on this? I'd like to help."
```

---

### 4. Additive, Not Destructive Edits

**Problem**: The agent removed existing relationships instead of adding new ones alongside them.

**Training Rule**:
```
In MONDO, the default behavior is ADDITIVE:
- ADD new is_a relationships; don't REMOVE existing ones
- ADD new annotations; don't REPLACE unless told to
- When simplifying, only remove what is EXPLICITLY requested

Exception: Only remove content if the issue/reviewer specifically says:
- "remove this relationship"
- "delete this annotation"
- "obsolete this term"
```

**Verification Step**:
Before committing, review the diff:
- Are you removing any is_a relationships? If yes, confirm this was requested.
- Are you removing any annotations? If yes, confirm this was requested.

---

### 5. Follow Reviewer Instructions Precisely

**Problem**: The agent made partial fixes or misinterpreted reviewer requests.

**Training Rule**:
```
When a reviewer provides feedback:
1. Copy each instruction into a checklist
2. Address EACH point explicitly
3. If an instruction is unclear, ask for clarification BEFORE implementing
4. In your response, show exactly how each point was addressed

Example response format:
"I have made the following changes:
1. ✅ [Instruction 1] - Changed X to Y
2. ✅ [Instruction 2] - Added annotation Z
3. ❓ [Instruction 3] - Unclear, could you clarify?"
```

**Training Rule - Ask for Examples**:
```
If told to "look at other terms for examples":
1. Actually search for similar terms in the ontology
2. Copy the EXACT pattern used
3. Show the example in your commit message or PR comment
```

---

### 6. Learn MONDO Obsoletion Patterns

**Problem**: Wrong obsoletion reasons and codes were used.

**Training Rule - Obsoletion Codes**:
```
Standard IAO codes for term obsoletion:

For merged terms (duplicates):
  property_value: IAO:0000231 MONDO:TermsMerged
  replaced_by: MONDO:XXXXXXX

For out-of-scope terms:
  property_value: IAO:0000231 MONDO:OutOfScope

For duplicate in MONDO:
  property_value: IAO:0000231 MONDO:duplicateInMondo

Always include issue tracker reference:
  property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/XXXX"
```

---

### 7. Validate Before Committing

**Problem**: OWL structure errors and syntax issues.

**Training Rule**:
```
Before pushing any commit:
1. Run: robot validate src/ontology/mondo-edit.obo
2. Run: robot convert -i src/ontology/mondo-edit.obo -o /dev/null
3. Check for Class vs Individual issues

If validation fails, FIX before pushing.
```

---

## Behavioral Guidelines

### Communication Pattern

```
When receiving a task:
1. Acknowledge the task
2. State your plan
3. Ask clarifying questions if needed
4. Implement
5. Show exactly what you did
6. Ask if anything needs adjustment

DO NOT:
- Claim you've made changes you haven't made
- Mark a review as "approved" (you're the contributor, not reviewer)
- Create duplicate PRs
- Ignore feedback
```

### Handling Feedback

```
When receiving review feedback:
1. Thank the reviewer
2. Address each point systematically
3. If you disagree, explain why politely
4. Commit to the SAME PR
5. Request re-review when done

Example:
"Thank you for the feedback! I've addressed each point:
1. [Point 1] - Done, see line 123
2. [Point 2] - Done, see line 456
3. [Point 3] - I have a question: [clarification]

Ready for re-review when you have time."
```

### When to Stop and Ask

```
STOP and ask a human when:
- You've created more than 2 PRs for the same issue
- A reviewer seems frustrated
- You're not sure if you understood the instructions
- You're about to delete significant content
- The issue is assigned to someone else
```

---

## Success Patterns to Reinforce

The following PR types had high success rates:

1. **Simple parent additions** (#9717, #9724, #9726)
   - Adding one is_a relationship
   - Clear issue request
   - Minimal changes

2. **Cross-reference additions** (#9283, #9198, #9652)
   - Adding xrefs or synonyms
   - Well-defined patterns

3. **URL/link fixes** (#9261)
   - Mechanical changes with clear before/after

4. **Follow-up fixes** (#9209)
   - Learning from previous failed attempt
   - Applying feedback correctly

---

## Metrics for Improvement

Target metrics after training:

| Metric | Current | Target |
|--------|---------|--------|
| Overall success rate | 44% | 75% |
| PRs per issue | 2.3 | 1.2 |
| "Update existing PR" compliance | 0% | 100% |
| Correct annotation format | ~30% | 95% |
| First-attempt success | ~40% | 60% |

---

## Implementation Checklist

For the agent developer/trainer:

- [ ] Add pre-PR check: search for existing PRs
- [ ] Add pre-commit validation: robot validate
- [ ] Add instruction parsing: create checklist from reviewer feedback
- [ ] Add branch awareness: detect when to update vs create
- [ ] Add pattern library: MONDO annotation examples
- [ ] Add reference converter: PMC/DOI to PMID lookup
- [ ] Add failure detection: recognize repeated mistakes

---

## Appendix: Quick Reference Card

```
MONDO Agent Quick Reference
===========================

BEFORE creating a PR:
□ Search for existing PRs on this issue
□ Check if anyone is already working on it
□ Read the full issue including all comments

WHEN making changes:
□ ADD relationships, don't REMOVE (unless explicit)
□ Use PMID format, not PMC or DOI
□ Individual annotations, not grouped
□ Use OMIM/PMID for sources, not GitHub URLs

WHEN receiving feedback:
□ Create checklist from reviewer comments
□ Address EACH point
□ Update SAME PR, don't create new one
□ Ask for clarification if unsure

BEFORE pushing:
□ Run robot validate
□ Check you're on the correct branch
□ Review diff for unintended deletions

IF struggling:
□ Stop after 2 failed PRs on same issue
□ Ask for a concrete example
□ Request human review of approach
```
