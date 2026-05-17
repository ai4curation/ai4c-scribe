---
repo: obophenotype/cell-ontology
issue_number: 3353
pr_number: 3354
issue_title: "[Text def] Create human specific term for chandelier Pvalb GABAergic neuron"
issue_created_at: "2025-09-29"
issue_closed_at: "2025-10-01"
pr_author: RiveraAndrea83
pr_merged_at: "2025-10-01"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 23
    deletions: 4
  - path: src/ontology/components/clm-cl.owl
    additions: 2
    deletions: 17
scoping: mostly_scoped
scoping_notes: >-
  Primary change is the new human-specific term, but also includes cleanup of the
  clm-cl.owl component file.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - neuron
  - chandelier-cell
  - parvalbumin
  - GABAergic
  - human-specific
  - taxon-specific
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Species-specific neuron term requiring understanding of taxon-specific classification patterns and GABAergic interneuron subtypes
case_quality: poor
case_quality_reason: placeholder_id_and_provenance_metadiff_artifact_plus_unstated_gold_side_edits
companion_prs: []
scoring_caveat: >-
  Metadiff F1 is ~0 for every attempt by construction, not because the agents
  failed. (1) The issue body is empty (template headers only); the entire task
  had to be inferred from the title. (2) The gold uses the canonical ID
  CL_4072046 while the agent config MANDATES placeholder CL_99xxxxx IDs for
  new terms, so the new-term ID can never match. (3) The gold's metadiff-blind
  provenance fields (terms:creator "GitHub Copilot", terms:date) and the
  gold PR's unstated parent-generalization side-edits (relabel CL_4023036
  dropping "cortical", reparent CL_4023018->CL_4023069, +develops_from
  UBERON_0004024, move NS-Forest marker comment + CLM_1000063 to the new
  term, plus a clm-cl.owl component cleanup) further crater recall. Judge
  attempts against the issue's actual ask (create a human-specific chandelier
  Pvalb GABAergic neuron term) and against the accepted canonical gold term
  CL_4072046 (subclass of CL_4023036 + RO_0002162 some NCBITaxon_9606), NOT
  the line-level metadiff.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Allen Brain Cell Atlas and other human brain atlases distinguish human-specific subtypes of GABAergic interneurons. Chandelier cells are a morphologically distinct type of parvalbumin-positive (Pvalb+) GABAergic interneuron that forms characteristic axo-axonic synapses. A human-specific term was needed to support human brain cell-type annotation.

## Changes Made

Added a new human-specific term for chandelier Pvalb GABAergic interneuron to `cl-edit.owl` with 23 lines added and 4 modified. The term includes appropriate parentage under the species-neutral chandelier cell, a taxon constraint for Homo sapiens, and molecular marker annotations. Also cleaned up the `clm-cl.owl` component file (removing 17 lines, adding 2).

## Resolution

Medium difficulty because creating species-specific neuron subtypes requires understanding the CL pattern for taxon-specific terms, including: proper parentage under the species-neutral type, correct taxon constraint assertions, and appropriate marker annotations based on transcriptomic evidence. The component file changes add additional complexity.

## Curation Note (data quality)

`quality_flagged_by: claude-opus-4.7` · `quality_flagged_at: 2026-05-16`

This is a **poor evaluation case**: the line-level metadiff score (best F1 = 0.034,
all others 0.000) does **not** reflect agent quality. Findings:

1. **Empty issue body.** Issue #3353 contains only the template headers
   (`**CL term**` / `**Suggested revision of textual definition**`) — no content.
   Every agent had to infer the entire task from the title alone, and all seven
   did so correctly ("create a human-specific chandelier Pvalb GABAergic neuron
   term").

2. **Placeholder-vs-canonical CL ID artifact (new_term).** The `cl-agent-config`
   CLAUDE.md explicitly mandates *"New term IDs MUST start with CL_99xxxxx"*.
   Agents correctly used `CL_9900000`/`CL_9900001`; the gold uses the minted
   canonical `CL_4072046`. The new-term ID can therefore never line-match the
   gold, forcing F1≈0 for an otherwise-correct term.

3. **Metadiff-blind provenance.** The config also instructs `terms:creator
   "GitHub Copilot"` and a `terms:date` timestamp for new terms; these are
   normalized/ignored or mismatched by OBO metadiff, adding further unavoidable
   line divergence.

4. **Gold has large unstated side-edits.** Beyond creating the new term, the
   gold PR generalized the parent `CL_4023036` (relabel — dropped "cortical";
   generalized the text definition; reparented `CL_4023018`→`CL_4023069`; added
   `develops from UBERON_0004024`), moved the NS-Forest marker comment +
   `RO_0015004 some CLM_1000063` and the ILX xref onto the new term, and cleaned
   up the `clm-cl.owl` component file. None of this was requested in the empty
   issue and could only be discovered by mining the source term's embedded
   marker comment — so well-scoped agents are penalized for *not* doing
   undocumented work.

**Substantive assessment vs the accepted canonical gold (`CL_4072046`, current
master: subclass of `CL_4023036` + `RO_0002162 some NCBITaxon_9606` +
`RO_0015004 some CLM_1000063`):** all seven attempts produced the correct core
modeling (human-specific subclass of `CL_4023036` with a Homo sapiens taxon
restriction). Best attempts: **pr178 (claude-opus-4.7)** — strongest
methodology, conventional naming research, conservative scope; and **pr283 /
pr225 (claude-sonnet-4.5)** — clean, minimal, no parent over-edit. **pr80
(gpt-5.4/codex)** over-edited the parent definition (partial scope creep).
**pr62 / pr43 / pr23 (gpt-5.5)** added a non-idiomatic second parent
`CL_4072029`. All are `partial_success`, not failures; F1 grossly
under-represents quality across the board. Single-PR resolution — no companion
PRs.
