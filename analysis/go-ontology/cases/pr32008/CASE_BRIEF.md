---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 25870
pr_number: 32008
issue_title: GO terms with EC:1.13.11.37 xref
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 0.667
best_model: claude-sonnet-4.5
---

# PR #32008 — GO terms with EC:1.13.11.37 xref

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #25870](https://github.com/geneontology/go-ontology/issues/25870) | [PR #32008](https://github.com/geneontology/go-ontology/pull/32008) | @dragon-ai-agent | merged 2026-04-28

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #25870 (opened July 2023) identified problems with GO terms carrying the EC:1.13.11.37 cross-reference. GO:0018581 "hydroxyquinol 1,2-dioxygenase activity" described only the first step of the reaction, while GO:0047074 described the complete reaction. This PR resolves the duplication by obsoleting GO:0018581 and renaming GO:0047074 to the more recognizable name.

## Changes Made

Two files were modified:
1. In `src/ontology/go-edit.obo`: GO:0018581 was obsoleted with `replaced_by: GO:0047074`, and GO:0047074 was renamed to "hydroxyquinol 1,2-dioxygenase activity" (taking the name from the obsoleted term since it is the more commonly used label)
2. In `src/ontology/imports/go-catalytic-activities-participants.owl`: Removed 31 lines of OWL axioms that referenced the obsoleted term's reaction participants

## Resolution

Merged directly. This addressed part of a long-standing issue (nearly 3 years old) about EC cross-reference alignment. The two-file change demonstrates that obsoletion can require cleanup in both the main edit file and the OWL imports that encode reaction participant relationships.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..4c1a6c46f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term described a sub-reaction of the complete two-step reaction represented by GO:0047074. The second step (non-enzymatic conversion of 3-hydroxy-cis,cis-muconate to maleylacetate) is not catalyzed separately, so this term is equivalent to GO:0047074 hydroxyquinol 1,2-dioxygenase activity.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,10 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}
diff --git a/src/ontology/imports/go-catalytic-activities-participants.owl b/src/ontology/imports/go-catalytic-activities-participants.owl
index fb8b76d32..f80973982 100644
--- a/src/ontology/imports/go-catalytic-activities-participants.owl
+++ b/src/ontology/imports/go-catalytic-activities-participants.owl
@@ -69756,37 +69756,6 @@
     
 
 
-    <!-- http://purl.obolibrary.org/obo/GO_0018581 -->
-
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0018581">
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_15378"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_15379"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_16971"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_58139"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-    </owl:Class>
-    
-
-
     <!-- http://purl.obolibrary.org/obo/GO_0018582 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0018582">

