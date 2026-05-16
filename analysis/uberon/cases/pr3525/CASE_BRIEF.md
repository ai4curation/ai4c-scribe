# PR #3525 — relationship is reversed between Uberon and NCIT for foramen secundum

- **Ontology**: uberon
- **Repo**: obophenotype/uberon
- **Issue**: [#3522](https://github.com/obophenotype/uberon/issues/3522)
- **PR**: [#3525](https://github.com/obophenotype/uberon/pull/3525)
- **Author**: @rays22
- **Merged**: 2025-05-27
- **task_type**: axiom_repair
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: multi_term
- **review_outcome**: approved_first_time

## Context

Issue #3522 reported that the logical definition (equivalence axiom) for foramen secundum (UBERON:0006678) was reversed relative to NCIT, and that foramen primum (UBERON:0009149) had a non-unique equivalence axiom that could cause reasoning errors. Both terms relate to openings in the interatrial septum during cardiac development.

## Changes Made

For UBERON:0009149 (foramen primum), the non-unique equivalence axiom was replaced with two explicit subclass assertions. For UBERON:0006678 (foramen secundum), the incorrect equivalence axiom was similarly replaced with subclass assertions, and the text definition was corrected. The changes totaled 5 additions and 5 deletions in uberon-edit.obo.

## Resolution

Medium difficulty. An agent would need to understand the difference between equivalence axioms and subclass assertions in OBO/OWL, recognize when an equivalence axiom is non-unique or incorrect, and have sufficient cardiac embryology knowledge to verify the corrected relationships between foramen primum, foramen secundum, and the interatrial septum. Merged after twelve days with no changes requested.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4a..61c8ce1465 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "The foramen secundum is an opening in the septum primum, a precursor to the interatrial septum of the human heart. It is formed at a later developmental stage than the foramen primum. Its location is also different relative to the site of the foramen primum in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114758,8 +114758,8 @@ xref: SCTID:308854001
 xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
-intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+is_a: UBERON:0004111 ! anatomical conduit
+relationship: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 
@@ -130525,8 +130525,8 @@ xref: SCTID:308852002
 xref: UMLS:C1517292 {source="ncithesaurus:Foramen_Primum"}
 xref: VHOG:0001470
 xref: Wikipedia:Primary_interatrial_foramen
-intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004154 ! atrial septum primum
+is_a: UBERON:0004111 ! anatomical conduit
+relationship: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "First of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001470", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001470", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 

```

## Agent Attempts (8)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#329](https://github.com/ai4curation/eval-ont-agent-uberon/pull/329)
- **F1**: 0.364  **Precision**: 0.286  **Recall**: 0.500  **Jaccard**: 0.222
- **Trace**: [25888675545](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25888675545)
- **Workflow run**: [25888675545](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888675545)

#### Agent PR Comment

## Changes Summary

Fixed the anatomical relationship for foramen secundum (UBERON:0006678) to correctly reflect that it is an opening in the septum primum, not the septum secundum.

### Changes Made

**File Modified:** `src/ontology/uberon-edit.obo`

#### Changes to UBERON:0006678 (foramen secundum):

1. **Definition updated:**
   - OLD: `"A foramen in the septum secundum."`
   - NEW: `"A foramen in the septum primum."`

2. **Logical definition (intersection_of) updated:**
   - OLD: `intersection_of: part_of UBERON:0004155 ! atrial septum secundum`
   - NEW: `intersection_of: part_of UBERON:0004154 ! atrial septum primum`

### Rationale

The foramen secundum is defined as an opening in the septum primum, as supported by:
- Wikipedia article on Foramen secundum
- Medical anatomy textbook references (ISBN: 9632412311)
- The existing external definition that states: "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart."

The correction resolves the discrepancy noted in issue #3522 between the UBERON and NCIT ontologies. The foramen secondum and foramen ovale are distinct structures in different septa - foramen secundum opens in the septum primum, while foramen ovale opens in the septum secundum.

### Validation

- Term definition and logical definition are now consistent with each other
- The anatomical relationship now correctly reflects that foramen secundum is part of the atrial septum primum (UBERON:0004154)
- Cross-references to external databases (FMA, NCIT, etc.) are preserved and remain valid

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888675545)


#### Agent Issue Comment

## Issue #3522: Fixed foramen secundum relationship

Changes committed in PR #<NN>

The anatomical relationship has been corrected to match the proper anatomy where foramen secundum is an opening in the septum primum, not the septum secundum.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888675545)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..1e45be56f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,7 +114759,7 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 

```

### Attempt 2: claude-haiku-4.5 / claude

- **Eval PR**: [#273](https://github.com/ai4curation/eval-ont-agent-uberon/pull/273)
- **F1**: 0.364  **Precision**: 0.286  **Recall**: 0.500  **Jaccard**: 0.222
- **Trace**: [25844162507](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25844162507)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..1e45be56f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,7 +114759,7 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 

```

### Attempt 3: gemma-4-31b / opencode

- **Eval PR**: [#111](https://github.com/ai4curation/eval-ont-agent-uberon/pull/111)
- **F1**: 0.364  **Precision**: 0.286  **Recall**: 0.500  **Jaccard**: 0.222
- **Trace**: [25683681447](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25683681447)
- **Workflow run**: [25683681447](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683681447)

#### Agent PR Comment

## Summary of Changes
Corrected the anatomical relationship for the term **foramen secundum** (UBERON:0006678).

### Changes:
- Updated the definition of `UBERON:0006678` from "A foramen in the septum secundum." to "A foramen in the atrial septum primum."
- Changed the `part_of` relationship of `UBERON:0006678` from `UBERON:0004155` (atrial septum secundum) to `UBERON:0004154` (atrial septum primum).

### Rationale:
The original relationship was incorrect. As noted in the issue and supported by anatomical references (including Wikipedia and medical textbooks), the foramen secundum (or ostium secundum) forms as a perforation in the *septum primum*, not the septum secundum. The septum secundum is a separate structure that grows alongside it.

### Validation:
- Verified the IDs for `atrial septum primum` (UBERON:0004154) and `atrial septum secundum` (UBERON:0004155) using `obo-grep.pl`.
- Checked the existing definition and relationship in `src/ontology/uberon-edit.obo`.
- Used `obo-checkout.pl` and `obo-checkin.pl` to apply the changes safely.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683681447)

#### Agent Issue Comment

The relationship for foramen secundum (UBERON:0006678) has been corrected to be 'part of' atrial septum primum (UBERON:0004154) instead of atrial septum secundum (UBERON:0004155). Changes committed in PR #<NN>.
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25683681447)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..3ce54daeb 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the atrial septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,7 +114759,7 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
 

```

### Attempt 4: claude-sonnet-4.5 / claude

- **Eval PR**: [#294](https://github.com/ai4curation/eval-ont-agent-uberon/pull/294)
- **F1**: 0.333  **Precision**: 0.286  **Recall**: 0.400  **Jaccard**: 0.200
- **Trace**: [25877965934](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25877965934)
- **Workflow run**: [25877965934](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877965934)

#### Agent PR Comment

# Fix foramen secundum anatomical relationship

## Summary

This PR corrects the anatomical relationship for foramen secundum (UBERON:0006678). The term was incorrectly defined as being part of the atrial septum secundum, when it should be part of the atrial septum primum.

## Changes Made

### Term: foramen secundum (UBERON:0006678)

1. **Definition updated**: Changed from "A foramen in the septum secundum" to "A foramen in the septum primum"

2. **Logical definition corrected**: Changed the `intersection_of` axiom from:
   - `part_of UBERON:0004155 ! atrial septum secundum`
   - to `part_of UBERON:0004154 ! atrial septum primum`

3. **Metadata added**:
   - `dcterms-date`: 2026-05-14T00:00:00Z
   - `term_tracker_item`: https://github.com/obophenotype/uberon/issues/3522

## Rationale

The foramen secundum is an opening that forms in the septum primum during heart development, not in the septum secundum. This correction is supported by:

1. **Wikipedia** (cited in the original definition): States "the foramen secundum or ostium secundum is a foramen in the septum primum"
2. **Medical textbooks**: ISBN: 9632412311 (as cited by @rays22)
3. **Existing external definition**: The term already had an `external_definition` property that correctly stated "Second of the two openings to perforate the septum primum" - this change brings the primary definition into alignment with this existing annotation

## Validation

The change was validated by:
- Checking the term stanza before and after modification
- Verifying the parent terms (UBERON:0004154 atrial septum primum and UBERON:0004155 atrial septum secundum) exist and are correctly named
- Ensuring consistency with the external_definition already present in the term
- Following the checkout/checkin workflow as specified in CLAUDE.md

## Notes

- The robot reserialization step was not performed as the robot tool was not available in the evaluation environment, but the changes have been properly checked in using the obo-checkout/obo-checkin workflow
- No other terms were modified as part of this fix
- The change aligns with anatomical and developmental biology literature

Fixes #3522

@dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877965934)


#### Agent Issue Comment

Fixed the incorrect relationship as identified by @rays22. The foramen secundum (UBERON:0006678) has been corrected to be part_of atrial septum primum (UBERON:0004154) rather than atrial septum secundum (UBERON:0004155).

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877965934)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..2a302633c 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,9 +114759,11 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3522" xsd:anyURI
 
 [Term]
 id: UBERON:0006679

```

### Attempt 5: claude-opus-4.7 / claude

- **Eval PR**: [#244](https://github.com/ai4curation/eval-ont-agent-uberon/pull/244)
- **F1**: 0.286  **Precision**: 0.286  **Recall**: 0.286  **Jaccard**: 0.167
- **Trace**: [25835001572](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25835001572)
- **Workflow run**: [25835001572](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835001572)

#### Agent PR Comment

## Summary

Fixes obophenotype/uberon#3522: corrects the reversed/incorrect `part_of` relationship and text definition on [`UBERON:0006678` foramen secundum](http://purl.obolibrary.org/obo/UBERON_0006678).

## Background

The issue reporter noted that Uberon and NCIT disagree on the direction of the `part_of` relationship between the foramen secundum and the septum secundum. A subsequent comment by @rays22 (Uberon MEMBER) identified that **both** assertions were wrong, and that the correct anatomy is:

> The foramen secundum is an opening in the **septum primum**, not the septum secundum.

This is supported by:

1. The cited Wikipedia article on [Foramen secundum](https://en.wikipedia.org/wiki/Foramen_secundum): *"the foramen secundum or ostium secundum is a foramen in the septum primum."*
2. The own definition of [`UBERON:0004154` atrial septum primum](http://purl.obolibrary.org/obo/UBERON_0004154) (already in Uberon): *"...perforations appear in the superior part of the septum primum, forming the ostium secundum."*
3. The pre-existing `external_definition` on `UBERON:0006678` itself: *"Second of the two openings to perforate the septum primum between the two atria of the embryonic heart."* — i.e. the text definition was already inconsistent with the term's own annotations, and only the logical axiom and the `def:` line needed to be brought in line with the rest of the annotations.
4. The medical anatomy textbook (ISBN: 9632412311) cited by @rays22.

This means the change here brings the term into internal consistency rather than introducing a new anatomical claim.

## Changes to `UBERON:0006678 foramen secundum`

| Field | Before | After |
| --- | --- | --- |
| `def` | "A foramen in the septum secundum." | "A foramen in the septum primum." |
| `intersection_of: part_of` | `UBERON:0004155 ! atrial septum secundum` | `UBERON:0004154 ! atrial septum primum` |
| `term_tracker_item` | (absent) | `https://github.com/obophenotype/uberon/issues/3522` |

The `xref: NCIT:C34179` (Foramen Secundum) is retained — it is a correct class-level mapping. The reversed NCIT `Anatomic_Structure_Is_Physical_Part_Of` axiom called out in the issue is an upstream NCIT issue and out of scope for Uberon to fix directly.

## Checklist

- [x] Read the issue and the follow-up MEMBER comment in full.
- [x] Verified `UBERON:0004154` (atrial septum primum) exists and is the correct target.
- [x] Verified `UBERON:0004155` (atrial septum secundum) is a sibling under `UBERON:0002085 ! interatrial septum`, confirming both are valid `is_a interatrial septum` classes (so the old part_of axiom was a relationship error, not a class error).
- [x] Checked all other references to `UBERON:0006678` in `uberon-edit.obo`: only one other axiom (`UBERON:0004754 disjoint_from UBERON:0006678`) refers to it, and that axiom remains correct.
- [x] Edited the term via `obo-checkout.pl` / `obo-checkin.pl` rather than touching the edit file directly.
- [x] Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- [x] Committed only the intended file (`src/ontology/uberon-edit.obo`).

Signed: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835001572)


#### Agent Issue Comment

Thanks for catching this — the part_of axiom on `UBERON:0006678 foramen secundum` was indeed incorrect, and matched neither the cited Wikipedia source nor the term's own `external_definition` (which already correctly described the foramen secundum as perforating the septum primum).

Following @rays22's analysis, I corrected the term so that:

- `def`: "A foramen in the septum primum." (was "septum secundum")
- logical def: `part_of` [UBERON:0004154 atrial septum primum](http://purl.obolibrary.org/obo/UBERON_0004154) (was `UBERON:0004155 atrial septum secundum`)

The NCIT mapping (`NCIT:C34179 Foramen Secundum`) on the Uberon term is left in place; the issue with the reversed `Anatomic_Structure_Is_Physical_Part_Of` axiom on the NCIT side will need to be raised separately with NCIT, but the Uberon class is now anatomically correct independent of that NCIT axiom.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835001572)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..dbb386a69 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -223,10 +223,10 @@ subset: common_anatomy
 subset: upper_level
 xref: BFO:0000003
 disjoint_from: UBERON:0001062 ! anatomical entity
-property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae
 relationship: present_in_taxon NCBITaxon:33208 ! Metazoa
 relationship: present_in_taxon NCBITaxon:4751 ! Fungi
+property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 
 [Term]
 id: UBERON:0000002
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the septum primum." [Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,9 +114759,10 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3522" xsd:anyURI
 
 [Term]
 id: UBERON:0006679

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#65](https://github.com/ai4curation/eval-ont-agent-uberon/pull/65)
- **F1**: 0.286  **Precision**: 0.286  **Recall**: 0.286  **Jaccard**: 0.167
- **Trace**: [25615969461](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615969461)
- **Workflow run**: [25615969461](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615969461)

#### Agent PR Comment

## Summary

This change addresses issue #3522 by correcting the anatomical placement of UBERON:0006678 `foramen secundum`.

## Changes made

- Updated the text definition from "A foramen in the septum secundum" to "A foramen in the atrial septum primum".
- Updated the logical definition from:
  - `anatomical conduit` and `part_of` some `atrial septum secundum`
  to:
  - `anatomical conduit` and `part_of` some `atrial septum primum`.
- Added a `term_tracker_item` property linking the term to issue #3522.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert` as required.

## Rationale

The issue discussion noted that the foramen secundum/ostium secundum forms as perforations in the septum primum, not in the septum secundum. This is also consistent with the existing UBERON:0004154 `atrial septum primum` definition, which states that perforations appear in the superior part of the septum primum, forming the ostium secundum.

## Checklist completed

- [x] Read issue context and comments.
- [x] Checked the existing `foramen secundum`, `atrial septum primum`, `atrial septum secundum`, and `anatomical conduit` terms.
- [x] Checked DOSDP patterns for an applicable anatomical conduit/part-of pattern; none appeared applicable.
- [x] Edited via `obo-checkout.pl` / `obo-checkin.pl` rather than directly editing the large ontology file.
- [x] Reserialized the ontology with `robot convert`.
- [x] Committed only `src/ontology/uberon-edit.obo`.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615969461)


