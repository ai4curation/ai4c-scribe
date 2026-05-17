---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 233
agent: std_claude_op47
model: claude-opus-4-7
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

The strongest attempt in the set on substance and self-awareness. It produced a byte-identical diff to the other three claude runs (blob `c8688e4`): on all 15 affected stomatogastric terms (UBERON:8910001, UBERON:8910010–UBERON:8910023) it replaced the contradictory `in_taxon NCBITaxon:6712 ! Astacidea` + `in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `in_taxon NCBITaxon:6692 ! Pleocyemata` — byte-identical to gold's substantive lines. The PR comment is excellent: a correct, detailed RO:0002162 semantics explanation, a complete affected-terms table, an explicit note that UBERON:8910000 was deliberately left alone (its single Arthropoda constraint is correct), and a candid disclosure that `robot convert` was unavailable so reserialization was skipped and may be needed before merge. Metadiff F1=0.073 grossly under-represents quality (recall=1.000; precision crushed by gold's ODK-import/reserialization noise).

## Strengths

- The 15 `in_taxon` replacement lines are exactly identical to gold's substantive curation decision, including the `! Pleocyemata` label — the single most ontologically meaningful change in the gold PR.
- Best methodological transparency of all 8 attempts: explicitly verified Pleocyemata is the closest common parent of Astacidea/Brachyura; verified post-edit that 0 occurrences of NCBITaxon:6712/6752 and 15 of NCBITaxon:6692 remain; correctly reasoned that UBERON:8910000 (parent, already Arthropoda-scoped) must NOT be changed — a subtle correct judgment some agents could have gotten wrong.
- Honest, accurate self-assessment that reserialization was not run and an import refresh may be needed before merge — exactly the right caveat, demonstrating it understood the remaining gap.
- Perfectly scoped; recall=1.000 confirms zero spurious lines relative to gold.

## Issues

- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `ncbitaxon_terms.txt` nor refresh `merged_import.owl`. Pleocyemata is now referenced and must be imported (gold imported it plus ancestors). The agent's own PR comment flags the reserialization gap but not the import-membership gap specifically; this is the one real defect.
- **Style vs human:** no `uberon-edit.obo` reserialization (environment lacked `robot`), so gold's xref-normalization/tag-reordering build artifacts are absent. Build artifacts, not curation — cleaner in isolation but the SOP expects a reserialization pass.
- **Metadiff caveat:** F1=0.073 is almost entirely an artifact of the gold PR's ODK-regenerated `merged_import.owl` (42 lines) and whole-file reserialization noise. On the substance the issue asked for, this attempt is essentially perfect and the best of the eight. Strongly under-represented. See METADATA.md case-quality flag.
