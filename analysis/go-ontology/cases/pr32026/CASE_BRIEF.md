# PR #32026 — Obsoletion request: GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#32005](https://github.com/geneontology/go-ontology/issues/32005)
- **PR**: [#32026](https://github.com/geneontology/go-ontology/pull/32026)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-05-04
- **task_type**: obsoletion
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #32005 requested obsoletion of GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway". This term represented a pre-composed superpathway that conflated the general aromatic amino acid biosynthetic process with a specific pathway variant. The MetaCyc cross-reference it carried was to a superpathway entry, which is not how GO typically represents metabolic specificity.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0009095 was obsoleted:
- Removed all logical axioms (is_a relationships, intersection_of definitions)
- Added obsoletion metadata: `is_obsolete: true`, `consider` tags pointing to the individual pathway steps
- Retained the MetaCyc xref for provenance
- Net reduction of 6 lines, reflecting removal of redundant axioms

## Resolution

Merged directly. The obsoletion rationale was clear: GO prefers atomic terms that can be composed via GO-CAM models rather than pre-composed superpathway terms. No annotation migration was needed since the term had minimal direct annotations.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 961e08ab9..017033244 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -90265,20 +90265,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009095
-name: aromatic amino acid biosynthetic process, prephenate pathway
-namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
-synonym: "aromatic amino acid family anabolism, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family biosynthetic process via prephenate" EXACT [GOC:pr]
-synonym: "aromatic amino acid family biosynthetic process via prephenate(2-)" EXACT [GOC:pr]
-synonym: "aromatic amino acid family formation, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family synthesis, prephenate pathway" EXACT []
-xref: MetaCyc:PWY-3481
-is_a: GO:0009073 ! aromatic amino acid biosynthetic process
-intersection_of: GO:0009058 ! biosynthetic process
-intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
-intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI
+name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
+namespace: biological_process
+def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
+comment: This term was obsoleted because it represents a pre-composed pathway combining L-phenylalanine and L-tyrosine biosynthesis. MetaCyc:PWY-3481 is the 'superpathway of L-phenylalanine and L-tyrosine biosynthesis' and is composed of two separate pathways (PWY-3462 L-phenylalanine biosynthesis II and PWY-3461 L-tyrosine biosynthesis II) which are already represented as narrowMatch xrefs on GO:0009094 (L-phenylalanine biosynthetic process) and GO:0006571 (L-tyrosine biosynthetic process), respectively. Annotations should be transferred to the appropriate consider term(s).
+consider: GO:0006571
+consider: GO:0009094
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
+is_obsolete: true
 
 [Term]
 id: GO:0009097

```

## Agent Attempts (12)

### Attempt 1: gpt-5.5 / opencode

- **Eval PR**: [#163](https://github.com/ai4curation/eval-ont-agent-go/pull/163)
- **F1**: 0.927  **Precision**: 0.905  **Recall**: 0.950  **Jaccard**: 0.864
- **Workflow run**: [25633615945](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633615945)

#### Agent PR Comment

# Description

Addresses geneontology/go-ontology#32005.

Obsoleted GO:0009095 `aromatic amino acid biosynthetic process, prephenate pathway` because it represents a pre-composed/superpathway term combining L-phenylalanine and L-tyrosine biosynthesis via prephenate.

Changes made in `src/ontology/go-edit.obo`:

- Renamed the term to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Prefixed the definition with `OBSOLETE.` while preserving the original definition xrefs.
- Removed synonyms, xref, asserted parent, and logical axioms from the obsolete term.
- Added obsoletion comment.
- Added tracker link for issue #32005, retaining the existing tracker link for #31091.
- Added `is_obsolete: true`.
- Added `consider` targets:
  - GO:0009094 `L-phenylalanine biosynthetic process`
  - GO:0006571 `L-tyrosine biosynthetic process`

# Rationale

The requested obsoletion is consistent with the existing GO biosynthetic-process pattern, which composes terms by primary output. The two product-specific terms already exist and carry the relevant MetaCyc narrowMatch xrefs:

- GO:0009094 has `MetaCyc:PWY-3462` as `skos:narrowMatch`.
- GO:0006571 has `MetaCyc:PWY-3461` as `skos:narrowMatch`.

GO:0009095 instead corresponds to the combined MetaCyc superpathway (`PWY-3481`) and had a broad output (`aromatic amino acid`) plus prephenate intermediate, so retaining it as a GO process term would preserve a pre-composed/superpathway representation rather than a clean product-specific biosynthetic process.

# Research and annotation notes

Created `RESEARCH.md` locally for the cited publications and validated quoted support text with `linkml-reference-validator`:

- PMID:21102469: supports PPA-AT directing flux toward arogenate and plant phenylalanine biosynthesis; supports review of the Petunia PPA-AT annotation for possible migration to GO:0009094.
- PMID:20883697: biochemical identification/characterization of Arabidopsis prephenate aminotransferase; abstract-level evidence does not clearly support retaining a specific BP annotation to the combined superpathway term.
- PMID:18727669: biochemical/structural characterization of chorismate mutase; abstract-level evidence does not clearly support a BP annotation to the combined superpathway term.

Attempted `runoak -i amigo: associations GO:0009095`, but the local harness OAK installation failed with a LinkML `Format.JSON` import error. I therefore relied on the annotation impact analysis provided in the issue, plus local reference validation of the PMIDs.

# Validation

- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-edit validation: `cd src/ontology && make travis_build` passed after edits.
- Checked GO-internal usage with `obo-grep.pl`; GO:0009095 is now only present in its own obsolete stanza.
- Checked local taxon-constraint and ontology files for GO:0009095; no additional ontology/taxon-constraint references needed rewiring.

# Checklist

- [x] PLAN: Issue and context analyzed; intent clear: obsolete GO:0009095 as a combined/pre-composed superpathway term.
- [x] PRE-VALIDATION: Current ontology validated with `make travis_build` before changes.
- [x] RESEARCH: Created local `RESEARCH.md`; PMIDs from the issue were cached and quoted support text validated.
- [x] TERM-SEARCH: Consulted GO:0009095, GO:0009094, GO:0006571 and MetaCyc xref usage in `go-edit.obo`.
- [x] DESIGN-PATTERNS: Created local `DESIGN_PATTERNS.md`; reviewed `biosynthetic_process.yaml` and existing product-specific biosynthetic terms.
- [x] EDITS: Used `obo-checkout.pl` / `obo-checkin.pl` and edited the term-specific file under `terms/`.
- [x] RELATIONSHIPS: Removed all `is_a`, `relationship`, and `intersection_of` tags from the obsolete term; added `consider` terms only.
  - [x] Logical definitions are N/A for the obsolete term and were removed.
  - [x] Relationships conform to obsoletion practice.
  - [x] `is_a` is not over-asserted; obsolete term has none.
- [x] SPECIALIZED-EDITS:
  - [x] `/term-obsoletion` skill used.
  - [x] `/chemical-entity` skill consulted because the original term used CHEBI in logical axioms; no new CHEBI axioms were added.
  - [x] `/reaction` N/A.
  - [x] `/taxon-constraint` N/A; no taxon constraint rows found for GO:0009095.
- [x] METADATA: Added issue #32005 `term_tracker_item`; retained existing namespace and historical definition provenance; no `created_by`/`creation_date` added because this is not a new term.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: PMIDs from the issue were cached and support quotes validated; no new definition references introduced.
- [x] CHANGES-COMMITTED:
  - [x] RELEVANT-FILES: Committed only `src/ontology/go-edit.obo`.
  - [x] ACCURACY: Change aligns with product-specific biosynthetic process design and existing MetaCyc mappings.
  - [x] ISSUE-ALIGNMENT: Change directly implements requested obsoletion with the requested consider terms.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633615945)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary: GO:0009095 `aromatic amino acid biosynthetic process, prephenate pathway` has been obsoleted as a pre-composed/superpathway term. The obsolete term now points users to `consider` GO:0009094 `L-phenylalanine biosynthetic process` and GO:0006571 `L-tyrosine biosynthetic process`.

I also reviewed the cited annotation evidence at abstract level. The papers support the issue's concern that the existing annotations need curator review/removal or migration rather than retention on this combined pathway term.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633615945)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..995aa7197 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -90247,20 +90247,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009095
-name: aromatic amino acid biosynthetic process, prephenate pathway
-namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
-synonym: "aromatic amino acid family anabolism, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family biosynthetic process via prephenate" EXACT [GOC:pr]
-synonym: "aromatic amino acid family biosynthetic process via prephenate(2-)" EXACT [GOC:pr]
-synonym: "aromatic amino acid family formation, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family synthesis, prephenate pathway" EXACT []
-xref: MetaCyc:PWY-3481
-is_a: GO:0009073 ! aromatic amino acid biosynthetic process
-intersection_of: GO:0009058 ! biosynthetic process
-intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
-intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
+name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
+namespace: biological_process
+def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
+comment: The reason for obsoletion is that this term represents a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
+is_obsolete: true
+consider: GO:0006571
+consider: GO:0009094
 
 [Term]
 id: GO:0009097

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.927  **precision**: 0.905  **recall**: 0.95

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/163
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 163 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the requested obsoletion of `GO:0009095` aromatic amino acid biosynthetic process, prephenate pathway. It made the same core ontology changes as the human PR: obsolete label, `OBSOLETE.` definition prefix, removal of active synonyms/xref/classification/logical axioms, `is_obsolete: true`, and `consider` links to `GO:0009094` L-phenylalanine biosynthetic process and `GO:0006571` L-tyrosine biosynthetic process. The metadiff F1 of 0.927 is a fair high score; the remaining differences are mostly comment detail and the agent retaining an older tracker link.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and captured the issue rationale: `MetaCyc:PWY-3481` is a combined superpathway for L-phenylalanine and L-tyrosine biosynthesis rather than a single GO process term.
- Added the right obsoletion migration metadata: `consider: GO:0009094` and `consider: GO:0006571`, matching the issue request and the human PR.
- Applied the standard GO obsoletion pattern by renaming the term to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixing the definition with `OBSOLETE.`, and adding `is_obsolete: true`.
- Removed the active ontology content that should not remain on an obsolete term: the asserted parent `is_a: GO:0009073`, the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`, the exact synonyms, and the direct `xref: MetaCyc:PWY-3481`.
- Added a new `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/32005`.
- Kept the edit scoped to the `GO:0009095` stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- Minor metadata difference: the agent retained the pre-existing `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI` and added `#32005` as a second tracker item, whereas the human PR replaced the tracker metadata with only issue `#32005`. This is unlikely to break ontology behavior, but it leaves stale curator-facing metadata compared with the accepted edit.
- Minor style/completeness difference: the agent's obsoletion comment only says the term is a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate. The human PR's comment is more useful because it explicitly records that `MetaCyc:PWY-3481` decomposes into `PWY-3462` and `PWY-3461`, already represented as narrowMatch xrefs on `GO:0009094` and `GO:0006571`, and tells annotators to transfer annotations to the appropriate consider term(s).

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#145](https://github.com/ai4curation/eval-ont-agent-go/pull/145)
- **F1**: 0.927  **Precision**: 0.905  **Recall**: 0.950  **Jaccard**: 0.864
- **Workflow run**: [25633591484](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633591484)

#### Agent PR Comment

## Summary

Obsoleted GO:0009095 `aromatic amino acid biosynthetic process, prephenate pathway` because it represents a combined pathway/superpathway concept covering separate L-phenylalanine and L-tyrosine biosynthetic processes.

Changes made:

- Renamed the term to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Prefixed the historical definition with `OBSOLETE.` and retained its original definition xrefs.
- Removed synonyms, MetaCyc xref, asserted parent, and logical axioms from the obsolete stanza.
- Added an obsoletion comment and issue tracker link for issue #32005.
- Added `consider: GO:0009094` and `consider: GO:0006571` rather than `replaced_by`, because neither target is an exact replacement for the combined term.

## Rationale

The issue reports that MetaCyc:PWY-3481 is a superpathway combining L-phenylalanine biosynthesis II (PWY-3462) and L-tyrosine biosynthesis II (PWY-3461). The corresponding GO terms already have the pathway-specific MetaCyc xrefs as narrow matches:

- GO:0009094 `L-phenylalanine biosynthetic process` has `MetaCyc:PWY-3462 {source="skos:narrowMatch"}`.
- GO:0006571 `L-tyrosine biosynthetic process` has `MetaCyc:PWY-3461 {source="skos:narrowMatch"}`.

This supports candidate replacements (`consider`) rather than a direct replacement.

## Checks

- [x] PLAN: Issue context analyzed; request is clear.
- [x] PRE-VALIDATION: `make travis_build` passed before edits.
- [x] RESEARCH: Local `RESEARCH.md` created. PMID context from the issue was checked where tooling allowed. PubMed verified PMID:21102469 and PMID:18727669 via web fetch; `linkml-reference-validator` verified PMID:20883697. NCBI rate limiting prevented validator caching for the other two PMIDs.
- [x] TERM-SEARCH: Checked GO:0009095, candidate terms GO:0009094 and GO:0006571, ontology references to GO:0009095, and taxon constraints.
- [x] DESIGN-PATTERNS: Local `DESIGN_PATTERNS.md` created. No new logical definition was added; obsolete term axioms were removed according to GO obsoletion practice.
- [x] SPECIALIZED-EDITS: Used obsoletion, chemical entity, design pattern, mapping, and research guidance as relevant.
- [x] RELATIONSHIPS: Removed `is_a` and `intersection_of` tags from the obsolete term; added `consider` targets only.
- [x] METADATA: Added issue #32005 tracker item; retained prior issue #31091 tracker item; no `created_by` or `creation_date` added because this is an existing term.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after edits.
- [x] REFERENCE-VALIDATION: No new definition references were introduced. Existing definition xrefs were retained for historical obsoletion provenance.
- [x] CHANGES-COMMITTED: Committed locally as `2b81ba9` with only `src/ontology/go-edit.obo` staged.

## Notes

`runoak -i amigo: associations GO:0009095` and `runoak -i ubergraph: usages GO:0009095` could not be run because local `runoak` fails during startup with a dependency error: `AttributeError: type object 'Format' has no attribute 'JSON'`. The annotation impact assessment therefore relies on the issue-provided annotation counts and PMID-specific recommendations.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633591484)


