---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 67
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.7
recall: 0.5
jaccard: 0.412
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a re-run of the same gpt-5.5/opencode configuration as eval PR #86 and produces a byte-identical diff (same blob `2edcd44`): a correctly created `RNU12-related minor spliceopathy disorder` term with the ClinGen-qualified synonym, RNU12 gene axiom, both requested children re-parented, and the `IAO:0000233` issue link on the new term. F1=0.583 **under-represents** quality for the same structural reason — the canonical merge-time ID `MONDO:1060223` (agent used placeholder `MONDO:7770747`) makes the `id:` and two `is_a` placement lines unmatchable. Substantively one of the best attempts; only minor curator cleanup needed.

## Strengths

- Correct ClinGen label, faithful definition citing affiliation 40060 and `PMID:39802771`.
- Reproduces the gold ClinGen synonym with the `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` qualifier.
- Both requested children (`MONDO:0011287`, `MONDO:0859360`) re-parented additively to the new term.
- Correct RNU12 gene axiom using verified `http://identifiers.org/hgnc/19380`; `IAO:0000233` issue provenance present.

## Issues

- Diff/claim mismatch: the PR comment states it also classified `MONDO:0033717` (congenital cerebellar ataxia due to RNU12 mutation) under the new term, but no such edit appears in the diff. The narrative over-claims relative to the actual changes.
- Same extra material as #86: `subset: clingen`, `subset: rare`, and an `intersection_of` logical definition not present in gold (over-editing, low risk).
- Parented under both `hereditary disease` and `syndromic disease`; gold kept only `hereditary disease` — defensible per the issue text but divergent from merged curation.
- Omissions vs gold: no `has_material_basis_in_germline_mutation_in HGNC:19380` added to the SCAR33 stanza (gold added it because SCAR33 lacked it); no `IAO:0000233` issue link on the two child stanzas; no `dcterms:creator` provenance.
