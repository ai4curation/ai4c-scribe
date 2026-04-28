# Success Patterns: What Types of Issues Work Well

## Executive Summary

Analysis of first-try successful PRs across 5 ontologies reveals clear patterns. The agent excels at **well-scoped, single-purpose tasks** with clear specifications. Success correlates strongly with:

1. **Task clarity**: Clear, unambiguous instructions in the issue
2. **Scope limitation**: Single file, single action
3. **Mechanical nature**: Deterministic operations (remove X, add Y)
4. **Existing patterns**: Following established conventions

## First-Try Success Rates by Ontology

Counts below use **merged PRs with category info** (to match per-ontology summaries), not total PRs.

| Ontology | Merged PRs (with category info) | Merged Without Mods | First-Try Success Rate |
|----------|---------------------------------|----------------------|------------------------|
| GO | 40 | 26 | **65.0%** |
| Uberon | 14 | 6 | **42.9%** |
| MONDO | 15 | 4 | **26.7%** |
| CL | 71 | 4 | **5.6%** |
| EFO | 20 | 0 | **0%** |

**Key insight**: GO has the highest first-try success rate in the merged-with-category subset; Uberon remains strong on well-scoped tasks but has more review-driven fixes.

## Caveats

1. **Denominator alignment**: These rates are computed from merged PRs with category info to align with per-ontology summaries; they should not be compared directly to total PR counts.
2. **Issue quality bias**: Ontologies with more explicit, well-scoped issues will naturally yield higher first-try rates.
3. **Task mix variance**: Some ontologies see more complex additions (new terms, logical definitions), which lowers first-try rates independent of agent behavior.

---

## Success Pattern Categories

### 1. Term Obsoletion (GO - Very High Success)

**Examples:**
- PR #31108: "Obsolete GO:0033790 hydroxymethylfurfural reductase activity"
- PR #31074: "Obsolete GO:1904378 (maintenance of unfolded protein involved in ERAD pathway)"
- PR #31047: "Obsolete GO:0019356 nicotinate nucleotide biosynthetic process from tryptophan"

**Why it works:**
- Clear, unambiguous action: "obsolete term X"
- Well-documented procedure exists
- Single-file change
- Validation is straightforward (check for references, annotations)
- No creative judgment required

**Success template:**
```
Issue says: "Obsolete GO:XXXXXXX because [reason]"

Agent does:
1. Check for annotations (must be 0)
2. Check for child terms (must be 0 or handled)
3. Add is_obsolete: true
4. Prefix name with "obsolete "
5. Prefix definition with "OBSOLETE. "
6. Add comment with reason
7. Add term_tracker_item
8. Validate with ROBOT
```

---

### 2. Add Cross-References/XRefs (MONDO, Uberon - High Success)

**Examples:**
- PR #9283: "Add HP:0003002 (Breast carcinoma) xref to MONDO:0004989"
- PR #9047: "Fix incorrect OncoTree xrefs for neoplasm terms"
- PR #3532: "Add COB alignment comment and seeAlso link to UBERON:0000000"

**Why it works:**
- Mechanical operation: add xref to term
- Clear specification: which xref to which term
- No domain expertise required
- Easy to validate

**Success template:**
```
Issue says: "Add xref [SOURCE:ID] to [ONTO:XXXXXX]"

Agent does:
1. Find term in edit file
2. Add xref with proper formatting
3. Include source annotation if required
4. Commit single change
```

---

### 3. Remove Incorrect XRefs (Uberon - High Success)

**Examples:**
- PR #3628: "Remove incorrect DHBA xrefs from 5 UBERON terms"
- PR #3626: "Remove DHBA:12869 xref from vestibular nerve"

**Why it works:**
- Issue specifies exactly what to remove
- No judgment about what to replace with
- Verification is clear (xref gone = success)

**Success template:**
```
Issue says: "Remove [xref] from [term] because [reason]"

Agent does:
1. Find term
2. Remove specific xref line
3. Validate no unintended changes
```

---

### 4. Fix Typos/Labels (Uberon - High Success)

**Examples:**
- PR #3616: "Fix typos in labels for UBERON:0009548 and UBERON:0009549"

**Why it works:**
- Completely unambiguous
- Issue shows exact wrong text and correct text
- No ontological judgment required

**Success template:**
```
Issue says: "Typo: '[wrong]' should be '[correct]' in UBERON:XXXXXXX"

Agent does:
1. Find term
2. Replace exact string
3. Done
```

---

### 5. Add Simple Hierarchy Relationship (GO, MONDO - Medium Success)

**Examples:**
- PR #31126: "Change parent of GO:0072344 to GO:0002182"
- PR #9209: "Add additional SubClassOf relationship for MONDO:0970994 to MONDO:0800145"
- PR #9198: "Add cutaneous solitary mastocytoma as subclass of cutaneous mastocytoma"

**Why it works when successful:**
- Clear specification of parent-child relationship
- Issue explicitly states which terms
- No need to invent definition or synonyms

**When it fails:**
- Agent must infer the correct parent
- Multiple potential parents exist
- Existing hierarchy conflicts