#### Agent Issue Comment

Updated UBERON:0006678 (foramen secundum) to place it as part of atrial septum primum rather than atrial septum secundum, and updated the text definition accordingly. Changes committed for PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615969461)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..e69c750bd 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -223,10 +223,10 @@ subset: common_anatomy
 subset: upper_level
 xref: BFO:0000003
 disjoint_from: UBERON:0001062 ! anatomical entity
-property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae
 relationship: present_in_taxon NCBITaxon:33208 ! Metazoa
 relationship: present_in_taxon NCBITaxon:4751 ! Fungi
+property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 
 [Term]
 id: UBERON:0000002
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the atrial septum primum." [GO:0003284, Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,9 +114759,10 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3522" xsd:anyURI
 
 [Term]
 id: UBERON:0006679

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#47](https://github.com/ai4curation/eval-ont-agent-uberon/pull/47)
- **F1**: 0.286  **Precision**: 0.286  **Recall**: 0.286  **Jaccard**: 0.167
- **Trace**: [25615927734](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615927734)
- **Workflow run**: [25615927734](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927734)

#### Agent PR Comment

## Summary

This PR addresses issue #3522 by correcting the UBERON representation of `foramen secundum` (`UBERON:0006678`).

## Changes

- Updated the text definition from "A foramen in the septum secundum" to "A foramen in the septum primum".
- Updated the logical definition from `part_of UBERON:0004155 ! atrial septum secundum` to `part_of UBERON:0004154 ! atrial septum primum`.
- Added a `term_tracker_item` link to issue #3522.

