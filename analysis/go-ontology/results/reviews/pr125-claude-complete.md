---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 125
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted GO:0043713 with `replaced_by: GO:0140175`, correctly resolving issue #31966 (blob `7fce679`, F1 = 0.889). The single divergence from the gold is the one-sentence obsoletion comment vs. the gold's three-sentence EC/RHEA explanation. This run did the most rigorous validation of the entire cohort; the 0.889 metadiff **under-represents** quality.

## Strengths

- All required obsoletion metadata correct: `obsolete` name prefix, `OBSOLETE.` def prefix retaining `[GOC:jl, PMID:16957230]`, `is_a: GO:0016616` removed, `is_obsolete: true`, `replaced_by: GO:0140175`, `term_tracker_item` for #31966 — per the term-obsoletion skill.
- Best-documented methodology of all 11 attempts: `make -C src/ontology travis_build` passed pre- and post-edit; `linkml-reference-validator cache reference PMID:16957230` succeeded with a validated support excerpt in a created `RESEARCH.md`; `DESIGN_PATTERNS.md` produced; checkout/checkin workflow used.
- Deep biochemical verification: confirmed via local RHEA resources that RHEA:10052 is a narrow/child reaction of RHEA:35643 (GO:0140175's exactMatch), and used the local ChEBI pH 7.3 mapping to support the CHEBI:55534 acid / CHEBI:55535 conjugate-base reasoning — substantiating the issue's rationale rather than merely restating it.
- Honest disclosure that live `runoak -i amigo: associations` failed on a linkml API mismatch, relying on the issue's stated 0 annotations.
- Tightly scoped: only `src/ontology/go-edit.obo` committed; internal-usage search confirmed no other GO terms reference GO:0043713.

## Issues

- Style only: terse one-sentence obsoletion comment vs. the gold's three-sentence form — the sole source of the 0.889 score, consistent with the term-obsoletion skill's short exemplar, and not a substantive defect. No errors, omissions, or scope problems.
