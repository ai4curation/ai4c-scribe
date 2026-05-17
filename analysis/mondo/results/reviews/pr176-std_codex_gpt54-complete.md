---
ontology: mondo
issue_number: 9987
pr_number: 10094
eval_repo_pr: 176
agent: std_codex_g54
agent_config_tag: v3
model: gpt-5.4
runtime: codex
f1: 0.857
precision: 1.000
recall: 0.750
jaccard: 0.750
case_type: axiom_repair
difficulty: simple
outcome: partial_success
failure_modes:
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

The agent correctly fixed the issue's target line in `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml` ("An acquired metabolic disease that is has its basis..." → "An inherited metabolic disease that has its basis..."), exactly matching gold PR #10094 for that file. It additionally fixed the same "is has" grammar typo in the sibling pattern `inborn_metabolic.yaml` — an edit the issue did not request and the human did not make. F1=0.857 (recall 0.75) understates correctness somewhat: the in-scope edit is perfect and the extra edit is defensible cleanup, but it is genuine scope creep that the issue explicitly bounded.

## Strengths

- The in-scope fix is exactly correct and byte-identical to gold for `inborn_metabolic_disrupts.yaml`: both the semantic ("acquired" → "inherited") and grammar ("is has" → "has") corrections.
- Sound reasoning: correctly identified "acquired" as a copy-paste error inconsistent with an inborn errors of metabolism pattern.
- Good validation: parsed both edited YAML files, ran `git diff --check` for whitespace/patch sanity.
- The extra edit is technically valid and arguably beneficial — the sibling `inborn_metabolic.yaml` genuinely still carries the identical "is has" typo on `main` today (it was never fixed by the human), so this is defensible "fix-the-bug-in-the-neighborhood" cleanup rather than an erroneous change.

## Issues

- **Scope creep**: Issue #9987 explicitly scoped the fix to `inborn_metabolic_disrupts.yaml` and noted only that file. Editing `inborn_metabolic.yaml` was out of scope; the issue did not ask for it and the human PR did not touch it. Defensible, but it lowers precision against the issue's stated boundary and is the sole reason F1 < 1.0.
- A more disciplined approach would have made the requested fix and *flagged* the sibling typo in a comment or follow-up issue rather than bundling an unrequested edit into the same PR.
