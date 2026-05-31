---
ontology: mondo
issue_number: 9493
pr_number: 9726
eval_repo_pr: 764
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
runtime_label: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: simple
f1: 0.4
precision: 0.5
recall: 0.333
jaccard: 0.25
outcome: failure
failure_modes:
  - wrong_pattern
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
case_quality: poor
case_quality_reason: gold_has_reviewer_added_pmid_xref
---

## Summary

The agent added `is_a: MONDO:0005550 {source=".../issues/9493", source="https://orcid.org/0000-0003-2955-4640"} ! infectious disease` plus the `IAO:0000233` issue-9493 tracker line (blob `a4db3da`). This implements **Option 1** — the literal user request — but curator @matentzn explicitly directed **Option 3** (`is_a: MONDO:0024352` viral respiratory tract infection) in the issue comments, declining the broader placement. This is the same wrong-option error the established METADATA Note classifies as a genuine failure (cf. gemma runs #292/#204), so despite F1=0.400 this is substantively a **failure**, not a metadiff artifact.

## Strengths

- Correct, minimal mechanics: a single well-formed `is_a` axiom with `source` provenance plus the `IAO:0000233 ".../issues/9493"` tracker line; existing parents (`MONDO:0001040`, `MONDO:0004867`) preserved; tightly scoped to one file.
- Used the requested ORCID `https://orcid.org/0000-0003-2955-4640` as a source.
- Correctly declined to add the proposed logical definition, consistent with @matentzn's instruction.
- Good methodology reporting: verified stanzas, ran `robot convert` for OBO syntax validation, and honestly disclosed the Docker/`make NORM` limitation.

## Issues

- **Wrong parent (the substantive error).** The agent chose `MONDO:0005550` (infectious disease, Option 1) — the issue *body's* request — but the issue comments contain an explicit curator directive to implement Option 3 (`MONDO:0024352`, viral respiratory tract infection, the most specific placement). Option 1 was the option @matentzn declined. `MONDO:0005550` is not ontologically false (common cold is an infectious disease, reachable via `MONDO:0024352 → MONDO:0005108 → MONDO:0005550`), but it ignores the available, explicit curator instruction and is redundant given the more specific intended parent. This is `wrong_pattern` + `missed_requirement` (failed to follow the Option-3 curator instruction present in the issue thread).
- Metadiff F1=0.400 slightly *over*-represents quality: the only gold-matched line is the cheap tracker annotation; the substantive `is_a` line targets the wrong parent entirely (not merely the reviewer-added `PMID:37426629` artifact that caps the correct Option-3 attempts at 0.5).
