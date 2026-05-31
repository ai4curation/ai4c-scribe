---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3495
pr_number: 3542
issue_title: epithelium and lamina propria for GI tract
pr_author: cmungall
pr_merged_at: '2025-05-27'
task_type: new_term
difficulty: hard
scoping: mostly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
scoping_notes: The issue requested both epithelium and lamina propria terms for GI
  tract segments. This PR addresses the lamina propria portion; epithelium terms were
  in a separate PR.
domain_area: gastrointestinal-anatomy
best_f1: 0.695
best_model: claude-opus-4.7
---

# PR #3542 — epithelium and lamina propria for GI tract

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3495](https://github.com/obophenotype/uberon/issues/3495) | [PR #3542](https://github.com/obophenotype/uberon/pull/3542) | @cmungall | merged 2025-05-27

`new_term` `hard` `mostly_scoped` `approved_first_time`

## Context

The Gut Cell Atlas project needed lamina propria terms for seven gut segments (ascending colon, descending colon, sigmoid colon, transverse colon, stomach, caecum, and rectum). Each term follows a compositional pattern: "The lamina propria that underlies the epithelial lining of the {gut segment}."

## Changes Made

Added seven new lamina propria terms to uberon-edit.obo with 88 lines of additions. Each term included a definition following the compositional pattern, appropriate synonyms, is_a classification under lamina propria, and part_of relationships to the specific gut segment. Some existing term stanzas were also updated (9 deletions).

## Resolution

Hard difficulty due to the scale and consistency requirements. The agent must create seven parallel term stanzas, each following the same compositional pattern but with segment-specific relationships. It must correctly identify the parent lamina propria class, use the right part_of targets for each colon region, and ensure no inconsistencies across the batch. This was a high-priority request from an external project.

## Curation Note (data quality)

Flagged `case_quality: poor` for **metadiff scoring purposes only** — the gold
PR #3542 is itself correct and well-scoped; the problem is that line-level
metadiff systematically under-represents agent quality on this case.

**Multi-PR resolution.** Issue #3495 asked for both epithelium and lamina
propria terms. The human resolved it with two PRs: **#3541** (4 colon
epithelium terms) and **#3542** (7 lamina propria terms — the gold for this
case). @dosumis's issue-comment-2896247830 explicitly scopes the lamina
propria request that PR #3542 fulfils. Agents that *also* added the four colon
epithelium terms (pr67, pr50, pr99, pr31) are reproducing companion PR #3541's
deliverable, which legitimately answers the issue but is out of scope for the
#3542 gold and is therefore penalised by metadiff as scope creep. The
well-scoped lamina-propria-only attempts are pr247 (claude-opus-4.7), pr82
(gpt-5.4 codex), and pr317 (claude-sonnet-4.5).

**Three case-wide metadiff distortions** (independent of agent quality):

1. **Placeholder-vs-canonical ID artifact.** Gold uses UBERON:8600134-140.
   Every agent used an unpredictable placeholder range (UBERON:9900001-7,
   UBERON:9900000-10, UBERON:7700001-11, or UBERON:8600051-57) per the
   project's documented placeholder convention. The agent cannot predict the
   canonical IDs the curator will assign; this alone caps F1 well below 1.0
   for every attempt.
2. **robot-convert reserialization churn.** Gold #3542 carries ~9 lines of
   non-issue churn from @dosumis's "reserialised" commit: annotation-attribute
   reordering (`{source=, seeAlso=}` → `{seeAlso=, source=}`) on unrelated
   terms (UBERON:0001638, UBERON:0012260/61/62, etc.) and the
   `property_value: seeAlso "...COB/issues/51"` line moved below the
   `relationship:` block on UBERON:0000003. Agents that ran `robot convert`
   (pr67/pr50/pr82/pr31) incidentally reproduce only the first `seeAlso` hunk;
   agents that did not (pr247/pr317/pr99) reproduce none. Either way this is
   serialization noise, not issue content.
