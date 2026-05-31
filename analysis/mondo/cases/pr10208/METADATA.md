---
repo: monarch-initiative/mondo
issue_number: 9909
pr_number: 10208
issue_title: "macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss nomenclature and synonyms"
issue_created_at: "2026-01-28"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9
    deletions: 7
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Synonym cleanup and addition for a term with complex nomenclature, requiring careful assessment of which synonyms are truly exact.
case_quality: poor
case_quality_reason: gold_uses_curator_orcid_source_and_expansive_reinterpretation
companion_prs: []
scoring_caveat: "Single gold PR #10208 (no companion PRs, no contamination, no gold leakage). However metadiff F1 is structurally depressed for every attempt: (1) the gold sources the new MATINS and the repaired MYH9-related disease synonyms to the curator's personal ORCID https://orcid.org/0000-0001-9310-0163 — a token no agent can guess, so even a correct MATINS add cannot normalize-match gold; (2) the gold goes well beyond the issue text by promoting six RELATED synonyms to EXACT (Alport syndrome with macrothrombocytopenia, FTNS, macrothrombocytopenia progressive deafness, MHA, MYH9 related disorders, SBS) and contradicts the requester's literal ask to *remove* historical names. Judge attempts against the issue + curator comment, not the line-level diff: best attempts (#396 Opus, #258 Kimi) did substantively correct, well-sourced work despite F1=0.20; #433 Sonnet-claude has F1=0.0 but a correct MATINS add. The genuinely poor attempts are the copilot runs (#518/#487) which added unsourced empty-bracket duplicate synonyms."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9909 addressed the nomenclature for MONDO:0015912 (macrothrombocytopenia and granulocyte inclusions with or without nephritis or sensorineural hearing loss). The request specified which synonyms should be marked as exact: "MATINS", "MYH9-Related Disease", and "MYH9-related syndromic thrombocytopenia", reflecting current clinical usage.

## Changes Made

The PR modified synonym annotations on MONDO:0015912, adding 9 lines and removing 7. This pattern of additions exceeding deletions while both being present indicates synonym scope corrections (e.g., changing RELATED to EXACT) alongside new synonym additions. The MYH9-related naming follows ClinGen gene-centric conventions.

## Resolution

Simple difficulty but requires attention to synonym scope accuracy. The curator needed to evaluate which existing synonyms had incorrect scope and which new synonyms to add. An agent would need to parse the issue request carefully, identify the target term, and apply both additions and scope modifications in a single coherent edit.

## Curation Note (data quality)

**Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15.**

This is a clean single-PR resolution (verified: `gh search prs` on issue 9909 and on "MATINS"/"MYH9-related disease" returns only #10208; the gold diff is intact in current `mondo-edit.obo`). There is **no companion-PR partiality, no eval base contamination, and no gold leakage** (every agent blob differs from gold and F1 < 1.0). Nonetheless this is a **poor reference case** because metadiff F1 is structurally depressed for *every* attempt for two reasons:

1. **Curator-ORCID source token (un-guessable).** The gold sources the newly added `synonym: "MATINS" EXACT [https://orcid.org/0000-0001-9310-0163]` and the repaired `synonym: "MYH9-related disease" EXACT [https://orcid.org/0000-0001-9310-0163]` to the human curator's personal ORCID. No agent can produce that token, so even a perfectly reasoned MATINS addition (which several attempts made, e.g. #396, #258, #433) cannot normalize-match the gold line. Agents instead supplied principled sources (OMIM:155100, Orphanet:182050, PMID:31384439) — arguably better practice than ORCID-as-synonym-source.

2. **Expansive curator reinterpretation beyond the issue text.** The requester (@galyea123) asked to *restrict* the exact-synonym list and *remove* the historical names. The curator (@MeeSiing) instead **kept** all historical names *and* promoted six RELATED synonyms to EXACT (`Alport syndrome with macrothrombocytopenia`, `FTNS`, `macrothrombocytopenia progressive deafness`, `MHA`, `MYH9 related disorders`, `SBS`) — treating them as exact synonyms of the unified MYH9-RD concept. This is a curator judgment call documented only tersely in the issue comment ("we will keep the other synonyms"); the six scope promotions were *not* requested anywhere and were missed by all 8 attempts. Missing them is defensible, but it caps recall at ~0.5 cohort-wide.

**Scoring guidance:** judge attempts against the issue + the curator comment, not the line diff. Best work: #396 (Opus, grounded in the curator comment, MATINS + empty-bracket fix + term tracker) and #258 (Kimi, same edits with verifiable PMID:31384439 provenance) — both F1=0.20 but substantively sound. #433 (Sonnet/claude) F1=0.0 but a correct, well-sourced minimal MATINS add. Genuinely poor: #518/#487 (copilot/Sonnet, deterministic duplicate) which *introduced* two unsourced empty-bracket synonyms including a capitalization-duplicate of an existing synonym — net-negative edits. #555 (codex/gpt-5.5) introduced a capitalization-duplicate `MYH9-Related Disease` synonym (over-editing). Downstream aggregation should down-weight or exclude this case's F1.
