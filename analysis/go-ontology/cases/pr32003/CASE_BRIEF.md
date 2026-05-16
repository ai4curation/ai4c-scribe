# PR #32003 — Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31966](https://github.com/geneontology/go-ontology/issues/31966)
- **PR**: [#32003](https://github.com/geneontology/go-ontology/pull/32003)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-04-28
- **task_type**: obsoletion
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #31966 requested obsoletion of GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity". Per @sjm41's analysis, this term had no direct EC cross-reference, but "(R)-2-hydroxyisocaproate dehydrogenase" is listed as a synonym of EC:1.1.1.345, which corresponds to GO:0140175 "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity". The specific substrate (isocaproate) is just one instance of the broader (2R)-2-hydroxyacid class.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0043713 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0140175` for annotation migration
- Removed logical axioms
- The replacement points annotators to the correct broader activity term

## Resolution

Merged directly. The biochemical reasoning was clearly laid out in the issue: the specific substrate term (isocaproate) is subsumed by the generic substrate class term ((2R)-2-hydroxyacid). This is a typical enzyme term consolidation where overly specific terms are replaced by appropriately general ones that match EC classification granularity.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..55fadafbd 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. "(R)-2-hydroxyisocaproate dehydrogenase" is a synonym of EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase (NAD+)), which is the exact match xref of GO:0140175. The reaction catalyzed (involving (R)-2-hydroxy-4-methylpentanoate / 2-oxoisocaproate, RHEA:10052) is a narrowMatch instance of the more general reaction in GO:0140175.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

## Agent Attempts (11)

### Attempt 1: gpt-5.4 / codex

- **Eval PR**: [#189](https://github.com/ai4curation/eval-ont-agent-go/pull/189)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640337905](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640337905)

#### Agent PR Comment

Obsoleted `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` as redundant with `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.

Rationale:
- `GO:0140175` already has `EC:1.1.1.345` as an exact-match xref.
- The issue rationale ties `(R)-2-hydroxyisocaproate dehydrogenase` to that EC class and to `RHEA:10052`, which is already a `skos:narrowMatch` xref on `GO:0140175`.
- This makes `GO:0043713` a redundant specific term rather than a distinct MF term that should remain active.

Edits made:
- Converted `GO:0043713` to an obsolete stanza.
- Preserved the original definition provenance by prefixing the definition with `OBSOLETE.`.
- Removed the active-term parentage.
- Added an obsoletion comment explaining the equivalence and reaction/EC basis.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`.

Validation and checks:
- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-validation: `cd src/ontology && make travis_build` passed after edits.
- Term search: inspected `GO:0043713` and `GO:0140175` in `src/ontology/go-edit.obo`.
- Design-pattern review: no new DP/logical definition work was needed because this was a direct obsoletion.
- Specialized guidance reviewed: `/term-obsoletion`, `/reaction`, `/chemical-entity`.
- Reference validation: N/A, no new references were introduced.

Environment limitation:
- The usual OAK-based annotation/usages checks could not be run because `runoak` fails in this environment with an `oaklib/linkml` import error. I therefore relied on the issue context and repo-local ontology inspection for impact assessment.

Checklist:
- [x] PLAN: The issue and context were analyzed and the intent was clear.
- [x] PRE-VALIDATION: Current ontology state validated before edits.
- [x] RESEARCH: N/A; no new biology or references were introduced.
- [x] TERM-SEARCH: Relevant GO terms were inspected.
- [x] DESIGN-PATTERNS: Reviewed; no DP changes required.
- [x] EDITS: Used checkout/checkin workflow via `terms/`.
- [x] RELATIONSHIPS: Removed active axioms from the obsolete term and used `replaced_by`.
- [x] SPECIALIZED-EDITS: Relevant obsoletion/reaction/chemical guidance reviewed.
- [x] METADATA: Obsoletion metadata and tracker link added.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: N/A; no new PMIDs/xrefs added.
- [x] CHANGES-COMMITTED
- [x] RELEVANT-FILES: Only `src/ontology/go-edit.obo` was committed.
- [x] ACCURACY: Change matches the EC/RHEA-based redundancy described in the issue.
- [x] ISSUE-ALIGNMENT: Change is scoped to obsoleting the requested term.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640337905)


#### Agent Issue Comment

Implemented in PR #<NN>.

Obsoleted `GO:0043713` and replaced it with `GO:0140175` because the former is redundant with the generic `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` term already carrying the relevant EC/RHEA mappings. The obsolete term now has a direct `replaced_by` and obsoletion comment preserving the rationale.

Validation:
- `make travis_build` passed before and after the change.

One environment note: the usual `runoak` annotation/usages checks could not be run here because of a local `oaklib/linkml` import error, so I relied on the issue context plus repo-local inspection for impact assessment.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640337905)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..55fadafbd 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. "(R)-2-hydroxyisocaproate dehydrogenase" is a synonym of EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase (NAD+)), which is the exact match xref of GO:0140175. The reaction catalyzed (involving (R)-2-hydroxy-4-methylpentanoate / 2-oxoisocaproate, RHEA:10052) is a narrowMatch instance of the more general reaction in GO:0140175.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/189
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 189 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and replaced it with `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`. Its diff matches the human PR exactly, so the metadiff F1/precision/recall of 1.0 accurately reflects a complete and tightly scoped solution.


## Strengths

- Selected the exact target term from issue `#31966`, `GO:0043713`, and the exact replacement requested by the curator, `GO:0140175`.
- Followed the GO obsoletion pattern correctly: changed the label to `obsolete ...`, prefixed the definition with `OBSOLETE.`, removed the active `is_a: GO:0016616` parent, added `is_obsolete: true`, and added `replaced_by: GO:0140175`.
- Preserved the full curator-facing obsoletion rationale from the human PR, including the link between `(R)-2-hydroxyisocaproate dehydrogenase`, `EC:1.1.1.345`, the exact-match xref on `GO:0140175`, and the `RHEA:10052` narrowMatch reaction.
- Added the correct tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the edit limited to the `GO:0043713` stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.