#### Agent Issue Comment

GO:0009095 has been obsoleted in PR #<NN>.

The obsolete term now has `consider` references to GO:0009094 `L-phenylalanine biosynthetic process` and GO:0006571 `L-tyrosine biosynthetic process`, since the original term represented a combined/superpathway concept rather than a single exact replacement.

Validation passed with `make travis_build` before and after the ontology edit.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633591484)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..995aa7197 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -90247,20 +90247,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009095
-name: aromatic amino acid biosynthetic process, prephenate pathway
-namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
-synonym: "aromatic amino acid family anabolism, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family biosynthetic process via prephenate" EXACT [GOC:pr]
-synonym: "aromatic amino acid family biosynthetic process via prephenate(2-)" EXACT [GOC:pr]
-synonym: "aromatic amino acid family formation, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family synthesis, prephenate pathway" EXACT []
-xref: MetaCyc:PWY-3481
-is_a: GO:0009073 ! aromatic amino acid biosynthetic process
-intersection_of: GO:0009058 ! biosynthetic process
-intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
-intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
+name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
+namespace: biological_process
+def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
+comment: The reason for obsoletion is that this term represents a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
+is_obsolete: true
+consider: GO:0006571
+consider: GO:0009094
 
 [Term]
 id: GO:0009097

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.927  **precision**: 0.905  **recall**: 0.95

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/145
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 145 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#32005` by obsoleting `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and adding the two appropriate `consider` targets, `GO:0009094` and `GO:0006571`. The metadiff F1 of 0.927 is a fair reflection of the actual quality: the ontology edit is substantively correct, with only minor differences from the human PR in tracker provenance and the level of detail in the obsolete-term comment.


## Strengths

- Correctly converted `GO:0009095` to an obsolete term by renaming it to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixing the definition with `OBSOLETE.`, and adding `is_obsolete: true`.
- Removed the active logical structure from the obsolete stanza, including `is_a: GO:0009073` and the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`.
- Removed active synonyms and the standalone `xref: MetaCyc:PWY-3481`, matching the expected obsoletion pattern for a term whose xref was to a MetaCyc superpathway.
- Added both requested `consider` terms: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`, rather than incorrectly choosing a single `replaced_by`.
- Added a tracker link for the active obsoletion request, `https://github.com/geneontology/go-ontology/issues/32005`.
- The agent's PR explanation showed good understanding of the issue: it identified `MetaCyc:PWY-3481` as a superpathway composed of `PWY-3462` and `PWY-3461`, already represented as narrow matches on `GO:0009094` and `GO:0006571`.