## Rationale

The issue discussion noted that the foramen secundum/ostium secundum forms in the septum primum, not in the septum secundum. This is also consistent with the existing `atrial septum primum` definition and the existing external definition on `UBERON:0006678`, which describes it as an opening perforating the septum primum.

## Checklist Completed

- Read the imported issue context and repository guidance.
- Checked relevant existing UBERON terms: `UBERON:0006678`, `UBERON:0004154`, `UBERON:0004155`, and `UBERON:0004111`.
- Checked the applicable DOSDP pattern for anatomical entities that are part of another anatomical entity.
- Reviewed the cited Wikipedia page for foramen secundum, which states it is in the septum primum and distinguishes it from the foramen ovale in the septum secundum.
- Edited via `obo-checkout.pl` and `obo-checkin.pl` rather than directly editing the main ontology file.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Validated logical consistency with `robot reason --reasoner ELK`.

@dragon-ai-agent

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927734)


#### Agent Issue Comment

Updated UBERON:0006678 so foramen secundum is defined as a foramen in the septum primum, with the logical `part_of` axiom changed from atrial septum secundum to atrial septum primum. Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615927734)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..e69c750bd 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -223,10 +223,10 @@ subset: common_anatomy
 subset: upper_level
 xref: BFO:0000003
 disjoint_from: UBERON:0001062 ! anatomical entity