## Issues

- No issues found. The agent PR is equivalent to the merged human solution for this single-term obsoletion.

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#502](https://github.com/ai4curation/eval-ont-agent-go/pull/502)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25888597175](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25888597175)
- **Workflow run**: [25888597175](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888597175)

#### Agent PR Comment

# Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity

## Summary
This PR obsoletes GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity and replaces it with GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity, as requested in issue #31966.

## Changes Made

### Modified Terms
- **GO:0043713** - Obsoleted with direct replacement by GO:0140175
  - Changed name to: `obsolete (R)-2-hydroxyisocaproate dehydrogenase activity`
  - Changed definition to: `OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+.`
  - Removed `is_a` relationship (GO:0016616)
  - Added `is_obsolete: true`
  - Added `replaced_by: GO:0140175`
  - Added obsoletion comment explaining equivalence to GO:0140175
  - Added `term_tracker_item` linking to issue #31966

## Rationale

The original issue identified that:
1. GO:0043713 represents a specific (R)-2-hydroxyisocaproate dehydrogenase activity
2. "(R)-2-hydroxyisocaproate dehydrogenase" is a synonym of EC:1.1.1.345 D-2-hydroxyacid dehydrogenase (NAD+)
3. EC:1.1.1.345 corresponds to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity
4. The specific RHEA reaction (RHEA:10052) for the (R)-2-hydroxyisocaproate conversion is already captured as a narrowMatch xref on GO:0140175
5. CHEBI:55535 ((2R)-hydroxy-4-methylpentanoate) is the conjugate base of the substrate in the specific reaction

GO:0043713 represents a narrower, specific case of the broader enzymatic activity already captured by GO:0140175. Since the specific reaction is already represented through RHEA mappings on the replacement term, maintaining a separate GO term for this specific activity creates unnecessary redundancy.

## Impact Analysis

### ✅ Pre-validation
- Ontology validated successfully before changes

### ✅ Ontology References
- Searched for all references to GO:0043713 in go-edit.obo
- **Result:** No other terms reference GO:0043713 (only its own stanza)
- No rewiring required

### ✅ Annotation Impact
- Checked for annotations using `runoak -i amigo: associations GO:0043713`
- **Result:** 0 annotations found
- No annotation migration required

### ✅ Post-validation
All validation tests passed:
- ✅ SPARQL QC checks (16 queries): 0 violations
  - equivalent-classes-violation
  - trailing-whitespace-violation  
  - owldef-self-reference-violation
  - synonym-label-match-violation
  - replacedby-obsolete-violation
  - replacedby-namespace-violation
  - missing-namespace-violation
  - duplicate-exact-synonym-violation
  - duplicate-synonym-violation
  - non-IRI-value-violation
  - non-anyURI-value-violation
  - obsolete-definition-violation
  - definition-constraints-violation
  - one-to-one-xrefs-by-subject-violation
  - one-to-one-xrefs-by-value-violation
  - xref-syntax-violation
- ✅ ELK reasoner: no errors

## Checklist

- [x] PLAN: Issue analyzed and plan created
- [x] PRE-VALIDATION: Current ontology validates before changes
- [x] TERM-SEARCH: Both GO:0043713 and GO:0140175 found and verified
- [x] DESIGN-PATTERNS: Term obsoletion skill used to ensure proper procedure
- [x] EDITS: Followed checkout/edit/checkin procedure
  - [x] Checked out term using obo-checkout.pl
  - [x] Made obsoletion edits following standard pattern
  - [x] Checked in term using obo-checkin.pl
- [x] RELATIONSHIPS: Removed is_a relationship as required for obsolete terms
- [x] METADATA: Correct obsoletion metadata added
  - [x] is_obsolete: true
  - [x] name prefixed with "obsolete"
  - [x] def prefixed with "OBSOLETE."
  - [x] comment explaining reason for obsoletion
  - [x] term_tracker_item linking to issue #31966
  - [x] replaced_by pointing to GO:0140175
- [x] SPECIALIZED-EDITS: N/A (straightforward obsoletion with direct replacement)
- [x] AUTOMATED-VALIDATION: All SPARQL checks and ELK reasoning passed
- [x] REFERENCE-VALIDATION: Original PMID:16957230 retained in obsolete definition
- [x] CHANGES-COMMITTED:
  - [x] RELEVANT-FILES: Only go-edit.obo modified and committed
  - [x] ACCURACY: Obsoletion is biologically justified based on EC and RHEA mappings
  - [x] ISSUE-ALIGNMENT: Changes directly address issue #31966 request
  - [x] PR created with detailed description
  - [x] Issue updated with summary
  
## Files Changed
- `src/ontology/go-edit.obo` - Obsoleted GO:0043713

Fixes #31966

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888597175)


#### Agent Issue Comment

GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity has been obsoleted and replaced by GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.

**Impact Analysis:**
- No ontology terms referenced GO:0043713 (except its own stanza)
- Zero annotations to GO:0043713 (confirmed via amigo search)
- Clean obsoletion with no downstream impacts

**Rationale:**
The specific reaction catalyzed in GO:0043713 is a narrower case of the broader activity represented by GO:0140175. The RHEA reaction (RHEA:10052) corresponding to the specific (R)-2-hydroxyisocaproate conversion is already captured as a narrowMatch xref on GO:0140175, which maps to EC:1.1.1.345.

