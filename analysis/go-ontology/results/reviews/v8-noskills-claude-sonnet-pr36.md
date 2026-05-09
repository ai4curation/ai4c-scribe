---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 36
agent_config_tag: v8-noskills
model: claude-sonnet-4-5-20250929
runtime: claude
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
instruction_following: 1
correctness: 1
completeness: 1
scope_discipline: 5
methodology: 1
overall: 1
outcome: no_changes
failure_modes:
  - permission_blocked
reviewed_by: claude-opus-4-7
reviewed_at: "2026-05-09"
---

## Summary

Claude Sonnet without skills produced zero file changes. Trace analysis from the earlier cmungall/go-ontology-eval-2026 runs (same config) shows the agent understood the issue, located the term, planned the correct changes, but was unable to execute file writes due to the permission system blocking tool calls that weren't pre-approved via skills' `allowed-tools` directives.

## Strengths

- None visible in output — the agent committed no changes.

## Issues

- **Total failure**: No ontology edits despite a clear, simple issue. The agent's trace shows it analyzed the issue correctly and planned the right approach, but could not execute.
- **Root cause**: Without skills installed, Claude Code's CLAUDE.md references `/term-obsoletion` and other skill names that don't resolve. The agent loses the procedural knowledge the skills provide (the checkout/checkin workflow, obsoletion patterns, validation commands) and apparently also loses tool permissions that skills grant via `allowed-tools`.
- **Contrast with Codex**: Codex without skills scored 0.800 on the same case — it doesn't depend on the skill mechanism for tool permissions since it runs with `danger-full-access` sandbox.
- This result demonstrates that skills are load-bearing infrastructure for Claude Code, not optional enhancements.
