---
repo: obophenotype/cell-ontology
issue_number: 3584
pr_number: 3585
issue_title: "Add myenteric neurons for HubMap"
issue_created_at: "2026-03-10"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-17"
pr_num_commits: 12
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 188
    deletions: 0
scoping: loosely_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - NTR
  - myenteric-neuron
  - enteric-nervous-system
  - HuBMAP
  - gut
  - batch-addition
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large batch of 14 myenteric neuron terms requiring coordinated hierarchy design for enteric nervous system cell types
case_quality: poor
case_quality_reason: gold_renegotiated_plus_placeholder_vs_canonical_cl_id_artifact
companion_prs: []
scoring_caveat: "Gold #3585 is the single complete human resolution but its merged state was renegotiated in PR review (curators had copilot remove unsatisfiable SubClassOf(CL_9900009 CL_0008015) and add SubClassOf(CL_9900001 CL_0007011)) and carries an out-of-scope edit to pre-existing CL_4033160 plus an unrequested BFO_0000050 some UBERON_0002005 on the generic Dogiel II class — none specified in issue #3584. Separately, 2 of 3 attempts (pr195 opus, pr214 sonnet) are ontologically equivalent to gold but numbered terms CL_9900000–CL_9900013 vs gold's CL_9900001–CL_9900014; both ID schemes are valid within idrange:81 (9900000–9999999), so the uniform off-by-one offset collapses their whole-file metadiff F1 to ~0.26 with zero substantive defect. Judge attempts against the issue spec, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The HuBMAP consortium needed myenteric neuron cell type terms for annotating gut tissue datasets. Issue #3584 (linked from the broader HuBMAP term request #3471) requested 14 new myenteric neuron terms covering the major functional subtypes found in the myenteric plexus of the gastrointestinal tract, including excitatory motor neurons, inhibitory motor neurons, interneurons, and intrinsic primary afferent neurons (IPANs).

## Changes Made

Added 188 new lines to `cl-edit.owl` defining 14 myenteric neuron terms. Each term follows the standard CL compositional pattern with class declaration, label, synonyms, textual definition, parentage under enteric neuron, part_of relationship to UBERON myenteric plexus, and functional axioms capturing neurotransmitter identity (cholinergic vs nitrergic) and functional role (motor, sensory, interneuron). The hierarchy was designed to reflect the functional classification of myenteric neurons.

## Resolution

Approved on first review after 12 commits of iterative development. Hard difficulty because designing a coherent hierarchy for 14 related neuron types required understanding enteric nervous system organization, correctly classifying each subtype by function and neurotransmitter phenotype, and ensuring the terms are mutually consistent and properly differentiated from each other.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16. The gold PR #3585 is the single complete human resolution (no companion PRs — search of `3584`/`myenteric` returns only #3585), so this is **not** a partial-gold case. However the metadiff against #3585 is misleading for two independent reasons:

1. **Gold renegotiated in PR review.** The merged gold state is not the agent-predictable issue spec. During review, curators (`dosumis`, `RiveraAndrea83`) had copilot (a) remove `SubClassOf(CL_9900009 obo:CL_0008015)` because it forced the spiny Dogiel I term to `SubClassOf owl:Nothing` (an unsatisfiability surfaced by the taxon-constraint reasoning bot), and (b) add `SubClassOf(CL_9900001 obo:CL_0007011)`. The gold also carries an **out-of-scope edit to pre-existing term `CL_4033160`** (`SubClassOf(CL_4033160 RO_0002215 some GO_0014055)`) that issue #3584 never requested, and an **unrequested `BFO_0000050 some UBERON_0002005`** (part of enteric nervous system) on the generic "Dogiel type II neuron" class, whose issue spec (Term 14) explicitly says "UBERON Terms: None". `dosumis` approved with "Good for now. Let's aim for a second round with more refs and slightly broadened terms," signalling the merged state is an interim, negotiated artifact. All three attempts faithfully follow the original issue text (including the unsatisfiability-prone `CL_0008015` axiom) and cannot be expected to reproduce these review-only / out-of-scope changes; this caps achievable F1 below 1.0 for every well-scoped attempt.

2. **Placeholder-vs-canonical CL ID artifact.** The 14 new terms use temporary IDs from `idrange:81` (CL_9900000–CL_9999999). Gold assigned CL_9900001–CL_9900014 (prerequisite generic Dogiel type II = CL_9900001). Attempt pr143 (haiku) matched that mapping and scored F1=0.711. Attempts pr195 (opus) and pr214 (sonnet) numbered CL_9900000–CL_9900013 (prerequisite = CL_9900000). Both schemes are equally valid — the issue pins no numeric IDs and both lie inside the allocated range — but the uniform off-by-one shift makes every axiom line mismatch under whole-file metadiff, collapsing pr195/pr214 to F1≈0.26 despite being ontologically equivalent to gold for all 14 terms. Their low scores are a scoring artifact, **not** a quality signal.

Downstream scoring/aggregation should down-weight or exclude this case, and the attempts should be judged against the issue #3584 specification rather than the line-level metadiff vs #3585. All three attempts are graded `success` on substance in the reviews.
