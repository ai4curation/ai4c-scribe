---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 237
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.900
precision: 0.900
recall: 0.900
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The gemma-4-31b/opencode run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024` and, structurally, produced the diff closest to the human gold PR #31994 — it also removed the trailing `created_by: dragon-ai-agent` line exactly as the human did. F1 = 0.900 is essentially representative; the residual gap is the brevity of the obsoletion comment relative to gold's fuller rationale.

## Strengths

- Complete, correct obsoletion pattern: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added.
- Best structural match to gold among all seven attempts: it **replaced** the `term_tracker_item` with the single #31948 line *and* removed the `created_by: dragon-ai-agent` line, mirroring the human's stanza reorganization line-for-line (modulo comment text).
- Strong result for a small (31B) open-weight model, demonstrating that the standard obsoletion skill in the v9 config is followed faithfully even by lighter-weight runtimes.
- Honest about validation limits: explicitly reported that `make travis_build` and `robot reason` failed due to missing `amm`/`robot` in the environment, rather than claiming a passing build, while correctly arguing that a metadata-only obsoletion introduces no logical inconsistency.

## Issues

- The `comment:` field is minimal — "The reason for obsoletion is that this term was added in error." It captures the canonical obsoletion reason but omits the substantive ontological rationale (non-orthogonal substrate axis, organize by transport domain, capture substrate via `has_input`) that the issue spells out and that the gold comment records in full. Defensible as a valid obsoletion comment, but lower information content than gold; this is the practical (not line-count) source of the quality gap.
- No impact-assessment narrative in the PR/issue comments (annotations, mappings, subsets, references) — the work appears correct but is less auditable than the claude-runtime attempts.