```

## Agent Attempts (6)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#453](https://github.com/ai4curation/eval-ont-agent-go/pull/453)
- **F1**: 0.667  **Precision**: 0.519  **Recall**: 0.933  **Jaccard**: 0.500
- **Trace**: [25847201917](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847201917)
- **Workflow run**: [25847201917](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847201917)

#### Agent PR Comment

## Summary

This PR addresses issue #25870 regarding EC:1.13.11.37 xref mapping for two GO terms representing different stages of the same catalytic reaction.

## Changes Made

### 1. Obsoleted GO:0018581 (hydroxyquinol 1,2-dioxygenase activity)

**Reason for obsoletion:** This term represented only the first enzymatic step of a two-step reaction (benzene-1,2,4-triol → 3-hydroxy-cis,cis-muconate). The second step is a non-enzymatic conversion to maleylacetate. The complete reaction is more accurately represented by GO:0047074.

**Obsoletion details:**
- Changed name to "obsolete hydroxyquinol 1,2-dioxygenase activity"
- Prefixed definition with "OBSOLETE."
- Removed all xrefs (EC:1.13.11.37, MetaCyc:RXN-17556, RHEA:19441, UM-BBD_reactionID:r0232)
- Removed is_a relationship to GO:0016702
- Added `is_obsolete: true`
- Added `replaced_by: GO:0047074`
- Added comment explaining the reason for obsoletion
- Retained term_tracker_items for provenance

**Impact analysis:**
- No experimental annotations to this term (confirmed in issue #25870)
- No other terms in the ontology reference GO:0018581
- Low-risk obsoletion with direct replacement

### 2. Renamed GO:0047074

**Name change:** "4-hydroxycatechol 1,2-dioxygenase activity" → "hydroxyquinol 1,2-dioxygenase activity"

**Rationale:** The new name matches the accepted EC:1.13.11.37 name. This term represents the complete reaction (enzymatic + non-enzymatic conversion) from benzene-1,2,4-triol to maleylacetate, which is exactly what EC:1.13.11.37 describes.

**Additional changes:**
- Added old name "4-hydroxycatechol 1,2-dioxygenase activity" as EXACT synonym
- Definition already correctly describes the complete reaction and matches EC
- EC:1.13.11.37 xref already has `skos:exactMatch` mapping (correct)
- All other xrefs and relationships retained

## Verification

### MetaCyc xrefs status:
- GO:0018581 previously had MetaCyc:RXN-17556 (correct replacement for obsolete HYDROXYQUINOL-12-DIOXYGENASE-RXN) - now removed as part of obsoletion
- GO:0047074 has MetaCyc:RXN-10137 (R308-RXN appears to have been previously removed)
- All MetaCyc xref updates from issue comments appear to have been addressed

### EC xref mapping:
- GO:0047074 now has EC:1.13.11.37 with `skos:exactMatch` ✓
- This correctly reflects that GO:0047074 represents the exact reaction described by EC:1.13.11.37

## Checklist

- [x] PLAN: Issue analyzed, intent clear, plan created
- [x] PRE-VALIDATION: Ontology structure verified before changes
- [x] RESEARCH: Background information confirmed (EC:1.13.11.37, RHEA terms)
- [x] TERM-SEARCH: Relevant terms found using obo-grep.pl
- [x] DESIGN-PATTERNS: N/A - obsoletion and rename only, no new logical axioms
- [x] EDITS: Proper checkout/checkin procedure followed
  - [x] Used obo-checkout.pl to extract terms to terms/ folder
  - [x] Edited individual term files
  - [x] Used obo-checkin.pl to integrate changes back into go-edit.obo
- [x] RELATIONSHIPS: N/A - no new relationships added
  - [x] GO:0018581 relationships removed as per obsoletion guidelines
  - [x] GO:0047074 relationships unchanged
- [x] SPECIALIZED-EDITS: /term-obsoletion skill guidelines followed
  - [x] Obsolete term has no logical axioms (is_a, intersection_of removed)
  - [x] Name prefixed with "obsolete"
  - [x] Definition prefixed with "OBSOLETE."
  - [x] All xrefs removed from obsolete term
  - [x] is_obsolete: true added
  - [x] replaced_by: GO:0047074 added
  - [x] Comment explaining obsoletion reason added
  - [x] No synonyms retained on obsolete term
  - [x] Namespace retained for historical provenance
  - [x] Impact analysis confirmed no annotations or ontology references
- [x] METADATA: Appropriate for this change
  - [x] No created_by/creation_date added (only editing existing terms, not creating new ones)
  - [x] Original term_tracker_items retained
  - [x] All terms have proper namespace (molecular_function)
- [x] AUTOMATED-VALIDATION: Changes validated
  - [x] Git diff reviewed - changes are clean and targeted
  - [x] No unintended modifications to other terms
- [x] REFERENCE-VALIDATION: N/A - no new references introduced
- [x] CHANGES-COMMITTED:
  - [x] RELEVANT-FILES: Only src/ontology/go-edit.obo modified (correct)
  - [x] ACCURACY: Changes are biologically correct - GO:0018581 was indeed a sub-reaction
  - [x] ISSUE-ALIGNMENT: Changes fully address issue #25870 requirements
  - [x] Detailed commit message with Co-Authored-By signature
  
## Technical Details

**Files modified:**
- `src/ontology/go-edit.obo`

**Lines changed:**
- GO:0018581 at line ~138332: Converted to obsolete term
- GO:0047074 at line ~291739: Renamed and synonym added

**Git commit:** f562925

## Notes

This change aligns GO's representation with the EC classification system and eliminates redundancy between terms representing partial vs. complete reactions. The obsoletion has minimal downstream impact due to the lack of annotations to GO:0018581.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847201917)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I've successfully obsoleted GO:0018581 and renamed GO:0047074 to "hydroxyquinol 1,2-dioxygenase activity" as requested. 

GO:0018581 represented only the first enzymatic step of the reaction (producing 3-hydroxy-cis,cis-muconate), while GO:0047074 represents the complete reaction to maleylacetate, which correctly matches EC:1.13.11.37. GO:0047074 now uses the official EC name and retains the previous name as a synonym.

The term had no experimental annotations, so this change should have minimal impact on existing data.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847201917)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..92b6a852a 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: This term was obsoleted because it represents only the first step of a two-step reaction. The complete reaction is represented by GO:0047074 (hydroxyquinol 1,2-dioxygenase activity). The second step is a non-enzymatic conversion of 3-hydroxy-cis,cis-muconate to maleylacetate.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,10 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#331](https://github.com/ai4curation/eval-ont-agent-go/pull/331)
- **F1**: 0.667  **Precision**: 0.519  **Recall**: 0.933  **Jaccard**: 0.500
- **Trace**: [25650667526](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650667526)
- **Workflow run**: [25650667526](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650667526)

#### Agent PR Comment

# Obsolete GO:0018581; rename GO:0047074

Addresses geneontology/go-ontology#25870.

## Background

EC:1.13.11.37 (accepted name: hydroxyquinol 1,2-dioxygenase) catalyzes:
`benzene-1,2,4-triol + O2 = maleylacetate + 2 H+` (RHEA:35595).

Two GO terms previously corresponded to this EC entry:

- **GO:0018581** "hydroxyquinol 1,2-dioxygenase activity" — described only the first step (`benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate`, RHEA:19441). The second step (3-hydroxy-cis,cis-muconate → maleylacetate) is non-enzymatic ([BioCyc RXN-10137](https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-10137)), so this is a sub-reaction and not an enzyme activity on its own.
- **GO:0047074** "4-hydroxycatechol 1,2-dioxygenase activity" — described the full reaction (RHEA:35595), and is the exact equivalent of EC:1.13.11.37.

Per the latest issue discussion (sjm41, raymond91125), GO:0018581 should be obsoleted (replaced by GO:0047074) and GO:0047074 should be renamed to "hydroxyquinol 1,2-dioxygenase activity" (the EC accepted name).

## Changes

### GO:0018581 — obsoleted

- Renamed to "obsolete hydroxyquinol 1,2-dioxygenase activity".
- Definition prefixed with "OBSOLETE.".
- `is_a`, all `xref`s removed (per term-obsoletion convention — obsolete terms retain no logical axioms or mappings).
- Added `is_obsolete: true` and `replaced_by: GO:0047074`.
- Added `comment` with the reason for obsoletion.
- Existing `term_tracker_item` properties retained.

### GO:0047074 — renamed

- `name` changed from "4-hydroxycatechol 1,2-dioxygenase activity" to "hydroxyquinol 1,2-dioxygenase activity".
- Previous label added as an EXACT synonym (hydroxyquinol and 4-hydroxycatechol are both names for benzene-1,2,4-triol).
- All other content unchanged. The skos-qualified mappings to EC:1.13.11.37 and RHEA:35595 (already at `exactMatch` from prior work on this issue) are preserved.

## Annotation impact

The issue states GO:0018581 has zero GO annotations. No annotation rewiring required.

## Checklist

- [x] PLAN: issue analyzed; intent is clear from raymond91125's directive comment
- [x] PRE-VALIDATION: ontology validates before changes (robot convert clean)
- [x] RESEARCH: N/A — task is mechanical obsoletion + rename; biological rationale already established in the issue thread and the existing definitions/xrefs
- [x] TERM-SEARCH: both terms inspected with `obo-grep.pl`; no other internal references to GO:0018581 in `src/ontology/go-edit.obo`
- [x] DESIGN-PATTERNS: N/A — no new logical axioms introduced; reaction term mappings already conform to the standard `EC + RHEA + MetaCyc` pattern with skos qualifiers
- [x] EDITS: used `obo-checkout.pl` / `obo-checkin.pl` via `terms/` folder
- [x] RELATIONSHIPS: obsolete term stripped of `is_a`; GO:0047074's `is_a` to GO:0016702 retained
- [x] SPECIALIZED-EDITS:
    - [x] /term-obsoletion: followed obsoletion conventions (name prefix, OBSOLETE. def, comment, no relationships, replaced_by)
    - [x] /reaction: skos-qualified mappings preserved on GO:0047074
    - [N/A] /chemical-entity: no CHEBI changes
    - [N/A] /taxon-constraint: no taxon constraint changes
- [x] METADATA:
    - GO:0047074 was an existing term; no `created_by`/`creation_date` added (per convention).
    - GO:0018581 was an existing term being obsoleted; only obsoletion metadata added.
    - `term_tracker_item` retained on both.
- [x] AUTOMATED-VALIDATION:
    - `robot convert` clean on `go-edit.obo`.
    - `robot verify` against the standard SPARQL-QC query set — all 16 rules PASS (0 violations).
    - `robot reason -r ELK` completed without unsatisfiable classes.
    - Note: full `make travis_build` could not run end-to-end in this environment because `amm` (Ammonite) is not installed; the individual robot-based checks listed above were run instead.
- [x] REFERENCE-VALIDATION: no new PMIDs introduced; existing RHEA references unchanged.
- [x] CHANGES-COMMITTED: single commit on `src/ontology/go-edit.obo`.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650667526)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary:
- Obsoleted GO:0018581 (hydroxyquinol 1,2-dioxygenase activity), `replaced_by` GO:0047074. The obsoleted term covered only the first step of the EC:1.13.11.37 reaction; the second step is non-enzymatic.
- Renamed GO:0047074 from "4-hydroxycatechol 1,2-dioxygenase activity" to "hydroxyquinol 1,2-dioxygenase activity" (the EC accepted name). The prior label is retained as an EXACT synonym.

GO:0047074 already carried the `EC:1.13.11.37 {source="skos:exactMatch"}` and `RHEA:35595 {source="skos:exactMatch"}` xrefs from earlier work on this issue, so no further mapping changes were needed.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650667526)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..23d9297bb 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term describes only the first step of the 2-step reaction catalyzed by EC:1.13.11.37 (the second step is non-enzymatic). The complete reaction is captured by GO:0047074, which is the exact equivalent of EC:1.13.11.37 (RHEA:35595).
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,10 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}

```

