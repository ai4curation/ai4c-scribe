---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 542
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.800
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The gpt-5.5/codex run correctly obsoleted GO:7770028 with `replaced_by: GO:0038024`. The obsoletion itself is fully correct; F1 = 0.842 is depressed only because the agent **kept the old `term_tracker_item` for #31038 and added a second one for #31948** instead of replacing it in place as gold did — an extra line that lowers precision but is itself a defensible curation choice.

## Strengths

- Correct, complete obsoletion: name `obsolete`-prefixed, definition `OBSOLETE.`-prefixed, `is_a: GO:0038024` removed, `is_obsolete: true` and `replaced_by: GO:0038024` added. The semantic outcome is identical to gold.
- Replacement target GO:0038024 matches the issue's explicit "Replace by" instruction.
- Minimal, surgical diff — no gratuitous reformatting of unrelated lines; `created_by: dragon-ai-agent` preserved (conservative provenance handling).

## Issues

- **Over-editing / scope (precision −):** retained `term_tracker_item ".../issues/31038"` and *appended* a second `term_tracker_item ".../issues/31948"`. Gold replaced the #31038 link with #31948 (single line). Keeping the original creation-issue tracker alongside the obsoletion-issue tracker is arguably *more* informative provenance (it preserves the term's full lifecycle), but it diverges from the gold convention and is the sole driver of the precision drop (0.800) and the ~0.06 F1 gap vs the top tier.
- The `comment:` is minimal — "The reason for obsoletion is that this term was added in error." Valid as a canonical obsoletion reason but omits the substantive rationale (non-orthogonal substrate axis; organize by transport domain; substrate via `has_input`) that the issue states and gold records. Lower information content than gold.
- No PR/issue comment captured in the attempt record, so the methodology (impact assessment, validation) is not auditable from the available artifacts.
