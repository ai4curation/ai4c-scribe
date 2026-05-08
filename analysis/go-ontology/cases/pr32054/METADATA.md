---
repo: geneontology/go-ontology
issue_number: 32044
pr_number: 32054
issue_title: "NTR: protein O-linked glycosylation via N-acetylglucosamine"
issue_created_at: "2026-05-07"
pr_author: sjm41
pr_merged_at: "2026-05-07"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 15
    deletions: 1
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward NTR for a well-defined glycosylation process, but required biochemical precision in the definition and harmonization of a sibling term's spelling
---

## Context

A new term request was filed for "protein O-linked glycosylation via N-acetylglucosamine" (GO:7770074), a biological process term representing the covalent attachment of a single GlcNAc residue to serine or threonine via a beta-glycosidic bond. This modification is distinct from the GalNAc-initiated mucin-type O-glycosylation and plays key roles in cellular signaling. The request originated from earlier issues #29770 and #23575 where the term was discussed but never created.

## Changes Made

The PR added GO:7770074 as a child of `GO:0006493 protein O-linked glycosylation` with a precise definition referencing the beta-glycosidic bond linkage and PMID citations. The definition specifies that this is a monosaccharide addition (not extended chain), distinguishing it from mucin-type glycosylation. As part of the same commit, the sibling term for GalNAc-initiated glycosylation had its spelling harmonized to use consistent nomenclature across the O-linked glycosylation branch.

## Resolution

The PR was merged the same day it was opened, with a single commit modifying `go-edit.obo`. The task required medium difficulty because the definition needed to precisely capture the biochemistry (beta-glycosidic bond, monosaccharide vs. chain extension) and the curator also identified an inconsistency in the sibling term that needed concurrent correction.
