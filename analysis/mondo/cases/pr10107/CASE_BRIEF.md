# PR #10107 — [Obsolete] OMIM merges

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9795](https://github.com/monarch-initiative/mondo/issues/9795)
- **PR**: [#10107](https://github.com/monarch-initiative/mondo/pull/10107)
- **Author**: @MeeSiing
- **Merged**: 2026-04-02
- **task_type**: obsoletion
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #9795 listed multiple OMIM merges needed in Mondo. This PR merged "cramps, familial adolescent" (MONDO:0009027) into MONDO:0007402 (creatine phosphokinase, elevated serum), following OMIM:218050's merge into OMIM:123320. The OMIM merge reflects that familial adolescent cramps and elevated serum CPK represent the same underlying condition.

## Changes Made

The PR merged MONDO:0009027 into MONDO:0007402 in a single clean commit. The 11 additions and 12 deletions represent the standard merge pattern: obsoleting the source term with replaced_by annotation, transferring synonyms and cross-references to the target term, and removing the source term's classification axioms. The near-equal additions and deletions indicate a straightforward metadata transfer.

## Resolution

Moderate difficulty because term merges always require judgment about which metadata to preserve and how to annotate the merge. However, this specific case was clean because the OMIM upstream merge provides clear justification and the terms had minimal conflicting annotations. An agent could handle this given clear merge SOPs and the ability to identify the source/target terms correctly.