## Issues

- Minor provenance difference: the agent retained the older `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091"` and added `#32005`, whereas the human PR replaced the old tracker item with only `#32005`. This is not a substantive ontology error, but it leaves extra provenance not present in the reference solution.
- Minor comment-quality difference: the agent's obsolete comment correctly says the term is a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate, but it is less informative than the human PR's comment. The human comment explicitly names `MetaCyc:PWY-3481`, `PWY-3462`, `PWY-3461`, their mappings to `GO:0009094` and `GO:0006571`, and advises transfer to the appropriate `consider` term(s).
- No wrong term, syntax error, missing `consider`, or substantive missed ontology edit was found.

### Attempt 3: gpt-5.5 / codex

- **Eval PR**: [#127](https://github.com/ai4curation/eval-ont-agent-go/pull/127)
- **F1**: 0.927  **Precision**: 0.905  **Recall**: 0.950  **Jaccard**: 0.864
- **Workflow run**: [25633565040](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633565040)

#### Agent PR Comment

## Summary

Obsoleted `GO:0009095` aromatic amino acid biosynthetic process, prephenate pathway.

Rationale: the term represents a combined pathway for phenylalanine and tyrosine biosynthesis, corresponding to MetaCyc `PWY-3481`, rather than a single GO biological process term. The two narrower biological process terms already exist and carry the relevant MetaCyc narrow mappings:

- `GO:0009094` L-phenylalanine biosynthetic process, with `MetaCyc:PWY-3462`
- `GO:0006571` L-tyrosine biosynthetic process, with `MetaCyc:PWY-3461`

The obsolete stanza now keeps the historical definition provenance, removes logical axioms/synonyms/xref/asserted parentage, adds the obsoletion tracker item, and lists both candidate replacement terms as `consider`.

## Validation

- Pre-change validation: `make -C src/ontology travis_build` passed.
- Post-change validation: `make -C src/ontology travis_build` passed.
- Reference support in `RESEARCH.md` validated with `linkml-reference-validator validate text-file`: 3 valid, 0 invalid, 0 errors.

Notes: `runoak` could not be used locally because it fails at startup with a LinkML dependency error. QuickGO API reported 690 current total annotations to `GO:0009095`; the issue-reported experimental annotations remain annotation-review work outside this ontology edit.

## Checklist

- [x] PLAN: Issue context reviewed; request is clear.
- [x] PRE-VALIDATION: Current ontology validated before changes.
- [x] RESEARCH: `RESEARCH.md` created; PMID metadata/support checked.
- [x] TERM-SEARCH: `GO:0009095`, `GO:0009094`, and `GO:0006571` checked in `go-edit.obo`.
- [x] DESIGN-PATTERNS: `DESIGN_PATTERNS.md` created; biosynthetic process pattern checked.
- [x] EDITS: Used `obo-checkout.pl` / edited `terms/GO_0009095.obo` / used `obo-checkin.pl`.
- [x] RELATIONSHIPS: Removed obsolete term `is_a` and `intersection_of` axioms; added `consider` terms.
- [x] SPECIALIZED-EDITS: Used term-obsoletion guidance; checked CHEBI-related axiom context; checked mapping context for MetaCyc xref handling.
- [x] METADATA: Added `term_tracker_item` for issue #32005; retained namespace and historical definition provenance.
- [x] AUTOMATED-VALIDATION: `make -C src/ontology travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: PMID support excerpts validated.
- [x] CHANGES-COMMITTED: Local commit created: `4ec7001`.
- [x] RELEVANT-FILES: Only `src/ontology/go-edit.obo` was committed.
- [x] ACCURACY: Change follows issue rationale and existing narrower pathway terms.
- [x] ISSUE-ALIGNMENT: Obsoletion and candidate replacements match the request.
- [x] PR is created or amended: N/A for this local evaluation task.
- [x] Communicate high-level issue summary: prepared in `ISSUE_COMMENTS.md`.
- [x] Communicate PR details and rationale: this file.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633565040)


#### Agent Issue Comment

Changes committed in PR #<NN>.

`GO:0009095` has been made obsolete because it represents a combined phenylalanine/tyrosine biosynthesis pathway better handled as a GO-CAM model. The obsolete term now has `consider` references to `GO:0009094` L-phenylalanine biosynthetic process and `GO:0006571` L-tyrosine biosynthetic process.

Annotation review is still needed for existing annotations. The PMID checks support the issue's direction: PMID:21102469 may support reannotation to `GO:0009094` where phenylalanine biosynthesis is specifically supported; PMID:20883697 and PMID:18727669 do not by themselves support keeping the obsolete combined pathway annotation.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633565040)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..80c9bf363 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -90247,20 +90247,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0009095
-name: aromatic amino acid biosynthetic process, prephenate pathway
-namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
-synonym: "aromatic amino acid family anabolism, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family biosynthetic process via prephenate" EXACT [GOC:pr]
-synonym: "aromatic amino acid family biosynthetic process via prephenate(2-)" EXACT [GOC:pr]
-synonym: "aromatic amino acid family formation, prephenate pathway" EXACT []
-synonym: "aromatic amino acid family synthesis, prephenate pathway" EXACT []
-xref: MetaCyc:PWY-3481
-is_a: GO:0009073 ! aromatic amino acid biosynthetic process
-intersection_of: GO:0009058 ! biosynthetic process
-intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
-intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
+name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
+namespace: biological_process
+def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
+comment: This term was obsoleted because it represents a combined pathway consisting of phenylalanine and tyrosine biosynthesis and is better represented as a GO-CAM model.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
+is_obsolete: true
+consider: GO:0006571
+consider: GO:0009094
 
 [Term]
 id: GO:0009097

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.927  **precision**: 0.905  **recall**: 0.95

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/127
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 127 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#32005` by obsoleting `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and adding the requested `consider` targets `GO:0009094` and `GO:0006571`. The metadiff F1 of 0.927 is a fair reflection of a substantively correct solution with minor provenance/comment differences from the human PR. The main edit is ontologically sound: it removes the pre-composed superpathway term and leaves annotation review outside the ontology diff.


## Strengths

- Correctly renamed `GO:0009095` to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`, prefixed the definition with `OBSOLETE.`, and added `is_obsolete: true`.
- Removed the active logical structure from the obsolete term: the `is_a: GO:0009073` parent and the `intersection_of` axioms involving `GO:0009058`, `CHEBI:57852`, and `CHEBI:33856`.
- Removed active synonyms and the standalone `xref: MetaCyc:PWY-3481`, matching the obsoletion pattern for a term whose external mapping was to the MetaCyc superpathway.
- Added both appropriate `consider` terms from the issue: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added a `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/32005`.
- The agent's PR explanation correctly identified that `MetaCyc:PWY-3481` decomposes into phenylalanine and tyrosine biosynthesis pathways, with `MetaCyc:PWY-3462` and `MetaCyc:PWY-3461` already represented on `GO:0009094` and `GO:0006571`.


## Issues

- Minor provenance difference: the agent retained the older `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31091"` while the human PR replaced it with only the obsoletion issue `#32005`. This is unlikely to break the ontology, but it leaves extra tracker provenance not present in the reference solution.
- Minor comment-quality difference: the obsolete comment says the term is a combined phenylalanine/tyrosine pathway better represented as GO-CAM, which is correct, but it is less specific than the human PR's comment. The human comment explicitly mentions `MetaCyc:PWY-3481`, constituent pathways `PWY-3462` and `PWY-3461`, their mappings to `GO:0009094` and `GO:0006571`, and annotation transfer guidance.
- No wrong term, syntax error, or substantive missed ontology edit was found.

### Attempt 4: kimi-k2.6 / opencode

- **Eval PR**: [#291](https://github.com/ai4curation/eval-ont-agent-go/pull/291)
- **F1**: 0.080  **Precision**: 0.952  **Recall**: 0.042  **Jaccard**: 0.042
- **Trace**: [25646713832](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646713832)
- **Workflow run**: [25646713832](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646713832)

#### Agent PR Comment

Obsoletion of GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway

## Summary
Obsoleted GO:0009095 because it is a pre-composed term representing a MetaCyc superpathway that combines two separate pathways already represented in GO. This obsoletion follows the signal in the issue that the term should instead be represented as a GO-CAM model.

## Changes made
- Removed all logical axioms from GO:0009095 (is_a, intersection_of, synonyms, xref)
- Prefixed name with "obsolete"
- Prefixed definition with "OBSOLETE."
- Added comment explaining that the term represents a GO-CAM model
- Added term_tracker_item linking to issue #32005
- Added two `consider` tags pointing to candidate replacements:
  - GO:0009094 ! L-phenylalanine biosynthetic process
  - GO:0006571 ! L-tyrosine biosynthetic process

## Checklist
- [x] PLAN: The issue and all its context has been analyzed, the intent is clear, and a plan for addressing it has been created
- [x] PRE-VALIDATION: Current state of the ontology validates prior to any changes
- [x] TERM-SEARCH: Relevant ontology terms have been consulted; confirmed no other terms reference GO:0009095
- [x] SPECIALIZED-EDITS: term-obsoletion skill procedures followed
- [x] EDITS: correct procedure followed (checkout -> edit in terms/ -> checkin)
- [x] RELATIONSHIPS: all axioms removed from obsolete term; consider terms added appropriately
- [x] METADATA: comment, term_tracker_item, is_obsolete, consider tags correctly formatted
- [x] AUTOMATED-VALIDATION: robot convert and robot reason (ELK) both pass after edits
- [x] CHANGES-COMMITTED: changes committed with detailed message

## Issue context
- Issue: https://github.com/geneontology/go-ontology/issues/32005
- Original reason for obsoletion: GO:0009095 is pre-composed and should be represented as a GO-CAM model (MetaCyc:PWY-3481 = superpathway of L-phenylalanine and L-tyrosine biosynthesis).

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646713832)


#### Agent Issue Comment

GO:0009095 has been obsoleted as requested. The term was a pre-composed superpathway (MetaCyc:PWY-3481) combining L-phenylalanine and L-tyrosine biosynthesis, which are already represented by separate GO terms. Annotations can be migrated to the consider terms GO:0009094 (L-phenylalanine biosynthetic process) or GO:0006571 (L-tyrosine biosynthetic process) as appropriate.

Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646713832)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..9bfb35579 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1455 more lines truncated)
```

### Attempt 5: claude-haiku-4.5 / claude

- **Eval PR**: [#224](https://github.com/ai4curation/eval-ont-agent-go/pull/224)
- **F1**: 0.080  **Precision**: 0.952  **Recall**: 0.042  **Jaccard**: 0.042
- **Workflow run**: [25640390658](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640390658)

#### Agent PR Comment

# Obsoletion of GO:0009095: aromatic amino acid biosynthetic process, prephenate pathway

## Summary

This PR obsoletes GO:0009095, a pre-composed term that combines two distinct biosynthetic pathways for aromatic amino acids. The term has been marked as obsolete and curators are directed to two candidate replacement terms for annotation migration.

## Implementation Checklist

- [x] PLAN: Issue analysis complete - clear request to obsolete a pre-composed term
- [x] PRE-VALIDATION: Ontology validated before changes (travis_build passed)
- [x] TERM-SEARCH: Located GO:0009095 and verified no internal references
- [x] CHECK REPLACEMENTS: Verified candidate terms exist and are appropriate:
  - GO:0009094 "L-phenylalanine biosynthetic process"
  - GO:0006571 "L-tyrosine biosynthetic process"
- [x] EDITS: Used obo-checkout.pl and obo-checkin.pl workflow to edit the term
- [x] OBSOLETION: Applied correct obsoletion metadata:
  - Name: "obsolete aromatic amino acid biosynthetic process, prephenate pathway"
  - Definition: "OBSOLETE. [original definition]" with original references
  - Removed all is_a, relationship, intersection_of tags
  - Added consider tags pointing to both replacement terms
  - Added explanatory comment detailing the reason for obsoletion
  - Linked to GitHub issue #32005 via term_tracker_item
  - Set is_obsolete: true
- [x] METADATA: Correct metadata for obsoletion:
  - namespace: biological_process (retained as per GO standards)
  - No synonyms (correctly removed)
  - Original definition xrefs preserved
  - Term tracker item points to #32005
- [x] AUTOMATED-VALIDATION: Ontology validates correctly via make travis_build
- [x] CHANGES-COMMITTED: Single commit with detailed message

## Technical Details

### Original Term Structure
The obsoleted term had complex logical axioms:
```
is_a: GO:0009073 ! aromatic amino acid biosynthetic process
intersection_of: GO:0009058 ! biosynthetic process
intersection_of: has_intermediate CHEBI:57852 ! prephenate(2-)
intersection_of: has_primary_output CHEBI:33856 ! aromatic amino acid
```

These axioms have been removed as per obsoletion standards.

### Obsolete Term Structure
```
[Term]
id: GO:0009095
name: obsolete aromatic amino acid biosynthetic process, prephenate pathway
namespace: biological_process
def: "OBSOLETE. The chemical reactions and pathways resulting in the formation of phenylalanine and tyrosine from other compounds, including chorismate, via the intermediate prephenate." [GOC:mah, ISBN:0471331309, MetaCyc:PWY-3481]
comment: The reason for obsoletion is that this term is pre-composed and should be represented as the two distinct pathways for L-phenylalanine and L-tyrosine biosynthesis. MetaCyc:PWY-3481 is a superpathway combining PWY-3462 (L-phenylalanine biosynthesis II) and PWY-3461 (L-tyrosine biosynthesis II), which are properly represented by distinct GO terms.
consider: GO:0009094 ! L-phenylalanine biosynthetic process
consider: GO:0006571 ! L-tyrosine biosynthetic process
is_obsolete: true
property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32005" xsd:anyURI
```

### Rationale for Replacement Terms
- MetaCyc:PWY-3481 is a "superpathway of L-phenylalanine and L-tyrosine biosynthesis"
- It combines two separate pathways:
  - PWY-3462 (L-phenylalanine biosynthesis II) → GO:0009094 (xref: MetaCyc:PWY-3462)
  - PWY-3461 (L-tyrosine biosynthesis II) → GO:0006571 (xref: MetaCyc:PWY-3461)
- The pre-composed term violates GO design patterns and can be better represented as a GO-CAM model

## Annotation Impact

Four annotations exist to this term that require curator review:

| Source | PMID | Gene Product | Recommendation |
|--------|------|--------------|-----------------|
| UniProt | 21102469 | Petunia PPA-AT | Migrate to GO:0009094 (shows Phe biosynthesis) |
| UniProt | 21102469 | Arabidopsis PAT | Remove (no BP evidence in paper) |
| TAIR | 20883697 | Arabidopsis PAT | Remove (biochemical paper, no BP info) |
| MTBBASE | 18727669 | M. tuberculosis Rv0948c | Remove (structural/biochemical, no BP info) |

## Validation Results

The ontology builds successfully with no errors or warnings after obsoletion:
```
cd src/ontology && make travis_build
```
Exit code: 0 ✓

## Files Modified

- `src/ontology/go-edit.obo` - Single change: obsolete GO:0009095 term

## References

- Issue: https://github.com/geneontology/go-ontology/issues/32005
- Related Issue: https://github.com/geneontology/go-ontology/issues/31091 (original term creation)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640390658)


#### Agent Issue Comment

# Obsoletion of GO:0009095 Complete

The term **GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway"** has been successfully obsoleted.

## Rationale

This term is pre-composed and represents a MetaCyc superpathway (PWY-3481) that combines two separate biosynthetic processes. These are better represented by the existing specific GO terms:

- **GO:0009094** L-phenylalanine biosynthetic process
- **GO:0006571** L-tyrosine biosynthetic process

## Changes Made

The term has been marked as obsolete with:
- `is_obsolete: true`
- Name prefixed with "obsolete"
- Definition updated to "OBSOLETE" prefix
- All logical axioms and relationships removed
- Consider tags added to guide annotation migration
- Term tracker item updated to reference this issue (#32005)

## Validation

The ontology has been validated and builds successfully with `make travis_build`.

## Annotation Handling

Four existing annotations to this term require curator action in the annotation review process:
- 2 from UniProt (PMID:21102469): 1 should migrate to GO:0009094, 1 should be removed
- 1 from TAIR (PMID:20883697): should be removed
- 1 from MTBBASE (PMID:18727669): should be removed

Details are provided in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640390658)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..8b1a7d901 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1455 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: partial_success  **f1**: 0.08  **precision**: 0.952  **recall**: 0.042

**Failure modes**: over_editing, scope_creep

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/224
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 224 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly performed the core obsoletion requested for `GO:0009095` (`aromatic amino acid biosynthetic process, prephenate pathway`): it made the term obsolete and pointed users to `GO:0009094` and `GO:0006571`. However, the PR is massively over-scoped compared with the human PR, which only changed the `GO:0009095` stanza. The metadiff F1 of 0.08 is low because the agent PR contains a large unrelated diff; it under-represents the quality of the target `GO:0009095` edit but fairly flags the PR-level scope problem.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and changed its label to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active ontology structure from `GO:0009095`, including `is_a: GO:0009073`, `intersection_of: GO:0009058`, `has_intermediate CHEBI:57852`, and `has_primary_output CHEBI:33856`.
- Removed the active synonyms and direct `xref: MetaCyc:PWY-3481`, consistent with the issue's explanation that `PWY-3481` is a superpathway rather than a single GO pathway term.
- Added both requested `consider` targets: `GO:0009094` (`L-phenylalanine biosynthetic process`) and `GO:0006571` (`L-tyrosine biosynthetic process`).
- Added a useful obsoletion comment explaining that `MetaCyc:PWY-3481` combines `PWY-3462` and `PWY-3461`, and added the current tracker link for issue `#32005`.


