---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 52
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.583
recall: 0.583
jaccard: 0.412
outcome: success
failure_modes: [missed_requirement, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Same gpt-5.5/codex agent, identical diff (blob `fc3f66d`) to attempt #29: a substantively correct TSEN2-related NDD term with correct logical definition, asserted gene relationship to `HGNC:28422`, the ClinGen-qualified EXACT synonym, and tracker annotation, plus the `TRACK syndrome` synonym sourced from `PMID:34964109`. The PR write-up here is terse (one line) versus #29's detailed rationale, but the ontology content is identical. F1=0.583 under-represents core correctness; the ceiling is the new_term canonical-ID artifact.

## Strengths

- Correct gene grounding (`HGNC:28422`) and correct logical definition; asserted `relationship` with sources.
- Reproduced gold's ClinGen-qualified EXACT synonym verbatim including the `{OMO:0002001=...}` annotation.
- Added a defensible `TRACK syndrome` synonym from the correct primary paper (`PMID:34964109`) — genuine domain knowledge.
- Term is well-formed OBO and self-contained.

## Issues

- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease); issue requested only `MONDO:0700092`.
- **Scope creep**: same as #29 — `PMID:34964109` added to def xrefs (beyond the issue's 7 PMIDs) and `intersection_of: MONDO:0100500` used as genus instead of gold's `MONDO:0700092`, with a dual `is_a` adding an unrequested parent.
- **Process transparency weaker than #29**: the PR/issue comments are a single sentence with no checklist or rationale, so the (good) reasoning visible in the sibling run is not documented here.
- Creator differs from human ORCID (unavoidable).
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