### Attempt 3: kimi-k2.6 / opencode

- **Eval PR**: [#254](https://github.com/ai4curation/eval-ont-agent-go/pull/254)
- **F1**: 0.667  **Precision**: 0.519  **Recall**: 0.933  **Jaccard**: 0.500
- **Trace**: [25646676580](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646676580)
- **Workflow run**: [25646676580](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646676580)

#### Agent PR Comment

## Summary

This PR obsoletes GO:0018581 and renames GO:0047074, completing the outstanding tasks from issue #25870.

## Changes made

### GO:0018581 — obsoleted
- Renamed to `obsolete hydroxyquinol 1,2-dioxygenase activity`
- Prefixed definition with "OBSOLETE."
- Removed all xrefs (EC, MetaCyc, RHEA, UM-BBD) and the `is_a` relationship
- Added comment: "The reason for obsoletion is that this term is equivalent to GO:0047074 4-hydroxycatechol 1,2-dioxygenase activity."
- Added `is_obsolete: true` and `replaced_by: GO:0047074`

Rationale: GO:0018581 described only the first half of the two-step reaction catalyzed by EC:1.13.11.37 (producing 3-hydroxy-cis,cis-muconate), whereas GO:0047074 describes the complete reaction to maleylacetate. It had zero experimental annotations, making obsoletion with direct replacement straightforward.

### GO:0047074 — renamed
- Primary label changed to `hydroxyquinol 1,2-dioxygenase activity` (matching the accepted EC:1.13.11.37 name)
- Added EXACT synonym: `4-hydroxycatechol 1,2-dioxygenase activity`

Rationale: Aligning the GO term name with the accepted EC name improves discoverability and consistency.

## Background / prior work

A number of the original checklist items from issue #25870 had already been completed in a prior commit for issue #30193:
- EC:1.13.11.37 on GO:0018581 already had `skos:broadMatch`
- EC-attributed synonyms had already been removed from GO:0018581
- GO:0018581 definition already used RHEA:19441
- EC:1.13.11.37 on GO:0047074 already had `skos:exactMatch`
- GO:0047074 definition already matched EC:1.13.11.37
- Obsolete MetaCyc xrefs had already been replaced/removed

The remaining scope was the obsoletion of GO:0018581 and rename of GO:0047074, which this PR addresses.

## Validation

- Checked for references to GO:0018581 elsewhere in the ontology: none found (clean obsoletion).
- Verified OBO syntax of modified stanzas.
- Full `make travis_build` / `robot` validation was not possible in this environment due to missing build tools (`amm`, `robot`), but the edits follow standard GO obsoletion patterns and catalytic-activity term conventions.

## Self-checklist

- [x] Issue analyzed and intent understood
- [x] No external references to GO:0018581 in ontology
- [x] GO:0018581 obsoleted with `is_obsolete: true` and `replaced_by: GO:0047074`
- [x] Obsoleted term stripped of xrefs, relationships, and synonyms
- [x] GO:0047074 renamed to match EC name
- [x] Previous label preserved as EXACT synonym on GO:0047074
- [x] `term_tracker_item` property values retained on both terms
- [x] Changes committed with descriptive message

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646676580)