3. **Late-arriving requirement.** The ORCID definition dbxref
   (`https://orcid.org/0000-0003-4389-9821`) and the
   `dcterms-date "2025-05-27T17:07:22Z"` only appeared in
   issue-comment-2913353220 (2025-05-27), after most agent runs. Attempts
   could not have known to use them, and the gold's own sigmoid-colon dbxref
   carries a human typo (`...4389-98219`, an extra "9") that persisted to
   master.

**Net.** Judge attempts on substance — seven lamina propria terms with genus
UBERON:0000030, correct segment-specific part_of targets
(UBERON:0001156/0001157/0001158/0001159/0000945/0001153/0001052), the
requested definition pattern, both synonym forms, and NO duplicated asserted
`relationship: part_of` (per @dosumis) — not on the compressed metadiff F1.
pr247 (F1 0.695) is substantively a clean success despite scoring < 0.7.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 76d60d4dd7..e4dcd64366 100644
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
@@ -930,7 +930,7 @@ intersection_of: has_quality PATO:0002236 ! aliform
 relationship: capable_of_part_of GO:0060361 ! flight
 relationship: in_taxon NCBITaxon:33213 ! Bilateria
 relationship: never_in_taxon NCBITaxon:118072 {source="bgee"} ! Coelacanthimorpha
-relationship: never_in_taxon NCBITaxon:186634 {source="bgee", seeAlso="Wikipedia:Flying_fish"} ! Otomorpha
+relationship: never_in_taxon NCBITaxon:186634 {seeAlso="Wikipedia:Flying_fish", source="bgee"} ! Otomorpha
 relationship: never_in_taxon NCBITaxon:314147 {source="bgee"} ! Glires
 relationship: never_in_taxon NCBITaxon:6231 {source="bgee"} ! Nematoda
 relationship: never_in_taxon NCBITaxon:7878 {source="bgee"} ! Dipnomorpha
@@ -22375,7 +22375,7 @@ relationship: preaxialmost_part_of UBERON:0002398 ! manus
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/6/64/Thumb-up.jpg" xsd:anyURI
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/2/2c/Thumbs_up.jpg" xsd:anyURI
 property_value: taxon_notes "Not present in Anurans (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012260"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012260", source="PMID:10220427", source="PhenoscapeRCN"}
 
 [Term]
 id: UBERON:0001464
@@ -28059,7 +28059,7 @@ relationship: part_of UBERON:0010272 ! hyoid apparatus
 property_value: axiom_lost_from_external_ontology "relationship loss: part_of hyoid plate (AAO:0000664)[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO"}
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/1/1f/Gray186.png" xsd:anyURI
 property_value: external_definition "Paired processes that extend posterolaterally from the posterior margin of the hyoid plate. These processes are the ossified posteromedial processes and invest the laryngeal apparatus.[AAO]" xsd:string {date_retrieved="2012-06-20", external_class="AAO:0000684", ontology="AAO", source="AAO:LAP"}
-property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {source="WP", seeAlso="https://github.com/obophenotype/uberon/issues/548"}
+property_value: taxon_notes "The hyoid bone is derived from the lower half of the second gill arch in fish, which separates the first gill slit from the spiracle. In many animals, it also incorporates elements of other gill arches, and has a correspondingly greater number of cornua. Amphibians and reptiles may have many cornua, while mammals (including humans) have two pairs, and birds only one. In birds, and some reptiles, the body of the hyoid is greatly extended forward, creating a solid bony support for the tongue. The howler monkey Alouatta has a pneumatized hyoid bone, one of the few cases of postcranial pneumatization of bones outside Saurischia." xsd:string {seeAlso="https://github.com/obophenotype/uberon/issues/548", source="WP"}
 
 [Term]
 id: UBERON:0001686
@@ -38534,7 +38534,7 @@ xref: Wikipedia:Spinal_accessory_nerve
 xref: XAO:0004214
 intersection_of: UBERON:0001021 ! nerve
 intersection_of: extends_fibers_into UBERON:0020358 ! accessory XI nerve nucleus