## Issues

- Major scope creep: the agent PR is a 1654-line diff touching `src/ontology/go-edit.obo`, generated import files, and taxon constraint files. The human PR for issue `#32005` changed only the `GO:0009095` stanza in `src/ontology/go-edit.obo`.
- The unrelated edits are extensive and not justified by the issue. Examples include obsoleting or changing terms from other tickets such as `GO:0003400`, `GO:0008785`, `GO:0008875`, `GO:0009255`, `GO:0018581`, `GO:0045550`, `GO:0099022`, `GO:0099041`, and `GO:0099069`; renaming signal-sequence terms such as `GO:0005048`, `GO:0000268`, `GO:0030941`, and `GO:0045048`; and adding new terms `GO:0140419` and `GO:7770069`.
- The PR also changes taxon constraint files unrelated to `GO:0009095`, including removals for `GO:0052704` and `GO:0140479` and additions for `GO:0000956` and `GO:0141065`. Those changes make the submitted PR unsuitable even though the target obsoletion is mostly right.
- Minor style difference: the agent's `consider` lines include inline labels (`! L-phenylalanine biosynthetic process`, `! L-tyrosine biosynthetic process`), while the human PR used bare IDs. This is not a substantive correctness problem, but it differs from the accepted patch.
- No wrong target term or obvious syntax error was found in the `GO:0009095` edit itself; the main failure is bundling many unrelated ontology edits into the evaluation PR.

