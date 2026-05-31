# Training Plan: Copilot-SWE-Agent on Cell Ontology

## Executive Summary

**CRITICAL REVISION:** Initial analysis showed 95.3% merge rate, but deeper analysis reveals only **5.6% first-try success rate**. Nearly every PR requires reviewer corrections before merging.

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Total PRs | 101 | |
| Merge Rate | 95.3% (81/85) | Looks good but misleading |
| **First-Try Rate** | **5.6% (4/71)** | Almost every PR needs fixes |
| Avg Commits per PR | 5-19 for complex terms | Extensive iteration required |

**This is not a success story - it's a warning.** Reviewers are essentially completing the agent's work.

**Caveat:** "Merged with modifications" includes a mix of true errors and quality improvements (e.g., definition concision). The guidance below focuses on recurring, objective corrections.

---

## Part 1: Closed Without Merge (4 PRs)

See `failures/` directory for detailed analysis.

### 1. Ontological Consistency Conflicts (PR #3449)

Agent added `lacks_plasma_membrane_part` axiom conflicting with existing subclass.

**Rule:** Before adding negative markers, query for conflicting subclasses.

### 2. Scope Creep (PR #3415)

Agent modified Makefile when only verifying subset contents.

**Rule:** Only modify files explicitly mentioned in issue.

### 3. Capability Limitations (PR #3349)

Agent created elaborate workarounds for external web access restrictions.

**Rule:** Report limitations immediately, don't create partial solutions.

### 4. Duplicate PR Creation (PR #3201)

Agent created duplicate PRs for same issue.

**Rule:** Search for existing PRs before creating new ones.

---

## Part 2: Merged With Modifications - The Hidden Problem (67 PRs)

See `feedback/PATTERNS.md` and `feedback/feedback-analysis-*.md` for detailed analysis.

### Most Common Feedback Patterns

| Rank | Issue | Frequency | Impact |
|------|-------|-----------|--------|
| 1 | **Database cross reference format** | Very High | Every PMID citation wrong |
| 2 | **ID range errors** | High | Using wrong ID prefix |
| 3 | **Synonym type (EXACT vs RELATED)** | High | Abbreviations marked wrong |
| 4 | **Species suffix missing** | Medium | Mouse terms lack "(Mmus)" |
| 5 | **Reference validation failures** | Medium | Cited content not in paper |
| 6 | **Definition scope issues** | Medium | Disease info in cell type def |

### Detailed Training Rules

#### Rule 1: Database Cross Reference Format

**The #1 cause of corrections.**

```
WRONG:
  - dc:source "PMID:12345"
  - rdfs:seeAlso "PMID:12345"
  - Any other annotation type

CORRECT:
  - oboInOwl:hasDbXref "PMID:12345"
  - This creates a "database cross reference"

This applies to ALL PMID citations in CL.
```

#### Rule 2: ID Range for New Terms

```
For NEW Cell Ontology terms:

CORRECT:
  - CL_9900000 (temporary NTR range)
  - CL_9900001, CL_9900002, etc.

WRONG:
  - CL_4XXXXXX (permanent range - assigned by curators)
  - CL_0XXXXXX (existing terms only)

Always use CL_99XXXXX for new terms. Curators will reassign.
```

#### Rule 3: Synonym Types

```
EXACT synonym: True synonyms with identical meaning
  Example: "B lymphocyte" EXACT for "B cell"

RELATED synonym: Abbreviations, informal names, partial matches
  Example: "OFF-s" RELATED for "alpha retinal ganglion cell OFF-sustained"

When in doubt, use RELATED rather than EXACT.
Abbreviations are ALWAYS RELATED, not EXACT.
```

#### Rule 4: Species-Specific Labels

```
For cell types specific to a species:

CORRECT:
  rdfs:label "alpha retinal ganglion cell OFF-sustained (Mmus)"

WRONG:
  rdfs:label "alpha retinal ganglion cell OFF-sustained"

Add species suffix:
  - Mouse: (Mmus)
  - Human: (Hsap)
  - Only for species-specific terms, not cross-species
```

#### Rule 5: Reference Validation

```
Before citing a PMID:

1. Confirm the PMID exists
2. Verify the specific content you're citing is IN that paper
3. Use PMID format, not author-year: "PMID:12345" not "Smith et al., 2020"
4. If you cannot verify, note uncertainty in PR description

Common error: "I cannot find 'G5' in the provided reference"
```