-relationship: dubious_for_taxon NCBITaxon:8292 {source="VHOG", source="Wikipedia", seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7"} ! Amphibia
+relationship: dubious_for_taxon NCBITaxon:8292 {seeAlso="http://code.google.com/p/xenopus-anatomy-ontology/issues/detail?id=7", source="VHOG", source="Wikipedia"} ! Amphibia
 relationship: in_taxon NCBITaxon:32523 ! Tetrapoda
 relationship: innervates UBERON:0001737 ! larynx
 relationship: innervates UBERON:3010692 {gci_relation="part_of", gci_filler="NCBITaxon:8292", source="ISBN:080184780X"} ! m. cucullaris
@@ -74530,7 +74530,7 @@ relationship: part_of UBERON:5003622 ! manual digit 2 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/d/d5/Index_finger.JPG" xsd:anyURI
 property_value: has_relational_adjective "indicis" xsd:string
 property_value: taxon_notes "Anurans lack manual digit 1, so manual digit 2 is the digit after the prepollex (Phenotype RCN Oct 2012)" xsd:string
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012261"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012261", source="PMID:10220427", source="PhenoscapeRCN"}
 
 [Term]
 id: UBERON:0003623
@@ -74567,7 +74567,7 @@ relationship: ambiguous_for_taxon NCBITaxon:8782 ! Aves
 relationship: part_of UBERON:0012141 {source="https://github.com/obophenotype/uberon/wiki/Inferring-part-of-relationships"} ! manual digitopodium region
 relationship: part_of UBERON:5003623 ! manual digit 3 plus metapodial segment
 property_value: depiction "https://upload.wikimedia.org/wikipedia/commons/f/fd/Middle_finger.jpg" xsd:anyURI
-property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", source="PMID:10220427", source="PhenoscapeRCN", seeAlso="UBERON:0012262"}
+property_value: taxon_notes "This class represents the standard tetrapod configuration. Wagner proposes that avian digits I,II,III develop from C2,C3,C4. To support this scheme we have separate classes representing the avian digits (here called alula, manual digit, major digit)." xsd:string {scope="NCBITaxon:8782", seeAlso="UBERON:0012262", source="PMID:10220427", source="PhenoscapeRCN"}
 
 [Term]
 id: UBERON:0003624
@@ -138778,7 +138778,7 @@ name: spleen marginal sinus
 def: "The border region surrounding the spleen B cell follicles and the periarteriolar lymphoid sheath that separates it from the marginal zone that mediates lymphocyte entry into the white pulp from the blood." [MP:MP]
 subset: pheno_slim
 synonym: "splenic marginal sinus" EXACT [MP:0002363]