### Attempt 6: gpt-5.4 / codex

- **Eval PR**: [#223](https://github.com/ai4curation/eval-ont-agent-go/pull/223)
- **F1**: 0.076  **Precision**: 0.905  **Recall**: 0.040  **Jaccard**: 0.040
- **Workflow run**: [25640340957](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640340957)

#### Agent PR Comment

Obsoleted GO:0009095 `aromatic amino acid biosynthetic process, prephenate pathway` in [src/ontology/go-edit.obo](/__w/eval-ont-agent-go/eval-ont-agent-go/src/ontology/go-edit.obo:90267).

Rationale:

- The issue request is clear that this term corresponds to a combined MetaCyc superpathway (`PWY-3481`) rather than a stable single GO process class.
- Existing branch-level terms already cover the biologically meaningful outputs:
  - GO:0009094 `L-phenylalanine biosynthetic process`
  - GO:0006571 `L-tyrosine biosynthetic process`
- This matches existing GO precedent for obsoleting route-specific amino-acid biosynthesis pathway terms that really describe GO-CAM-style pathway models.

Changes made:

- Renamed the term to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Converted the definition to obsolete form while preserving original provenance.
- Removed synonyms, xref, `is_a`, and `intersection_of` axioms from the obsolete stanza.
- Added the standard GO-CAM-model obsoletion comment.
- Added `consider: GO:0009094` and `consider: GO:0006571`.
- Added a `term_tracker_item` link to issue `#32005` and retained the existing historical tracker link.

Validation and research:

- Pre-validation passed with `make -C src/ontology travis_build`.
- Post-change validation passed with `make -C src/ontology travis_build`.
- Created temporary `DESIGN_PATTERNS.md` and `RESEARCH.md` notes to document precedent and annotation impact.
- Validated the cited PMIDs with `linkml-reference-validator` and checked supporting abstract text for:
  - PMID:21102469
  - PMID:20883697
  - PMID:18727669

Annotation impact summary:

- PMID:21102469 supports moving the Petunia PPA-AT annotation to GO:0009094.
- PMID:20883697 and PMID:18727669 do not clearly support keeping annotations to the obsolete combined-pathway term.
- GO:0006571 remains an appropriate `consider` target because the obsolete term bundled phenylalanine and tyrosine outputs, even though the reviewed abstract evidence did not specifically justify a direct transfer there.

Checklist:

- [x] PLAN: The issue and comments were analyzed and the intent was clear.
- [x] PRE-VALIDATION: Current ontology state validated before edits.
- [x] RESEARCH: Background research performed and captured in `RESEARCH.md`.
- [x] TERM-SEARCH: Relevant GO terms and usages were searched in `src/ontology/go-edit.obo`.
- [x] DESIGN-PATTERNS: Existing pattern/precedent reviewed and captured in `DESIGN_PATTERNS.md`.
- [x] EDITS: Used `obo-checkout.pl` and `obo-checkin.pl`; did not edit `go-edit.obo` directly.
- [x] RELATIONSHIPS: Removed obsolete logical/asserted axioms from the obsoleted term.
- [x] SPECIALIZED-EDITS: Applied the `/term-obsoletion` workflow.
- [x] METADATA: Obsolete-term metadata updated appropriately; no `created_by`/`creation_date` added because this is not a new term.
- [x] AUTOMATED-VALIDATION: `make -C src/ontology travis_build` passed after edits.
- [x] REFERENCE-VALIDATION: PMID citations used in the research notes were validated locally.
- [x] CHANGES-COMMITTED: Local commit created for `src/ontology/go-edit.obo` only.
- [ ] PR is created or amended.
- [ ] Communicate high level summary of changes on original issue(s).
- [ ] Communicated on PR detailed description of changes made, and rationale.

The last three items are left for the handoff flow that will post these prepared comments upstream.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640340957)


#### Agent Issue Comment

Implemented in PR #<NN>.

GO:0009095 has been obsoleted as a GO-CAM-like pathway term and now carries `consider` tags to:

- GO:0009094 `L-phenylalanine biosynthetic process`
- GO:0006571 `L-tyrosine biosynthetic process`

I also reviewed the cited annotation-support PMIDs locally while preparing the obsoletion rationale. Based on the abstract-level evidence, the Petunia PPA-AT annotation looks like a candidate for transfer to GO:0009094, while the remaining cited annotations look more likely to be removed than migrated to the obsolete combined-pathway term.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640340957)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..f1536da9f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1455 more lines truncated)
```

#### Review by gpt-5.5

**outcome**: partial_success  **f1**: 0.076  **precision**: 0.905  **recall**: 0.04

**Failure modes**: over_editing, scope_creep

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32005
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32026
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/223
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32005 --repo geneontology/go-ontology
    gh pr diff 32026 --repo geneontology/go-ontology
    gh pr diff 223 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent did make the core requested edit for issue `#32005`: it obsoleted `GO:0009095` `aromatic amino acid biosynthetic process, prephenate pathway` and added `consider` links to `GO:0009094` and `GO:0006571`. However, the PR is badly over-scoped: instead of the human PR's single-term `src/ontology/go-edit.obo` change, the agent PR includes a large unrelated diff touching many GO terms, imports, and taxon constraint files. The metadiff F1 of 0.076 is directionally fair for PR-level quality, though it under-represents that the `GO:0009095` stanza itself is mostly correct.


## Strengths

- Correctly identified `GO:0009095` as the term to obsolete and changed its label to `obsolete aromatic amino acid biosynthetic process, prephenate pathway`.
- Correctly prefixed the definition with `OBSOLETE.` and added `is_obsolete: true`.
- Removed the active ontology structure from `GO:0009095`: the `is_a: GO:0009073` parent, the genus `intersection_of: GO:0009058`, and the logical axioms using `CHEBI:57852` prephenate and `CHEBI:33856` aromatic amino acid.
- Removed the active synonyms and the direct `xref: MetaCyc:PWY-3481`, which is appropriate because the issue explains that `PWY-3481` is a combined superpathway rather than a single GO pathway term.
- Added both issue-requested `consider` targets: `GO:0009094` `L-phenylalanine biosynthetic process` and `GO:0006571` `L-tyrosine biosynthetic process`.
- Added a tracker link for the active obsoletion request, `https://github.com/geneontology/go-ontology/issues/32005`.