Changes committed in PR #<NN>

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888597175)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#477](https://github.com/ai4curation/eval-ont-agent-go/pull/477)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25847321933](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847321933)
- **Workflow run**: [25847321933](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847321933)

#### Agent PR Comment

# Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity

This PR obsoletes GO:0043713 and replaces it with GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity, addressing issue #31966.

## Rationale

GO:0043713 describes a specific enzymatic activity that is already captured by the broader term GO:0140175:

- **GO:0043713**: Specific to (R)-2-hydroxyisocaproate
- **GO:0140175**: Covers all (2R)-2-hydroxyacids, including (R)-2-hydroxyisocaproate

The equivalence is supported by:
1. EC:1.1.1.345 "D-2-hydroxyacid dehydrogenase (NAD+)" explicitly lists "(R)-2-hydroxyisocaproate dehydrogenase" as a synonym
2. GO:0140175 is mapped to EC:1.1.1.345 (exactMatch)
3. RHEA:10052, which describes the specific reaction with (2R)-hydroxy-4-methylpentanoate (systematic name for (R)-2-hydroxyisocaproate), is listed as a narrowMatch xref on GO:0140175

## Research Conducted

Comprehensive research was performed to verify the biological and chemical relationships:

### EC and RHEA Verification
- Confirmed EC:1.1.1.345 synonyms include both "D-2-hydroxyisocaproate dehydrogenase" and "(R)-2-hydroxyisocaproate dehydrogenase"
- Verified RHEA:10052 involves the same substrate using systematic nomenclature
- Sources: BRENDA, ExplorEnz, EXPASY ENZYME databases

### Chemical Nomenclature
- CHEBI:55534 is (R)-2-hydroxy-4-methylpentanoic acid, synonym "(R)-2-hydroxyisocaproic acid"
- CHEBI:55535 is the conjugate base (R)-2-hydroxy-4-methylpentanoate
- "Isocaproate" and "4-methylpentanoate" refer to the same structure

### Literature Support
- PMID:16957230 (Kim et al., 2006) characterizes (R)-2-hydroxyisocaproate dehydrogenase from C. difficile
- The enzyme is stereospecific for the R-isomer
- Substrates: 2-oxoisocaproate + NADH → (R)-2-hydroxyisocaproate + NAD+

Full research findings documented in accompanying research notes.

## Impact Analysis

### Annotations
- **Direct annotations**: 0 found (verified via `runoak -i amigo: associations GO:0043713`)
- **No annotation migration required**

### External Dependencies
- **Ubergraph analysis**: Only internal is_a relationship to GO:0016616
- No external ontologies reference this term
- No rewiring of relationships required

### Ontology References
- **Internal references**: None found (verified via grep)
- No other GO terms use GO:0043713 in axioms

## Changes Made

### GO:0043713 Obsoletion
- ✓ Added "obsolete" prefix to name
- ✓ Added "OBSOLETE." prefix to definition
- ✓ Removed is_a relationship to GO:0016616
- ✓ Added `is_obsolete: true` tag
- ✓ Added `replaced_by: GO:0140175` tag
- ✓ Added comment explaining reason for obsoletion
- ✓ Added term_tracker_item linking to issue #31966
- ✓ Retained namespace (molecular_function)
- ✓ Retained original definition provenance (GOC:jl, PMID:16957230)

### Verification
- ✓ Replacement term GO:0140175 exists and is active
- ✓ GO:0140175 has appropriate EC and RHEA xrefs
- ✓ No synonyms retained on obsolete term
- ✓ All logical axioms removed from obsolete term

## Complete Checklist

- [x] **PLAN**: Issue analyzed, intent clear, plan created
- [x] **PRE-VALIDATION**: Ontology state verified before changes
- [x] **RESEARCH**: Background research performed using /research skill
  - [x] EC:1.1.1.345 synonyms verified
  - [x] RHEA:10052 relationship confirmed
  - [x] CHEBI nomenclature verified
  - [x] PMID:16957230 validated
- [x] **TERM-SEARCH**: Relevant terms located and examined
  - [x] GO:0043713 structure analyzed
  - [x] GO:0140175 structure analyzed
  - [x] Confirmed equivalence relationship
- [x] **DESIGN-PATTERNS**: N/A (term obsoletion, not creation/modification)
- [x] **EDITS**: Correct checkout/checkin procedure followed
  - [x] Term checked out to terms/GO_0043713.obo
  - [x] Obsoletion changes applied
  - [x] Term checked back in to src/ontology/go-edit.obo
- [x] **RELATIONSHIPS**: N/A (obsoletion removes relationships)
- [x] **SPECIALIZED-EDITS**: /term-obsoletion skill used
  - [x] Impact on annotations analyzed (0 found)
  - [x] Impact on external ontologies analyzed (none found)
  - [x] Impact on internal references analyzed (none found)
  - [x] Proper obsoletion format followed
  - [x] No rewiring required
- [x] **METADATA**: Obsoletion metadata is correct
  - [x] is_obsolete: true present
  - [x] replaced_by: GO:0140175 present
  - [x] Comment with reason present
  - [x] term_tracker_item linking to issue #31966
  - [x] Original definition provenance retained
  - [x] No inappropriate metadata added/retained
- [x] **AUTOMATED-VALIDATION**: Validation attempted
  - Note: Full travis_build encountered environment dependency issue (missing amm tool)
  - Obsoletion format manually verified to be correct
  - Syntax validation confirmed
  - Replacement term existence verified
- [x] **REFERENCE-VALIDATION**: All references validated
  - [x] PMID:16957230 cached and verified
  - [x] No new references introduced
  - [x] Original definition provenance retained correctly
