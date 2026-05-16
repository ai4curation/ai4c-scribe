# PR #32028 — NTR: Terreic acid biosynthetic process

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31114](https://github.com/geneontology/go-ontology/issues/31114)
- **PR**: [#32028](https://github.com/geneontology/go-ontology/pull/32028)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-05-05
- **task_type**: axiom_repair
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: multi_term
- **review_outcome**: changes_requested

## Context

Issue #31114 originally requested new terms for terreic acid biosynthetic processes. During implementation, it was noticed that three terms had `created_by: PomBase:vw` instead of the expected GO convention. This PR attempted to fix them by changing to `GOC:vw`.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was changed from `PomBase:vw` to `GOC:vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

## Resolution

While the PR was merged, @pgaudet subsequently clarified that the correct format uses bare initials (`vw`) without any prefix. This prompted a follow-up PR (#32032) to make the final correction. This case demonstrates the importance of verifying metadata conventions with experienced curators rather than guessing at the pattern.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..eaa8ef407 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483087,7 +483087,7 @@ is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483097,7 +483097,7 @@ namespace: biological_process
 def: "Any process that  that stops, prevents, or reduces the frequency, rate or extent of carbohydrate utilization." [GOC:vw]
 is_a: GO:0043610 ! regulation of carbohydrate utilization
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31261" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-01-19T11:52:03Z
 
 [Term]
@@ -483109,7 +483109,7 @@ is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

## Agent Attempts (8)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#452](https://github.com/ai4curation/eval-ont-agent-go/pull/452)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25847219059](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847219059)
- **Workflow run**: [25847219059](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847219059)

#### Agent PR Comment

## Summary

This PR swaps the primary labels and synonyms for two terreic acid biosynthetic process terms and corrects their metadata, as requested in #31114.

## Changes Made

### GO:0180067 (terreic acid biosynthetic process)
- **Label**: Changed from "terreate biosynthetic process" → "terreic acid biosynthetic process"
- **Synonym**: Changed from "terreic acid biosynthetic process" → "terreate biosynthetic process" (RELATED)
- **Metadata**: Fixed `created_by` from "PomBase:vw" → "GOC:vw"

### GO:0180069 (positive regulation of terreic acid biosynthetic process)
- **Label**: Changed from "positive regulation of terreate biosynthetic process" → "positive regulation of terreic acid biosynthetic process"
- **Synonym**: Added "positive regulation of terreate biosynthetic process" (RELATED)
- **Metadata**: Fixed `created_by` from "PomBase:vw" → "GOC:vw"

## Rationale

The changes align with the biologist-friendly naming convention while maintaining correct chemical references:
- Primary labels now use "terreic acid" (the biologist-friendly name requested in the original issue)
- The "terreate" forms remain as synonyms for searchability
- Logical definitions continue to reference CHEBI:233617 (terreate, the pH 7.3 form)

This follows the established GO chemical-entity pattern where labels use common biological names while logical definitions use the appropriate pH 7.3 CHEBI terms.

## Checklist

- [x] EDITS: Terms checked out, edited, and checked in using obo-checkout.pl/obo-checkin.pl
- [x] METADATA: Fixed created_by field from "PomBase:vw" to "GOC:vw" as requested
- [x] RELATIONSHIPS: Logical definitions and relationships unchanged
- [x] CHANGES-COMMITTED: Changes committed to src/ontology/go-edit.obo with detailed commit message
- [x] ISSUE-ALIGNMENT: Changes match the request in issue #31114 comments from @ValWood and @pgaudet

## Validation

Note: Full validation (make travis_build) could not be completed in this environment due to missing dependencies (amm, robot). However, the changes are simple label/synonym swaps and metadata corrections to already-valid terms, maintaining all structural relationships and logical definitions.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847219059)


#### Agent Issue Comment

The requested changes have been completed in PR #<NN>:

- GO:0180067 and GO:0180069 now use "terreic acid biosynthetic process" as the primary label
- The "terreate biosynthetic process" forms are RELATED synonyms
- Fixed `created_by` from "PomBase:vw" to "GOC:vw" for both terms

The logical definitions remain unchanged, using CHEBI:233617 (terreate, pH 7.3 form) as per GO chemical-entity conventions.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847219059)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..ffd927318 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
 def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
 def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#451](https://github.com/ai4curation/eval-ont-agent-go/pull/451)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25775987534](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775987534)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..eaa8ef407 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483087,7 +483087,7 @@ is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483097,7 +483097,7 @@ namespace: biological_process
 def: "Any process that  that stops, prevents, or reduces the frequency, rate or extent of carbohydrate utilization." [GOC:vw]
 is_a: GO:0043610 ! regulation of carbohydrate utilization
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31261" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-01-19T11:52:03Z
 
 [Term]
@@ -483109,7 +483109,7 @@ is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#441](https://github.com/ai4curation/eval-ont-agent-go/pull/441)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25775948832](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775948832)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..eaa8ef407 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483087,7 +483087,7 @@ is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483097,7 +483097,7 @@ namespace: biological_process
 def: "Any process that  that stops, prevents, or reduces the frequency, rate or extent of carbohydrate utilization." [GOC:vw]
 is_a: GO:0043610 ! regulation of carbohydrate utilization
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31261" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-01-19T11:52:03Z
 
 [Term]
@@ -483109,7 +483109,7 @@ is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 4: claude-haiku-4.5 / claude

- **Eval PR**: [#411](https://github.com/ai4curation/eval-ont-agent-go/pull/411)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25761791566](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25761791566)
- **Workflow run**: [25761791566](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761791566)

#### Agent PR Comment

# Rename terreic acid biosynthetic process terms to use biologist-friendly labels

## Summary

This PR completes the label swap for GO:0180067 and GO:0180069 to align with the originally-requested term names and GO chemical-entity conventions. The terms now use biologist-friendly labels ("terreic acid") while maintaining the pH 7.3 CHEBI reference in the logical definitions.

## Changes

### GO:0180067 (terreic acid biosynthetic process)
- **Name**: 'terreate biosynthetic process' → 'terreic acid biosynthetic process'
- **Definition**: Updated text to reference "terreic acid" instead of "terreate"
- **Synonym**: 'terreic acid biosynthetic process' (was EXACT/primary) is now 'terreate biosynthetic process' (RELATED)
- **Logical definition**: Unchanged — still references CHEBI:233617 ! terreate (pH 7.3 form)
- **Metadata**: Fixed `created_by` from 'PomBase:vw' to 'vw'

### GO:0180069 (positive regulation of terreic acid biosynthetic process)
- **Name**: 'positive regulation of terreate biosynthetic process' → 'positive regulation of terreic acid biosynthetic process'
- **Definition**: Updated to standard GO positive regulation phrasing and references "terreic acid biosynthetic process"
- **Synonym**: Added 'positive regulation of terreate biosynthetic process' as RELATED
- **Logical definition**: Updated intersection_of reference to match new term name (GO:0180067)
- **Metadata**: Fixed `created_by` from 'PomBase:vw' to 'vw'

## Rationale

This follows GO chemical-entity conventions as documented in `.claude/skills/chemical-entity/SKILL.md`:
- Use biologist-friendly labels for term names (e.g., "terreic acid")
- Reference the pH 7.3 CHEBI form in logical definitions (CHEBI:233617 ! terreate)
- Exemplar: L-histidine transmembrane transporter activity uses the biologist-friendly label with CHEBI:57595 ! L-histidine zwitterion in the logical def

This addresses the user's request to swap labels and fixes the `created_by` metadata as requested in the issue comments.

## Validation

- Ontology structure validated: terms check out and check back in cleanly
- Logical definitions maintained: no changes to intersection_of axioms
- References unchanged: CHEBI:233617 ! terreate in logical definitions; PMID:25265334 in definitions
- No new IDs minted; this is a label swap only
- Both `is_a` and `intersection_of` relationships properly updated

## Checklist

- [x] PLAN: Issue analyzed and approach determined
- [x] RESEARCH: Background reviewed (terreate vs terreic acid relationship clarified in earlier comments)
- [x] TERM-SEARCH: Relevant terms (GO:0180067, GO:0180069) located and examined
- [x] EDITS: Checkin/checkout procedure followed; edits made in terms/ folder
- [x] RELATIONSHIPS: Logical definitions maintained; is_a and intersection_of properly updated
- [x] METADATA: created_by corrected; creation_date, term_tracker_item unchanged (existing terms)
- [x] SPECIALIZED-EDITS: Chemical-entity convention applied (biologist label + pH 7.3 CHEBI in def)
- [x] AUTOMATED-VALIDATION: Ontology structure valid; changes properly reflected in go-edit.obo
- [x] REFERENCE-VALIDATION: PMID:25265334 confirmed valid; CHEBI:233617 confirmed correct
- [x] CHANGES-COMMITTED: Single focused commit with detailed message

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761791566)


#### Agent Issue Comment

Changes committed in PR #<NN>

Completed the label swap for GO:0180067 and GO:0180069 to use biologist-friendly labels ("terreic acid" instead of "terreate") as requested, with the chemistry names as RELATED synonyms. Also fixed the `created_by` field from `PomBase:vw` to `vw`.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761791566)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..d3e085b18 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+def: "The chemical reactions and pathways resulting in the formation of terreic acid, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
-def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+def: "Any process that activates or increases the frequency, rate or extent of terreic acid biosynthetic process." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
-intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
+intersection_of: positively_regulates GO:0180067 ! terreic acid biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 5: claude-sonnet-4.5 / copilot

