---
repo: obophenotype/uberon
issue_number: 3657
pr_number: 3671
issue_title: "New term requests by HRA/HuBMAP"
issue_created_at: "2026-02-02"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-23"
pr_num_commits: 7
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 55
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: oral-anatomy
tags:
  - HRA
  - HuBMAP
  - salivary-gland
  - new-term-request
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term addition requiring domain knowledge of salivary gland and oral anatomy structures
case_quality: poor
case_quality_reason: gold_renegotiated_in_review
companion_prs: [3673]
scoring_caveat: "Metadiff vs the merged gold PR #3671 penalizes all attempts for reviewer-driven changes (RiveraAndrea83) made AFTER the issue #3657 discussion closed: salivon parent changed from is_a lobule to is_a UBERON:0000063 organ subunit + part_of UBERON:0009911 lobule; dentogingival junction changed from is_a tissue to is_a UBERON:0007651 anatomical junction; 'approximately 90%' removed from the submandibular def; def references changed to PMID:30855909. The issue thread itself converged on a different proposal (is_a lobule; dentogingival is_a tissue; 'approximately 90%') that agents correctly reproduced. Judge attempts against the issue's negotiated proposal, not the post-review gold. F1 under-represents quality for pr265 and pr301; pr173's low F1 is mostly genuine (OBO syntax errors + disputed in_taxon)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The HRA/HuBMAP project requested five new anatomical terms related to oral and salivary gland anatomy: salivary gland ducto-acinar unit, parotid gland ducto-acinar unit, sublingual gland ducto-acinar unit, submandibular gland ducto-acinar unit, and dentogingival junction. These terms were needed to support the Human Reference Atlas tissue mapping efforts.

## Changes Made

The PR added 55 lines to src/ontology/uberon-edit.obo, creating five new term stanzas with definitions, is_a relationships, and appropriate part_of axioms linking each ducto-acinar unit to its parent salivary gland structure. The dentogingival junction was placed in the appropriate oral anatomical hierarchy.

## Resolution

Medium difficulty. While the individual term additions follow standard OBO patterns, an agent would need domain knowledge to correctly place the ducto-acinar units under their parent gland structures and assign appropriate part_of relationships. The seven commits suggest iterative refinement during review. Merged after approximately seven weeks from issue creation.

## Curation Note (data quality)

`case_quality: poor` — `gold_renegotiated_in_review`.

Issue #3657 contains an extensive, fully-resolved negotiation between the
requesters (zhengj2007 / HRA) and dragon-ai-agent. The thread converged on a
concrete final proposal with explicit labels, definitions, parents, and
synonyms, which all three agent attempts faithfully reproduced. That converged
proposal specified:

- `salivary gland ducto-acinar unit`: `is_a UBERON:0009911 lobule`, `part_of
  UBERON:0001044 saliva-secreting gland`
- `dentogingival junction`: `is_a UBERON:0000479 tissue`, `part_of
  UBERON:0001828 gingiva`
- submandibular def: "a mixture of predominantly serous acini (approximately
  90%) ..."
- def references: `[PMID:24862590, https://www.ncbi.nlm.nih.gov/books/NBK538325/]`

The merged gold PR #3671, however, diverges from this proposal because the
human reviewer (RiveraAndrea83) requested structural changes during PR review,
*after* the issue discussion had closed. The seven commits implement those
review-driven changes (confirmed via PR line-comment threads):

1. salivon parent → `is_a UBERON:0000063 organ subunit` + `relationship:
   part_of UBERON:0009911 lobule` (reviewer: "the lobule contains the
   ducto-acinar unit"); also added `part_of UBERON:0001044`.
2. `dentogingival junction` → `is_a UBERON:0007651 anatomical junction`
   (reviewer: "i'd consider using only part_of as it represents the space
   between gingival tissue and tooth surface").
3. submandibular def → "predominantly serous acini with a minority of mucous
   acini" (reviewer asked to generalise the "90%").
4. def references → `[PMID:24862590, PMID:30855909]`.

These reviewer decisions were unpredictable from the issue thread and cap every
attempt's metadiff F1 well below 1.0 for reasons unrelated to agent skill.
Downstream scoring/aggregation should treat the issue's negotiated proposal as
the practical target for pr265/pr301 (whose F1 of 0.781/0.719 under-represents
quality). pr173's low F1 (0.281) is mostly genuine — it has invalid OBO syntax
(`part_of:` tag, `EXACT_SYNONYM` deprecated tags) and added a disputed
`in_taxon NCBITaxon:9606` constraint the requesters explicitly left open and
the gold omitted.

A separate follow-up companion PR #3673 (referenced by nicolevasilevsky in the
PR thread and by cmungall requesting logical definitions) added subset tags /
logical definitions; it is not part of the diff scored here but confirms the
issue's resolution spanned more than the single scored PR's final state.

`quality_flagged_by: claude-opus-4.7`, `quality_flagged_at: 2026-05-16`.