- [x] **CHANGES-COMMITTED**
  - [x] **RELEVANT-FILES**: Only src/ontology/go-edit.obo committed
  - [x] **ACCURACY**: Changes are biologically correct (research-backed)
  - [x] **ISSUE-ALIGNMENT**: Changes address issue request completely
  - [x] **PR**: Commit made with detailed message
  - [x] **COMMUNICATION**: Issue and PR comments prepared

## Files Modified

- `src/ontology/go-edit.obo`: GO:0043713 obsoleted with proper metadata

## Notes for Reviewers

The obsoletion is straightforward with zero impact:
- No annotations to migrate
- No external dependencies
- No internal references to rewire
- Direct equivalence relationship confirmed by multiple authoritative sources (EC, RHEA, literature)

The term can be safely obsoleted as requested.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847321933)


#### Agent Issue Comment

GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity has been successfully obsoleted and replaced with GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.

## Summary

The obsoletion has been completed as requested. Research confirmed that:
- EC:1.1.1.345 "D-2-hydroxyacid dehydrogenase (NAD+)" includes "(R)-2-hydroxyisocaproate dehydrogenase" as an accepted synonym
- GO:0140175 is already properly mapped to EC:1.1.1.345 with exactMatch
- RHEA:10052 (the reaction involving (2R)-hydroxy-4-methylpentanoate, aka (R)-2-hydroxyisocaproate) is listed as a narrowMatch xref on GO:0140175
- The activity described by GO:0043713 represents a specific instance of the broader activity already captured by GO:0140175

## Impact Analysis

- **Annotations**: 0 annotations found (verified via runoak)
- **External dependencies**: Only internal relationship to GO:0016616
- **Ontology references**: No other GO terms reference GO:0043713
- **Rewiring**: None required

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847321933)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..c25b55b80 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. The activity described by GO:0043713 represents a specific instance of the broader enzymatic activity already captured by GO:0140175, which is properly mapped to EC:1.1.1.345 where "(R)-2-hydroxyisocaproate dehydrogenase" is listed as a synonym.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 4: claude-sonnet-4.5 / copilot