-xref: EMAPA:37964 {seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117", source="MA:th"}
+xref: EMAPA:37964 {source="MA:th", seeAlso="https://github.com/obophenotype/mouse-anatomy-ontology/issues/117"}
 xref: MA:0000754
 xref: NCIT:C49776
 xref: UMLS:C1710157 {source="ncithesaurus:Splenic_Marginal_Sinus"}
@@ -151539,7 +151539,7 @@ xref: SCTID:361795009
 xref: Wikipedia:Malleolus
 is_a: UBERON:0005913 ! zone of bone organ
 relationship: part_of UBERON:0004410 ! distal epiphysis of fibula
-property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", source="UBERON:skansa", seeAlso="UBERON:0004410"}
+property_value: taxon_notes "In bovids, the distal end of the fibula is present only as the lateral malleolus, a separate bone that articulates with the lateral side of the distal tibia." xsd:string {scope="NCBITaxon:9895", seeAlso="UBERON:0004410", source="UBERON:skansa"}
 
 [Term]
 id: UBERON:0012292
@@ -224872,6 +224872,85 @@ relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-
 relationship: part_of UBERON:0006642 ! muscle layer of oviduct
 property_value: dcterms-date "2025-03-04T15:33:17Z" xsd:dateTime
 
+[Term]
+id: UBERON:8600134
+name: ascending colon lamina propria
+def: "The lamina propria that underlies the epithelial lining of the ascending colon." [https://orcid.org/0000-0003-4389-9821]
+synonym: "ascending colonic lamina propria" EXACT []
+synonym: "lamina propria of ascending colon" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001156 ! ascending colon
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600135
+name: descending colon lamina propria
+def: "The lamina propria that underlies the epithelial lining of the descending colon." [https://orcid.org/0000-0003-4389-9821]
+synonym: "descending colonic lamina propria" EXACT []
+synonym: "lamina propria of descending colon" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001158 ! descending colon
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600136
+name: sigmoid colon lamina propria
+def: "The lamina propria that underlies the epithelial lining of the sigmoid colon." [https://orcid.org/0000-0003-4389-98219]
+synonym: "lamina propria of sigmoid colon" EXACT []
+synonym: "sigmoid colonic lamina propria" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001159 ! sigmoid colon
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600137
+name: transverse colon lamina propria
+def: "The lamina propria that underlies the epithelial lining of the transverse colon." [https://orcid.org/0000-0003-4389-9821]
+synonym: "lamina propria of transverse colon" EXACT []
+synonym: "transverse colonic lamina propria" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001157 ! transverse colon
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600138
+name: stomach lamina propria
+def: "The lamina propria that underlies the epithelial lining of the stomach." [https://orcid.org/0000-0003-4389-9821]
+synonym: "gastric lamina propria" EXACT []
+synonym: "lamina propria of stomach" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0000945 ! stomach
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600139
+name: caecum lamina propria
+def: "The lamina propria that underlies the epithelial lining of the caecum." [https://orcid.org/0000-0003-4389-9821]
+synonym: "cecal lamina propria" EXACT []
+synonym: "cecum lamina propria" EXACT []
+synonym: "lamina propria of caecum" EXACT []
+synonym: "lamina propria of cecum" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001153 ! caecum
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600140
+name: rectum lamina propria
+def: "The lamina propria that underlies the epithelial lining of the rectum." [https://orcid.org/0000-0003-4389-9821]
+synonym: "lamina propria of rectum" EXACT []
+synonym: "rectal lamina propria" EXACT []
+intersection_of: UBERON:0000030 ! lamina propria
+intersection_of: part_of UBERON:0001052 ! rectum
+relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
+property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
+
 [Term]
 id: UBERON:8700000
 name: aorta-gonad-mesonephros

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.695 | 0.611 | 0.805 | `b00612b` | [#247](https://github.com/ai4curation/eval-ont-agent-uberon/pull/247) | [attempt](attempts/pr247.md) |
| 2 | gpt-5.5 | opencode | 0.544 | 0.519 | 0.571 | `9a93c87` | [#67](https://github.com/ai4curation/eval-ont-agent-uberon/pull/67) | [attempt](attempts/pr67.md) |
| 3 | gpt-5.5 | opencode | 0.544 | 0.519 | 0.571 | `9a93c87` | [#50](https://github.com/ai4curation/eval-ont-agent-uberon/pull/50) | [attempt](attempts/pr50.md) |
| 4 | gpt-5.4 | codex | 0.432 | 0.352 | 0.559 | `193c5d1` | [#82](https://github.com/ai4curation/eval-ont-agent-uberon/pull/82) | [attempt](attempts/pr82.md) |
| 5 | gpt-5.4 | opencode | 0.400 | 0.352 | 0.463 | `1abe664` | [#664](https://github.com/ai4curation/eval-ont-agent-uberon/pull/664) | [attempt](attempts/pr664.md) |
| 6 | gpt-5.4 | opencode | 0.400 | 0.352 | 0.463 | `1abe664` | [#603](https://github.com/ai4curation/eval-ont-agent-uberon/pull/603) | [attempt](attempts/pr603.md) |
| 7 | claude-haiku-4.5 | claude | 0.354 | 0.315 | 0.405 | `459175c` | [#99](https://github.com/ai4curation/eval-ont-agent-uberon/pull/99) | [attempt](attempts/pr99.md) |
| 8 | claude-sonnet-4.5 | claude | 0.256 | 0.185 | 0.417 | `6a07ea5` | [#317](https://github.com/ai4curation/eval-ont-agent-uberon/pull/317) | [attempt](attempts/pr317.md) |
| 9 | gpt-5.5 | codex | 0.235 | 0.222 | 0.250 | `46d8d7b` | [#31](https://github.com/ai4curation/eval-ont-agent-uberon/pull/31) | [attempt](attempts/pr31.md) |
