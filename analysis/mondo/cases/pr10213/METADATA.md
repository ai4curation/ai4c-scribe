---
repo: monarch-initiative/mondo
issue_number: 9940
pr_number: 10213
issue_title: "EFL1-related Shwachman-Diamond syndrome"
issue_created_at: "2026-02-12"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 5
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Single-term update adding ClinGen preferred label and updating definition with minimal changes.
case_quality: ok
scoring_caveat: "Gold PR #10213 is the complete, sole human resolution (no companion PRs, curator-approved). However the agent config CLAUDE.md ClinGen section documents the synonym xref as empty brackets `EXACT [] {OMO:0002001=.../clingen}` (contradicting the same file's general 'never use empty brackets' rule), while the human used the GCEP affiliation URL `EXACT [https://clinicalgenome.org/affiliation/40157/]`. Agents that followed their instructions are systematically penalized on the synonym line; this drives pr298 (haiku) to a misleading F1=0.0 despite a substantively near-correct synonym. Treat per-line F1 on the synonym as config-vs-gold mismatch noise; judge attempts on substance: only pr554 matched the synonym xref, and no attempt performed the issue-requested definition rewrite or added the human's intersection_of genus-differentia axiom."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9940 requested adding "EFL1-related Shwachman-Diamond syndrome" as the ClinGen preferred label for MONDO:0044205. The request followed the standard ClinGen gene-centric naming template, providing the preferred label, synonyms, parent term, and supporting evidence.

## Changes Made

The PR added the ClinGen preferred label as an exact synonym to MONDO:0044205 and updated the term's definition. The 5 additions and 1 deletion reflect adding synonym lines and modifying the definition text to better align with current understanding of this EFL1-associated variant of Shwachman-Diamond syndrome.

## Resolution

Simple difficulty because it follows a well-established pattern for ClinGen label requests. The curator needs to locate the term stanza, add the synonym with appropriate scope and source annotations, and optionally update the definition. An agent with knowledge of OBO synonym format and ClinGen naming conventions could handle this reliably.

## Curation Note (data quality)

This is **not** a poor case in the Step 3a/3b sense: issue #9940 was resolved by the single PR #10213 (no companion PRs), the gold is genuine curator work approved by sabrinatoro, all attempts used the canonical `MONDO:0044205` (no placeholder artifact), and there is no gold leakage or base-state contamination (best F1 across 7 attempts is only 0.5).

However, a config-vs-gold pattern mismatch makes the per-line metadiff under-represent agent quality on the synonym:

- The mondo-agent-config `template/CLAUDE.md` ClinGen section explicitly documents the preferred-label synonym with **empty brackets**: `synonym: "Hajdu-Cheney syndrome-NOTCH2" EXACT [] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`. This directly contradicts the same file's general rule ("Never use empty brackets").
- The human curator instead used the GCEP affiliation URL: `EXACT [https://clinicalgenome.org/affiliation/40157/]`.
- Agents that followed the ClinGen-specific instruction (pr517, pr483, pr400, pr246, pr429, pr298) all emit `EXACT []` and are penalized for instruction-following. This drives pr298 (haiku, single correct synonym line) to a misleading **F1=0.0**.
- Only pr554 (gpt-5.5/codex) independently chose the affiliation URL and matched the human synonym line (best F1=0.5).

Substance check (judge against the issue's explicit asks, not only the metadiff): the issue requested (1) the ClinGen preferred label and (2) a new EFL1-specific definition. The human additionally (3) added `intersection_of` genus-differentia axioms (defined class under the disease-series-by-gene pattern) and (4) a second `IAO:0000233` term-tracker for #9940 while retaining the existing #4948 line. **No attempt** performed the definition rewrite (an explicit issue request) or added the equivalence axiom. pr429 (sonnet/claude) destructively overwrote the existing #4948 tracker instead of appending #9940 — a provenance regression a curator would reject. Overall the best attempts are partial successes; the metadiff slightly over-represents quality relative to the issue's full ask, except for pr298 where it under-represents.
