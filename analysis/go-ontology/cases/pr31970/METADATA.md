---
repo: geneontology/go-ontology
issue_number: 31962
pr_number: 31970
issue_title: "Missing EC/RHEA xrefs to add to oxidoreductase activity GO terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 12
    deletions: 3
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - enzymes
  - EC-xref
  - RHEA-xref
  - oxidoreductase
  - xref-addition
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Batch addition of missing enzyme cross-references requiring knowledge of match semantics (exactMatch vs broadMatch vs narrowMatch)
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #31962 identified four oxidoreductase activity GO terms that were missing their EC and/or RHEA cross-references. These mappings are critical for interoperability between GO and enzyme databases and for automated reaction-based reasoning.

## Changes Made

In `src/ontology/go-edit.obo`, cross-references were added to 4 terms:
- GO:0036441 (2-dehydropantolactone reductase activity): Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`
- GO:0070675 (hypoxanthine oxidase activity): Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}` and `xref: RHEA:68012 {source="skos:broadMatch"}`
- Two additional oxidoreductase terms received similar xref additions

The match semantics (`exactMatch` vs `broadMatch`) were chosen based on whether the GO term scope matches the EC entry exactly or represents a subset/superset.

## Resolution

Merged same-day by the author. Adding EC/RHEA cross-references is medium difficulty because it requires biochemical knowledge to determine the correct match type (exact, broad, or narrow) and to verify that the reaction described by the GO term definition actually corresponds to the external database entry.
