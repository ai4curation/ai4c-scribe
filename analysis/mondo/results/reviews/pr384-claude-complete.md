---
ontology: mondo
issue_number: 9855
pr_number: 10115
eval_repo_pr: 384
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.333
precision: 0.286
recall: 0.4
jaccard: 0.2
outcome: partial_success
failure_modes: [missed_requirement, under_editing, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9855
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10115
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/384
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

Issue #9855 (ClinGen submitter) requested a new term for the PADI6-related female-infertility /
early-embryonic-arrest disorder (OMIM:617234), parented under MONDO:0014769 (inherited oocyte
maturation defect). The defining subtlety of the gold PR (#10115, MONDO:1010200) was that the
human recognized this concept was the **same as the previously obsoleted MONDO:0014978** ("obsolete
preimplantation embryonic lethality 2"), migrated its salvageable metadata into the new term, and
updated the obsolete stanza with `replaced_by: MONDO:1010200`, an issue-9855 `IAO:0000233`, and a
`comment`. This claude/opus-4.7 attempt produced a high-quality, well-researched new stanza
(MONDO:7770012) but, like every attempt in this case, **did not discover the obsoleted predecessor**
and therefore did not perform the obsolete→new-term reconciliation that is the heart of the gold
solution. F1=0.333 under-represents the quality of the stanza in isolation but correctly reflects
that a whole half of the gold change (the MONDO:0014978 update plus metadata salvage) is missing.

## Strengths

- **Correct biology and identifiers.** Genus/parent `MONDO:0014769` is exactly as requested and as
  in gold. PADI6 resolved to the correct `http://identifiers.org/hgnc/20449` (HGNC:20449), and the
  agent documents verifying it against the HGNC REST API. OMIM:617234, MEDGEN:934626 and
  UMLS:C4310659 were cross-checked via MedGen rather than guessed.
- **Pattern-conformant logical definition.** The `intersection_of: MONDO:0014769` +
  `intersection_of: has_material_basis_in_germline_mutation_in .../hgnc/20449` axioms match the
  `disease_series_by_gene` DOSDP pattern and the gold. Genus/differentia mirror the text definition.
- **Sound primary-label decision.** Choosing the short OMIM-aligned label `oocyte/zygote/embryo
  maturation arrest 16` over the long ClinGen request string, and recording the ClinGen long form
  as an EXACT synonym with the `OMO:0002001` community-preferred-label qualifier pointing at
  ClinGen, is exactly what the gold did (same synonym, same qualifier URI). This is a non-obvious,
  correct call and well justified in the PR comment.
- **Strong evidential discipline.** PMIDs 27545678 (Xu et al.) and 29693651 (Qian et al.) are the
  correct primary and phenotype-expansion references and match the gold's citations; the agent
  reports actually fetching PMC5010645/PMC6018785.
- **Honest, verifiable methodology.** The checklist, ID-clash check (MONDO:7770012 vs prior 777
  range), and the explicit note that `make NORM`/`robot convert` were unavailable (validated via
  owltools round-trip instead) are transparent and accurate.

## Issues

- **Missed the core requirement (obsolete-term reconciliation).** The agent explicitly *found*
  MONDO:0014978 and OMIM:617234's `obsoleteEquivalent` link (see PR comment and checklist), but
  decided to leave MONDO:0014978 untouched. The gold did the opposite: it obsoletion-with-exact-
  replacement, adding `replaced_by: MONDO:1010200`, `comment: Term replaced by ... based on user
  request.`, and `property_value: IAO:0000233 ".../issues/9855"` to MONDO:0014978, and stripping
  its now-duplicate logical axioms/synonyms/xref. None of this is present. This is the single
  largest substantive gap and the dominant driver of the missing recall.
- **Metadata not salvaged from the predecessor (under-editing).** The gold preserved the legacy
  synonym `PADI6 preimplantation embryonic lethality` (with `MONDO:design_pattern,
  MONDO:patterns/disease_series_by_gene` provenance) and migrated the MalaCards
  `property_value: curated_content_resource "...oocyte_zygote_embryo_maturation_arrest_16" ...`
  onto the new term. This attempt has neither; the MalaCards curated-content resource is silently
  lost.
- **Synonym scoping differs from gold (defensible).** The agent demotes `preimplantation embryonic
  lethality 2` / `PREMBL2` to RELATED on the argument that they are obsolete OMIM nomenclature; the
  gold keeps `preimplantation embryonic lethality type 2` EXACT and `PREMBL2` EXACT ABBREVIATION.
  Both are defensible curatorial judgments; the gold's is more conservative (these are still valid
  alternate names for the same OMIM entry).
- **Minor scope additions (over-editing, low risk).** `subset: omim`, the `early embryonic arrest`
  synonym, the extra MEDGEN/UMLS xrefs, and the standalone `relationship:
  has_material_basis_in_germline_mutation_in` line (redundant with the `intersection_of`
  equivalence the DOSDP pattern already implies) are all reasonable and common in MONDO but go
  beyond the gold's minimal stanza, lowering precision without introducing errors.
- **Creator provenance differs (cosmetic).** Uses `dc:creator doi:10.1186/s13326-024-00320-3`
  (the agent-framework paper) where gold uses the curator ORCID; metadiff-normalized and not a
  quality concern, but not a real curator attribution.

Net: a technically excellent single-term build that is, on its own, mergeable, but it solves only
the "create the term" half of the issue and entirely misses the obsolete-predecessor cleanup that
made this case `medium` rather than `easy`. F1=0.333 modestly under-represents stanza quality but
fairly represents overall task completeness.
