---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 46
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

A second gpt-5.5/opencode run, again producing a clean, correct, tightly-scoped fix: the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` lines were removed from UBERON:0007181 and UBERON:0007182 with no collateral edits. F1 of 1.000 accurately represents the outcome. This run is the most explicit of all eight about the reserialization risk — the checklist states it "removed incidental unrelated serialization-only hunks from the final diff," which is exactly why it scored 1.0 where the metadiff-blind attempts (#197/#24/#240) did not.

## Strengths

- **Correct minimal repair** with the right rationale: no replacement assertion needed because each term retains `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum`, matching the text definitions and the `anatomyPartOfAnatomy` compositional pattern (the agent explicitly checked the relevant part-of DOSDP pattern).
- **Best validation discipline of all eight attempts:** ran `robot convert` syntax validation AND `robot reason --reasoner ELK` on the final ontology, and explicitly pruned ROBOT's incidental serialization-only hunks from the diff so the submission stayed clean.
- Inspected UBERON:0007181, UBERON:0007182, UBERON:0003983 and UBERON:0003984 stanzas before editing.

## Issues

- None. Correct, complete, clean, and the best-validated of the eight attempts.
