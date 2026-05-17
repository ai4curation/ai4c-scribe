---
repo: monarch-initiative/mondo
issue_number: 9873
pr_number: 10126
issue_title: "Request for new term Southern tick-associated rash illness"
issue_created_at: "2026-01-13"
pr_author: katiermullen
pr_merged_at: "2026-04-17"
pr_num_commits: 8
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds a single new disease term with definition, synonyms, and cross-references.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: infectious-disease
tags:
  - new-term-request
  - tick-borne-disease
  - infectious-disease
  - STARI
  - NCIT
  - SNOMED
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request with review iteration on definition wording, requiring cross-reference alignment to NCIT and SNOMED
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
companion_prs: []
scoring_caveat: "Gold PR #10126 assigns MONDO:1010205, but the agent config CLAUDE.md explicitly instructs agents that new terms start in the MONDO:777xxxx range; every agent correctly followed this and used MONDO:7770018. The differing ID forces a different id: line AND a different file-insertion locus (agents anchor near MONDO:7770011/infectious discitis ~line 658378; gold anchors near MONDO:1010206 ~line 619475), so the id line, all surrounding context lines, and the is_a/transmitted_by ! comment lines never match by construction. Metadiff F1 is therefore structurally capped well below 1.0 (observed range 0.40-0.64) for all 9 attempts regardless of quality. Judge attempts on substantive modeling (parent MONDO:0025294, transmitted_by NCBITaxon:6943 vector axiom, SCTID: vs SNOMED: prefix, synonym scopes, def/PMIDs), not the metadiff. Additionally the gold definition is a curator post-review rewrite and the synonym source PMID:18452807 and curator creator ORCID 0000-0002-5002-8648 were not in the issue, none of which an agent could reproduce."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

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
