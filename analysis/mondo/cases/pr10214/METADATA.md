---
repo: monarch-initiative/mondo
issue_number: 9956
pr_number: 10214
issue_title: "New Term Request/TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-02-18"
issue_closed_at: "2026-05-01"
pr_author: MeeSiing
pr_merged_at: "2026-05-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term stanza with no unrelated modifications.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - neurodevelopmental-disorder
  - gene-disease
  - TSEN2
  - HGNC:28422
  - ClinGen
  - thrombotic-microangiopathy
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean new disease term requiring gene-disease logical axioms, ClinGen provenance, and multi-parent classification
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
companion_prs: []
scoring_caveat: "Single-PR resolution (no companion PRs; Step 3a clean, no gold leakage). However metadiff F1 is structurally capped for ALL 14 attempts (max 0.667) because this is a new_term case: agents cannot know the merge-time canonical ID MONDO:1060216 and correctly use placeholder MONDO:777xxxx NTR-range IDs, the stanza insertion location differs from gold, and the gold creator ORCID (0000-0002-7638-4659, the human curator) is unreproducible. Judge attempts on substance (gene grounding HGNC:28422, logical definition intersection_of MONDO:0700092 + has_material_basis_in_germline_mutation_in, definition fidelity, ClinGen-qualified synonym) not on metadiff. The gold curator's second parent is_a MONDO:0002254 (syndromic disease) was added beyond the issue's explicit single-parent request and beyond the approving reviewer's only comment (suggesting a logical definition); its omission by agents is a defensible scoping decision, not a failure."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

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

## Curation Note (data quality)

Flagged `case_quality: poor` (reason: `new_term_canonical_id_artifact`) on 2026-05-15 by claude-opus-4.7 after reviewing all 14 attempts.

**Not a Step 3a problem.** Issue #9956 was resolved by exactly one PR (#10214); `gh search prs` for both `9956` and `TSEN2` returns only #10214. No companion PRs, no gold leakage, no F1=1.0 fakes, no curator repudiation (the only review, by sabrinatoro, approved and merely suggested adding a logical definition — which agents did).

**The problem is the standard new_term metadiff artifact.** F1 is structurally capped for *every* attempt (best 0.667, gpt-5.5/opencode #84/#64; worst 0.435, sonnet/copilot #521/#482) because:

1. **Placeholder-vs-canonical ID**: gold's `MONDO:1060216` is assigned only at merge. Agents correctly use placeholder `MONDO:777xxxx` NTR-range IDs per Mondo convention (the right behavior). The `id:` line and stanza insertion location therefore never match gold. Attempt #254 (kimi) is the lone exception that used `MONDO:1060216` and gold's insertion location — verified as genuine agent work (definition wording, expanded per-axiom source lists, and creator value all diverge from gold; not a copied stanza), and it scored highest recall as a result.
2. **Creator ORCID**: gold uses the human curator's ORCID `0000-0002-7638-4659`; agents cannot reproduce this.
3. **Gold's second parent** `is_a: MONDO:0002254` (syndromic disease) was added by the curator beyond the issue's explicit single-parent request (`Parent term: MONDO:0700092`). Almost no agent added it; this is a defensible scoping decision (claude-opus #404 explicitly flagged the dual-parent question for reviewer attention — exemplary behavior), not a failure.

**Net**: metadiff substantially **under-represents** quality for the strong attempts (gpt-5.5 opencode/codex, kimi, claude-opus all produced substantively correct, mergeable terms with correct `HGNC:28422` grounding and correct `intersection_of MONDO:0700092 + has_material_basis_in_germline_mutation_in` logical definitions). Genuine quality differentiators that metadiff does *not* capture well: pr521/pr482 (copilot) truncated the term name (real `wrong_term`); pr199/pr23 (haiku) split the label into bogus "with/without TMA" EXACT synonyms and mis-cited TRACK syndrome; pr551 (sonnet) likely fabricated a TRACK-expansion synonym; pr32 (opencode) omitted the synonym entirely. Downstream aggregation should down-weight raw F1 for this case and rely on the substantive review narratives.