- **Eval PR**: [#375](https://github.com/ai4curation/eval-ont-agent-go/pull/375)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25752269531](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25752269531)
- **Workflow run**: [25752269531](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752269531)

#### Agent PR Comment

# PR: Swap primary names and synonyms for terreic acid biosynthesis terms

#### Agent Issue Comment

Changes committed in PR #<NN>.

**Summary of changes:**
- GO:0180067: Primary name changed from "terreate biosynthetic process" to "**terreic acid biosynthetic process**" (with "terreate biosynthetic process" now as a RELATED synonym)
- GO:0180069: Primary name changed from "positive regulation of terreate biosynthetic process" to "**positive regulation of terreic acid biosynthetic process**" (with "positive regulation of terreate biosynthetic process" now as a RELATED synonym)
- Both terms: Fixed `created_by` metadata from "PomBase:vw" to "vw" as requested by @pgaudet

The logical definitions remain unchanged and still reference `CHEBI:233617 ! terreate` (the pH 7.3 form), which aligns with GO's chemical-entity convention of using biologist-friendly labels while retaining the pH 7.3 form in the logical definition.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752269531)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..2cc4923c8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
 def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
 def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 6: claude-opus-4.7 / claude

- **Eval PR**: [#336](https://github.com/ai4curation/eval-ont-agent-go/pull/336)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25650673058](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650673058)
- **Workflow run**: [25650673058](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650673058)

#### Agent PR Comment

## Summary

Renames two existing terms (no new IDs minted) to the labels originally requested in issue #31114, and fixes the `created_by` value.

The terms were originally requested in #31114 as `terreic acid biosynthetic process` / `positive regulation of terreic acid biosynthetic process`, but were added in PR #31612 with `terreate` (the pH 7.3 chemistry name) as the primary label and `terreic acid` as a RELATED synonym. PR #31374 attempted the rename but was closed due to ID conflicts. PR #32014 was a previous attempt that was not merged.

This PR redoes the rename and folds in the `created_by` cleanup requested in [issue comment](https://github.com/geneontology/go-ontology/issues/31114#issuecomment-4377304070).

## Changes

| Term | Before | After |
| --- | --- | --- |
| GO:0180067 name | `terreate biosynthetic process` | `terreic acid biosynthetic process` |
| GO:0180067 RELATED synonym | `terreic acid biosynthetic process` | `terreate biosynthetic process` |
| GO:0180067 def | `...formation of terreate, a fungal metabolite...` | `...formation of terreic acid, a fungal metabolite...` |
| GO:0180067 created_by | `PomBase:vw` | `GOC:vw` |
| GO:0180069 name | `positive regulation of terreate biosynthetic process` | `positive regulation of terreic acid biosynthetic process` |
| GO:0180069 RELATED synonym | (none) | `positive regulation of terreate biosynthetic process` |
| GO:0180069 def | `Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate.` | `Any process that activates or increases the frequency, rate or extent of terreic acid biosynthetic process.` (standard positive-regulation phrasing) |
| GO:0180069 created_by | `PomBase:vw` | `GOC:vw` |

Logical definitions, asserted `is_a`, and `creation_date` are unchanged. The pH 7.3 form `CHEBI:233617 ! terreate` remains the chemical referenced in the equivalence axiom, in line with the chemical-entity skill convention (cf. the L-histidine exemplar: biologist-friendly label, pH 7.3 CHEBI in the logical def).

`term_tracker_item` already pointed to this issue.

## Rationale

- **Label swap**: pgaudet approved swapping the label and synonym in the [issue thread](https://github.com/geneontology/go-ontology/issues/31114#issuecomment-4371043399). Antonialock previously confirmed the term and `terrein biosynthetic process` (GO:0140880) describe distinct pathways with different gene clusters, so `terreic acid biosynthetic process` is a valid distinct term.
- **Definition rewording**: the GO:0180067 def needed `terreate` → `terreic acid` to mirror the new primary label. The GO:0180069 def was rewritten to match the standard `positive regulation of X` phrasing used elsewhere (cf. GO:1900378 `positive regulation of secondary metabolite biosynthetic process`).
- **`created_by` fix**: ValWood explicitly requested `GOC:vw`. Note that pgaudet's earlier suggestion was just `vw` (no prefix), which matches the dominant convention in the file (no `GOC:` prefixed `created_by` values exist elsewhere). I went with the more recent, explicit user instruction; flagged in the issue comment so this can be revisited if reviewers prefer plain `vw`.

## Checklist

- [x] PLAN: issue analyzed, intent clear (label/synonym swap + `created_by` fix).
- [x] PRE-VALIDATION: ontology validates (ROBOT SPARQL QC + ELK reasoning).
- [N/A] RESEARCH: no new biology — terms exist; this is a rename.
- [x] TERM-SEARCH: confirmed only GO:0180067 and GO:0180069 reference `terreate`/`terreic` in the edit file. No other terms cross-reference these by name.
- [N/A] DESIGN-PATTERNS: no structural change. Logical def already follows the `biosynthetic process` + `has_primary_output CHEBI` pattern; chemical-entity convention re-confirmed (label uses biologist form, axiom uses pH 7.3 CHEBI).
- [x] EDITS: used `obo-checkout.pl` / `obo-checkin.pl` workflow on `terms/`.
- [x] RELATIONSHIPS: unchanged. `intersection_of`, `is_a`, and `positively_regulates` axioms preserved.
- [N/A] SPECIALIZED-EDITS:
  - `/term-obsoletion`: N/A (no obsoletion).
  - `/chemical-entity`: applied — kept pH 7.3 `CHEBI:233617 ! terreate` in the logical def while exposing the biologist-friendly label.
  - `/reaction`: N/A (not a catalytic activity).
  - `/taxon-constraint`: N/A.
- [x] METADATA: `created_by` updated per request; `creation_date` and `term_tracker_item` preserved. No `created_by`/`creation_date` added to existing terms beyond fixing the malformed value.
- [x] AUTOMATED-VALIDATION: ROBOT SPARQL QC checks all PASS; ELK reasoning completes without error. (`make travis_build` not run in this environment — skipped due to missing Make targets/IO outside ROBOT, but core SPARQL QC + reasoning are the relevant checks for a rename.)
- [N/A] REFERENCE-VALIDATION: existing PMID:25265334 retained, no new references introduced.
- [x] CHANGES-COMMITTED: only `src/ontology/go-edit.obo` modified.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650673058)


#### Agent Issue Comment

@ValWood — done in PR #<NN>.

Both terms now use the originally-requested labels:

- **GO:0180067** `terreic acid biosynthetic process` (was `terreate biosynthetic process`)
- **GO:0180069** `positive regulation of terreic acid biosynthetic process` (was `positive regulation of terreate biosynthetic process`)

The previous primary labels are kept as RELATED synonyms. The logical definitions still reference `CHEBI:233617 ! terreate` (the pH 7.3 form), per the GO chemical-entity convention of biologist-friendly label + pH 7.3 CHEBI in the equivalence axiom.

`created_by` updated from `PomBase:vw` to `GOC:vw` as you requested. Note: @pgaudet's earlier suggestion was just `vw` (no prefix), which is the more common pattern in the file — let me know if you'd prefer that instead and I'll change it.

Validation: ROBOT SPARQL QC checks pass; ELK reasoning succeeds.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650673058)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..ff761b537 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+def: "The chemical reactions and pathways resulting in the formation of terreic acid, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
-def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+def: "Any process that activates or increases the frequency, rate or extent of terreic acid biosynthetic process." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
-intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
+intersection_of: positively_regulates GO:0180067 ! terreic acid biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 7: kimi-k2.6 / opencode

- **Eval PR**: [#267](https://github.com/ai4curation/eval-ont-agent-go/pull/267)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25646681853](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646681853)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..54cbaeeb3 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+def: "The chemical reactions and pathways resulting in the formation of terreic acid, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
-def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+def: "Any process that activates or increases the frequency, rate, or extent of terreic acid biosynthetic process." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
-intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
+intersection_of: positively_regulates GO:0180067 ! terreic acid biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

### Attempt 8: gemma-4-31b / opencode

- **Eval PR**: [#242](https://github.com/ai4curation/eval-ont-agent-go/pull/242)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25646632071](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646632071)
- **Workflow run**: [25646632071](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646632071)

#### Agent PR Comment

## Summary
Renamed `terreate biosynthetic process` to `terreic acid biosynthetic process` and its positive regulation child, following the GO chemical-entity convention of using biologist-friendly labels for names while keeping the pH 7.3 CHEBI ID in logical definitions.

## Changes
- **GO:0180067**: 
    - Name: `terreate biosynthetic process` -> `terreic acid biosynthetic process`
    - Definition: updated `terreate` to `terreic acid`
    - Synonym: added `terreate biosynthetic process` as RELATED
    - `created_by`: `PomBase:vw` -> `GOC:vw`
- **GO:0180069**: 
    - Name: `positive regulation of terreate biosynthetic process` -> `positive regulation of terreic acid biosynthetic process`
    - Definition: updated to standard 'positive regulation' phrasing and updated chemical name to `terreic acid`
    - Synonym: added `positive regulation of terreate biosynthetic process` as RELATED
    - `created_by`: `PomBase:vw` -> `GOC:vw`

## Validation
- Performed `obo-checkout` and `obo-checkin`.
- Ran `make go-edit.obo-check` which passed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646632071)


#### Agent Issue Comment

Changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646632071)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..274e543c7 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483079,15 +483079,15 @@ creation_date: 2025-06-27T07:22:01Z
 
 [Term]
 id: GO:0180067
-name: terreate biosynthetic process
+name: terreic acid biosynthetic process
 namespace: biological_process
-def: "The chemical reactions and pathways resulting in the formation of terreate, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
-synonym: "terreic acid biosynthetic process" RELATED []
+def: "The chemical reactions and pathways resulting in the formation of terreic acid, a fungal metabolite with ecological, antimicrobial, antiproliferative, and antioxidative activities." [PMID:25265334]
+synonym: "terreate biosynthetic process" RELATED []
 is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483102,14 +483102,15 @@ creation_date: 2026-01-19T11:52:03Z
 
 [Term]
 id: GO:0180069
-name: positive regulation of terreate biosynthetic process
+name: positive regulation of terreic acid biosynthetic process
 namespace: biological_process
-def: "Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of terreate." [PMID:25265334]
+def: "Any process that activates or increases the frequency, rate or extent of terreic acid biosynthetic process." [PMID:25265334]
+synonym: "positive regulation of terreate biosynthetic process" RELATED []
 is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```
