---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 15
agent: std_claude_sonnet45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.750
precision: 0.750
recall: 0.750
jaccard: 0.600
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of both CL_0001203 and CL_0001204, and removed "CD44-high, and
CD122-high" from both definitions — the full substantive task. F1 of 0.750
**under-represents** quality: the only divergences from gold are (a) the
addition of PMID:41254224, which the issue explicitly requested but the gold
omitted, and (b) text-form differences. The core immunology repair is exactly
right.

## Strengths

- Both EquivalentClasses axioms repaired correctly and identically for the
  CD8 (CL_0001203) and CD4 (CL_0001204) classes; all other differentiae
  preserved (CL_0000909/CL_0000897, PR_000001380 CD25, PR_000001017 CD45RO,
  PR_000001869 CD127, NCBITaxon_9606, GO_0043379).
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224),
  satisfying the issue's explicit "add these along existing ones" instruction
  more completely than the gold (gold added only 24258910 + 21926977).
- Excellent PR write-up with accurate comparative-immunology rationale (CD44
  high on most human T cells; CD122-high specific to T_SCM/virtual-memory
  subsets) — demonstrates genuine domain understanding rather than mechanical
  pattern-matching.
- Correctly recognized the human in-taxon context and that mouse markers
  over-constrain the human hierarchy.

## Issues

- Style/deviation: added a leading "A" to the CL_0001204 definition
  ("A CD4-positive, alpha-beta long-lived T cell ...") whereas both the gold
  and the issue's proposed definition omit it. Minor and arguably an
  improvement for consistency, but diverges from the verbatim issue text.
- No `term_tracker_item` (IAO_0000233) added — minor process miss vs the
  config guidance, though it keeps the attempt closer to gold.
- No errors or scope creep; the diff is tightly confined to the two target
  classes.
