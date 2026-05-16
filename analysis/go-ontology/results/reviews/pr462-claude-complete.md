---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 462
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
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

The claude-sonnet-4.5/claude run correctly obsoleted GO:7770028 "glycoprotein cargo receptor activity" with `replaced_by: GO:0038024`, matching every functionally significant element of the human gold PR #31994. F1 = 0.900 slightly under-represents the quality: the only deviation from gold is that the agent retained the trailing `created_by: dragon-ai-agent` line (gold removed it during stanza reordering) — a cosmetic difference with no ontological consequence.

## Strengths

- Applied the complete, correct obsoletion pattern: name prefixed with `obsolete`, definition prefixed with `OBSOLETE.`, `is_a: GO:0038024` axiom removed, `is_obsolete: true` and `replaced_by: GO:0038024` added. This is exactly the gold transformation.
- Correctly **replaced** the `term_tracker_item` from issue #31038 with #31948 in place (single tracker line), matching the gold structure rather than accumulating two tracker lines (the precision-lowering behavior seen in attempts #542, #390, #270).
- The `comment:` field captures the substantive rationale from the issue — substrate-type classification is non-orthogonal because most vesicle cargo are glycoproteins; organize by transport domain with substrate via `has_input`. Semantically equivalent to the gold comment.
- Strong, verifiable methodology: documented impact assessment confirming 0 annotations (via amigo), no internal RHEA/EC/MetaCyc mappings, no subset membership, no taxon constraints, and no other terms referencing GO:7770028 — all of which match the issue reporter's and curator's stated findings.
- Honest reporting: explicitly noted that full `make travis_build` could not run due to missing environment dependencies, rather than falsely claiming a clean build.

## Issues

- Minor style deviation: the agent kept `created_by: dragon-ai-agent` as the final line of the stanza, whereas the gold PR removed it (the human reorganized the stanza so it no longer appears). This is the sole source of the 0.1 F1 gap and has no ontological significance — `created_by` is provenance metadata that is conventionally retained, so the agent's choice is arguably more conservative than gold.
- The comment is paraphrased rather than copied from the issue; it omits the explicit "added in error" phrasing that the gold comment leads with. Defensible — the rationale conveyed is faithful — but slightly less aligned with the canonical obsoletion-comment template.