-property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae
 relationship: present_in_taxon NCBITaxon:33208 ! Metazoa
 relationship: present_in_taxon NCBITaxon:4751 ! Fungi
+property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 
 [Term]
 id: UBERON:0000002
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen in the atrial septum primum." [GO:0003284, Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,9 +114759,10 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3522" xsd:anyURI
 
 [Term]
 id: UBERON:0006679

```

### Attempt 8: gpt-5.5 / codex

- **Eval PR**: [#26](https://github.com/ai4curation/eval-ont-agent-uberon/pull/26)
- **F1**: 0.286  **Precision**: 0.286  **Recall**: 0.286  **Jaccard**: 0.167
- **Trace**: [25615885326](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615885326)
- **Workflow run**: [25615885326](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615885326)

#### Agent PR Comment

## Summary

This change addresses issue #3522 by correcting the Uberon relationship for `UBERON:0006678` foramen secundum.

## Changes

- Updated the text definition for `UBERON:0006678` from a foramen in the septum secundum to a foramen that perforates the atrial septum primum.
- Updated the logical definition from:
  - `intersection_of: part_of UBERON:0004155 ! atrial septum secundum`
  - to `intersection_of: part_of UBERON:0004154 ! atrial septum primum`
- Added `term_tracker_item` linking the term to issue #3522.

## Rationale

The issue and follow-up comment indicate that neither the current Uberon axiom nor the NCIT inverse relationship captures the anatomy correctly. Uberon's own existing external definition for `UBERON:0006678` states that the foramen secundum is one of the openings that perforate the septum primum between the two atria of the embryonic heart. The updated definition and logical axiom now align with that existing supporting metadata and with the proposed correction in the issue thread.

## Checklist

- Read `__issue_context__.json`.
- Checked the current stanzas for `UBERON:0006678`, `UBERON:0004154`, `UBERON:0004155`, and `UBERON:0004111`.
- Checked for relevant DOSDP patterns under `src/patterns/dosdp-patterns`.
- Edited `UBERON:0006678` via `obo-checkout.pl` / `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Rechecked the updated `UBERON:0006678` stanza with `obo-grep.pl`.
- Ran `git diff --check -- src/ontology/uberon-edit.obo`.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615885326)


