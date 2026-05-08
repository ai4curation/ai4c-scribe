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
---

## Context

The HuBMAP consortium needed myenteric neuron cell type terms for annotating gut tissue datasets. Issue #3584 (linked from the broader HuBMAP term request #3471) requested 14 new myenteric neuron terms covering the major functional subtypes found in the myenteric plexus of the gastrointestinal tract, including excitatory motor neurons, inhibitory motor neurons, interneurons, and intrinsic primary afferent neurons (IPANs).

## Changes Made

Added 188 new lines to `cl-edit.owl` defining 14 myenteric neuron terms. Each term follows the standard CL compositional pattern with class declaration, label, synonyms, textual definition, parentage under enteric neuron, part_of relationship to UBERON myenteric plexus, and functional axioms capturing neurotransmitter identity (cholinergic vs nitrergic) and functional role (motor, sensory, interneuron). The hierarchy was designed to reflect the functional classification of myenteric neurons.

## Resolution

Approved on first review after 12 commits of iterative development. Hard difficulty because designing a coherent hierarchy for 14 related neuron types required understanding enteric nervous system organization, correctly classifying each subtype by function and neurotransmitter phenotype, and ensuring the terms are mutually consistent and properly differentiated from each other.
