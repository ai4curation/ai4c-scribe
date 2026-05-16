---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9956
pr_number: 10214
issue_title: New Term Request/TSEN2-related neurodevelopmental disorder with or without
  thrombotic microangiopathy
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 14
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
domain_area: rare-disease
best_f1: 0.667
best_model: gpt-5.5
---

# PR #10214 — New Term Request/TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9956](https://github.com/monarch-initiative/mondo/issues/9956) | [PR #10214](https://github.com/monarch-initiative/mondo/pull/10214) | @MeeSiing | merged 2026-05-01

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for a TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy. TSEN2 encodes a subunit of the tRNA splicing endonuclease complex. Mutations cause a complex phenotype including intellectual disability, growth delay, hypotonia, motor delay, ataxia, vision issues, cardiac features, pulmonary complications, and brain structural anomalies. Some patients also develop renal thrombotic microangiopathy.

The request was backed by ClinGen curation (https://clinicalgenome.org/affiliation/40069/) and supported by 8 PMIDs.

## Changes Made

Added new term MONDO:1060216 to `src/ontology/mondo-edit.obo`:

- **ID**: MONDO:1060216
- **Name**: TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy
- **Definition**: Comprehensive clinical description citing 8 PMIDs (PMID:18711368, PMID:20952379, PMID:23562994, PMID:32404165, PMID:38347586, PMID:38438125, PMID:38622473) and ClinGen as source
- **Classification** (multi-parent):
  - is_a MONDO:0002254 (syndromic disease) — because multiple organ systems affected
  - is_a MONDO:0700092 (neurodevelopmental disorder) — primary presentation
- **Logical definition** (equivalence axiom):
  - intersection_of: MONDO:0700092 (neurodevelopmental disorder)
  - intersection_of: has_material_basis_in_germline_mutation_in HGNC:28422 (TSEN2)
- **Gene relationship**: has_material_basis_in_germline_mutation_in HGNC:28422 (TSEN2)
- **Provenance**: ClinGen affiliation as source on all axioms, creator ORCID, term_tracker_item

## Resolution

Medium difficulty because it requires:
1. **Multi-parent classification**: Determining that the disease is both a syndromic disease AND a neurodevelopmental disorder (not just one or the other)
2. **Logical axiom construction**: Building the equivalence axiom (intersection_of) correctly linking the disease class to its causal gene via the appropriate relation
3. **Source attribution**: Every axiom annotated with ClinGen provenance
4. **Definition writing**: Comprehensive clinical description synthesizing findings from 8 publications

An agent would need to understand Mondo's patterns for gene-disease terms: the specific use of `has_material_basis_in_germline_mutation_in`, the intersection_of pattern for logical definitions, and how to correctly attribute sources to individual axioms.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 28406f6c4f..0c6f2c245a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -659045,6 +659045,19 @@ is_a: MONDO:0021074 {source="PMID:37775701", source="PMID:40684183", source="htt
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9781" xsd:anyURI
 
+[Term]
+id: MONDO:1060216
+name: TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy
+def: "Any neurodevelopmental disorder in which the cause of the disease is a variation in the TSEN2 gene. This condition is associated with intellectual disability, growth delay, hypotonia, motor delay, ataxia, vision issues, cardiac features (including left ventricular hypertrophy), and pulmonary complications (such as acute respiratory distress and edema). It is also linked to brain structural anomalies such as pontine and cerebellar hypoplasia, cortical atrophy, and dilated ventricles. Renal features include proteinuria, thrombotic microangiopathy, end-stage kidney disease, and high-severity hypertension." [https://clinicalgenome.org/affiliation/40069/, PMID:18711368, PMID:20952379, PMID:23562994, PMID:32404165, PMID:38347586, PMID:38438125, PMID:38622473]
+synonym: "TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy" EXACT [https://clinicalgenome.org/affiliation/40069/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0002254 {source="https://clinicalgenome.org/affiliation/40069/"} ! syndromic disease
+is_a: MONDO:0700092 {source="https://clinicalgenome.org/affiliation/40069/"} ! neurodevelopmental disorder
+intersection_of: MONDO:0700092 ! neurodevelopmental disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422 ! TSEN2
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422 {source="https://clinicalgenome.org/affiliation/40069/"} ! TSEN2
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (14)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.667 | 0.667 | 0.667 | [#84](https://github.com/ai4curation/eval-ont-agent-mondo/pull/84) | [attempt](attempts/pr84.md) |
| 2 | gpt-5.5 | opencode | 0.667 | 0.667 | 0.667 | [#64](https://github.com/ai4curation/eval-ont-agent-mondo/pull/64) | [attempt](attempts/pr64.md) |
| 3 | kimi-k2.6 | opencode | 0.609 | 0.583 | 0.636 | [#254](https://github.com/ai4curation/eval-ont-agent-mondo/pull/254) | [attempt](attempts/pr254.md) |
| 4 | claude-opus-4.7 | claude | 0.583 | 0.583 | 0.583 | [#404](https://github.com/ai4curation/eval-ont-agent-mondo/pull/404) | [attempt](attempts/pr404.md) |
| 5 | gpt-5.5 | codex | 0.583 | 0.583 | 0.583 | [#29](https://github.com/ai4curation/eval-ont-agent-mondo/pull/29) | [attempt](attempts/pr29.md) |
| 6 | gpt-5.5 | codex | 0.583 | 0.583 | 0.583 | [#52](https://github.com/ai4curation/eval-ont-agent-mondo/pull/52) | [attempt](attempts/pr52.md) |
| 7 | claude-sonnet-4.5 | claude | 0.560 | 0.583 | 0.538 | [#551](https://github.com/ai4curation/eval-ont-agent-mondo/pull/551) | [attempt](attempts/pr551.md) |
| 8 | gpt-5.5 | opencode | 0.545 | 0.500 | 0.600 | [#32](https://github.com/ai4curation/eval-ont-agent-mondo/pull/32) | [attempt](attempts/pr32.md) |
| 9 | gpt-5.4 | codex | 0.538 | 0.583 | 0.500 | [#21](https://github.com/ai4curation/eval-ont-agent-mondo/pull/21) | [attempt](attempts/pr21.md) |
| 10 | gpt-5.4 | codex | 0.538 | 0.583 | 0.500 | [#16](https://github.com/ai4curation/eval-ont-agent-mondo/pull/16) | [attempt](attempts/pr16.md) |
| 11 | claude-haiku-4.5 | claude | 0.480 | 0.500 | 0.462 | [#199](https://github.com/ai4curation/eval-ont-agent-mondo/pull/199) | [attempt](attempts/pr199.md) |
| 12 | claude-haiku-4.5 | claude | 0.480 | 0.500 | 0.462 | [#23](https://github.com/ai4curation/eval-ont-agent-mondo/pull/23) | [attempt](attempts/pr23.md) |
| 13 | claude-sonnet-4.5 | copilot | 0.435 | 0.417 | 0.455 | [#521](https://github.com/ai4curation/eval-ont-agent-mondo/pull/521) | [attempt](attempts/pr521.md) |
| 14 | claude-sonnet-4.5 | copilot | 0.435 | 0.417 | 0.455 | [#482](https://github.com/ai4curation/eval-ont-agent-mondo/pull/482) | [attempt](attempts/pr482.md) |