#### Agent Issue Comment

Updated UBERON:0006678 so foramen secundum is defined as perforating the atrial septum primum, with its logical `part_of` axiom pointing to UBERON:0004154 rather than UBERON:0004155.

Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615885326)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d1d6c46d4..798336a66 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -223,10 +223,10 @@ subset: common_anatomy
 subset: upper_level
 xref: BFO:0000003
 disjoint_from: UBERON:0001062 ! anatomical entity
-property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae
 relationship: present_in_taxon NCBITaxon:33208 ! Metazoa
 relationship: present_in_taxon NCBITaxon:4751 ! Fungi
+property_value: seeAlso "https://github.com/OBOFoundry/COB/issues/51" xsd:anyURI
 
 [Term]
 id: UBERON:0000002
@@ -114747,7 +114747,7 @@ intersection_of: bounding_layer_of UBERON:0000483 ! epithelium
 [Term]
 id: UBERON:0006678
 name: foramen secundum
-def: "A foramen in the septum secundum." [Wikipedia:Foramen_secundum]
+def: "A foramen that perforates the atrial septum primum between the two atria of the embryonic heart." [VHOG:0001471, Wikipedia:Foramen_secundum]
 synonym: "foramen secundum" RELATED OMO:0003011 [Wikipedia:Foramen_secundum]
 synonym: "ostium secundum" EXACT OMO:0003011 [VHOG:0001471]
 xref: EHDAA2:0001828
