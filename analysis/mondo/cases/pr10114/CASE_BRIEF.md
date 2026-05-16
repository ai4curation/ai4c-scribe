---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9799
pr_number: 10114
issue_title: '[Obsolete]MONDO:0023124 familial pulmonary arterial hypertension leucopenia
  and atrial septal defect'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
best_f1: 0.727
best_model: kimi-k2.6
---

# PR #10114 — [Obsolete]MONDO:0023124 familial pulmonary arterial hypertension leucopenia and atrial septal defect

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9799](https://github.com/monarch-initiative/mondo/issues/9799) | [PR #10114](https://github.com/monarch-initiative/mondo/pull/10114) | @MeeSiing | merged 2026-04-02

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9799 proposed obsoleting MONDO:0023124 (familial pulmonary arterial hypertension leucopenia and atrial septal defect) because the term's only cross-reference appeared to match Dursun syndrome in OMIM. Rather than obsoleting, the curator relabeled the term to "Dursun syndrome" based on OMIM's included term designation.

## Changes Made

The PR relabeled MONDO:0023124 from the long descriptive name to "Dursun syndrome" and added associated metadata. The 9 additions include the new label, synonyms preserving the original name, and OMIM-sourced annotations. The 4 deletions remove the old label and outdated annotations. This approach preserves the term ID while improving its naming.

## Resolution

Simple difficulty because relabeling is less destructive than obsoletion and follows a clear pattern: change the rdfs:label, move the old label to a synonym, and add source annotations. The curator chose relabeling over obsoletion after verifying the OMIM alignment, which is a pragmatic decision that preserves term stability for downstream users.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..f2827f9d38 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -539379,14 +539379,19 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0023124
-name: familial pulmonary arterial hypertension leucopenia and atrial septal defect
-comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term represents an actual existing disease. After obsoletion, this term will not have a replacement ID, but one could consider the following term: none-
-subset: obsoletion_candidate
+name: Dursun syndrome
+def: "A syndromic disease caused by mutation in the G6PC3 gene, characterized by familial pulmonary arterial hypertension, leukopenia, and atrial septal defect." [OMIM:612541, PMID:20799326]
 synonym: "familial PAH, leucopenia and ASD" RELATED [GARD:0010455]
+synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [OMIM:612541]
 synonym: "familial pulmonary arterial hypertension, leucopenia and ASD" RELATED [GARD:0010455]
+synonym: "familial pulmonary arterial hypertension, leucopenia, and atrial septal defect" EXACT [OMIM:612541]
+xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}
+xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}
 is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-6601-2165"} ! syndromic disease
+intersection_of: MONDO:0002254 ! syndromic disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24861 ! G6PC3
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24861 {source="OMIM:612541", source="PMID:20799326"} ! G6PC3
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9799" xsd:anyURI
-property_value: IAO:0006012 "2026-02-01" xsd:string
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/10455/familial-pulmonary-arterial-hypertension-leucopenia-and-atrial-septal-defect" xsd:anyURI {source="GARD:0010455"}
 
 [Term]

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.727 | 0.615 | 0.889 | [#262](https://github.com/ai4curation/eval-ont-agent-mondo/pull/262) | [attempt](attempts/pr262.md) |
| 2 | gpt-5.4 | codex | 0.727 | 0.615 | 0.889 | [#162](https://github.com/ai4curation/eval-ont-agent-mondo/pull/162) | [attempt](attempts/pr162.md) |
| 3 | claude-opus-4.7 | claude | 0.667 | 0.538 | 0.875 | [#382](https://github.com/ai4curation/eval-ont-agent-mondo/pull/382) | [attempt](attempts/pr382.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.636 | 0.538 | 0.778 | [#530](https://github.com/ai4curation/eval-ont-agent-mondo/pull/530) | [attempt](attempts/pr530.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.636 | 0.538 | 0.778 | [#494](https://github.com/ai4curation/eval-ont-agent-mondo/pull/494) | [attempt](attempts/pr494.md) |
| 6 | claude-sonnet-4.5 | claude | 0.519 | 0.538 | 0.500 | [#443](https://github.com/ai4curation/eval-ont-agent-mondo/pull/443) | [attempt](attempts/pr443.md) |
| 7 | claude-haiku-4.5 | claude | 0.519 | 0.538 | 0.500 | [#188](https://github.com/ai4curation/eval-ont-agent-mondo/pull/188) | [attempt](attempts/pr188.md) |
| 8 | gpt-5.5 | opencode | 0.483 | 0.538 | 0.438 | [#134](https://github.com/ai4curation/eval-ont-agent-mondo/pull/134) | [attempt](attempts/pr134.md) |
| 9 | gpt-5.5 | opencode | 0.483 | 0.538 | 0.438 | [#115](https://github.com/ai4curation/eval-ont-agent-mondo/pull/115) | [attempt](attempts/pr115.md) |
| 10 | gpt-5.5 | codex | 0.462 | 0.462 | 0.462 | [#95](https://github.com/ai4curation/eval-ont-agent-mondo/pull/95) | [attempt](attempts/pr95.md) |
