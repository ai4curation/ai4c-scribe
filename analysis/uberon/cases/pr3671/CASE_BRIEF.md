---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3657
pr_number: 3671
issue_title: New term requests by HRA/HuBMAP
pr_author: nicolevasilevsky
pr_merged_at: '2026-03-23'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-17'
domain_area: oral-anatomy
best_f1: 0.781
best_model: claude-opus-4.7
---

# PR #3671 — New term requests by HRA/HuBMAP

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3657](https://github.com/obophenotype/uberon/issues/3657) | [PR #3671](https://github.com/obophenotype/uberon/pull/3671) | @nicolevasilevsky | merged 2026-03-23

`new_term` `medium` `tightly_scoped` `approved_first_time`

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

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index f7788e570..a653f8d41 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -221013,6 +221013,61 @@ relationship: dc-contributor https://orcid.org/0000-0001-5208-3432 ! Nicole Vasi
 relationship: has_part UBERON:0002354 {source="https://github.com/obophenotype/uberon/issues/1785", source="https://orcid.org/0000-0001-5208-3432", source="https://orcid.org/0000-0002-9791-0064"} ! cardiac Purkinje fiber
 relationship: part_of UBERON:0004146 {source="https://github.com/obophenotype/uberon/issues/1785", source="https://orcid.org/0000-0001-5208-3432", source="https://orcid.org/0000-0002-9791-0064"} ! His-Purkinje system
 
+[Term]
+id: UBERON:8000010
+name: salivary gland ducto-acinar unit
+def: "A lobule of a salivary gland consisting of the ducto-acinar unit and the secretory acini together with their contiguous ductal segments, including the intercalated duct and striated duct, together with associated myoepithelial cells, stromal tissue, and vasculature. This structural-functional unit is responsible for the production of primary saliva by the acinar cells and its ionic modification during transit through the ductal segments." [PMID:24862590, PMID:30855909]
+comment: Also known as the "salivon" in classical salivary physiology literature. The three major salivary glands (parotid, submandibular, sublingual) contain gland-specific variants of this unit that differ in acinar cell composition (serous vs. mucous vs. mixed).
+subset: added_by_HRA
+synonym: "salivary gland ducto-acinar" RELATED []
+synonym: "salivon" EXACT []
+is_a: UBERON:0000063 ! organ subunit
+relationship: part_of UBERON:0001044 ! saliva-secreting gland
+relationship: part_of UBERON:0009911 ! lobule
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657" xsd:anyURI
+
+[Term]
+id: UBERON:8000011
+name: parotid gland ducto-acinar unit
+def: "A salivary gland ducto-acinar unit that is part of the parotid gland, consisting of purely serous acini together with their contiguous intercalated and striated ductal segments, and associated myoepithelial cells, stromal tissue, and vasculature. This unit produces a watery, protein-rich serous saliva." [PMID:24862590, PMID:30855909]
+subset: added_by_HRA
+synonym: "parotid gland ducto-acinar" RELATED []
+is_a: UBERON:8000010 ! salivary gland ducto-acinar unit
+relationship: part_of UBERON:0001831 ! parotid gland
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657" xsd:anyURI
+
+[Term]
+id: UBERON:8000012
+name: sublingual gland ducto-acinar unit
+def: "A salivary gland ducto-acinar unit that is part of the sublingual gland, consisting of predominantly mucous acini (with minor serous demilunes) together with their contiguous ductal segments, and associated myoepithelial cells, stromal tissue, and vasculature. This unit produces a viscous, mucin-rich saliva." [PMID:24862590, PMID:30855909]
+subset: added_by_HRA
+synonym: "sublingual gland ducto-acinar" RELATED []
+is_a: UBERON:8000010 ! salivary gland ducto-acinar unit
+relationship: part_of UBERON:0001832 ! sublingual gland
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657" xsd:anyURI
+
+[Term]
+id: UBERON:8000013
+name: submandibular gland ducto-acinar unit
+def: "A salivary gland ducto-acinar unit that is part of the submandibular gland, consisting of a mixture of predominantly serous acini with a minority of mucous acini, together with their contiguous ductal segments, and associated myoepithelial cells, stromal tissue, and vasculature. This unit produces a mixed serous-mucous saliva." [PMID:24862590, PMID:30855909]
+subset: added_by_HRA
+synonym: "submandibular gland ducto-acinar" RELATED []
+is_a: UBERON:8000010 ! salivary gland ducto-acinar unit
+relationship: part_of UBERON:0001736 ! submandibular gland
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657" xsd:anyURI
+
+[Term]
+id: UBERON:8000014
+name: dentogingival junction
+def: "A multi-tissue anatomical complex that constitutes the attachment zone between the gingival tissue and the tooth surface, comprising the junctional epithelium, the supracrestal connective tissue attachment fibers, and supporting stromal and vascular elements. This structure seals the periodontal space from the oral cavity and serves as the primary physical and biological interface anchoring the free and attached gingiva to the tooth." [ISBN:9780323096300, PMID:38876998]
+subset: added_by_HRA
+synonym: "dentogingival complex" RELATED []
+synonym: "gingival attachment" RELATED []
+synonym: "supracrestal tissue attachment" RELATED []
+is_a: UBERON:0007651 ! anatomical junction
+relationship: part_of UBERON:0001828 ! gingiva
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657" xsd:anyURI
+
 [Term]
 id: UBERON:8200002
 name: copepodite stage 1

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.781 | 0.781 | 0.781 | `9e49191` | [#265](https://github.com/ai4curation/eval-ont-agent-uberon/pull/265) | [attempt](attempts/pr265.md) |
| 2 | gpt-5.5 | opencode | 0.762 | 0.750 | 0.774 | `54249f8` | [#644](https://github.com/ai4curation/eval-ont-agent-uberon/pull/644) | [attempt](attempts/pr644.md) |
| 3 | gpt-5.5 | opencode | 0.762 | 0.750 | 0.774 | `54249f8` | [#585](https://github.com/ai4curation/eval-ont-agent-uberon/pull/585) | [attempt](attempts/pr585.md) |
| 4 | claude-sonnet-4.5 | claude | 0.719 | 0.719 | 0.719 | `132555f` | [#301](https://github.com/ai4curation/eval-ont-agent-uberon/pull/301) | [attempt](attempts/pr301.md) |
| 5 | gpt-5.4 | codex | 0.545 | 0.562 | 0.529 | `7995ad0` | [#389](https://github.com/ai4curation/eval-ont-agent-uberon/pull/389) | [attempt](attempts/pr389.md) |
| 6 | gpt-5.4 | opencode | 0.382 | 0.406 | 0.361 | `95b972b` | [#683](https://github.com/ai4curation/eval-ont-agent-uberon/pull/683) | [attempt](attempts/pr683.md) |
| 7 | gpt-5.4 | opencode | 0.382 | 0.406 | 0.361 | `95b972b` | [#621](https://github.com/ai4curation/eval-ont-agent-uberon/pull/621) | [attempt](attempts/pr621.md) |
| 8 | claude-haiku-4.5 | claude | 0.281 | 0.281 | 0.281 | `adc43df` | [#173](https://github.com/ai4curation/eval-ont-agent-uberon/pull/173) | [attempt](attempts/pr173.md) |
