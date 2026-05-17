---
repo: obophenotype/cell-ontology
issue_number: 3460
pr_number: 3508
issue_title: "NTR - Prehypertrophic chondrocyte (preHTCs)"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-12-15"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 10
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - chondrocyte
  - prehypertrophic
  - growth-plate
  - cartilage
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for prehypertrophic chondrocyte stage in the chondrocyte maturation sequence within the growth plate
case_quality: poor
case_quality_reason: placeholder_id_artifact_and_inverted_gold_relation
companion_prs: []
scoring_caveat: "Single gold PR #3508 fully resolves the issue (no companion PRs), but metadiff is misleading for two reasons: (1) the gold introduced the term under temporary ID CL_9900000, which the ODK release process renamed to canonical CL:0020022 — agents that pick any other valid temp ID (e.g. CL_9900001) or the eventual canonical ID score F1=0 on an arbitrary, curatorially-immaterial ID-number convention; (2) the gold encodes SubClassOf(RO:0002207 some CL_0000743) = 'prehypertrophic chondrocyte directly develops FROM hypertrophic chondrocyte', which is the biological inverse of the issue's explicit request 'develops directly into hypertrophic chondrocyte'. Agents using RO:0002203 (develops into) or RO:0002210 (directly develops into) are biologically more correct yet are penalized by metadiff. Also: the agent CLAUDE.md mandates terms:date/terms:creator/IAO:0000233 axioms that the gold omitted, depressing precision for compliant agents. Judge attempts on substance against the issue, not the metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A new term was requested for the prehypertrophic chondrocyte (preHTC), a distinct stage in the chondrocyte maturation sequence within the growth plate. Prehypertrophic chondrocytes are located between the proliferative zone and the hypertrophic zone and are characterized by exit from the cell cycle and the onset of Indian hedgehog (Ihh) expression. This term complements the existing hypertrophic chondrocyte (CL:0000743) and the newly added terms for the chondrocyte lineage.

## Changes Made

Added 10 new lines to `cl-edit.owl` defining the prehypertrophic chondrocyte with class declaration, label, textual definition referencing the growth plate zonal organization, subClassOf axiom under chondrocyte, and logical axioms capturing the cell's anatomical location and developmental stage markers.

## Resolution

Approved on first review after 7 commits. Medium difficulty because correctly positioning this cell type requires understanding the spatial and temporal sequence of chondrocyte maturation in endochondral ossification: resting -> proliferative -> prehypertrophic -> hypertrophic.

## Curation Note (data quality)

**Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16.** This is a single-PR resolution (gold PR #3508, no companion PRs), so it is *not* a partial-gold case. However, the metadiff F1/precision/recall is a poor proxy for agent quality here for three reasons:

1. **Placeholder-vs-canonical CL ID artifact.** The gold PR introduced the term under the temporary ID `CL_9900000` (from `idrange:81`, the NTR range). The ODK release pipeline subsequently renamed it to the canonical `CL:0020022`, which is what OLS and current `cl-edit.owl` carry today (with the exact gold definition, contributor, synonym, and axioms). The choice of temp-ID *number* is curatorially immaterial — it is overwritten at release. Yet agents that selected a different valid temp ID (`CL_9900001`: attempts pr212, pr101) or the eventual canonical ID (`CL_0020022`: attempt pr30) score F1=0.000 across the board, even when the ontology content is otherwise correct. The metadiff is keyed entirely to the gold's arbitrary `CL_9900000`.

2. **Biologically inverted gold relation.** The gold (and the released ontology) asserts `SubClassOf(CL_9900000 ObjectSomeValuesFrom(RO:0002207 CL_0000743))`. `RO:0002207` = "directly develops from", so this reads "prehypertrophic chondrocyte *directly develops from* hypertrophic chondrocyte" — the biological inverse of the issue's explicit request, "develops directly into 'hypertrophic chondrocyte'" (preHTC matures *into* the hypertrophic cell, not from it). Agents that used `RO:0002203` ("develops into": pr181, pr67, pr47, pr212) or `RO:0002210` ("directly develops into": pr30) are biologically *more* faithful to the issue, yet the metadiff penalizes them for not matching the likely-erroneous gold axiom. The curators reviewed and shipped the gold axiom, but it is very probably a curation error.

3. **Config-mandated metadata absent from gold.** The agent `CLAUDE.md` requires `terms:date`, `terms:creator "GitHub Copilot"`, and an `IAO:0000233` term-tracker axiom on new terms. The gold PR includes none of these. Compliant agents are therefore penalized on precision for following their instructions.

**Recommendation for downstream scoring:** down-weight or exclude metadiff for this case. On substance, attempt pr181 (claude-opus-4.7) is a clear success, pr212 (claude-sonnet-4.5) is substantively near-correct (only an arbitrary temp-ID difference), and pr30 (gpt-5.5/codex) is ontologically the most biologically accurate despite an ID-minting instruction violation — all of which the F1 numbers (0.625 / 0.000 / 0.000) badly under-represent.
