# Dragon-AI-Agent GO Ontology PR Analysis

## Overall Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| Merged | 45 | 66.2% |
| Closed (not merged) | 13 | 19.1% |
| Open | 10 | 14.7% |
| **Total** | **68** | 100% |

**Success rate of closed PRs:** 45/58 = **77.6%**

## First-Try Success Rate

Of the merged PRs (from extracted data with category info):

| Category | Count | Percentage |
|----------|-------|------------|
| Merged without modifications | 26 | 65.0% |
| Merged with modifications | 14 | 35.0% |
| **Total merged (in dataset)** | **40** | 100% |

**First-try success rate:** 26/40 = **65.0%**

This means 35% of merged PRs required reviewer feedback and additional commits before merging.

## Failed PRs Checklist

- [ ] **PR #30310** - Merge GO:0017050 D-erythro-sphingosine kinase activity into GO:0008481 sphingosine kinase activity
- [ ] **PR #30312** - Merge GO:0017050 D-erythro-sphingosine kinase activity into GO:0008481 sphingosine kinase activity (duplicate)
- [ ] **PR #30604** - Add taxon constraint for GO:0061708 excluding fungi
- [ ] **PR #30730** - Obsolete 7 nucleotide-sugar catabolic process terms (wrong content)
- [ ] **PR #30731** - Obsolete 7 nucleotide-sugar catabolic process terms (issue #30685) (wrong content)
- [ ] **PR #30799** - Add blank line to README (Permission Test) - intentional test
- [ ] **PR #30827** - Obsolete GO:0007156 and create broader replacement term for homophilic cell adhesion
- [ ] **PR #30828** - Obsolete organic anion/cation transport/transporter terms
- [ ] **PR #30985** - Add enteroendocrine cell differentiation terms
- [ ] **PR #31004** - Add three new transmembrane transporter activity terms for issue #30986
- [ ] **PR #31005** - Create GO:7770027 dimethylarginine transmembrane transporter with CHEBI:133775 (duplicate)
- [ ] **PR #31045** - Add new term: glycoprotein cargo receptor activity (GO:7770028)
- [ ] **PR #31244** - Obsolete four pre-composed proteolysis terms

## Failure Pattern Summary

Failure modes by count (some PRs have multiple issues):

| # | Failure Mode | PRs Affected | Count |
|---|--------------|--------------|-------|
| 1 | Duplicate PRs created | 30312, 31004, 31005 | 4 |
| 2 | Obsoletion convention errors | 30310, 30312, 31244 | 3 |
| 3 | Changes need discussion first | 30827, 30828, 30985 | 3 |
| 4 | Content didn't match objective | 30730 | 1 |
| - | Superseded by human (technically correct) | 30731 | 1 |
| 5 | File format error | 30604 | 1 |
| 6 | Term ID conflict | 31045 | 1 |
| 8 | Permission test (non-training) | 30799 | 1 |

Note: 30312 appears in multiple categories. PR 30731 was technically correct but superseded by human PR.

## Detailed Failure Analysis Files

See individual analysis files (all 13 PRs accounted for):
- [failure-analysis-30310.md](./failure-analysis-30310.md) - Obsoletion errors
- [failure-analysis-30312.md](./failure-analysis-30312.md) - Duplicate PR + obsoletion errors
- [failure-analysis-30604.md](./failure-analysis-30604.md) - File format error
- [failure-analysis-30730.md](./failure-analysis-30730.md) - Content mismatch
- [failure-analysis-30731.md](./failure-analysis-30731.md) - Scope creep
- [failure-analysis-30799.md](./failure-analysis-30799.md) - Permission test (non-training)
- [failure-analysis-30827.md](./failure-analysis-30827.md) - Needed discussion first
- [failure-analysis-30828.md](./failure-analysis-30828.md) - High-impact changes
- [failure-analysis-30985.md](./failure-analysis-30985.md) - Needed discussion first
- [failure-analysis-31004.md](./failure-analysis-31004.md) - Duplicate PR
- [failure-analysis-31005.md](./failure-analysis-31005.md) - Duplicate PR
- [failure-analysis-31045.md](./failure-analysis-31045.md) - Term ID conflict
- [failure-analysis-31244.md](./failure-analysis-31244.md) - Obsoletion rework

## Key Learnings

1. **Always update existing PR branches** rather than creating new PRs when asked to revise
2. **GO obsoletion has strict conventions** that must be followed exactly
3. **Verify PR content matches the stated objective** before submitting
4. **Complex obsoletion tasks require additional steps** (email announcements, annotation review, RHEA updates)
5. **Check file formats carefully** when modifying configuration files like TSV