- **Eval PR**: [#430](https://github.com/ai4curation/eval-ont-agent-go/pull/430)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25775243342](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775243342)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 5: claude-opus-4.7 / claude

- **Eval PR**: [#340](https://github.com/ai4curation/eval-ont-agent-go/pull/340)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25650702963](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650702963)
- **Workflow run**: [25650702963](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650702963)

#### Agent PR Comment

# Obsolete GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity

Closes geneontology/go-ontology#31966.

## Summary

`GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity` has been obsoleted with a direct replacement by `GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.

## Rationale

Provided by the issue, and verified against the edit file:

- `GO:0140175` carries `xref: EC:1.1.1.345 {source="skos:exactMatch"}`. EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase (NAD+)) lists "(R)-2-hydroxyisocaproate dehydrogenase" as a synonym.
- `(R)-2-hydroxyisocaproate` is `(R)-2-hydroxy-4-methylpentanoic acid` (CHEBI:55534); its conjugate base (2R)-hydroxy-4-methylpentanoate (CHEBI:55535) is the substrate of RHEA:10052, which is already present on `GO:0140175` as `xref: RHEA:10052 {source="skos:narrowMatch"}`.
- Hence the obsoleted reaction is just the specific (R)-2-hydroxyisocaproate / 2-oxoisocaproate instance of the general (2R)-2-hydroxyacid / 2-oxocarboxylate reaction captured by GO:0140175.
- The obsoleted term had no annotations (per the issue).

## Diff

Only `src/ontology/go-edit.obo` was modified. The obsoleted stanza now reads:

```
[Term]
id: GO:0043713
name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
namespace: molecular_function
def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. ...
property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
is_obsolete: true
replaced_by: GO:0140175
```

Logical axioms (`is_a: GO:0016616`) were removed as required for obsolete terms.

## Checklist

- [x] PLAN: Issue analysed; intent is clear (direct-replacement obsoletion).
- [x] PRE-VALIDATION: N/A in this environment - `make travis_build` cannot run locally because `robot` and `amm` are not installed in this container. The ontology was inspected with `obo-grep.pl` before edits; the file parses cleanly and the target term resolved as expected.
- [x] RESEARCH: N/A - the case is fully justified by the existing xrefs on the replacement term (`EC:1.1.1.345`, RHEA:10052) and CHEBI relationships cited in the issue; no further literature work needed.
- [x] TERM-SEARCH: Confirmed `GO:0043713` and `GO:0140175` via `obo-grep.pl` on `src/ontology/go-edit.obo`. No other GO terms reference `GO:0043713` (verified with `obo-grep.pl GO:0043713`).
- [x] DESIGN-PATTERNS: N/A - obsoletion only; no new logical definition.
- [x] EDITS: Used `obo-checkout.pl` -> edit in `terms/GO_0043713.obo` -> `obo-checkin.pl`.
- [x] RELATIONSHIPS: All `is_a`/`relationship`/`intersection_of` tags removed from the obsoleted term, per the term-obsoletion skill.
- [x] SPECIALIZED-EDITS: Followed `/term-obsoletion` skill (category 1, direct replacement). `/reaction` and `/chemical-entity` considerations: confirmed the CHEBI/RHEA chain from the issue resolves the substrate identity (CHEBI:55534 acid <-> CHEBI:55535 conjugate base, substrate of RHEA:10052).
- [x] METADATA: `name`, `def`, `namespace` retained per obsoletion convention; obsoletion `comment`, `term_tracker_item`, `is_obsolete: true`, and `replaced_by: GO:0140175` added. No `created_by`/`creation_date` touched (not a new term).
- [ ] AUTOMATED-VALIDATION: Could not run `make travis_build` locally - `robot` and `amm` are not installed in this environment. Build will run in CI on this PR.
- [x] REFERENCE-VALIDATION: No new references introduced. The retained `PMID:16957230` was already on the term.
- [x] CHANGES-COMMITTED: One commit on `src/ontology/go-edit.obo`.

## Annotation impact

Per the issue, `GO:0043713` has zero annotations. `runoak -i amigo: associations` cannot run in this environment (the local `oaklib` install has a `linkml` `Format.JSON` import error), so this was not re-verified here, but the requester stated 0 annotations.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650702963)


#### Agent Issue Comment

GO:0043713 has been obsoleted with `replaced_by: GO:0140175` ((2R)-2-hydroxyacid dehydrogenase (NAD+) activity), as requested. The reason is captured in the obsoletion comment: '(R)-2-hydroxyisocaproate dehydrogenase' is a synonym of EC:1.1.1.345 (the exactMatch xref of GO:0140175), and the specific reaction (RHEA:10052) is already present as a narrowMatch xref on GO:0140175. No annotations are affected.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650702963)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..0bba8e8b2 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity. The substrate (R)-2-hydroxyisocaproate is a specific (2R)-2-hydroxyacid, and '(R)-2-hydroxyisocaproate dehydrogenase' is listed as a synonym of EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase (NAD+)), which is the exact match for GO:0140175. RHEA:10052 ((2R)-hydroxy-4-methylpentanoate + NAD+ = 4-methyl-2-oxopentanoate + NADH + H+) is a narrowMatch xref on GO:0140175 and captures this specific reaction.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 6: kimi-k2.6 / opencode

- **Eval PR**: [#275](https://github.com/ai4curation/eval-ont-agent-go/pull/275)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25646706883](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646706883)
- **Workflow run**: [25646706883](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646706883)

#### Agent PR Comment

Obsoletion of GO:0043713

## Summary
This PR obsoletes GO:0043713 `(R)-2-hydroxyisocaproate dehydrogenase activity` because it is equivalent to the existing GO:0140175 `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.

## Changes made
- GO:0043713 was modified to an obsolete term with `replaced_by: GO:0140175`
  - Name prefixed with `obsolete`
  - Definition prefixed with `OBSOLETE.`
  - Removed `is_a` relationship
  - Added obsoletion comment, `term_tracker_item`, and `is_obsolete: true`

## Rationale
As outlined in issue #31966, the substrate specificity of GO:0043713 is covered by the broader EC:1.1.1.345 / RHEA:35643 reaction captured in GO:0140175. One of the narrowMatch RHEA reactions for GO:0140175 (RHEA:10052) specifically describes the same 4-methyl-2-oxopentanoate / (2R)-hydroxy-4-methylpentanoate interconversion, confirming equivalence. Since GO:0043713 had no annotations, a direct replacement obsoletion is the cleanest path.

## Checklist
- [x] PLAN: Issue analyzed and intent is clear
- [x] PRE-VALIDATION: Searched for build tooling (robot/amm unavailable in this environment; checked file syntax and stanza structure manually)
- [x] TERM-SEARCH: Confirmed GO:0043713 exists and GO:0140175 is the appropriate replacement
- [x] DESIGN-PATTERNS: Followed standard GO obsoletion pattern (name, def, no logical axioms, replaced_by)
- [x] EDITS: Used obo-checkout.pl / obo-checkin.pl workflow
- [x] RELATIONSHIPS: Removed all logical axioms from obsolete term; no other terms reference GO:0043713
- [x] SPECIALIZED-EDITS: Term-obsoletion skill applied
- [x] METADATA:
  - Term tracker item points to issue #31966
  - Original definition provenance retained (GOC:jl, PMID:16957230)
  - No created_by/creation_date added (existing term)
- [x] REFERENCE-VALIDATION: No new references introduced
- [x] CHANGES-COMMITTED: Single commit on `src/ontology/go-edit.obo`

## Impact assessment
- **Annotations**: 0 direct annotations to GO:0043713
- **Ontology references**: No other GO terms reference GO:0043713
- **External mappings**: None identified in the edit file

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646706883)


#### Agent Issue Comment

Changes committed in PR #<NN>.

GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity has been obsoleted and replaced by GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity, as discussed in the issue. No external references to GO:0043713 were found in the ontology, so no rewiring of other terms was needed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646706883)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 7: gemma-4-31b / opencode

- **Eval PR**: [#246](https://github.com/ai4curation/eval-ont-agent-go/pull/246)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Trace**: [25646657698](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646657698)
- **Workflow run**: [25646657698](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646657698)

#### Agent PR Comment

## Summary of Changes
Obsoleted GO:0043713 ((R)-2-hydroxyisocaproate dehydrogenase activity) and replaced it with GO:0140175 ((2R)-2-hydroxyacid dehydrogenase (NAD+) activity).

#### Agent Issue Comment

Changes committed in PR #<NN>

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646657698)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fa9725a6 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 ((2R)-2-hydroxyacid dehydrogenase (NAD+) activity).
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

### Attempt 8: claude-haiku-4.5 / claude

