# CL Feedback Patterns Analysis

## Overview

Analysis of 67 PRs that were merged with modifications reveals consistent feedback patterns. Understanding these patterns is critical for improving first-try success rate from 5.6% to a target of 50%+.

## Feedback Pattern Categories

### 1. ID Range Errors (Very Common)

**Pattern:** Agent uses incorrect term ID ranges.

**Examples:**
- PR #3503: "Copilot added a ID not in the correct range" / "It should start with 99"

**Rule:**
```
For new Cell Ontology terms:
- Use temporary NTR range: CL_9900000, CL_9900001, etc.
- NOT CL_4XXXXXX range (that's for permanent IDs)
- Check recent term additions to confirm current pattern
```

---

### 2. "Database Cross Reference" Format (Very Common)

**Pattern:** Agent uses wrong annotation type for references.

**Examples:**
- PR #3501: "please change to `database cross reference`" (repeated 4 times)

**Rule:**
```
For PMID citations in CL:
- Use: oboInOwl:hasDbXref with "PMID:XXXXXXX"
- Label it as "database cross reference"
- NOT: dc:source or other annotation types
```

---

### 3. Synonym Type Corrections (Common)

**Pattern:** Agent uses "EXACT" synonym when "RELATED" is appropriate.

**Examples:**
- PR #3501: "Please change to related synonym"
- PR #3510: "add related synonym instead of exact"

**Rule:**
```
Synonym types in CL:
- EXACT: True synonyms (same meaning)
- RELATED: Abbreviations, partial matches, informal names
- NARROW: More specific terms
- BROAD: More general terms

When in doubt, use RELATED rather than EXACT.
```

---

### 4. Species Label Suffix (Common)

**Pattern:** Mouse-specific terms should include "(Mmus)" in label.

**Examples:**
- PR #3501: "Ignore if there is a specific reason for this but I would suggest adding (Mmus) to the label if it is specific to mouse"
- PR #3510: "Adding Mmus to the label"

**Rule:**
```
For species-specific cell types:
- Add species suffix to label: "cell type name (Mmus)" for mouse
- This distinguishes from cross-species terms
- Check if the reference is species-specific before deciding
```

---

### 5. Reference Validation Errors (Common)

**Pattern:** Agent cites reference that doesn't support the claim, or can't be found.

**Examples:**
- PR #3501: "I cannot find 'G5' in the provided reference. I found it here PMID: 26735013"
- PR #3484: "I cannot find this reference 'Stoof and Kebabian, 1981'"

**Rule:**
```
Before citing a reference:
1. Verify the PMID exists and is accessible
2. Confirm the cited content actually appears in the paper
3. Use full PMID format, not author-year citations
4. If you can't verify, note uncertainty in PR description
```

---

### 6. Definition Content Issues (Common)

**Pattern:** Agent includes disease progression or clinical details that don't belong in cell type definition.

**Examples:**
- PR #3503: "I'd probably remove this phrase: An EC is abundant in relatively preserved or early-stage osteoarthritic cartilage..."

**Rule:**
```
Cell type definitions should:
- Focus on what the cell TYPE is (markers, location, function)
- NOT include disease associations or clinical progression
- NOT include experimental context
- Be general enough to apply across contexts
```

---

### 7. Subclass Relationship Errors (Occasional)

**Pattern:** Agent creates new term that overlaps with existing term, or misses obvious parent.

**Examples:**
- PR #3501: "should this be a subclass of the OFF-sustained term?"
- PR #3510: "If alpha-RGC is the same as existing retinal ganglion cell A - add this as a subclass"

**Rule:**
```
Before adding a new cell type:
1. Search for existing terms with similar names/synonyms
2. Check if this should be a subclass of an existing term
3. Verify parent class is the most specific appropriate class
4. Add subclass relationship if term overlaps with existing
```

---

### 8. Ticket Link Cleanup (Occasional)

**Pattern:** Agent leaves GitHub issue tracker links in places they shouldn't be.

**Examples:**
- PR #3503: "Please remove the ticket link"

