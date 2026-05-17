---
ontology: uberon
issue_number: 2911
pr_number: 3508
eval_repo_pr: 74
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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

gpt-5.4 under codex produced a clean, correct fix: the two erroneous `relationship: part_of UBERON:0003983 ! conus arteriosus` lines were removed from UBERON:0007181 and UBERON:0007182 with no collateral changes. F1 of 1.000 accurately represents the outcome. Notably, the agent reports running `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo` for reserialization yet still produced a clean two-hunk diff — meaning either the reserialization was idempotent on this base or the agent correctly pruned incidental hunks, avoiding the serialization-churn artifact that sank attempts #197/#24/#240.

## Strengths

- **Correct minimal repair** matching the maintainer's explicit instruction ("remove the incorrect part-ofs on UBERON:0007181 and UBERON:0007182"); both terms retain their correct `intersection_of: part_of UBERON:0003984 ! uterine tube infundibulum` definitions.
- **Documented, disciplined methodology:** read imported issue context, inspected stanzas with `obo-grep.pl`, used `obo-checkout.pl`/`obo-checkin.pl`, and re-verified with `obo-grep.pl` that the bad assertions were gone and the uterine-tube axioms remained.
- **Clean final diff despite running `robot convert`** — the agent explicitly confirmed "the final diff was limited to the intended ontology fix," demonstrating good awareness of the reserialization-churn risk that other attempts fell into.

## Issues

- None. Correct, complete, and tightly scoped, with the best-documented process among the F1=1.0 attempts.
