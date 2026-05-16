---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9873
pr_number: 10126
issue_title: Request for new term Southern tick-associated rash illness
pr_author: katiermullen
pr_merged_at: '2026-04-17'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR adds a single new disease term with definition, synonyms, and cross-references.
domain_area: infectious-disease
best_f1: 0.64
best_model: gpt-5.4
---

# PR #10126 — Request for new term Southern tick-associated rash illness

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9873](https://github.com/monarch-initiative/mondo/issues/9873) | [PR #10126](https://github.com/monarch-initiative/mondo/pull/10126) | @katiermullen | merged 2026-04-17

`new_term` `medium` `tightly_scoped` `changes_requested`

## Context

A user requested a new Mondo term for Southern tick-associated rash illness (STARI), also known as Masters disease. STARI is an infectious disease transmitted by the lone star tick (Amblyomma americanum) that presents with an erythema migrans-like rash similar to Lyme disease but with a distinct etiology. The request (issue #9873) included exact synonyms (STARI, Masters disease), a proposed definition with PubMed references, and cross-references to NCIT:C128427 and SNOMED:444100007.

## Changes Made

The PR added 13 lines to `src/ontology/mondo-edit.obo` introducing a new term stanza classified under MONDO:0025294 "tick-borne infectious disease." The 8 commits reflect review iteration: the initial submission received a CHANGES_REQUESTED review from a senior curator asking for an updated definition, after which the definition was revised and the PR was approved. Cross-references to NCIT and SNOMED were included for interoperability.

## Resolution

Medium difficulty because while the new term follows standard Mondo patterns, the definition required iteration based on reviewer feedback. An agent would need to construct the term stanza with the correct parent classification, parse the user-provided synonyms and cross-references, and be able to revise the definition in response to curator feedback. The review cycle (changes requested then approved) is representative of typical NTR workflows.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f5..45dbc41774 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -619475,6 +619475,19 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
 
+[Term]
+id: MONDO:1010205
+name: southern tick-associated rash illness
+def: "A tick-borne infectious disease transmitted by the lone star tick, Amblyomma americanum, and causing an erythema migrans–like rash with or without mild constitutional symptoms." [https://orcid.org/0000-0001-5705-7831, PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:18452807]
+synonym: "STARI" EXACT ABBREVIATION [PMID:18452807]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:1010206
 name: meningeal neoplasm, non-human animal

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.4 | codex | 0.640 | 0.667 | 0.615 | [#173](https://github.com/ai4curation/eval-ont-agent-mondo/pull/173) | [attempt](attempts/pr173.md) |
| 2 | claude-sonnet-4.5 | claude | 0.522 | 0.500 | 0.545 | [#463](https://github.com/ai4curation/eval-ont-agent-mondo/pull/463) | [attempt](attempts/pr463.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#476](https://github.com/ai4curation/eval-ont-agent-mondo/pull/476) | [attempt](attempts/pr476.md) |
| 4 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#422](https://github.com/ai4curation/eval-ont-agent-mondo/pull/422) | [attempt](attempts/pr422.md) |
| 5 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#77](https://github.com/ai4curation/eval-ont-agent-mondo/pull/77) | [attempt](attempts/pr77.md) |
| 6 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#58](https://github.com/ai4curation/eval-ont-agent-mondo/pull/58) | [attempt](attempts/pr58.md) |
| 7 | claude-opus-4.7 | claude | 0.417 | 0.417 | 0.417 | [#388](https://github.com/ai4curation/eval-ont-agent-mondo/pull/388) | [attempt](attempts/pr388.md) |
| 8 | kimi-k2.6 | opencode | 0.417 | 0.417 | 0.417 | [#281](https://github.com/ai4curation/eval-ont-agent-mondo/pull/281) | [attempt](attempts/pr281.md) |
| 9 | gpt-5.5 | codex | 0.400 | 0.417 | 0.385 | [#40](https://github.com/ai4curation/eval-ont-agent-mondo/pull/40) | [attempt](attempts/pr40.md) |