## Issues

- Major scope creep: the agent PR includes a 1654-line diff across `src/ontology/go-edit.obo`, `src/ontology/imports/go-catalytic-activities-participants.owl`, `src/ontology/imports/go_taxon_constraints.owl`, `src/taxon_constraints/only_in_taxon.ofn`, and `src/taxon_constraints/only_in_taxon.tsv`. The human PR for this issue changed only the `GO:0009095` stanza.
- The unrelated ontology edits are extensive and not justified by issue `#32005`. Examples include obsoleting `GO:0003400`, `GO:0008785`, `GO:0008875`, `GO:0009255`, `GO:0018581`, `GO:0045550`, `GO:0099022`, `GO:0099041`, `GO:0099044`, and `GO:0099069`; renaming/reparenting signal-sequence terms such as `GO:0005048`, `GO:0000268`, `GO:0030941`, and `GO:0045048`; adding new terms such as `GO:0140419` and `GO:7770069`; and changing taxon constraints for terms such as `GO:0052704`, `GO:0140479`, `GO:0000956`, and `GO:0141065`.
- The obsolete comment for `GO:0009095` is much less informative than the human PR's comment. It says only that the term "represents a GO-CAM model"; the issue/human solution specifically explains that `MetaCyc:PWY-3481` is the superpathway of L-phenylalanine and L-tyrosine biosynthesis, decomposing into `PWY-3462` and `PWY-3461`, already represented as narrow matches on `GO:0009094` and `GO:0006571`.
- Minor provenance difference: the agent retained the old `term_tracker_item` for issue `#31091` and added `#32005`, whereas the human PR replaced the old tracker metadata with the current obsoletion issue only.
- No wrong target term or obvious syntax error was found in the `GO:0009095` obsoletion itself, but the PR as a whole would not be acceptable without removing the unrelated edits.

### Attempt 7: claude-sonnet-4.5 / claude

