---
ontology: mondo
issue_number: 9703
pr_number: 9770
eval_repo_pr: 91
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.268
precision: 0.347
recall: 0.218
jaccard: 0.155
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9703
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/9770
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/91
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9703 --repo monarch-initiative/mondo
    gh pr diff 9770 --repo monarch-initiative/mondo
    gh pr diff 91 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #9770 addressed `reclassification` for issue #9703: Updates to Gene-Disease
Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group. Human
resolution summary: The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`,
involving new labels, new terms, updated inheritance annotations, and restructured classification
for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting
underscores in definitions were also included. The 7 commits reflect an iterative curation process
responding to expert review feedback. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.268 (precision=0.347, recall=0.218). It matched 14/35 accepted additions and 5/9 accepted
deletions.

## Strengths

- Matched 19 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9703" xsd:anyURI`
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: HMBS-related hepatic porphyria`
- Matched accepted addition: `is_a: MONDO:0002520 {source="https://clinicalgenome.org/affiliation/40097/"} ! hepatic porphyria`
- Matched accepted deletion: `def: "Erythropoietic protoporphyria caused by a compound heterozygous or homozygous mutation in the gene encoding ferrochelatase (FECH) on chromoso...`
- Matched accepted deletion: `def: "Congenital erythropoietic porphyria, or G\xfcnther disease, is a form of erythropoietic porphyria characterized by very severe and mutilating...`
- Matched accepted deletion: `def: "X-linked form of erythropoietic protoporphyria." [MONDO:patterns/x_linked]`

## Issues

- Missing accepted changes: 21 additions and 4 deletions from the human PR were not reproduced.
- Missing accepted addition: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Missing accepted addition: `is_a: MONDO:0700382 {source="https://clinicalgenome.org/affiliation/40097/"} ! HMBS-related hepatic porphyria`
- Missing accepted addition: `is_a: MONDO:0100498 {source="https://clinicalgenome.org/affiliation/40097/"} ! UROD-related inherited porphyria`
- Missing accepted addition: `is_a: MONDO:0700383 {source="https://clinicalgenome.org/affiliation/40097/"} ! PPOX-related hepatic porphyria`
- Missing accepted addition: `def: "An erythropoietic protoporphyria caused by biallelic variants in FECH (an autosomal recessive inheritance pattern) and causing primarily accu...`
- Missing accepted deletion: `SPARQL_OBO_EXCLUDE=qc-single-child qc-omimps-should-be-inherited qc-omim-subsumption qc-permitted-properties qc-duplicate-exact-synonym-no-abbrev q...`
- Missing accepted deletion: `intersection_of: MONDO:0015104 ! porphyria cutanea tarda`
- Missing accepted deletion: `intersection_of: has_characteristic MONDO:0021152 ! inherited`
- Missing accepted deletion: `synonym: "ALAD-related porphyria" EXACT [https://clinicalgenome.org/affiliation/40097/] {OMO:0002001="https://w3id.org/information-resource-registr...`
- Extra changes beyond the accepted PR: 65 additions and 19 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:0800180 {source="https://clinicalgenome.org/affiliation/40097/", source="https://clinicalgenome.org/working-groups/clinical-domain/inbo...`
- Extra agent addition: `is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40097/"} ! HMBS-related hepatic porphyria`
- Extra agent addition: `is_a: MONDO:7770005 {source="https://clinicalgenome.org/affiliation/40097/"} ! PPOX-related hepatic porphyria`
- Extra agent addition: `name: FECH-related erythropoietic protoporphyria`
- Extra agent addition: `def: "An erythropoietic protoporphyria caused by biallelic variants in FECH and primarily causing accumulation of protoporphyrin IX. Symptoms inclu...`
- Extra agent deletion: `is_a: MONDO:0800180 {source="https://clinicalgenome.org/affiliation/40097/", source="https://clinicalgenome.org/working-groups/clinical-domain/inbo...`
- Extra agent deletion: `name: protoporphyria, erythropoietic, 1`
- Extra agent deletion: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3647 {source="OMIM:177000"} ! FECH`
- Extra agent deletion: `name: cutaneous porphyria`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
