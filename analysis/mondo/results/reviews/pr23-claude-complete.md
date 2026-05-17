---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 23
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.48
precision: 0.5
recall: 0.462
jaccard: 0.316
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, scope_creep]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Same claude-haiku-4.5/claude agent, identical diff (blob `3ad01f1`) to attempt #199: correct gene logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`) and asserted relationship, but a weak synonym set (mechanical "with/without TMA" split, mis-cited TRACK synonym) and single-PMID provenance on all axioms. Core gene/axiom modeling is correct; metadata quality is the weakest tier on this case. F1=0.480 reflects both the canonical-ID artifact and genuine defects.

## Strengths

- Correct gene grounding (`HGNC:28422`), correct logical definition and asserted `relationship`, correct primary parent `MONDO:0700092`, tracker → issue #9956.
- Definition cites exactly the 7 issue PMIDs + ClinGen URL (no out-of-scope literature).

## Issues

- **Questionable synonyms**: same as #199 — `"...with thrombotic microangiopathy"` / `"...without thrombotic microangiopathy"` EXACT synonyms produced by splitting the label; gold's ClinGen-qualified synonym omitted. `"TRACK syndrome" EXACT [PMID:38622473]` mis-cites (TRACK syndrome is `PMID:34964109`).
- **Provenance under-sourcing**: all axioms sourced only to `PMID:38622473` rather than the ClinGen affiliation gold used.
- **Omission (defensible)**: missing gold curator's `is_a: MONDO:0002254` (syndromic disease).
- **No PR/issue narrative captured** in this attempt file (unlike sibling #199), so methodology cannot be independently assessed here; the diff is identical so the underlying work is the same.
- Creator points at the Claude Code aidocs URL — non-standard creator value.
- **Case quality note**: F1 ceiling is partly a new_term scoring artifact; the synonym/provenance defects are real — see METADATA Curation Note.
