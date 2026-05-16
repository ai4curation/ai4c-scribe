# PR #32009 — Obsolete GO:0045550 geranylgeranyl reductase activity

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31963](https://github.com/geneontology/go-ontology/issues/31963)
- **PR**: [#32009](https://github.com/geneontology/go-ontology/pull/32009)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-04-28
- **task_type**: obsoletion
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #31963 requested obsoletion of GO:0045550 "geranylgeranyl reductase activity" because it duplicates GO:0102067 "geranylgeranyl diphosphate reductase activity". The terms describe the same enzymatic reaction but GO:0102067 has the more precise name matching the EC classification.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0045550 was obsoleted with:
- `is_obsolete: true`
- `replaced_by: GO:0102067` (direct replacement for automatic annotation migration)
- Removal of logical axioms

This is the standard pattern for enzyme term consolidation where one term subsumes another.

## Resolution

Merged directly. The obsoletion was straightforward because a clear 1:1 replacement existed. Per @raymond91125's analysis in the issue, GO:0045550 and GO:0102067 describe the same reaction, and the latter has the correctly precise name. Annotations can be automatically migrated using the `replaced_by` tag.