#### Rule 6: Definition Content Scope

```
Cell type definitions SHOULD include:
  - What the cell IS (identity)
  - Key markers or features
  - Anatomical location
  - Key functions

Cell type definitions should NOT include:
  - Disease associations ("depleted in osteoarthritis...")
  - Clinical progression ("becomes depleted during...")
  - Experimental context ("observed in experiments...")
  - Pathological states

Keep definitions applicable across all contexts.
```

#### Rule 7: Subclass Relationships

```
Before adding a new cell type:

1. Search for existing terms with similar names:
   grep -i "alpha.*ganglion" cl-edit.owl

2. Check if your term should be a SUBCLASS of existing term

3. If there's overlap, establish proper hierarchy

Common error: Creating new term that should be subclass of existing
```

#### Rule 8: Ticket Link Placement

```
GitHub issue links:

CORRECT placement:
  property_value: term_tracker_item "https://github.com/.../issues/123"

WRONG placement:
  - In definition text
  - In synonym annotations
  - In comments (unless specifically appropriate)
```

#### Rule 9: Label vs Abbreviation

```
Primary label: Use full descriptive name
  CORRECT: rdfs:label "alpha retinal ganglion cell OFF-sustained"
  WRONG: rdfs:label "OFF-s"

Abbreviations go in synonyms:
  hasRelatedSynonym "OFF-s"
  hasRelatedSynonym "alpha-RGC OFF-s"
```

---

## Pre-Submission Checklist for CL

**Complete this for EVERY PR before submitting:**

### ID and Format
- [ ] New term ID uses temporary range (CL_9900000, CL_9900001)
- [ ] All PMID references use `hasDbXref` ("database cross reference")
- [ ] Full descriptive name as primary label, not abbreviation

### Annotations
- [ ] Abbreviations marked as RELATED synonym, not EXACT
- [ ] Species-specific terms have suffix: "(Mmus)" for mouse
- [ ] GitHub issue link only in `term_tracker_item` property

### Content
- [ ] Definition focuses on cell type identity, not disease context
- [ ] All cited references verified to contain claimed information
- [ ] Checked for existing overlapping terms in ontology

### Hierarchy
- [ ] Appropriate parent class assigned
- [ ] Checked if term should be subclass of existing term
- [ ] No conflicts with existing subclass markers

### Validation
- [ ] Ran `robot convert --check`
- [ ] Ran `robot reason` to check satisfiability

---

## Pattern Matching Strategy

**The most effective way to improve first-try rate:**

1. Find a recently merged term of the SAME TYPE as what you're adding
2. Copy the EXACT annotation patterns
3. Replace only the content-specific parts

Example: Adding a new retinal ganglion cell type?
1. Find PR for another recently merged retinal ganglion cell term
2. Use identical structure for hasDbXref, synonyms, hierarchy
3. Only change the specific label, definition, markers

---

## Metrics and Targets

### Current State

| Metric | Value |
|--------|-------|
| Merge Rate | 95.3% |
| First-Try Rate | 5.6% |
| Avg Reviews per PR | 3-10 |
| Avg Commits per PR | 5-19 |

### Target State

| Metric | Target |
|--------|--------|
| Merge Rate | Maintain 95%+ |
| First-Try Rate | **50%+** |
| Avg Reviews per PR | <2 |
| Avg Commits per PR | <3 |

### Key Improvements Needed

| Fix | Expected Impact |
|-----|-----------------|
| Correct hasDbXref format | +20% first-try |
| Correct ID range | +10% first-try |
| Correct synonym types | +10% first-try |
| Pre-submission validation | +10% first-try |

---

## Directory Structure

```
analyses/trainer/cl/
├── failures/           # Closed without merge (4 PRs)
│   ├── failure-analysis-3201.md
│   ├── failure-analysis-3349.md
│   ├── failure-analysis-3415.md
│   └── failure-analysis-3449.md
├── feedback/           # Merged with modifications (67 PRs)
│   ├── PATTERNS.md     # Common feedback patterns
│   ├── feedback-analysis-3501.md
│   └── feedback-analysis-3503.md
├── successes/          # Merged first-try (4 PRs)
│   └── (to be analyzed)
├── summary.md
└── training-plan.md
```

---

*Updated: 2025-12-21*
*Based on deep analysis of 101 PRs with focus on the 67 merged-with-modifications cases*