- **Eval PR**: [#213](https://github.com/ai4curation/eval-ont-agent-go/pull/213)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Workflow run**: [25640387995](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640387995)

#### Agent PR Comment

## Obsoletion of GO:0043713

### Summary of Changes

GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity has been obsoleted and replaced with GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.

### Rationale

- **Equivalence**: GO:0043713 represents the specific enzyme (R)-2-hydroxyisocaproate dehydrogenase, which is actually a synonym of EC:1.1.1.345 (D-2-hydroxyacid dehydrogenase).
- **Better term**: GO:0140175 provides more general and accurate coverage of 2-hydroxyacid dehydrogenase enzymes with proper enzyme cross-references (EC:1.1.1.345) and RHEA mappings.
- **Substrate alignment**: (R)-2-hydroxyisocaproate is chemically equivalent to (2R)-hydroxy-4-methylpentanoate, which is covered by the RHEA reactions in GO:0140175.

### Impact Assessment

- **Annotations**: GO:0043713 has 0 annotations - no annotation migration required.
- **Other term references**: No other GO terms reference GO:0043713.
- **External ontologies**: No external ontology dependencies identified.

### Changes Made

**File**: `src/ontology/go-edit.obo`

**Term Structure (GO:0043713)**:
- Updated name to: `obsolete (R)-2-hydroxyisocaproate dehydrogenase activity`
- Updated definition to: `OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+.`
- Removed: `is_a` relationship
- Added: `is_obsolete: true`
- Added: `replaced_by: GO:0140175`
- Added: `comment` explaining the reason for obsoletion
- Added: `property_value: term_tracker_item` linking to issue #31966

### Validation Checklist

- [x] Issue and context analyzed
- [x] Pre-validation: ontology structure verified
- [x] Term search: both GO:0043713 and GO:0140175 examined
- [x] Impact assessment: no annotations or references to migrate
- [x] Obsoletion: proper metadata applied following GO conventions
- [x] Metadata: term_tracker_item correctly linked to GitHub issue
- [x] Changes committed: single focused commit with detailed message

### Notes

This is a straightforward obsoletion with direct replacement. The replacement term GO:0140175 is more general and appropriately captures the enzyme function with proper cross-references to enzyme databases.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640387995)

#### Agent Issue Comment

## Obsoletion Complete

GO:0043713 (R)-2-hydroxyisocaproate dehydrogenase activity has been successfully obsoleted and replaced by GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.

**Summary of changes:**
- Term obsoleted with `replaced_by` link to GO:0140175
- No annotations to migrate (term has 0 annotations)
- No other terms reference this term
- Changes committed to PR #<NN>

The replacement term (GO:0140175) provides more general and accurate coverage of 2-hydroxyacid dehydrogenase enzymes with proper enzyme cross-references and RHEA mappings.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640387995)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..9559c8fc6 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to (2R)-2-hydroxyacid dehydrogenase (NAD+) activity (GO:0140175), which provides more general coverage of 2-hydroxyacid dehydrogenase enzymes.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

#### Review by gpt-5-codex

**outcome**: success  **f1**: 0.889  **precision**: 0.889  **recall**: 0.889

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/213
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 213 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue #31966 by obsoleting GO:0043713 `(R)-2-hydroxyisocaproate dehydrogenase activity` and replacing it with GO:0140175 `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`. Its diff matches the human PR in all functional ontology changes: obsolete label, `OBSOLETE.` definition prefix, removal of the `is_a` parent, `is_obsolete: true`, `replaced_by: GO:0140175`, and issue tracker metadata. The metadiff F1 of 0.889 slightly under-represents the practical quality because the only substantive divergence is the shorter obsoletion comment.


## Strengths

- Correctly identified GO:0140175 as the replacement term requested in the issue, based on EC:1.1.1.345 and the relationship between the GO:0043713 reaction and the broader `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.
- Correctly obsoleted GO:0043713 by prefixing the label with `obsolete`, prefixing the definition with `OBSOLETE.`, removing the active `is_a: GO:0016616` classification, and adding `is_obsolete: true`.
- Added the key replacement metadata `replaced_by: GO:0140175`, preserving a direct migration target for users and annotations.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`, matching the human PR's traceability pattern.
- Kept the edit tightly scoped to the single affected term in `src/ontology/go-edit.obo`; it did not make unrelated ontology changes.
- The agent's PR notes correctly reported that GO:0043713 had 0 annotations and no other GO term references, so no annotation migration or dependent-term cleanup was needed.


## Issues

- No significant correctness issues. The only difference from the human PR is that the agent's obsoletion `comment` is much shorter: it says GO:0140175 provides more general coverage, while the human PR also records the EC:1.1.1.345 synonym evidence and the RHEA:10052 / CHEBI rationale from the issue. The agent's comment is acceptable for this straightforward obsoletion, but the human version is more useful provenance for future curators.

### Attempt 9: gpt-5.5 / opencode

