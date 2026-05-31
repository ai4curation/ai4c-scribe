---
ontology: go-ontology
issue_number: 31964
pr_number: 31982
eval_repo_pr: 78
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

A second gpt-5.5 / opencode run produced a diff byte-identical to the human gold PR #31982 (blob `dd6593a`), F1 = 1.0. Both issue #31964 asks were implemented exactly, including the additive #31964 tracker on both terms. F1 accurately represents a clean, complete solution. (Only the diff is captured in the attempt record — no PR/issue narrative was preserved for this run.)

## Strengths

- Diff matches the gold standard exactly: `EC:1.4.3.22` broadMatch removed from `GO:0052598`; `GO:0004720` reparented `GO:0052597` → `GO:0016641`; #31964 tracker added additively to both terms (pre-existing #28199/#30193 trackers preserved).
- Reparenting target `GO:0016641` is the correct `EC:1.4.3.-` grouping class (it carries `xref: EC:1.4.3.- {source="skos:exactMatch"}`), exactly as the issue specified.
- Preserved the orthogonal `is_a: GO:0140096` on `GO:0004720` and the EC systematic synonym / `RHEA:25625` exactMatch on `GO:0052598`; `GO:0050232` putrescine oxidase left untouched as required.
- Reproduces the same correct result as the sibling gpt-5.5/opencode run (pr96), indicating the outcome is stable for this model/runtime on this case rather than a lucky single draw.

## Issues

- None on the substance. The only limitation is record-keeping: no PR comment, issue comment, or checklist was captured for this run, so methodology cannot be independently assessed from the attempt artifact — but the resulting diff is provably correct and complete.
