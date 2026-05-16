---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9781
pr_number: 10111
issue_title: Request for new term [preneoplastic lesion]
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: new_term
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
scoping_notes: PR adds a single new term with definition and classification.
domain_area: oncology
best_f1: 0.571
best_model: claude-opus-4.7
---

# PR #10111 — Request for new term [preneoplastic lesion]

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9781](https://github.com/monarch-initiative/mondo/issues/9781) | [PR #10111](https://github.com/monarch-initiative/mondo/pull/10111) | @MeeSiing | merged 2026-04-02

`new_term` `simple` `tightly_scoped` `approved_first_time`

## Context

A user requested a new term for "preneoplastic lesion" to capture conditions that precede neoplastic transformation. This is a high-level grouping class rather than a specific gene-disease term. The definition and parent term were confirmed through discussion with the requesting user in the issue thread.

## Changes Made

Added MONDO:1060215 (preneoplastic lesion) to `src/ontology/mondo-edit.obo` with 8 lines. The term is compact, containing an ID, name, definition, and parent classification. No logical axioms or complex cross-references were needed for this grouping term.

## Resolution

Easy difficulty because it is a simple grouping term without gene-disease logical axioms or complex cross-references. The main requirement was confirming the definition and appropriate parent class with the requesting user, which was done in the issue discussion.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..8babe163bc 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665275,6 +665275,14 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
 
+[Term]
+id: MONDO:1060215
+name: preneoplastic lesion
+def: "A precancerous condition characterized by accumulation of some molecular alterations necessary for malignant transformation in a clonal proliferation of cells, representing an intermediate stage in carcinogenesis with increased risk of progression to invasive neoplasia." [https://orcid.org/0000-0002-2336-2552, PMID:37775701, PMID:39754221, PMID:40624726, PMID:40684183]
+is_a: MONDO:0021074 {source="PMID:37775701", source="PMID:40684183", source="https://orcid.org/0000-0002-2336-2552"} ! precancerous condition
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9781" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.571 | 0.571 | 0.571 | `55ed082` | [#378](https://github.com/ai4curation/eval-ont-agent-mondo/pull/378) | [attempt](attempts/pr378.md) |
| 2 | kimi-k2.6 | opencode | 0.571 | 0.571 | 0.571 | `8673bae` | [#276](https://github.com/ai4curation/eval-ont-agent-mondo/pull/276) | [attempt](attempts/pr276.md) |
| 3 | gpt-5.5 | opencode | 0.571 | 0.571 | 0.571 | `a35ae63` | [#73](https://github.com/ai4curation/eval-ont-agent-mondo/pull/73) | [attempt](attempts/pr73.md) |
| 4 | gpt-5.5 | opencode | 0.571 | 0.571 | 0.571 | `a35ae63` | [#54](https://github.com/ai4curation/eval-ont-agent-mondo/pull/54) | [attempt](attempts/pr54.md) |
| 5 | gpt-5.5 | codex | 0.571 | 0.571 | 0.571 | `1a71c68` | [#35](https://github.com/ai4curation/eval-ont-agent-mondo/pull/35) | [attempt](attempts/pr35.md) |
| 6 | claude-sonnet-4.5 | claude | 0.533 | 0.571 | 0.500 | `e9deb1e` | [#466](https://github.com/ai4curation/eval-ont-agent-mondo/pull/466) | [attempt](attempts/pr466.md) |
| 7 | claude-sonnet-4.5 | claude | 0.533 | 0.571 | 0.500 | `e9deb1e` | [#460](https://github.com/ai4curation/eval-ont-agent-mondo/pull/460) | [attempt](attempts/pr460.md) |
| 8 | gemma-4-31b | opencode | 0.533 | 0.571 | 0.500 | `ebc0935` | [#259](https://github.com/ai4curation/eval-ont-agent-mondo/pull/259) | [attempt](attempts/pr259.md) |
| 9 | gemma-4-31b | opencode | 0.533 | 0.571 | 0.500 | `ebc0935` | [#214](https://github.com/ai4curation/eval-ont-agent-mondo/pull/214) | [attempt](attempts/pr214.md) |
| 10 | gpt-5.4 | codex | 0.533 | 0.571 | 0.500 | `7e752fe` | [#161](https://github.com/ai4curation/eval-ont-agent-mondo/pull/161) | [attempt](attempts/pr161.md) |
| 11 | claude-haiku-4.5 | claude | 0.429 | 0.429 | 0.429 | `1ac50b5` | [#475](https://github.com/ai4curation/eval-ont-agent-mondo/pull/475) | [attempt](attempts/pr475.md) |
| 12 | claude-haiku-4.5 | claude | 0.429 | 0.429 | 0.429 | `1ac50b5` | [#421](https://github.com/ai4curation/eval-ont-agent-mondo/pull/421) | [attempt](attempts/pr421.md) |
