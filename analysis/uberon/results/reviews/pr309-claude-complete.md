---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 309
agent: claude_claude-sonnet-4.5
model: claude-sonnet-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.073
precision: 0.038
recall: 1.000
jaccard: 0.038
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_reserialization_and_odk_import_domination
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is the cleanest, most surgical expression of the substantive fix the issue demanded. On all 15 affected stomatogastric terms (UBERON:8910001, UBERON:8910010–UBERON:8910023) it replaced the contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship: in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon NCBITaxon:6692 ! Pleocyemata` — **byte-identical to the gold PR's substantive lines, including the `! Pleocyemata` label**. It made no other changes (no reserialization, no import refresh). The metadiff F1 of 0.073 grossly under-represents quality: every line the agent changed appears in gold (recall=1.000), but gold's diff is dominated by ~26 reserialization/ODK-import lines the agent (correctly, minimally) did not touch, crushing precision to 0.038.

## Strengths

- The 15 `in_taxon` replacement lines are exactly identical to gold's substantive curation decision, including the human-readable `! Pleocyemata` comment — the single most ontologically meaningful change in the entire gold PR.
- Perfectly scoped: no collateral edits to definitions, synonyms, hierarchy, or unrelated stanzas. Recall=1.000 confirms zero spurious lines relative to gold.
- Correct ontological reasoning in the PR comment: accurately explains `in_taxon` (RO:0002162) semantics and why two sibling-taxon assertions are contradictory; correctly identifies Pleocyemata as the common parent.

## Issues

- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `src/ontology/imports/ncbitaxon_terms.txt` nor refresh `src/ontology/imports/merged_import.owl`. Pleocyemata is now referenced and must be imported (gold imported it plus ancestors Eucarida/Decapoda/Eumalacostraca). Without this the import/build is incomplete. This is the one real defect.
- **Style vs human:** did not reserialize `uberon-edit.obo` with `robot convert`, so the xref-formatting normalization and tag reordering that gold's reserialization produced are absent. These are build artifacts, not curation; not reproducing them is arguably cleaner, but the project SOP does expect a reserialization pass.
- **Metadiff caveat:** F1=0.073 is almost entirely an artifact of the gold PR's ODK-regenerated `merged_import.owl` (42 lines) and whole-file reserialization noise. On the substance the issue actually asked for, this attempt is essentially perfect. Strongly under-represented. See METADATA.md case-quality flag.