**Rule:**
```
GitHub issue links (term_tracker_item):
- Include in property_value for provenance
- Do NOT include in definition text
- Do NOT include in synonym annotations
```

---

### 9. Abbreviation vs Full Name (Occasional)

**Pattern:** Agent uses abbreviation as primary label when full name is preferred.

**Examples:**
- PR #3501: "I would suggest re-naming it to 'alpha retinal ganglion cell OFF-s' instead of 'OFF-s'"

**Rule:**
```
For cell type labels:
- Use full descriptive name as primary label
- Put abbreviations as RELATED synonyms
- Include any standard nomenclature abbreviations
```

---

### 10. Logical Axiom Completeness (Suggestion-level)

**Pattern:** Reviewers suggest additional logical axioms could be added.

**Examples:**
- PR #3501: "This is more of a comment but in the future - you can try and add more logical axioms related to projections and so on"

**Note:** This is improvement feedback, not error correction. But indicates room for richer submissions.

---

### 11. No Learning Between PRs (Critical)

**Pattern:** Agent makes identical mistakes across related PRs.

**Examples:**
- PR #3510: "I would suggest the same changes as the previous PRs" (same issues as #3501)

**Rule:**
```
When working on related terms (e.g., multiple retinal ganglion cell types):
1. Review feedback from previous related PRs
2. Apply ALL corrections to new submissions
3. Don't repeat the same mistakes

If reviewer says "same as before" - you've failed to learn.
```

---

### 12. Definition Quality / Verbosity

**Pattern:** Agent creates verbose or unclear definitions that reviewers must rewrite.

**Examples:**
- PR #3393: Reviewer used Perplexity to create "concise version of the definition"

**Rule:**
```
Definitions should be:
- Concise (1-3 sentences for most cell types)
- Focused on distinguishing characteristics
- Free of speculative interpretations
- Written in formal ontology style

If your definition needs AI rewriting, it's too verbose.
```

---

### 13. Import File Contamination

**Pattern:** Agent commits changes to generated/import files.

**Examples:**
- PR #3404: "All this addition needs to be removed. When refreshing the import, don't commit this file."

**Rule:**
```
NEVER commit changes to:
- Import files (generated by make refresh-imports)
- Catalog files
- Build artifacts

ONLY commit changes to:
- src/ontology/cl-edit.owl (main source)
- Other explicitly source files
```

---

## Summary: Top 10 Most Common Corrections

| Rank | Issue | Frequency | Fix |
|------|-------|-----------|-----|
| 1 | Database cross reference format | Very High | Use hasDbXref for PMIDs |
| 2 | ID range | High | Use CL_9900000 temp range |
| 3 | Synonym type | High | Use RELATED not EXACT for abbreviations |
| 4 | Species suffix in label | Medium | Add "(Mmus)" for mouse-specific |
| 5 | Reference validation | Medium | Verify PMID contains cited info |
| 6 | Definition scope (disease context) | Medium | Keep definitions context-neutral |
| 7 | Missing subclass relationships | Medium | Check for existing overlapping terms |
| 8 | No learning between PRs | Medium | Apply previous feedback to new PRs |
| 9 | Definition verbosity | Medium | Keep definitions concise |
| 10 | Import file contamination | Low | Don't commit generated files |

---

## Training Recommendations

### Pre-submission Checklist for CL

```
[ ] ID uses temporary NTR range (CL_9900000, CL_9900001)
[ ] PMID references use hasDbXref ("database cross reference")
[ ] Abbreviations marked as RELATED, not EXACT synonyms
[ ] Species-specific terms have (Mmus) suffix if mouse
[ ] Definition focuses on cell type, not disease/clinical context
[ ] All cited references verified to contain claimed information
[ ] Checked for existing overlapping terms
[ ] GitHub issue links only in term_tracker_item, not elsewhere
[ ] Full descriptive name as label, abbreviations as synonyms
```

### Pattern Matching Template

Before submitting, compare your entry to a recently merged term of the same type. Copy the exact annotation patterns.