#### Agent Issue Comment

Hi @sjm41, @raymond91125 — the requested changes have been implemented and committed.

**What was done:**

- **GO:0018581** has been obsoleted with `replaced_by: GO:0047074`. It had no annotations in the ontology, so this is a clean obsoletion.
- **GO:0047074** has been renamed to **"hydroxyquinol 1,2-dioxygenase activity"** (matching the accepted EC:1.13.11.37 name), with the previous label preserved as an EXACT synonym.

Upon inspection, the earlier items from the original checklist (updating EC xref qualifiers, removing EC synonyms, updating MetaCyc xrefs, etc.) had already been addressed in a prior commit for issue #30193. The remaining scope was the obsoletion and rename, which is now complete.

Changes are in PR #<NN>.

Thanks!

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646676580)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..12e6e5736 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term is equivalent to GO:0047074 4-hydroxycatechol 1,2-dioxygenase activity.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,10 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}

```

### Attempt 4: claude-sonnet-4.5 / copilot

- **Eval PR**: [#374](https://github.com/ai4curation/eval-ont-agent-go/pull/374)
- **F1**: 0.651  **Precision**: 0.519  **Recall**: 0.875  **Jaccard**: 0.483
- **Trace**: [25752244915](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25752244915)
- **Workflow run**: [25752244915](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752244915)

#### Agent PR Comment

# Obsolete GO:0018581 and rename GO:0047074

This PR addresses issue #25870 by obsoleting GO:0018581 and renaming GO:0047074 to align with EC nomenclature.

#### Agent Issue Comment

The requested changes have been completed and committed in PR #<NN>.

**Summary of changes:**

1. **Obsoleted GO:0018581** (hydroxyquinol 1,2-dioxygenase activity)
   - This term represented only the first step of the 2-step reaction (benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate)
   - Replaced by GO:0047074, which represents the complete 2-step reaction
   - No gene annotations were affected (0 annotations)

2. **Renamed GO:0047074** from "4-hydroxycatechol 1,2-dioxygenase activity" to "hydroxyquinol 1,2-dioxygenase activity"
   - This aligns with the EC:1.13.11.37 accepted name
   - The old name has been retained as an EXACT synonym

The term now correctly represents the complete reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+, which matches EC:1.13.11.37 and RHEA:35595.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25752244915)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..9e3607e37 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: This term was made obsolete because it represents a sub-reaction of RHEA:35595. The complete 2-step reaction (benzene-1,2,4-triol + O2 = maleylacetate + 2 H+) is represented by GO:0047074.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,11 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
+synonym: "benzene-1,2,4-triol:oxygen 1,2-oxidoreductase (decyclizing)" RELATED []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}

```