@@ -114759,9 +114759,10 @@ xref: UMLS:C1517293 {source="ncithesaurus:Foramen_Secundum"}
 xref: VHOG:0001471
 xref: Wikipedia:Foramen_secundum
 intersection_of: UBERON:0004111 ! anatomical conduit
-intersection_of: part_of UBERON:0004155 ! atrial septum secundum
+intersection_of: part_of UBERON:0004154 ! atrial septum primum
 property_value: external_definition "Second of the two openings to perforate the septum primum between the two atria of the embryonic heart. [TFD][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="http://bgee.unil.ch/", source="http://medical-dictionary.thefreedictionary.com/foramen"}
 property_value: homology_notes "The tetrapod clade develops a complete atrial septum and loses the fifth aortic arch altogether. [ISBN:978-0030223693 Liem KF, Bemis WE, Walker WF, Grande L, Functional Anatomy of the Vertebrates: An Evolutionary Perspective (2001) p.620]; [about heart development] In the various tetrapod classes ontogenetic events essentially recapitulate the phylogenetic stages.[well established][VHOG]" xsd:string {date_retrieved="2012-09-17", external_class="VHOG:0001471", ontology="VHOG", source="ISBN:978-0721676678 p.433", source="http://bgee.unil.ch/"}
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3522" xsd:anyURI
 
 [Term]
 id: UBERON:0006679

```
