# Copilot (app/copilot-swe-agent) EFO Ontology PR Analysis

## Overall Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| Merged | 20 | 39.2% |
| Closed (not merged) | 28 | 54.9% |
| Open | 3 | 5.9% |
| **Total** | **51** | 100% |

**Success rate of closed PRs:** 20/48 = **41.7%**

## First-Try Success Rate

From sample analysis of extracted data, all 20 merged copilot PRs are categorized as `merged_with_mods`.

**First-try success rate:** ~0% (all merged PRs required modifications)

*Note: Full analysis limited by file size (16GB extracted data file).*

## Failed PRs Checklist

### Duplicate PRs (Same Issue, Multiple Attempts)

**Issue #2490 - CHEBI terms for 'response to' EFO terms (13 PRs)**
- [ ] **PR #2491** - Add has_primary_input axioms to EFO 'response to' terms linking to CHEBI
- [ ] **PR #2493** - Add CHEBI terms to 'response to ...' EFO terms using has_primary_input relationships
- [ ] **PR #2494** - Add has_primary_input axioms to response to terms with exact CHEBI matches
- [ ] **PR #2497** - Systematic evaluation and addition of has_primary_input axioms
- [ ] **PR #2501** - Add has_primary_input axioms to 31 'response to' EFO terms
- [ ] **PR #2502** - Add has_primary_input axioms to 35 EFO 'response to' terms
- [ ] **PR #2505** - Add CHEBI has_primary_input axioms to 25 'response to' EFO terms
- [ ] **PR #2507** - Add CHEBI has_primary_input axioms to 'response to' EFO terms
- [ ] **PR #2509** - Add RO:0004009 (has_primary_input) relationships to 'response to' EFO terms
- [ ] **PR #2511** - Add has_primary_input relationships to 44 'response to' EFO terms
- [ ] **PR #2514** - Add RO:0004009 (has_primary_input) relationships to 16 'response to' EFO terms
- [ ] **PR #2558** - Add has_primary_input (RO:0004009) axioms to chemical response terms
- [ ] **PR #2559** - Add RO:0004009 (has_primary_input) axioms linking 'response to' terms to CHEBI

**Issue #2546 - Bronchiectasis endotype terms (4 PRs)**
- [ ] **PR #2547** - [WIP] Add new endotypes of bronchiectasis terms
- [ ] **PR #2548** - Add bronchiectasis endotype terms from PMID:30215383
- [ ] **PR #2553** - [WIP] Add new endotypes of bronchiectasis terms
- [ ] **PR #2554** - Add bronchiectasis inflammatory endotype terms from PMID:30215383

**Issue #2562 - GWAS drug response terms (4 PRs)**
- [ ] **PR #2563** - [WIP] Add missing drug response terms for GWAS catalog
- [ ] **PR #2564** - Add 8 drug response terms for GWAS Catalog with ChEBI linkage
- [ ] **PR #2565** - Add drug response terms for GWAS catalog mapped to ChEBI
- [ ] **PR #2569** - [WIP] Add missing drug response terms for GWAS catalog

**Issue #2445 - Slide-seq update (2 PRs)**
- [ ] **PR #2450** - Add bead-based spatial transcriptomics term and update Slide-seq hierarchy
- [ ] **PR #2452** - [WIP] [Update] Request for update to Slide-seq

### Other Failed PRs

- [ ] **PR #2454** - Import OBA body fat mass and tissue mass terms (closed without explanation)
- [ ] **PR #2495** - [WIP] Using OLS, which term in NCIT is 'COVID-19 Terminology'? (query not implementation)
- [ ] **PR #2532** - Add DLCO change measurement term (closed - similar term exists, needs discussion)
- [ ] **PR #2539** - Add mean diffusivity term (closed without explanation)
- [ ] **PR #2588** - Import 11 OBA protein measurement terms (most recent, closed without explanation)

## Failure Pattern Summary

| # | Failure Mode | PRs Affected | Count |
|---|--------------|--------------|-------|
| 1 | Duplicate PRs for same issue | 2491-2514, 2547-2554, 2558-2569 | 23 |
| 2 | WIP placeholder PRs never completed | 2452, 2495, 2547, 2553, 2563, 2569 | 6 |
| 3 | Closed without clear resolution | 2450, 2454, 2539, 2588 | 4 |
| 4 | Scope/approach issues needing discussion | 2532 | 1 |

**Note:** Many PRs appear in multiple categories (e.g., WIP and duplicate).

## Detailed Failure Analysis Files

See individual analysis files:
- [failure-analysis-2490-series.md](./failure-analysis-2490-series.md) - CHEBI terms duplicate PRs
- [failure-analysis-2546-series.md](./failure-analysis-2546-series.md) - Bronchiectasis duplicate PRs
- [failure-analysis-2562-series.md](./failure-analysis-2562-series.md) - GWAS terms duplicate PRs
- [failure-analysis-2450.md](./failure-analysis-2450.md) - Slide-seq hierarchy
- [failure-analysis-2454.md](./failure-analysis-2454.md) - OBA imports
- [failure-analysis-2532.md](./failure-analysis-2532.md) - DLCO term
- [failure-analysis-2539.md](./failure-analysis-2539.md) - Mean diffusivity
- [failure-analysis-2588.md](./failure-analysis-2588.md) - OBA protein terms

## Key Learnings

1. **CRITICAL: Never create multiple PRs for the same issue** - Agent created 13 PRs for issue #2490 alone
2. **Update existing branches** instead of creating new PRs when asked to revise
3. **Complete WIP PRs** before creating new ones - many [WIP] placeholders were abandoned
4. **Discuss approach first** for complex or contentious changes
5. **Check for existing similar terms** before adding new ones
