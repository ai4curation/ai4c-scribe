# PR #32012 — NTR: MF vesicle membrane tethering activity

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31863](https://github.com/geneontology/go-ontology/issues/31863)
- **PR**: [#32012](https://github.com/geneontology/go-ontology/pull/32012)
- **Author**: @dragon-ai-agent
- **Merged**: 2026-04-29
- **task_type**: obsoletion
- **difficulty**: hard
- **scoping**: tightly_scoped
- **scope**: multi_term
- **review_outcome**: approved_first_time

## Context

Issue #31863 requested a new MF term for vesicle membrane tethering activity, which was added in PR #31895 as GO:7770062. This follow-up PR completes the namespace correction by obsoleting 5 biological_process terms that described vesicle tethering activities and rewiring their associated protein complexes to point at the new MF term.

## Changes Made

In `src/ontology/go-edit.obo` (net +10 lines from 40 additions / 30 deletions):
- Obsoleted 5 vesicle-tethering BP terms that represented molecular functions
- Rewired protein complex terms that previously had `part_of` relationships to the obsoleted BP terms, pointing them instead to the new MF term GO:7770062
- Added appropriate `replaced_by` and `consider` tags for annotation migration guidance
- Updated relationship axioms on complex terms to maintain graph connectivity

## Resolution

Merged directly despite the complexity. This was a well-planned cascade from the new term addition in PR #31895, with clear obsoletion rationale (MF_in_BP correction) and explicit curator approval in the issue discussion. The 40-line addition reflects both obsoletion metadata and the relationship rewiring needed to maintain ontology coherence.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f6a5e38a4..6e6af3307 100644
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
 
@@ -6943,7 +6943,7 @@ synonym: "Golgi associated retrograde protein complex" EXACT []
 synonym: "VFT tethering complex" EXACT []
 synonym: "Vps fifty three tethering complex" EXACT []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 relationship: part_of GO:0031410 ! cytoplasmic vesicle
 
@@ -131917,7 +131917,7 @@ synonym: "conserved oligomeric Golgi complex" EXACT []
 synonym: "Golgi transport complex" EXACT []
 synonym: "Sec34/35 complex" NARROW []
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099041 ! vesicle tethering to Golgi
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005794 ! Golgi apparatus
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31397" xsd:anyURI
 
@@ -161601,7 +161601,7 @@ synonym: "TRAPP1" NARROW [GOC:vw]
 synonym: "TRAPP2" NARROW [GOC:vw]
 xref: Wikipedia:TRAPP_complex
 is_a: GO:0140535 ! intracellular protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 
 [Term]
 id: GO:0030009
@@ -171204,7 +171204,7 @@ name: HOPS complex
 namespace: cellular_component
 def: "A multimeric protein complex that associates with the vacuolar membrane, late endosomal (multivesicular body) and lysosomal membranes. HOPS is a tethering complex involved in vesicle fusion." [PMID:10944212, PMID:23645161]
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0016020 ! membrane
 
 [Term]
@@ -196041,7 +196041,7 @@ name: CORVET complex
 namespace: cellular_component
 def: "A multimeric protein complex that acts as an endosomal tethering complex (CORVET = class C core vacuole/endosome tethering) by cooperating with Rab GTPases to capture endosomal vesicles and trap them prior to the action of SNAREs; the complex is involved in endo-lysosomal biogenesis and required for transport between endosome and vacuole. The Saccharomyces cerevisiae complex contains Vps8p, Vps3p, Pep5p, Vps16p, Pep3p, and Vps33p." [PMID:17488625]
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005768 ! endosome
 
 [Term]
@@ -385478,7 +385478,7 @@ synonym: "CATCHR family complex" BROAD []
 synonym: "Dsl1p complex" EXACT [PMID:19151722]
 synonym: "NZR complex" EXACT [PMID:25364732]
 is_a: GO:0032991 ! protein-containing complex
-relationship: capable_of_part_of GO:0099022 ! vesicle tethering
+relationship: capable_of GO:7770062 ! vesicle membrane tethering activity
 relationship: part_of GO:0005783 ! endoplasmic reticulum
 created_by: mah
 creation_date: 2009-09-22T03:41:38Z
@@ -418674,12 +418674,14 @@ creation_date: 2013-01-08T11:08:57Z
 
 [Term]
 id: GO:0090522
-name: vesicle tethering involved in exocytosis
+name: obsolete vesicle tethering involved in exocytosis
 namespace: biological_process
-def: "The initial, indirect interaction between a secretory vesicle membrane and a site of exocytosis in the plasma membrane. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior to docking and fusion." [GOC:rn, PMID:10559876, PMID:17052174, PMID:17488620, PMID:22420621, PMID:27243008]
-synonym: "vesicle tethering to plasma membrane" NARROW []
-intersection_of: GO:0099022 ! vesicle tethering
-intersection_of: part_of GO:0006887 ! exocytosis
+def: "OBSOLETE. The initial, indirect interaction between a secretory vesicle membrane and a site of exocytosis in the plasma membrane. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior to docking and fusion." [GOC:rn, PMID:10559876, PMID:17052174, PMID:17488620, PMID:22420621, PMID:27243008]
+comment: This term was obsoleted because it represents a molecular function (vesicle membrane tethering activity) rather than a biological process, and is pre-composed; the same information is better represented as a GO-CAM model. Annotations should be reviewed and reannotated to the new MF term GO:7770062 'vesicle membrane tethering activity', combined with GO:0006887 'exocytosis' or a descendant as appropriate.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31872" xsd:anyURI
+is_obsolete: true
+consider: GO:7770062
+consider: GO:0006887
 created_by: tb
 creation_date: 2013-01-08T15:07:50Z
 
@@ -435256,11 +435258,13 @@ intersection_of: part_of GO:0032541 ! cortical endoplasmic reticulum
 
 [Term]
 id: GO:0099022
-name: vesicle tethering
+name: obsolete vesicle tethering
 namespace: biological_process
-def: "The initial, indirect interaction between a vesicle membrane and a membrane to which it is targeted for fusion. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior to interaction between factors involved in fusion." [PMID:27243008]
-is_a: GO:0016043 ! cellular component organization
-relationship: part_of GO:0006903 ! vesicle targeting
+def: "OBSOLETE. The initial, indirect interaction between a vesicle membrane and a membrane to which it is targeted for fusion. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior to interaction between factors involved in fusion." [PMID:27243008]
+comment: This term was obsoleted because it represents a molecular function (vesicle membrane tethering activity) rather than a biological process. Annotations should be reviewed and reannotated to the new MF term GO:7770062 'vesicle membrane tethering activity', and where appropriate combined with the relevant vesicle-mediated transport / exocytosis process term in a GO-CAM model.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31881" xsd:anyURI
+is_obsolete: true
+consider: GO:7770062
 
 [Term]
 id: GO:0099023
@@ -435268,7 +435272,7 @@ name: vesicle tethering complex
 namespace: cellular_component
 def: "Any protein complex that plays a role in vesicle tethering." [GOC:dos, GOC:vw, PMID:27243008]
 intersection_of: GO:0032991 ! protein-containing complex
-intersection_of: capable_of_part_of GO:0099022 ! vesicle tethering
+intersection_of: capable_of GO:7770062 ! vesicle membrane tethering activity
 
 [Term]
 id: GO:0099024
@@ -435440,11 +435444,13 @@ intersection_of: has_primary_input CHEBI:17761 ! ceramide
 
 [Term]
 id: GO:0099041
-name: vesicle tethering to Golgi
+name: obsolete vesicle tethering to Golgi
 namespace: biological_process
-def: "The initial, indirect interaction between a transport vesicle membrane and the membrane of the Golgi. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior fusion." [PMID:27243008]
-intersection_of: GO:0099022 ! vesicle tethering
-intersection_of: immediately_causally_upstream_of GO:0048280 ! vesicle fusion with Golgi apparatus
+def: "OBSOLETE. The initial, indirect interaction between a transport vesicle membrane and the membrane of the Golgi. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior fusion." [PMID:27243008]
+comment: This term was obsoleted because it represents a molecular function rather than a biological process, and is pre-composed; the same information is better represented as a GO-CAM model. Annotations should be reviewed and reannotated to GO:7770062 'vesicle membrane tethering activity', combined with the appropriate vesicle transport pathway BP term as part of a GO-CAM model.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31872" xsd:anyURI
+is_obsolete: true
+consider: GO:7770062
 created_by: tb
 creation_date: 2013-01-08T15:07:50Z
 
@@ -435468,11 +435474,13 @@ is_obsolete: true
 
 [Term]
 id: GO:0099044
-name: vesicle tethering to endoplasmic reticulum
+name: obsolete vesicle tethering to endoplasmic reticulum
 namespace: biological_process
-def: "The initial, indirect interaction between a transport vesicle membrane and the membrane of the endoplasmic reticulum. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior fusion." [PMID:27243008]
-intersection_of: GO:0099022 ! vesicle tethering
-intersection_of: immediately_causally_upstream_of GO:0048279 ! vesicle fusion with endoplasmic reticulum
+def: "OBSOLETE. The initial, indirect interaction between a transport vesicle membrane and the membrane of the endoplasmic reticulum. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. Interaction can occur via direct binding to membrane phospholipids or membrane proteins, or via binding to vesicle coat proteins. This process is distinct from and prior fusion." [PMID:27243008]
+comment: This term was obsoleted because it represents a molecular function rather than a biological process. Annotations should be reviewed; the VAP-related proteins previously annotated here are lipid transfer/adaptor proteins rather than vesicle tethers, and other types of membrane adaptor terms may be more appropriate. Where the activity is genuinely vesicle tethering, reannotate to GO:7770062 'vesicle membrane tethering activity'.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31868" xsd:anyURI
+is_obsolete: true
+consider: GO:7770062
 created_by: tb
 creation_date: 2013-01-08T15:07:50Z
 
@@ -435706,12 +435714,14 @@ relationship: part_of GO:0007416 ! synapse assembly
 
 [Term]
 id: GO:0099069
-name: synaptic vesicle tethering involved in synaptic vesicle exocytosis
+name: obsolete synaptic vesicle tethering involved in synaptic vesicle exocytosis
 namespace: biological_process
-def: "The initial, indirect interaction between a synaptic vesicle membrane and a the preseynaptic membrane active zone. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. This process is distinct from and prior to synaptic vesicle priming and fusion." [GOC:rn]
-intersection_of: GO:0099022 ! vesicle tethering
-intersection_of: has_participant GO:0008021 ! synaptic vesicle
-intersection_of: part_of GO:0016081 ! synaptic vesicle docking
+def: "OBSOLETE. The initial, indirect interaction between a synaptic vesicle membrane and a the preseynaptic membrane active zone. This interaction is mediated by tethering factors (or complexes), which interact with both membranes. This process is distinct from and prior to synaptic vesicle priming and fusion." [GOC:rn]
+comment: This term was obsoleted because it represents a molecular function (vesicle membrane tethering activity) rather than a biological process, and is pre-composed; the same information is better represented as a GO-CAM model. Annotations should be reviewed and reannotated to the new MF term GO:7770062 'vesicle membrane tethering activity', combined with GO:0016079 'synaptic vesicle exocytosis' as appropriate.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31871" xsd:anyURI
+is_obsolete: true
+consider: GO:7770062
+consider: GO:0016079
 
 [Term]
 id: GO:0099070

```