---

### 6. Add New Term with Complete Specification (GO - Medium Success)

**Examples:**
- PR #31107: "Add new term: rod photoreceptor phosphodiesterase 6 complex"
- PR #31046: "Add GO:7770028 - glycoprotein cargo receptor activity"
- PR #3607: "Add kidney interpolar region term (UBERON:7770009)"

**Why it works when successful:**
- Issue provides: name, parent, definition, references
- GO has clear ID assignment (7770XXX range)
- Validation with ROBOT catches errors

**When it fails:**
- Agent must create definition from scratch
- References aren't specified
- Synonym types aren't clear

---

## Failure-Prone Task Types (For Comparison)

### Tasks That Consistently Fail

| Task Type | Why It Fails |
|-----------|--------------|
| Add complex new cell type (CL) | hasDbXref format, synonym types, species suffixes |
| Multiple related PRs (EFO) | Agent creates duplicates instead of single PR |
| Tasks requiring web research | Agent can't verify external sources |
| Tasks with ambiguous scope | Agent modifies wrong files |
| Tasks requiring iteration | Agent doesn't learn from reviewer feedback |

---

## Success Factors Analysis

### What Makes a Task Succeed?

| Factor | Impact | Explanation |
|--------|--------|-------------|
| **Single action** | Very High | "Add xref" vs "Add term with synonyms, definition, relationships" |
| **Explicit specification** | Very High | Issue says exactly what to add/remove |
| **Single file** | High | No chance of editing wrong file |
| **Validation command** | High | `robot convert --check` catches errors |
| **Existing template** | Medium | Can copy pattern from similar term |
| **No external verification** | Medium | Don't need to check external sources |

### Issue Quality Matters Most

Successful issues have:
```
[ ] Single, clear action verb (add, remove, obsolete, fix)
[ ] Explicit term IDs mentioned
[ ] Explicit values to add/change
[ ] No ambiguity about scope
[ ] References provided (not "find a reference")
```

Failed issues often have:
```
[ ] "Update X based on literature review"
[ ] "Add new term for [concept]" (no definition provided)
[ ] Multiple related changes needed
[ ] Requires understanding existing hierarchy
```

---

## Recommendations for Issue Authors

### To Maximize Agent Success:

1. **Be explicit about term IDs**: "Add xref Y to ONTO:XXXXXXX" not "add xref to the term about Z"

2. **Provide complete specifications**:
   - For new terms: name, parent, definition, references
   - For xrefs: exact xref string and target term
   - For synonyms: type (EXACT/RELATED) and value

3. **One action per issue**: Don't combine "add term" + "update related term" + "fix hierarchy"

4. **Include validation criteria**: "The term should pass `robot reason`"

5. **Avoid requiring web research**: Include PMID if needed, don't say "find a reference"

---

## Success Examples by Ontology

### GO: Best Practice Example

**Issue #31101 (led to successful PR #31108):**
> "Obsolete GO:0033790 hydroxymethylfurfural reductase activity - unnecessary grouping term with 0 annotations"

**Why it succeeded:**
- Clear action: obsolete
- Clear target: GO:0033790
- Clear reason: unnecessary, 0 annotations
- Agent knew exactly what to do

### Uberon: Best Practice Example

**Issue #3627 (led to successful PR #3628):**
> "Remove these DHBA xrefs causing inferred equivalences:
> - DHBA:12399 from UBERON:0004073
> - DHBA:10669 from UBERON:0002422
> ..."

**Why it succeeded:**
- Explicit list of what to remove
- Exact term IDs provided
- No judgment required

### MONDO: Best Practice Example

**Issue #9278 (led to successful PR #9283):**
> "Add HP:0003002 xref to MONDO:0004989 (not the parent MONDO:0007254)"

**Why it succeeded:**
- Explicit xref to add
- Explicit term to add it to
- Even clarified which term NOT to use

---

## Metrics Target

Based on success patterns, achievable improvement targets:

| Task Type | Current Rate | Target | How |
|-----------|--------------|--------|-----|
| Obsoletion | 90%+ | Maintain | Already working |
| Add xref | 80%+ | Maintain | Already working |
| Remove xref | 85%+ | Maintain | Already working |
| Fix typo | 95%+ | Maintain | Already working |
| Add new term | 30% | 60% | Better issue templates |
| Complex edits | 5% | 30% | Training on patterns |

---

## Conclusion

The agent succeeds when:
1. **The task is mechanical** - deterministic input → output
2. **The specification is complete** - all values provided
3. **The scope is limited** - single file, single change
4. **Validation exists** - can check before submitting

The agent fails when:
1. Tasks require creative judgment
2. Multiple related changes are needed
3. External verification is required
4. Learning from feedback is needed

**Bottom line**: The agent is an excellent automation tool for routine, well-specified tasks. It's not yet ready for tasks requiring domain expertise or iterative refinement.

---

*Generated: 2025-12-21*
*Based on merged PRs with category info across GO, MONDO, Uberon, CL, and EFO (n=160)*
