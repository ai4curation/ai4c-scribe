---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 178
agent: claude_claude-haiku-4.5
model: claude-haiku-4-5
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

Byte-identical core fix to the other three claude runs (blob `c8688e4`): on all 15 affected stomatogastric terms (UBERON:8910001, UBERON:8910010–UBERON:8910023) it replaced the contradictory `in_taxon NCBITaxon:6712 ! Astacidea` + `in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `in_taxon NCBITaxon:6692 ! Pleocyemata` — byte-identical to gold's substantive lines including the `! Pleocyemata` label. No reserialization or import refresh. Strong substantive result on a hard case from the smallest model; metadiff F1=0.073 grossly under-represents quality (recall=1.000; precision crushed by gold's ODK-import/reserialization noise). The PR/issue comment bodies were truncated to headers in the captured attempt, so methodology documentation is thinner than the opus run, but the diff itself is correct and minimal.

## Strengths

- The 15 `in_taxon` replacement lines are exactly identical to gold's substantive curation decision, including the `! Pleocyemata` label — the single most ontologically meaningful change in the gold PR. Notable that claude-haiku-4.5 reached the same correct answer as the larger models.
- Perfectly scoped: no collateral edits; recall=1.000 confirms zero spurious lines relative to gold.
- Correctly limited the change to the 15 child terms and left UBERON:8910000 (parent, already Arthropoda-scoped) untouched, matching gold.

## Issues

- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `ncbitaxon_terms.txt` nor refresh `merged_import.owl`. Pleocyemata is now referenced and must be imported (gold imported it plus ancestors). Import/build incomplete without it — the one real defect.
- **Style vs human:** no `uberon-edit.obo` reserialization, so gold's xref-normalization/tag-reordering build artifacts are absent. Build artifacts, not curation.
- **Documentation thin:** captured PR/issue comments are header-only (no rationale body), unlike the opus run; cannot confirm depth of taxon-constraint reasoning from the artifact, though the diff is correct.
- **Metadiff caveat:** F1=0.073 is almost entirely an artifact of the gold PR's ODK-regenerated `merged_import.owl` (42 lines) and whole-file reserialization noise. On substance, essentially perfect. Strongly under-represented. See METADATA.md case-quality flag.
