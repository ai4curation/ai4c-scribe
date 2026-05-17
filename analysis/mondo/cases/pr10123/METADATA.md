---
repo: monarch-initiative/mondo
issue_number: 9877
pr_number: 10123
issue_title: "GPR161-related medulloblastoma predisposition"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-01-14"
pr_author: katiermullen
pr_merged_at: "2026-04-06"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 10
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term with no unrelated changes.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cancer-predisposition
tags:
  - gene-disease
  - GPR161
  - medulloblastoma
  - cancer-predisposition
  - ClinGen
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New cancer predisposition term requiring correct classification under both cancer and predisposition hierarchies
case_quality: poor
case_quality_reason: gold_diverges_from_prescribed_design_pattern
companion_prs: []
scoring_caveat: "Gold PR #10123 modeled the term with a deliberately minimal classification (is_a: MONDO:0015356 hereditary neoplastic syndrome, asserted germline-mutation relationship only, NO logical/equivalence axiom, NO predisposes_towards). The documented susceptibility_by_gene DOSDP pattern — which the agent config directs agents to apply — prescribes parent MONDO:0020573 inherited disease susceptibility plus a full intersection_of equivalence axiom and predisposes_towards. All 9 attempts followed the pattern faithfully and are ontologically richer/pattern-compliant, so metadiff F1 is uniformly compressed (0.32-0.55) by construction even for correct work. Judge attempts against the issue's explicit asks (correct gene HGNC:23694, ClinGen-preferred label, ClinGen attribution, def from issue text) and the design pattern, not line-match to the minimal gold. F1 under-represents quality for the pattern-faithful attempts."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A new term request was filed for GPR161-related medulloblastoma predisposition. GPR161 is a G protein-coupled receptor involved in the Hedgehog signaling pathway, and germline mutations predispose to medulloblastoma, a common pediatric brain tumor. This term captures the genetic predisposition rather than the cancer itself, requiring careful placement in the ontology hierarchy.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 10 lines. The term includes a definition, gene-disease logical axioms linking to GPR161, and classification under the cancer predisposition hierarchy. The compact size reflects a well-structured new term following established patterns.

## Resolution

Medium difficulty because cancer predisposition terms require dual classification: they must be linked to both the cancer type (medulloblastoma) and the predisposition concept, while also encoding the causal gene relationship. An agent needs to understand the distinction between a cancer and a predisposition to cancer and apply the correct Mondo pattern.

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_diverges_from_prescribed_design_pattern`) on 2026-05-15 by claude-opus-4.7.

This is a clean single-PR resolution (gold PR #10123, approved first time, closes #9877; no companion PRs — Step 3a does not apply). The poor-case signature is the Step 3b "gold caps well-scoped agents" variety:

- **Gold model is deliberately minimal and non-pattern.** Human PR #10123 added only:
  `is_a: MONDO:0015356 ! hereditary neoplastic syndrome`,
  `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694`,
  a single ClinGen EXACT synonym, the issue's near-verbatim definition, `dc:creator`
  (ORCID `https://orcid.org/0000-0002-5002-8648`), and the `IAO:0000233` tracker link.
  It has **no logical/equivalence (`intersection_of`) axiom**, **no `predisposes_towards`**,
  and does **not** use `MONDO:0020573 inherited disease susceptibility` as parent.
- **The prescribed design pattern says the opposite.** `src/patterns/dosdp-patterns/susceptibility_by_gene.yaml`
  defines genus `MONDO:0020573 inherited disease susceptibility`, an `equivalentTo`/`intersection_of`
  axiom (`'inherited disease susceptibility' and ('has material basis in germline mutation in'
  some GENE) and ('predisposes towards' some DISEASE)`), and a pattern name/synonym. The
  agent config (`ai4curation/mondo-agent-config@v3`) directs agents to consult and apply
  design patterns.
- **Consequence:** all 9 attempts applied the pattern faithfully and are therefore
  *ontologically richer and pattern-compliant*, yet metadiff F1 is uniformly compressed
  (0.320–0.545) because the pattern axioms + parent are precisely the lines gold omitted.
  F1 **under-represents** quality for the pattern-faithful attempts (especially #78/#59
  gpt-5.5, #389 opus-4.7, #39/#250 which also recovered gold's `MONDO:0015356` parent and/or
  the issue definition text).

Real, non-artifact defects observed across attempts (use these, not F1, to discriminate):
incorrect citation PMID:36961676 in #534/#492 (correct is PMID:31609649); ClinGen-preferred
label synonym with the `OMO:0002001` clingen axiom annotation dropped by #534/#492/#250/#440/#174;
wrong `dc:creator` (Mondo methods-paper DOI `doi:10.1186/s13326-024-00320-3` or a ClinGen
affiliation URL) instead of the requester ORCID in most attempts; synonym xref convention
slips (`[MONDO:design_pattern]`) and possible classification redundancy from dual `is_a` +
equivalence in #174.

Downstream scoring should down-weight or exclude this case's metadiff F1 and judge against the
issue's explicit asks and the design pattern.