### Attempt 5: claude-haiku-4.5 / claude

- **Eval PR**: [#406](https://github.com/ai4curation/eval-ont-agent-go/pull/406)
- **F1**: 0.634  **Precision**: 0.481  **Recall**: 0.929  **Jaccard**: 0.464
- **Trace**: [25761750600](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25761750600)
- **Workflow run**: [25761750600](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761750600)

#### Agent PR Comment

# Pull Request: Obsolete GO:0018581 and Rename GO:0047074

#### Agent Issue Comment

## Status Update

Changes have been committed to address issue #25870.

### Summary of Actions Completed

- [x] Obsolete GO:0018581 (hydroxyquinol 1,2-dioxygenase activity) with GO:0047074 as the replacement term
- [x] Rename GO:0047074 from "4-hydroxycatechol 1,2-dioxygenase activity" to "hydroxyquinol 1,2-dioxygenase activity" to match the EC:1.13.11.37 name

### Rationale

GO:0018581 describes only the first step of the 2-step reaction catalyzed by EC:1.13.11.37, while GO:0047074 describes the complete 2-step reaction that the enzyme actually performs. As GO:0018581 has no annotations and is effectively superseded by GO:0047074, it has been obsoleted with GO:0047074 as the direct replacement. The rename of GO:0047074 ensures consistency with the EC number nomenclature.

Changes committed in PR #<NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761750600)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..cd135231b 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term is equivalent to GO:0047074. This term describes only the first step of the 2-step reaction that GO:0047074 describes. GO:0047074 has been renamed to 'hydroxyquinol 1,2-dioxygenase activity' to match the EC number name.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,7 +291739,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
 xref: EC:1.13.11.37 {source="skos:exactMatch"}

```

### Attempt 6: gemma-4-31b / opencode

- **Eval PR**: [#252](https://github.com/ai4curation/eval-ont-agent-go/pull/252)
- **F1**: 0.634  **Precision**: 0.481  **Recall**: 0.929  **Jaccard**: 0.464
- **Trace**: [25646627554](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646627554)
- **Workflow run**: [25646627554](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646627554)

#### Agent PR Comment

## Summary of Changes
- Obsoleted `GO:0018581` (hydroxyquinol 1,2-dioxygenase activity).
- Renamed `GO:0047074` from "4-hydroxycatechol 1,2-dioxygenase activity" to "hydroxyquinol 1,2-dioxygenase activity".
- Linked `GO:0018581` to `GO:0047074` via `replaced_by`.

#### Agent Issue Comment

The changes have been committed in PR #<NN>.

- Obsoleted GO:0018581 (hydroxyquinol 1,2-dioxygenase activity).
- Renamed GO:0047074 to "hydroxyquinol 1,2-dioxygenase activity".
- Set GO:0018581 as replaced_by GO:0047074.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646627554)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..a62d9b9e8 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term is equivalent to GO:0047074.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,7 +291739,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
 xref: EC:1.13.11.37 {source="skos:exactMatch"}

```
