---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 156
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.923
precision: 0.857
recall: 1.0
jaccard: 0.857
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9703
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/9770
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/156
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9703 --repo monarch-initiative/mondo
    gh pr diff 9770 --repo monarch-initiative/mondo
    gh pr diff 156 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #9770 addressed `reclassification` for issue #9703: Updates to Gene-Disease
Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group. Human
resolution summary: The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`,
involving new labels, new terms, updated inheritance annotations, and restructured classification
for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting
underscores in definitions were also included. The 7 commits reflect an iterative curation process
responding to expert review feedback. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.923 (precision=0.857, recall=1.0). It matched 34/35 accepted additions and 8/9 accepted
deletions.

## Strengths

- Matched 42 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `is_a: MONDO:0700382 {source="https://clinicalgenome.org/affiliation/40097/"} ! HMBS-related hepatic porphyria`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI`
- Matched accepted addition: `is_a: MONDO:0100498 {source="https://clinicalgenome.org/affiliation/40097/"} ! UROD-related inherited porphyria`
- Matched accepted addition: `is_a: MONDO:0700383 {source="https://clinicalgenome.org/affiliation/40097/"} ! PPOX-related hepatic porphyria`
- Matched accepted deletion: `intersection_of: MONDO:0015104 ! porphyria cutanea tarda`
- Matched accepted deletion: `intersection_of: has_characteristic MONDO:0021152 ! inherited`
- Matched accepted deletion: `def: "Erythropoietic protoporphyria caused by a compound heterozygous or homozygous mutation in the gene encoding ferrochelatase (FECH) on chromoso...`
- High precision indicates the agent mostly edited within the accepted change surface.
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 1 additions and 1 deletions from the human PR were not reproduced.
- Missing accepted addition: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Missing accepted deletion: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Extra changes beyond the accepted PR: 10 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: PPOX-related hepatic porphyria`
- Extra agent addition: `def: "A hepatic porphyria (or variegate porphyria) caused by monoallelic and biallelic variants in PPOX, presenting as a spectrum of disease (a sem...`
- Extra agent addition: `synonym: "PPOX-related hepatic porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource...`
- Extra agent addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/9280 ! PPOX`
- Extra agent addition: `id: MONDO:0700384`
- Extra agent deletion: `def: "Any inherited porphyria in which the cause of the disease is monoallelic or biallelic variants in the CPOX gene." [https://clinicalgenome.org...`
- Overall this is a successful attempt; any differences above are minor relative to the requested curation.