- **Eval PR**: [#161](https://github.com/ai4curation/eval-ont-agent-go/pull/161)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Workflow run**: [25633614723](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633614723)

#### Agent PR Comment

## Summary

Obsoleted GO:0043713 `(R)-2-hydroxyisocaproate dehydrogenase activity` because it is equivalent to GO:0140175 `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.

Changes made in `src/ontology/go-edit.obo`:

- Renamed GO:0043713 to `obsolete (R)-2-hydroxyisocaproate dehydrogenase activity`.
- Prefixed the original definition with `OBSOLETE.` while preserving the original definition xrefs.
- Removed the asserted `is_a` parent from the obsolete term.
- Added an obsoletion comment explaining equivalence to GO:0140175.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`.

GO:0140175 already carries the relevant EC/RHEA mappings, including `EC:1.1.1.345` as an exact match and `RHEA:10052` as a narrow match for the specific substrate reaction discussed in the issue.

## Validation

- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-edit validation: `cd src/ontology && make travis_build` passed after edits.
- Ontology-internal usage check: `obo-grep.pl --noheader -r 'GO:0043713' src/ontology/go-edit.obo` now returns only the obsolete term stanza itself.
- Annotation impact: the issue reports 0 annotations. I attempted to query OAK/amigo and ubergraph, but the local `runoak` installation fails on import with a LinkML/SSSOM dependency error in this environment, so the live query could not be completed here.

## Checklist

- [x] PLAN: Issue context reviewed; requested action is clear: obsolete GO:0043713 with direct replacement GO:0140175.
- [x] PRE-VALIDATION: Current ontology validated successfully before edits using `make travis_build`.
- [x] RESEARCH: N/A; no new references or new biological claims were introduced beyond the supplied issue rationale and existing replacement-term mappings.
- [x] TERM-SEARCH: Existing GO terms GO:0043713 and GO:0140175 were inspected with `obo-grep.pl`.
- [x] DESIGN-PATTERNS: Obsoletion pattern applied; no new logical definition or new term pattern was needed.
- [x] EDITS: Followed checkout/edit/checkin workflow using `obo-checkout.pl` and `obo-checkin.pl` via `terms/GO_0043713.obo`.
- [x] RELATIONSHIPS: Removed asserted parent from obsolete term; added direct `replaced_by: GO:0140175`.
  - [x] Logical definitions are N/A; obsolete term has no logical axioms.
  - [x] Relationships conform to GO obsoletion practice.
  - [x] `is_a` is not over-asserted; obsolete term has no `is_a`.
- [x] SPECIALIZED-EDITS:
  - [x] term-obsoletion skill used.
  - [x] reaction skill consulted because this is a catalytic activity term with EC/RHEA context.
  - [x] chemical-entity skill consulted because the issue discusses ChEBI chemical entities/protonation.
  - [x] taxon-constraint N/A.
- [x] METADATA: Added term tracker item, obsoletion comment, `is_obsolete: true`, and `replaced_by`. No `created_by`/`creation_date` added because this is an existing term.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after edits.
- [x] REFERENCE-VALIDATION: N/A; no new reference IDs were introduced.
- [x] CHANGES-COMMITTED: Committed only `src/ontology/go-edit.obo`.
  - [x] RELEVANT-FILES: `src/ontology/go-edit.obo` committed with a signed-off commit.
  - [x] ACCURACY: Direct replacement aligns with the issue rationale and existing GO:0140175 mappings.
  - [x] ISSUE-ALIGNMENT: Change implements the requested obsoletion and replacement.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633614723)


#### Agent Issue Comment

GO:0043713 has been obsoleted with `replaced_by: GO:0140175` as requested.

Validation passed with `cd src/ontology && make travis_build`. Changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633614723)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.889  **precision**: 0.889  **recall**: 0.889

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/161
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 161 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology diff matches the human PR in all functional changes: obsolete label, `OBSOLETE.` definition prefix, removal of the active `is_a: GO:0016616` parent, tracker metadata, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-rates the result because the only real difference is a shorter obsoletion comment.


## Strengths

- Selected the correct target term, `GO:0043713`, and the correct replacement term, `GO:0140175`, matching the issue and the merged human PR.
- Followed the GO obsoletion pattern for the term stanza: prefixed the name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a: GO:0016616` classification, and added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`, which is the key migration metadata for annotations to the obsolete specific enzyme activity.
- Added the expected tracker link, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the change tightly scoped to `GO:0043713` in `src/ontology/go-edit.obo`, with no unrelated term edits.


## Issues

- Minor: the obsoletion comment is less informative than the human PR's comment. The merged PR records the biochemical rationale that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that this EC entry is an exact-match xref for `GO:0140175`, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader replacement term. The agent's shorter comment is still correct, but it preserves less curator-facing evidence in the ontology.

### Attempt 10: gpt-5.5 / opencode

