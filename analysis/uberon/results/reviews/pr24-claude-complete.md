---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 24
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.333
precision: 1.000
recall: 0.200
jaccard: 0.200
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The substantive repair is **fully correct and identical to the F1=1.0 attempts**: the agent removed exactly the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` lines from UBERON:0007181 and UBERON:0007182, leaving the correct `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` definitions intact. F1 of 0.333 (recall 0.200, precision 1.000) **substantially under-represents quality** — it is depressed solely by a `robot convert` reserialization-churn artifact on two unrelated stanzas, with no semantic change. Notably, the agent itself disclosed this in its PR comment ("`robot convert` also normalized definition xref ordering in two unrelated stanzas; no semantic changes were made there"), demonstrating it understood the artifact but chose not to revert it.

## Strengths

- **Correct, minimal core fix** (precision 1.000), matching the maintainer instruction and gold PR substance.
- **Sound rationale:** correctly notes conus arteriosus is a heart/right-ventricle structure and that the affected uterine terms already carry the appropriate `part_of UBERON:0003984` logical definition, so no replacement assertion is needed.
- **Honest, transparent reporting:** explicitly flagged the unrelated xref-ordering normalization as semantically null and ran `git diff --check` plus `obo-grep.pl` verification that UBERON:0003983 no longer links the two uterine terms — good methodology and disclosure.

## Issues

- **ROBOT reserialization-churn artifact (cosmetic, the sole issue):** identical to attempt #197 — the diff carries two extra hunks on UBERON:0013540 (Brodmann 1909 area 9) and UBERON:0034891 (insular cortex) where only the order of definition xrefs changed (ORCID/Wikipedia/MESH list reordering). Zero semantic content; pure `robot convert -f obo` round-trip noise that whole-file metadiff penalizes, cratering recall to 0.200.
- The agent recognized the artifact but did not prune it from the diff (attempts #46/#61/#74 did). This is a diff-hygiene miss, not an ontology error.
- Net assessment: substantively a **success-quality** fix; the F1 is a serialization-artifact false negative. Graded `partial_success` for the diff-hygiene lapse only.
