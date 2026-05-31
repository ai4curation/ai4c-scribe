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
num_agent_attempts: 11
generated_at: '2026-05-17'
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

## Curation Note (data quality)

Flagged `case_quality: poor` (reason `gold_id_range_unmatchable`) by claude-opus-4.7 on 2026-05-15 after reviewing all 9 attempts.

The issue (#9873) was resolved by a single human PR (#10126) — no companion PRs (`gh search prs` for "9873" and "Southern tick-associated rash" returns only #10126). So this is **not** a multi-PR partial-gold case (Step 3a does not apply). However it is a **Step 3b poor case** for a different reason:

- The gold PR assigns the new term `MONDO:1010205`. The agent config repo (`ai4curation/mondo-agent-config`) `CLAUDE.md` explicitly instructs: *"New terms start MONDO:777xxxx"* and to `grep id: MONDO:777` for the next free ID. Every one of the 9 agents correctly followed this instruction and used `MONDO:7770018`.
- Because the ID differs, agents also inserted the stanza at a completely different file locus (after `MONDO:7770011` / before `MONDO:8000000 infectious discitis`, ~line 658378) than the human (after the issue-9877 term / before `MONDO:1010206`, ~line 619475). The `id:` line, every surrounding diff-context line, and the `is_a`/`transmitted_by` trailing `! comment` lines therefore cannot match the gold by construction.
- Net effect: metadiff F1 is structurally capped at roughly 0.40–0.64 for **all** attempts regardless of actual quality. The metric is uninformative for ranking quality on this case and systematically **under-represents** it.

Additional non-reproducible gold elements (not in the issue): the merged definition is a curator post-review rewrite ("...transmitted by the lone star tick... erythema migrans–like rash with or without mild constitutional symptoms"); synonyms are sourced to `PMID:18452807`; the creator `dcterms:creator` is the curator's ORCID `0000-0002-5002-8648` rather than the submitter's. No agent could infer these.

**Scoring guidance for this case**: rank attempts by substantive modeling, not metadiff. The discriminating substantive criteria are: (1) correct parent `is_a: MONDO:0025294`; (2) presence of the `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum` vector axiom (present in gold; captured by 7/9 attempts — missing in the two haiku runs #476/#422); (3) canonical `xref: SCTID:` prefix vs the issue's literal `SNOMED:` (the haiku runs used the non-canonical `SNOMED:`); (4) both synonyms with correct scopes; (5) all three PMIDs in the definition. By that standard the strongest attempts are #173 (gpt-5.4/codex), #77 & #58 (gpt-5.5/opencode, byte-identical pair), #388 (claude-opus-4.7), and #281 (kimi-k2.6/opencode) — all effectively successful — while the two claude-haiku-4.5 runs (#476, #422, also a byte-identical pair) are genuinely weaker (missing vector axiom, wrong xref prefix, stray `namespace:` line).

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

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.640 | 0.667 | 0.615 | `56f050a` | [#173](https://github.com/ai4curation/eval-ont-agent-mondo/pull/173) | [attempt](attempts/pr173.md) |
| 2 | claude-sonnet-4.5 | claude | 0.522 | 0.500 | 0.545 | `840b4dd` | [#463](https://github.com/ai4curation/eval-ont-agent-mondo/pull/463) | [attempt](attempts/pr463.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `f6ffe25` | [#476](https://github.com/ai4curation/eval-ont-agent-mondo/pull/476) | [attempt](attempts/pr476.md) |
| 4 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `f6ffe25` | [#422](https://github.com/ai4curation/eval-ont-agent-mondo/pull/422) | [attempt](attempts/pr422.md) |
| 5 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `02b16b1` | [#77](https://github.com/ai4curation/eval-ont-agent-mondo/pull/77) | [attempt](attempts/pr77.md) |
| 6 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `02b16b1` | [#58](https://github.com/ai4curation/eval-ont-agent-mondo/pull/58) | [attempt](attempts/pr58.md) |
| 7 | gpt-5.4 | opencode | 0.435 | 0.417 | 0.455 | `e694a3e` | [#747](https://github.com/ai4curation/eval-ont-agent-mondo/pull/747) | [attempt](attempts/pr747.md) |
| 8 | gpt-5.4 | opencode | 0.435 | 0.417 | 0.455 | `e694a3e` | [#692](https://github.com/ai4curation/eval-ont-agent-mondo/pull/692) | [attempt](attempts/pr692.md) |
| 9 | claude-opus-4.7 | claude | 0.417 | 0.417 | 0.417 | `33c1d10` | [#388](https://github.com/ai4curation/eval-ont-agent-mondo/pull/388) | [attempt](attempts/pr388.md) |
| 10 | kimi-k2.6 | opencode | 0.417 | 0.417 | 0.417 | `e9f85ec` | [#281](https://github.com/ai4curation/eval-ont-agent-mondo/pull/281) | [attempt](attempts/pr281.md) |
| 11 | gpt-5.5 | codex | 0.400 | 0.417 | 0.385 | `d9f233b` | [#40](https://github.com/ai4curation/eval-ont-agent-mondo/pull/40) | [attempt](attempts/pr40.md) |