- **Eval PR**: [#141](https://github.com/ai4curation/eval-ont-agent-go/pull/141)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.889  **precision**: 0.889  **recall**: 0.889

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/141
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 141 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology edit matches the human PR in all functional changes: obsolete label and definition prefix, removal of the `is_a: GO:0016616` parent, `term_tracker_item`, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-represents the actual quality because the only substantive mismatch is that the agent used a shorter obsoletion comment.

## Strengths

- Selected the correct obsolete term, `GO:0043713`, and the correct replacement, `GO:0140175`, exactly as requested in issue `#31966`.
- Followed the GO obsoletion pattern: prefixed the name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the active `is_a: GO:0016616` assertion, and added `is_obsolete: true`.
- Added `replaced_by: GO:0140175`, which is the key annotation migration metadata for this enzyme activity consolidation.
- Added the correct tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- Kept the edit tightly scoped to the single affected stanza in `src/ontology/go-edit.obo`, with no unrelated ontology changes.

## Issues

- Minor: the obsoletion comment is less informative than the human PR's comment. The human version records the supporting details that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that `GO:0140175` has `EC:1.1.1.345` as an exact-match xref, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader `GO:0140175` reaction. The agent's shorter comment is still correct and sufficient for the obsoletion, but it preserves less curator-facing rationale in the ontology.

### Attempt 11: gpt-5.5 / codex

- **Eval PR**: [#125](https://github.com/ai4curation/eval-ont-agent-go/pull/125)
- **F1**: 0.889  **Precision**: 0.889  **Recall**: 0.889  **Jaccard**: 0.800
- **Workflow run**: [25633563528](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633563528)

#### Agent PR Comment

## Summary

Obsoleted GO:0043713 `(R)-2-hydroxyisocaproate dehydrogenase activity` because it is equivalent to GO:0140175 `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity`.

Changes made in `src/ontology/go-edit.obo`:

- Prefixed the GO:0043713 label with `obsolete`.
- Prefixed the definition with `OBSOLETE.` while retaining original provenance.
- Removed the asserted `is_a` parent from the obsolete term.
- Added obsoletion comment, term tracker item for issue #31966, `is_obsolete: true`, and `replaced_by: GO:0140175`.

## Rationale

GO:0140175 already represents the broader EC/RHEA activity described in the issue, with `xref: EC:1.1.1.345 {source="skos:exactMatch"}`, `xref: RHEA:35643 {source="skos:exactMatch"}`, and `xref: RHEA:10052 {source="skos:narrowMatch"}`. Local RHEA resources confirm RHEA:10052 is a child/narrow reaction of RHEA:35643. The local ChEBI pH 7.3 mapping also supports the issue's acid/conjugate-base reasoning for CHEBI:55534 and CHEBI:55535.

## Validation

- Pre-validation: `make -C src/ontology travis_build` passed before edits.
- Research/reference validation: `linkml-reference-validator cache reference PMID:16957230` succeeded, and the support excerpt in `RESEARCH.md` validated successfully.
- Post-change validation: `make -C src/ontology travis_build` passed after edits.
- Internal term/reference search: `GO:0043713` was found only in its own ontology stanza and evaluation/imported issue artifacts.
- Annotation impact: the issue reports 0 annotations. I attempted `runoak -i amigo: associations GO:0043713`, but the local OAK installation fails to import because of a `linkml` API mismatch, so direct AmiGO annotation lookup could not be completed in this environment.

## Checklist

- [x] PLAN: Issue context and comments reviewed; direct replacement obsoletion request is clear.
- [x] PRE-VALIDATION: Ontology validated before edits with `make -C src/ontology travis_build`.
- [x] RESEARCH: `RESEARCH.md` created; PMID:16957230 validated; RHEA and ChEBI local evidence checked.
- [x] TERM-SEARCH: GO:0043713 and GO:0140175 checked in `go-edit.obo`; internal usages searched.
- [x] DESIGN-PATTERNS: `DESIGN_PATTERNS.md` created; no new logical definition or pattern change needed for this obsoletion.
- [x] EDITS: Used `obo-checkout.pl` and `obo-checkin.pl`; edited term-specific file under `terms/`.
- [x] RELATIONSHIPS: Removed obsolete term parent assertion; no `relationship` or `intersection_of` tags remain on obsolete term.
- [x] SPECIALIZED-EDITS: Used term-obsoletion guidance; reaction guidance for EC/RHEA context; chemical-entity guidance for CHEBI pH 7.3 check.
- [x] METADATA: Added issue tracker link, obsoletion comment, `is_obsolete: true`, and `replaced_by: GO:0140175`; no `created_by`/`creation_date` added because this is an existing term.
- [x] AUTOMATED-VALIDATION: Post-change `make -C src/ontology travis_build` passed.
- [x] REFERENCE-VALIDATION: PMID:16957230 cached and support excerpt validated.
- [x] CHANGES-COMMITTED: Local commit created: `2f5c39e Obsolete GO:0043713`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633563528)


#### Agent Issue Comment

GO:0043713 has been obsoleted and replaced by GO:0140175 in PR #<NN>.

I confirmed GO:0140175 already carries the relevant EC:1.1.1.345 exact match and RHEA mappings, including RHEA:10052 as a narrow match. The obsolete term now has a `replaced_by` link to GO:0140175.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633563528)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index c1698b781..7fce679cc 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -255886,10 +255886,13 @@ is_a: GO:0008410 ! CoA-transferase activity
 
 [Term]
 id: GO:0043713
-name: (R)-2-hydroxyisocaproate dehydrogenase activity
+name: obsolete (R)-2-hydroxyisocaproate dehydrogenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
-is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+def: "OBSOLETE. Catalysis of the reaction: 2-oxoisocaproate + NADH + H+ = (R)-2-hydroxyisocaproate + NAD+." [GOC:jl, PMID:16957230]
+comment: The reason for obsoletion is that this term is equivalent to GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0140175
 
 [Term]
 id: GO:0043714

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.889  **precision**: 0.889  **recall**: 0.889

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31966
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32003
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/125
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31966 --repo geneontology/go-ontology
    gh pr diff 32003 --repo geneontology/go-ontology
    gh pr diff 125 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the requested obsoletion of `GO:0043713` `(R)-2-hydroxyisocaproate dehydrogenase activity` and used `GO:0140175` `(2R)-2-hydroxyacid dehydrogenase (NAD+) activity` as the replacement. Its ontology diff matches the human PR in all functional edits: obsolete label and definition prefix, removal of the `is_a: GO:0016616` parent, `term_tracker_item`, `is_obsolete: true`, and `replaced_by: GO:0140175`. The metadiff F1 of 0.889 slightly under-represents the practical quality, because the mismatch is just a shorter obsoletion comment.


## Strengths

- The agent selected the correct target term, `GO:0043713`, and the correct replacement term, `GO:0140175`, exactly as requested in issue `#31966`.
- It followed the standard GO obsoletion pattern: prefixed the term name with `obsolete`, prefixed the definition with `OBSOLETE.`, removed the asserted `is_a` parent to `GO:0016616`, added `is_obsolete: true`, and retained the `molecular_function` namespace.
- It added `replaced_by: GO:0140175`, which is the important migration aid for a term whose activity is covered by the broader EC-aligned `GO:0140175`.
- It added the correct tracker link, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31966" xsd:anyURI`.
- The agent's PR rationale shows it understood the biochemical basis for the obsoletion: `GO:0140175` has `EC:1.1.1.345` as an exact match and includes `RHEA:10052` as a narrow match, corresponding to the reaction described by `GO:0043713`.


## Issues

- The obsoletion comment is less informative than the human PR's comment. The human version explicitly records that `(R)-2-hydroxyisocaproate dehydrogenase` is a synonym of `EC:1.1.1.345`, that `EC:1.1.1.345` is an exact-match xref on `GO:0140175`, and that the specific `RHEA:10052` reaction is a narrowMatch instance of the broader `GO:0140175` reaction. The agent's shorter comment is still correct, but it preserves less curator-facing justification in the ontology.
- No substantive ontology error found. The shorter comment accounts for the non-perfect metadiff score, but it does not change the correctness of the obsoletion or replacement.
