---
repo: obophenotype/cell-ontology
issue_number: 3196
pr_number: 3248
issue_title: "[NTR] Unclassified Fallopian Tube Progenitor (UCFP)"
issue_created_at: "2025-07-15"
issue_closed_at: "2025-08-13"
pr_author: Caroline-99
pr_merged_at: "2025-08-13"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 16
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: reproductive-biology
tags:
  - NTR
  - progenitor-cell
  - fallopian-tube
  - reproductive-tract
  - dual-feature
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term request from external community requiring novel cell type placement with dual-lineage progenitor characteristics
case_quality: poor
case_quality_reason: placeholder_vs_canonical_id_and_gold_deviates_from_issue_spec
companion_prs: []
scoring_caveat: "All 6 attempts score F1≈0 (best 0.231) due to a placeholder-vs-canonical-ID artifact, NOT agent failure. The cl-agent-config CLAUDE.md MANDATES new-term IDs in the CL_99xxxxx range, so agents correctly used CL_9900000/CL_9900001; but the gold PR #3248 used the live-assigned canonical ID CL_4052070, so OBO metadiff cannot align ANY annotation line and scores 0 by construction. Codex #13 scored 0.231 only because it read CL_4052070 from the live CL browser. Compounding factors: (1) gold's part_of filler UBERON_8600124 (fallopian tube epithelium) was a brand-new UBERON ID minted concurrently and absent from the eval base snapshot, not resolvable from the label alone; (2) gold OMITTED the two 'develops into' axioms the issue's reviewed logical definition explicitly requested, while most agents correctly INCLUDED them; (3) gold used hasNarrowSynonym for the NCSE2 synonyms where the issue text said 'related synonym'. Judge attempts against the issue #3196 reviewed spec (2025-08-12 comment), not the metadiff. Substantively, 5 of 6 attempts are successes; haiku (#87) is a partial_success (ID-range instruction violation); both gpt-5.5/opencode attempts (#58/#39) have a backwards develops_from (RO_0002202 vs RO_0002203) relation defect."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term request was submitted by an external contributor for the "unclassified fallopian tube progenitor" (UCFP), a dual-feature progenitor cell found in the fallopian tube that can give rise to both epithelial and stromal lineages. This cell type was identified through single-cell transcriptomic studies of the human fallopian tube.

## Changes Made

Added 16 lines and modified 2 lines in `cl-edit.owl`. The new term includes a class declaration, label, textual definition citing relevant single-cell RNA-seq publications, synonyms, parentage under an appropriate progenitor cell class, and anatomical location assertions linking to fallopian tube structures in UBERON.

## Resolution

Approved on first review. Medium difficulty because placing a novel dual-lineage progenitor cell requires understanding progenitor cell classification patterns, choosing appropriate parent classes when the cell has multi-potent differentiation potential, and correctly asserting anatomical location relationships.

## Curation Note (data quality)

Flagged `case_quality: poor` (claude-opus-4.7, 2026-05-16). This case's metadiff
scores are systematically misleading and should be excluded or heavily
down-weighted in any aggregate quality metric.

**Primary artifact — placeholder vs canonical ID.** The `cl-agent-config`
CLAUDE.md explicitly *mandates* that new-term IDs be drawn from the
`CL_99xxxxx` range ("New term IDs MUST start with CL_99xxxxx"). Agents that
followed this instruction used `CL_9900000`/`CL_9900001`. The gold PR #3248,
however, used `CL_4052070` — an ID issued by the live CL ID-assignment system
that is not present in the eval base snapshot and is not derivable by any
agent. Because OBO metadiff keys on subject IRIs, *every* annotation line of a
correct term fails to align, forcing F1=0 by construction. Only codex #13
(F1=0.231) scored nonzero, solely because it read `CL_4052070` from the live
CL browser — not because its content was uniquely better.

**Secondary factors that further suppress F1 / penalize correct agents.**
- Gold's `part of` filler is `UBERON_8600124` ("fallopian tube epithelium"),
  a high-numbered UBERON ID minted essentially concurrently with this PR
  (the reasoned PR diff shows `UBERON_8600124` itself "Added Class"). It is
  not resolvable from the label "fallopian tube epithelium" alone; reasonable
  agents chose `UBERON_0003889` (fallopian tube) or `UBERON_0007589` (oviduct
  epithelium). The two gpt-5.5/opencode runs (#58, #39) *did* land on
  `UBERON_8600124` correctly.
- The issue's reviewed (2025-08-12, approved by @biobenkj) logical definition
  explicitly lists `'develops into' some 'fallopian tube secretory epithelial
  cell'` and `'develops into' some 'fallopian tube multiciliated epithelial
  cell'`. The gold PR **omitted both** develops-into axioms. Most agents
  correctly **included** them — i.e. they followed the curator-reviewed spec
  more faithfully than the merged gold did, yet are scored down for it.
- The issue text says the NCSE2 synonyms are "related synonym"; gold encoded
  them as `hasNarrowSynonym`. Agents that used related synonyms followed the
  issue.

**Reviewer judgement (against issue #3196, not metadiff):** 4 of 6 attempts
are substantive successes (codex #13, sonnet #216, opus #172, opencode #58
and #39 — though #58/#39 share a backwards `develops_from`/`RO_0002202`
relation defect that should have been `RO_0002203`). haiku #87 is a
partial_success: content is sound but it violated the mandatory `CL_99xxxxx`
ID-range instruction by using `CL_4072103`. opus #172 is the strongest,
best-documented attempt overall. No companion PRs — issue #3196 was fully
resolved by the single PR #3248.
