---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 409
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.441
precision: 0.531
recall: 0.377
jaccard: 0.283
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9703
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/9770
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/409
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9703 --repo monarch-initiative/mondo
    gh pr diff 9770 --repo monarch-initiative/mondo
    gh pr diff 409 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #9770 addressed `reclassification` for issue #9703: Updates to Gene-Disease
Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group. Human
resolution summary: The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`,
involving new labels, new terms, updated inheritance annotations, and restructured classification
for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting
underscores in definitions were also included. The 7 commits reflect an iterative curation process
responding to expert review feedback. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.441 (precision=0.531, recall=0.377). It matched 21/35 accepted additions and 6/9 accepted
deletions.

## Strengths

- Matched 27 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI`
- Matched accepted addition: `synonym: "FECH-related erythropoietic protoporphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/informat...`
- Matched accepted addition: `synonym: "UROS-related erythropoietic porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-r...`
- Matched accepted addition: `synonym: "ALAS2-related erythropoietic protoporphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/informa...`
- Matched accepted deletion: `def: "Erythropoietic protoporphyria caused by a compound heterozygous or homozygous mutation in the gene encoding ferrochelatase (FECH) on chromoso...`
- Matched accepted deletion: `def: "Congenital erythropoietic porphyria, or G\xfcnther disease, is a form of erythropoietic porphyria characterized by very severe and mutilating...`
- Matched accepted deletion: `def: "X-linked form of erythropoietic protoporphyria." [MONDO:patterns/x_linked]`

## Issues

- Missing accepted changes: 14 additions and 3 deletions from the human PR were not reproduced.
- Missing accepted addition: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Missing accepted addition: `is_a: MONDO:0700382 {source="https://clinicalgenome.org/affiliation/40097/"} ! HMBS-related hepatic porphyria`
- Missing accepted addition: `is_a: MONDO:0100498 {source="https://clinicalgenome.org/affiliation/40097/"} ! UROD-related inherited porphyria`
- Missing accepted addition: `is_a: MONDO:0700383 {source="https://clinicalgenome.org/affiliation/40097/"} ! PPOX-related hepatic porphyria`
- Missing accepted addition: `def: "An erythropoietic protoporphyria caused by biallelic variants in FECH (an autosomal recessive inheritance pattern) and causing primarily accu...`
- Missing accepted deletion: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Missing accepted deletion: `intersection_of: MONDO:0015104 ! porphyria cutanea tarda`
- Missing accepted deletion: `intersection_of: has_characteristic MONDO:0021152 ! inherited`
- Extra changes beyond the accepted PR: 51 additions and 10 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40097/", source="https://github.com/monarch-initiative/mondo/issues/9703"} ! HM...`
- Extra agent addition: `is_a: MONDO:7770005 {source="https://clinicalgenome.org/affiliation/40097/", source="https://github.com/monarch-initiative/mondo/issues/9703"} ! PP...`
- Extra agent addition: `name: FECH-related erythropoietic protoporphyria`
- Extra agent addition: `def: "An erythropoietic protoporphyria caused by biallelic variants in FECH (an autosomal recessive inheritance pattern) and causing primarily accu...`
- Extra agent addition: `name: UROS-related erythropoietic porphyria`
- Extra agent deletion: `name: protoporphyria, erythropoietic, 1`
- Extra agent deletion: `name: cutaneous porphyria`
- Extra agent deletion: `name: X-linked erythropoietic protoporphyria`
- Extra agent deletion: `name: porphyria due to ALA dehydratase deficiency`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