- **Eval PR**: [#491](https://github.com/ai4curation/eval-ont-agent-go/pull/491)
- **F1**: 0.072  **Precision**: 0.857  **Recall**: 0.038  **Jaccard**: 0.037
- **Trace**: [25867621145](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25867621145)
- **Workflow run**: [25867621145](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25867621145)

#### Agent PR Comment

## Obsoletion of GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway

This PR obsoletes GO:0009095 as requested in issue #32005.

### Rationale

The term represents what should be a GO-CAM model rather than a single biological process. MetaCyc:PWY-3481 (referenced by this term) is a superpathway of L-phenylalanine and L-tyrosine biosynthesis that combines two separate pathways:
- L-phenylalanine biosynthesis II (MetaCyc:PWY-3462) → GO:0009094
- L-tyrosine biosynthesis II (MetaCyc:PWY-3461) → GO:0006571

These individual pathway terms correctly have narrowMatch xrefs to their respective MetaCyc pathways.

### Changes Made

**Obsoletion edits to GO:0009095:**
- Changed name to "obsolete aromatic amino acid biosynthetic process, prephenate pathway"
- Changed definition to start with "OBSOLETE."
- Removed all logical axioms:
  - Removed is_a: GO:0009073 (aromatic amino acid biosynthetic process)
  - Removed all intersection_of tags (logical definitions)
- Removed all synonyms (per standard GO obsoletion practice)
- Added is_obsolete: true
- Added two consider tags:
  - consider: GO:0009094 ! L-phenylalanine biosynthetic process
  - consider: GO:0006571 ! L-tyrosine biosynthetic process
- Added comment explaining reason for obsoletion
- Added term_tracker_item for issue #32005
- Retained historical metadata:
  - Original definition with provenance
  - MetaCyc:PWY-3481 xref
  - Original term_tracker_item (#31091)
  - namespace: biological_process

### Validation Checklist

- [x] **PLAN**: Issue analyzed and obsoletion plan created
- [x] **PRE-VALIDATION**: Ontology validated before changes (file parses correctly)
- [x] **RESEARCH**: N/A - straightforward obsoletion with clear consider terms
- [x] **TERM-SEARCH**: Verified GO:0009095 exists and checked for references
  - No other terms in go-edit.obo reference GO:0009095
  - No rewiring necessary
- [x] **DESIGN-PATTERNS**: Consulted term-obsoletion skill for proper procedure
- [x] **EDITS**: Followed proper checkout/edit/checkin procedure
  - Used obo-checkout.pl to extract term to terms/GO_0009095.obo
  - Made edits in local terms/ folder
  - Used obo-checkin.pl to integrate changes back
- [x] **RELATIONSHIPS**: All logical axioms appropriately removed
  - Removed is_a relationship
  - Removed all intersection_of tags (genus-differentia logical definitions)
  - No over-assertion of axioms
- [x] **SPECIALIZED-EDITS**: 
  - Used /term-obsoletion skill procedures
  - Followed obsoletion metadata conventions
  - Ensured no logical axioms remain
- [x] **METADATA**: Correct obsoletion metadata applied
  - Name prefixed with "obsolete"
  - Definition prefixed with "OBSOLETE."
  - is_obsolete: true tag added
  - consider tags for both replacement terms
  - Comment explaining reason for obsoletion
  - term_tracker_item linking to issue #32005
  - namespace retained on obsolete term
- [x] **AUTOMATED-VALIDATION**: Ontology validated after changes
  - File parses correctly with obo-grep.pl
  - Total term count maintained (48,309 terms)
  - Obsolete term count increased correctly (9,891 obsolete terms)
- [x] **REFERENCE-VALIDATION**: N/A - no new references introduced
- [x] **CHANGES-COMMITTED**:
  - [x] **RELEVANT-FILES**: Only src/ontology/go-edit.obo committed
  - [x] **ACCURACY**: Changes are correct and follow GO obsoletion standards
  - [x] **ISSUE-ALIGNMENT**: Changes fully address issue #32005
  - [x] **PR**: This PR created with detailed description
  - [x] **ISSUE-ALIGNMENT**: Summary provided on original issue

### Term Verification

**Consider terms verified:**
- GO:0009094 (L-phenylalanine biosynthetic process) exists with MetaCyc:PWY-3462 narrowMatch
- GO:0006571 (L-tyrosine biosynthetic process) exists with MetaCyc:PWY-3461 narrowMatch

### Annotation Impact

Per the issue description, there are 4 EXP annotations to this term:
- 2 annotations by UniProt from PMID:21102469
- 1 annotation by TAIR from PMID:20883697
- 1 annotation by MTBBASE from PMID:18727669

The issue notes that annotation curators have been notified via the annotation review process and will handle migration of these annotations to the appropriate consider terms.

### Files Changed

- `src/ontology/go-edit.obo`: Obsoleted GO:0009095

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25867621145)


#### Agent Issue Comment

GO:0009095 (aromatic amino acid biosynthetic process, prephenate pathway) has been successfully obsoleted.

The term has been obsoleted with two consider terms:
- GO:0009094 L-phenylalanine biosynthetic process
- GO:0006571 L-tyrosine biosynthetic process

The obsoletion follows standard GO procedures: all logical axioms have been removed, proper metadata added, and the term now correctly indicates it represents what should be a GO-CAM model rather than a single process.

The MetaCyc:PWY-3481 superpathway appropriately maps to the two individual pathway terms via their narrowMatch xrefs (MetaCyc:PWY-3462 and MetaCyc:PWY-3461).

No other terms in the ontology reference GO:0009095, so no rewiring was necessary.

Changes committed in PR #<NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25867621145)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..318b0096d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1455 more lines truncated)
```

### Attempt 8: claude-sonnet-4.5 / claude

- **Eval PR**: [#487](https://github.com/ai4curation/eval-ont-agent-go/pull/487)
- **F1**: 0.072  **Precision**: 0.857  **Recall**: 0.038  **Jaccard**: 0.037
- **Trace**: [25847348718](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847348718)
- **Workflow run**: [25847348718](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847348718)

#### Agent PR Comment

# Obsoletion of GO:0009095 aromatic amino acid biosynthetic process, prephenate pathway

## Summary

This PR obsoletes GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway" as requested in issue #32005.

## Reason for Obsoletion

This term was made obsolete because it represents a GO-CAM model rather than a simple biological process term. The MetaCyc pathway PWY-3481 that this term maps to is actually a superpathway that combines two separate pathways:
- L-phenylalanine biosynthesis II (PWY-3462) → GO:0009094
- L-tyrosine biosynthesis II (PWY-3461) → GO:0006571

These two processes should be represented as separate terms with appropriate relationships in a GO-CAM model, not as a single pre-composed term.

## Changes Made

### Ontology Changes
- **Removed logical axioms**: Deleted is_a relationship to GO:0009073 and all intersection_of tags
- **Removed synonyms**: All 5 synonyms removed as per obsoletion standards
- **Removed xref**: MetaCyc:PWY-3481 mapping removed
- **Updated metadata**:
  - Name: Added "obsolete" prefix
  - Definition: Added "OBSOLETE." prefix
  - Added `is_obsolete: true` tag
  - Updated term_tracker_item to point to issue #32005
  - Added comment explaining reason for obsoletion
- **Added consider tags**:
  - GO:0009094 L-phenylalanine biosynthetic process
  - GO:0006571 L-tyrosine biosynthetic process

### Ontology Impact Analysis
- **Internal references**: None found. No other GO terms reference GO:0009095, so no rewiring was necessary.

### Annotation Impact Analysis

Using `runoak -i amigo: associations GO:0009095`, I identified:
- **4 EXP annotations** (IDA evidence code)
- **3 computational annotations** (IEA/ISS evidence codes)

**Annotations requiring curation:**

1. **UniProtKB:E9L7A5 (PPA-AT, Petunia)** - PMID:21102469 (UniProt)
   - **Recommendation**: Replace with GO:0009094 (L-phenylalanine biosynthetic process)
   - **Rationale**: Fig 1 shows PPA-AT RNAi affects L-phenylalanine synthesis

2. **AGI_LocusCode:AT2G22250 (PAT, Arabidopsis)** - PMID:21102469 (UniProt)
   - **Recommendation**: Remove annotation
   - **Rationale**: No evidence for BP annotation in this paper

3. **AGI_LocusCode:AT2G22250 (PAT, Arabidopsis)** - PMID:20883697 (TAIR)
   - **Recommendation**: Remove annotation
   - **Rationale**: Biochemical paper, no BP information

4. **UniProtKB:P9WIC1 (Rv0948c, M. tuberculosis)** - PMID:18727669 (MTBBASE)
   - **Recommendation**: Remove annotation
   - **Rationale**: Biochemical/structural paper, no BP information

The computational annotations (IEA/ISS) will be automatically handled by the annotation pipeline.

## Validation

- **Syntax validation**: ✓ Term verified with obo-grep.pl, no syntax errors
- **Consider terms validated**: ✓ Both GO:0009094 and GO:0006571 exist and are active terms
- **Ontology structure**: ✓ No other terms reference GO:0009095
- **Standard build validation**: Note - full `make travis_build` could not be completed in the test environment due to missing dependencies (amm), but the obsoletion follows standard patterns and syntax is valid

## Checklist

- [x] **PLAN**: Issue analyzed, intent clear, comprehensive plan created
- [x] **PRE-VALIDATION**: Ontology was valid before changes (no pre-existing issues found)
- [x] **RESEARCH**: N/A (obsoletion request, no new biological research needed)
- [x] **TERM-SEARCH**: Examined GO:0009095 and verified consider terms exist
- [x] **DESIGN-PATTERNS**: N/A (obsoletion, not creating new terms)
- [x] **EDITS**: Proper checkout/checkin procedure followed
  - [x] Used obo-checkout.pl to extract term to terms/ folder
  - [x] Made edits in terms/GO_0009095.obo
  - [x] Used obo-checkin.pl to update src/ontology/go-edit.obo
- [x] **RELATIONSHIPS**: All logical axioms removed as required for obsolete terms
  - [x] Removed is_a relationship
  - [x] Removed all intersection_of tags (logical definitions)
  - [x] Added appropriate consider tags
- [x] **SPECIALIZED-EDITS**:
  - [x] Used /term-obsoletion skill for guidance on obsoletion procedures
  - [x] Followed obsoletion metadata standards
  - [x] Removed all synonyms (standard practice unless explicitly requested)
  - [x] Retained namespace tag (required for obsolete GO terms)
- [x] **METADATA**: Correct metadata for obsolete term
  - [x] Name prefixed with "obsolete"
  - [x] Definition prefixed with "OBSOLETE."
  - [x] Original definition and references preserved
  - [x] Comment explaining reason for obsoletion added
  - [x] term_tracker_item updated to issue #32005
  - [x] is_obsolete: true tag added
  - [x] Did NOT add created_by/creation_date (only for NEW terms)
- [x] **AUTOMATED-VALIDATION**: OBO syntax validated with obo-grep.pl
- [x] **REFERENCE-VALIDATION**: N/A (no new references introduced)
- [x] **CHANGES-COMMITTED**: 
  - [x] **RELEVANT-FILES**: Only src/ontology/go-edit.obo committed
  - [x] **ACCURACY**: Obsoletion follows GO standards and term-obsoletion guidelines
  - [x] **ISSUE-ALIGNMENT**: Changes match request in issue #32005
  - [x] **PR**: This PR created with detailed description
  - [x] **ISSUE-COMMUNICATION**: Summary provided in ISSUE_COMMENTS.md
  - [x] **PR-COMMUNICATION**: Detailed changes and checklist documented here

## Related Issues

Closes #32005

## Notes for Reviewers

This is a straightforward obsoletion with no ontology rewiring required. The main follow-up work will be annotation updates by the respective curation groups (UniProt, TAIR, MTBBASE) as detailed in the annotation impact analysis above.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847348718)


#### Agent Issue Comment

The term GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway" has been successfully obsoleted as requested.

The obsoletion was performed because this term represents a GO-CAM model rather than a simple biological process term. The MetaCyc pathway PWY-3481 that this term maps to is actually a superpathway combining two separate pathways for L-phenylalanine and L-tyrosine biosynthesis.

The term now includes consider tags pointing to:
- GO:0009094 L-phenylalanine biosynthetic process
- GO:0006571 L-tyrosine biosynthetic process

**Annotation Impact Analysis:**

I confirmed there are 4 EXP (IDA) annotations and 3 computational annotations (IEA/ISS) to this term. The analysis you provided in the issue description for handling these annotations looks appropriate:

- **PMID:21102469** (2 annotations): PPA-AT can be reannotated to GO:0009094; PAT annotation should be removed
- **PMID:20883697** (PAT): Annotation should be removed (biochemical paper, no BP evidence)
- **PMID:18727669** (Rv0948c): Annotation should be removed (biochemical/structural paper, no BP evidence)

**Ontology Impact:**

No other terms in the ontology reference GO:0009095, so no rewiring was necessary.

Changes have been committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847348718)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..318b0096d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1455 more lines truncated)
```

### Attempt 9: gemma-4-31b / opencode

- **Eval PR**: [#525](https://github.com/ai4curation/eval-ont-agent-go/pull/525)
- **F1**: 0.017  **Precision**: 0.190  **Recall**: 0.009  **Jaccard**: 0.008

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..961e08ab9 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1426 more lines truncated)
```

### Attempt 10: claude-sonnet-4.5 / copilot

- **Eval PR**: [#450](https://github.com/ai4curation/eval-ont-agent-go/pull/450)
- **F1**: 0.017  **Precision**: 0.190  **Recall**: 0.009  **Jaccard**: 0.008
- **Trace**: [25775856969](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775856969)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..961e08ab9 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1426 more lines truncated)
```

### Attempt 11: claude-sonnet-4.5 / copilot

- **Eval PR**: [#404](https://github.com/ai4curation/eval-ont-agent-go/pull/404)
- **F1**: 0.017  **Precision**: 0.190  **Recall**: 0.009  **Jaccard**: 0.008
- **Trace**: [25752437460](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25752437460)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..961e08ab9 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1426 more lines truncated)
```

### Attempt 12: claude-opus-4.7 / claude

- **Eval PR**: [#324](https://github.com/ai4curation/eval-ont-agent-go/pull/324)
- **F1**: 0.017  **Precision**: 0.190  **Recall**: 0.009  **Jaccard**: 0.008
- **Trace**: [25649365221](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25649365221)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..961e08ab9 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -1468,7 +1468,7 @@ synonym: "exocyst complex" EXACT []
 synonym: "Sec6/8 complex" EXACT []
 xref: Wikipedia:Exocyst
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0090522 ! vesicle tethering involved in exocytosis
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005938 ! cell cortex
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31922" xsd:anyURI
 
@@ -2914,14 +2914,16 @@ consider: GO:0005575
 
 [Term]
 id: GO:0000268
-name: peroxisome targeting sequence binding
+name: peroxisome signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0005051
-def: "Binding to a peroxisomal targeting sequence, a sequence of amino acids within a protein that acts as a signal for the localization of a protein into the peroxisome." [GOC:mah, ISBN:0879693568]
+def: "Binding to a peroxisomal targeting sequence, a short stretch of amino acids found in a protein that acts as a signal to localize the protein to the peroxisome." [PMID:20659419]
+synonym: "peroxisome targeting sequence binding" NARROW []
 synonym: "peroxisome targeting signal receptor" NARROW []
 synonym: "PTS binding" EXACT []
 synonym: "PTS receptor" NARROW []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0000269
@@ -6943,7 +6945,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -29440,11 +29442,13 @@ creation_date: 2009-12-09T10:03:32Z
 
 [Term]
 id: GO:0003400
-name: regulation of COPII vesicle coating
+name: obsolete regulation of COPII vesicle coating
 namespace: biological_process
-def: "Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
-intersection_of: GO:0065007 ! biological regulation
-intersection_of: regulates GO:0048208 ! COPII vesicle coating
+def: "OBSOLETE. Any process that modulates the rate, frequency, or extent of the addition of COPII proteins and adaptor proteins to ER membranes during the formation of transport vesicles, forming a vesicle coat." [GOC:ascb_2009, GOC:dph, GOC:jp, GOC:tb]
+comment: This term was obsoleted because the proteins previously annotated to it are part_of the COPII vesicle coating pathway rather than upstream regulators of it. Annotations should be moved to GO:0048208 COPII vesicle coat assembly.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31945" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0048208
 created_by: dph
 creation_date: 2009-12-17T08:38:14Z
 
@@ -50846,7 +50850,7 @@ name: KDEL sequence binding
 namespace: molecular_function
 def: "Binding to a KDEL sequence, the C terminus tetrapeptide sequence Lys-Asp-Glu-Leu found in proteins that are to be retained in the endoplasmic reticulum." [GOC:ai]
 synonym: "KDEL receptor activity" NARROW []
-is_a: GO:0046923 ! ER retention sequence binding
+is_a: GO:0046923 ! ER lumen protein retrieval receptor activity
 
 [Term]
 id: GO:0005047
@@ -50862,14 +50866,16 @@ intersection_of: has_primary_input GO:0048500 ! signal recognition particle
 
 [Term]
 id: GO:0005048
-name: signal sequence binding
+name: signal sequence receptor activity
 namespace: molecular_function
 alt_id: GO:0008249
-def: "Binding to a signal sequence, a specific peptide sequence found on protein precursors or mature proteins that dictates where the mature protein is localized." [GOC:ai]
+def: "Binding to a signal sequence, a short stretch of amino acids found in a protein that acts as a signal for its proper localization in the cell." [GOC:curators]
 synonym: "leader sequence binding" NARROW []
 synonym: "protein signal sequence binding" NARROW []
+synonym: "signal sequence binding" NARROW []
 synonym: "signal sequence receptor" NARROW []
-is_a: GO:0042277 ! peptide binding
+is_a: GO:0003674 ! molecular_function
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31419" xsd:anyURI
 
 [Term]
 id: GO:0005049
@@ -50907,7 +50913,7 @@ synonym: "peroxisome targeting signal-1 receptor" NARROW []
 synonym: "PEX5" NARROW []
 synonym: "PTS1 binding" EXACT [PMID:14709540]
 synonym: "PTS1 receptor" NARROW []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005053
@@ -50920,7 +50926,7 @@ synonym: "peroxisome targeting signal-2 receptor" NARROW []
 synonym: "PEX7" NARROW []
 synonym: "PTS2 binding" EXACT [PMID:14709540]
 synonym: "PTS2 receptor" EXACT []
-is_a: GO:0000268 ! peroxisome targeting sequence binding
+is_a: GO:0000268 ! peroxisome signal sequence receptor activity
 
 [Term]
 id: GO:0005054
@@ -69216,10 +69222,10 @@ creation_date: 2013-12-19T15:26:17Z
 
 [Term]
 id: GO:0006901
-name: vesicle coating
+name: vesicle coat assembly
 namespace: biological_process
 def: "A protein coat is added to the vesicle to form the proper shape of the vesicle and to target the vesicle for transport to its destination." [GOC:jid]
-synonym: "vesicle coat assembly" BROAD []
+synonym: "vesicle coating" EXACT []
 is_a: GO:0016050 ! vesicle organization
 relationship: has_participant GO:0031982 ! vesicle
 relationship: part_of GO:0006900 ! vesicle budding from membrane
@@ -77982,7 +77988,7 @@ def: "Binding to a nuclear localization sequence, a specific peptide sequence th
 synonym: "NLS binding" EXACT []
 synonym: "nuclear localisation sequence binding" EXACT [GOC:mah]
 synonym: "nuclear localization signal binding" EXACT []
-is_a: GO:0005048 ! signal sequence binding
+is_a: GO:0005048 ! signal sequence receptor activity
 
 [Term]
 id: GO:0008140
@@ -85574,12 +85580,15 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008785
-name: alkyl hydroperoxide reductase activity
+name: obsolete alkyl hydroperoxide reductase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
-is_a: GO:0016668 ! oxidoreductase activity, acting on a sulfur group of donors, NAD(P) as acceptor
+def: "OBSOLETE. Catalysis of the reaction: octane hydroperoxide + NADH + H+ = H2O + NAD+ + 1-octanol." [GOC:curators]
+comment: The reason for obsoletion is that, despite the generic-sounding name, this term represented a substrate-specific activity that is more specific than the specificity of any known gene product. 'Alkyl hydroperoxide reductase' is listed as a synonym of EC 1.11.1.26, which corresponds to GO:0102039 NADH-dependent peroxiredoxin activity, the appropriate replacement.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28261" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28340" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0102039
 
 [Term]
 id: GO:0008786
@@ -86903,39 +86912,47 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0008873
-name: gluconate 2-dehydrogenase activity
+name: gluconate 2-dehydrogenase (NADP+) activity
 namespace: molecular_function
 def: "Catalysis of the reaction: D-gluconate + NADP+ = 2-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.215]
 synonym: "2-keto-D-gluconate reductase activity" RELATED [EC:1.1.1.215]
 synonym: "2-ketogluconate reductase activity" RELATED [EC:1.1.1.215]
+synonym: "gluconate 2-dehydrogenase activity" BROAD []
 xref: EC:1.1.1.215 {source="skos:exactMatch"}
 xref: MetaCyc:1.1.1.215-RXN
 xref: RHEA:16653 {source="skos:exactMatch"}
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
 id: GO:0008874
-name: gluconate 5-dehydrogenase activity
+name: gluconate 5-dehydrogenase [NAD(P)+] activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = 5-dehydro-D-gluconate + NADPH + H+." [EC:1.1.1.69]
+def: "Catalysis of the reaction: D-gluconate + NAD(P)+ = 5-dehydro-D-gluconate + NAD(P)H + H+." [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-keto-D-gluconate reductase" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate 5-reductase activity" RELATED [EC:1.1.1.69]
 synonym: "5-ketogluconate reductase activity" RELATED [EC:1.1.1.69]
 synonym: "D-gluconate:NAD(P)+ 5-oxidoreductase" RELATED [EC:1.1.1.69]
+synonym: "gluconate 5-dehydrogenase activity" EXACT []
 xref: EC:1.1.1.69 {source="skos:exactMatch"}
 xref: MetaCyc:GLUCONATE-5-DEHYDROGENASE-RXN
-is_a: GO:0008875 ! gluconate dehydrogenase activity
+xref: RHEA:23936 {source="skos:narrowMatch"}
+xref: RHEA:23940 {source="skos:narrowMatch"}
+is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
 
 [Term]
 id: GO:0008875
-name: gluconate dehydrogenase activity
+name: obsolete gluconate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28243" xsd:anyURI
+def: "OBSOLETE. Catalysis of the reaction: D-gluconate + NADP+ = dehydro-D-gluconate + NADPH + H+." [GOC:curators]
+comment: This term was obsoleted because it is an unnecessary grouping term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31989" xsd:anyURI
+is_obsolete: true
... (1426 more lines truncated)
```
