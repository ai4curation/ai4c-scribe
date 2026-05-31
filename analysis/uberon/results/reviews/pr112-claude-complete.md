---
ontology: uberon
issue_number: 3471
pr_number: 3472
eval_repo_pr: 112
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.667
precision: 1.000
recall: 0.500
jaccard: 0.500
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: []
scoring_caveat: "Gold PR #3472 only added the def line; it never removed the redundant `part_of UBERON:0002021 ! occipital lobe` axiom that issue #3471 explicitly asked to be removed (still present in upstream master 2026-05). Agents that removed it are MORE complete than gold but are penalized on recall. metadiff F1 under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent fully and correctly resolved both explicit asks in issue #3471: it added the textual definition using the exact wording and all three references supplied in the issue (`ISBN:978-0-323-10027-4`, `ISSN:0072-9752`, `WikipediaVersioned:Visual_cortex&oldid=1268682728`), and it removed the redundant `relationship: part_of UBERON:0002021 ! occipital lobe` axiom that the issue reporter explicitly flagged. The metadiff F1 of 0.667 (recall 0.500) substantially **under-represents** quality: the gold PR #3472 only performed the first half of the issue (single `+def:` line, zero deletions) and never removed the redundant axiom — so the agent is penalized on recall precisely for doing the correct extra work the issue requested. This is the best outcome in the cohort along with the haiku/claude attempt (#95), and the diff is byte-clean with no contamination.

## Strengths

- Definition matches the issue's suggested wording verbatim, including all three xref sources, so it exactly reproduces the gold `def:` line.
- Correctly removed `relationship: part_of UBERON:0002021 {source="MA"} ! occipital lobe`. The redundancy claim is sound: UBERON:0022232 `part_of` UBERON:0000411 (visual cortex), and UBERON:0000411 has `relationship: part_of UBERON:0002021 ! occipital lobe`, so the direct axiom is entailed by `part_of` transitivity. Verified against current upstream uberon-edit.obo.
- Precision 1.000: no spurious edits, no provenance/metadata noise, no serialization churn. The diff is exactly the two issue-relevant changes and nothing else.
- PR comment articulates the redundancy reasoning correctly and concisely.

## Issues

- None substantive. The only deviation from gold (removing the occipital-lobe axiom) is a correct improvement that the issue explicitly requested; the gold PR's failure to do so is a gold defect, not an agent error.
- Note: the agent did not add a `term_tracker_item` provenance property. This is neither required nor present in gold, so it is not counted against the agent.
