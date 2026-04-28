# Copilot-SWE-Agent Cell Ontology PR Analysis

## Executive Summary

**WARNING: The 95.3% merge rate is misleading.** Only **5.6% of PRs succeed on first try**. Reviewers are doing most of the work.

## Overall Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| Merged | 81 | 80.2% |
| Closed (not merged) | 4 | 4.0% |
| Open | 16 | 15.8% |
| **Total** | **101** | 100% |

**Merge rate of closed PRs:** 81/85 = **95.3%**

## First-Try Success Rate (The Real Metric)

| Category | Count | Percentage |
|----------|-------|------------|
| Merged without modifications | 4 | **5.6%** |
| Merged with modifications | 67 | **94.4%** |
| **Total merged (in dataset)** | **71** | 100% |

**First-try success rate:** 4/71 = **5.6%**

This means:
- **94.4% of PRs require reviewer corrections**
- Reviewers are essentially completing the agent's work
- The agent is creating drafts, not finished submissions

---

## Feedback Analysis: Why PRs Need Modifications

See `feedback/` directory for detailed case studies.

### Most Common Issues (from merged-with-mods analysis)

| Rank | Issue | Frequency | Examples |
|------|-------|-----------|----------|
| 1 | **hasDbXref format for PMIDs** | Very High | Every PR with citations |
| 2 | **ID range errors** | High | Using CL_4XXXXXX instead of CL_9900000 |
| 3 | **Synonym type (EXACT vs RELATED)** | High | Abbreviations marked EXACT |
| 4 | **Species suffix missing** | Medium | Mouse terms lack "(Mmus)" |
| 5 | **Definition content issues** | Medium | Disease info in cell type def |
| 6 | **Missing subclass relationships** | Medium | Not linking to existing terms |
| 7 | **No learning between PRs** | Medium | Same mistakes repeated |
| 8 | **Import file contamination** | Low | Committing generated files |

### Feedback Analysis Files

- [feedback-analysis-3501.md](./feedback/feedback-analysis-3501.md) - 19 commits, 10 reviews - ALL common issues
- [feedback-analysis-3503.md](./feedback/feedback-analysis-3503.md) - ID range + definition scope
- [feedback-analysis-3510.md](./feedback/feedback-analysis-3510.md) - Repeated same mistakes from 3501
- [feedback-analysis-3393.md](./feedback/feedback-analysis-3393.md) - Definition quality/length
- [feedback-analysis-3489.md](./feedback/feedback-analysis-3489.md) - Disease context in definitions
- [feedback-analysis-3404.md](./feedback/feedback-analysis-3404.md) - Import file issues
- [PATTERNS.md](./feedback/PATTERNS.md) - Comprehensive pattern analysis

---

## Failed PRs (Closed Without Merge)

See `failures/` directory for detailed analysis.

- [ ] **PR #3449** - Ontological consistency conflict (lacks marker vs subclass)
- [ ] **PR #3415** - Scope creep (modified Makefile)
- [ ] **PR #3349** - Capability limitation (web access)
- [ ] **PR #3201** - Duplicate PR creation

---

## Critical Problems Identified

### 1. No Learning Between PRs

PR #3510 received feedback: "I would suggest the same changes as the previous PRs"

The agent made identical mistakes across multiple retinal ganglion cell PRs:
- Missing (Mmus) suffix
- Wrong synonym types
- Missing subclass relationships

**This indicates the agent doesn't carry learning from one PR to the next.**

### 2. Definition Quality Issues

Multiple PRs had definitions that were:
- Too verbose (reviewer used Perplexity to rewrite)
- Including disease context (should be in comments)
- Missing key molecular markers
- Using abbreviations without expansion

### 3. Systematic Format Errors

The hasDbXref format issue appears in nearly every PR. This single fix would dramatically improve first-try rate.

### 4. Hierarchy Ignorance

Agent creates new terms without checking for:
- Existing overlapping terms
- Appropriate parent classes
- Subclass relationships

---

## Comparison: Merge Rate vs First-Try Rate

| Metric | Value | What It Means |
|--------|-------|---------------|
| Merge Rate | 95.3% | PRs eventually get accepted |
| First-Try Rate | 5.6% | Agent rarely gets it right initially |
| **Gap** | **89.7%** | Reviewers fix 9 out of 10 PRs |

**Conclusion:** The high merge rate reflects reviewer patience and effort, not agent quality.

---

## Recommendations

1. **Fix hasDbXref format** - Single biggest impact
2. **Use template matching** - Copy patterns from recent merged terms
3. **Implement learning between PRs** - Track corrections and apply to future submissions
4. **Pre-submission validation** - Check ID ranges, synonym types, species suffixes
5. **Search before adding** - Check for existing overlapping terms

---

## Open PRs (16)

Many open PRs likely have the same issues. Review patterns suggest these will require modifications when reviewed.

---

*Updated: 2025-12-21*
*Based on analysis of 101 PRs with focus on the 67 merged-with-modifications cases*
