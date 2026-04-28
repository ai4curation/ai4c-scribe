# Uberon PRs by dragon-ai-agent - Summary

## Overview

- **Repository**: obophenotype/uberon
- **Agent**: dragon-ai-agent
- **Analysis Date**: 2025-12-20
- **Total PRs**: 14
- **Merged**: 14 (100%)
- **Not Merged**: 0

## Success Rate

| Metric | Count | Percentage |
|--------|-------|------------|
| Total PRs | 14 | 100% |
| Merged without modifications | 6 | 42.9% |
| Merged with modifications | 8 | 57.1% |
| Not merged | 0 | 0% |

**Effective Success Rate**: While all PRs eventually merged, only 42.9% were accepted on first submission without requiring changes.

## PRs Requiring Modifications (Checklist)

These PRs required changes after initial submission:

- [ ] **PR #3573** - Fix esophagus and esophageal artery partonomy
  - Status: `merged_with_mods`
  - Issue: Required `#gogoeditdiff` bot runs to verify changes

- [ ] **PR #3603** - Add occlusal surface of tooth (UBERON:8600149)
  - Status: `merged_with_mods`
  - Issue: Modifications made after initial submission

- [ ] **PR #3609** - Add new term: ileocecal fold (UBERON:9900001)
  - Status: `merged_with_mods`
  - Issue: Used temporary ID that required replacement; review was DISMISSED then re-approved
  - Required commits: 2 post-review

- [ ] **PR #3619** - Fix tracheal mucosa logical definition
  - Status: `merged_with_mods`
  - Issue: Triggered "Large scale logical changes" bot warning; required CHANGES_REQUESTED approval override
  - Required commits: 1 post-review; 5 total reviews

- [ ] **PR #3620** - Add sixth lumbar dorsal root ganglion (UBERON:9900001)
  - Status: `merged_with_mods`
  - Issue: Wrong contributor name (Sarah vs Stan Laulederkind)

- [ ] **PR #3630** - Add term: carotid artery intima-media region
  - Status: `merged_with_mods`
  - Issue: Modifications needed after initial submission

- [ ] **PR #3633** - Update occlusal surface of tooth term
  - Status: `merged_with_mods`
  - Issue: Follow-up to PR #3603

- [ ] **PR #3638** - Add uterine fundus (UBERON:9900001)
  - Status: `merged_with_mods`
  - Issue: Agent incorrectly questioned valid PMIDs as "out of range"

## PRs Merged Without Issues

- **PR #3560** - Fix dorsolateral prefrontal cortex hierarchy
- **PR #3607** - Add kidney interpolar region term
- **PR #3608** - Add bivalve adductor muscle
- **PR #3616** - Fix typos in UBERON:0009548/0009549
- **PR #3626** - Remove DHBA:12869 xref from vestibular nerve
- **PR #3628** - Remove incorrect DHBA xrefs from 5 terms

## Key Failure Modes Identified

1. **PMID Validation Error** (PR #3638): Agent incorrectly rejected valid PMIDs claiming they were "beyond current range"
2. **Contributor Attribution Error** (PR #3620): Used wrong person's name/ORCID
3. **Temporary ID Usage** (PR #3609): Used placeholder IDs requiring manual replacement
4. **Logical Definition Impact Awareness** (PR #3619): Changes triggered large-scale inference changes

## Recommendations

See `training-plan.md` for detailed training instructions to address these failure modes.
