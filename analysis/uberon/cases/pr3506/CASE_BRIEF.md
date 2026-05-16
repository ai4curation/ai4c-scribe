# PR #3506 — two new defs for undefined terms

- **Ontology**: uberon
- **Repo**: obophenotype/uberon
- **Issue**: [#3448](https://github.com/obophenotype/uberon/issues/3448)
- **PR**: [#3506](https://github.com/obophenotype/uberon/pull/3506)
- **Author**: @cmungall
- **Merged**: 2025-04-23
- **task_type**: axiom_repair
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: multi_term
- **review_outcome**: approved_first_time

## Context

Issue #3448 identified two Uberon terms lacking text definitions: insular cortex (UBERON:0034891) and Brodmann (1909) area 9 (UBERON:0013540). Definitions were provided by a domain expert (Dana Gabuxda, ORCID:0000-0002-4964-5083) as part of the SCORCH Project's efforts to improve neuroanatomical term quality.

## Changes Made

The PR added two definition lines to src/ontology/uberon-edit.obo, one for each term. The definitions include proper OBO format references and contributor ORCID attribution. Insular cortex was defined based on its location and functional role, and Brodmann area 9 was defined based on its cytoarchitectural characteristics and location in the prefrontal cortex.

## Resolution

Simple difficulty. Adding text definitions to existing terms is a straightforward operation in OBO format. The key requirement is having an accurate, well-sourced definition text. In this case, the definitions were provided by a domain expert in the issue, so an agent would primarily need to format them correctly in OBO syntax with proper attribution.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd11801..82a8b281c3 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9, or BA9, refers to a cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia:Brodmann_area_9, https://orcid.org/0000-0002-4964-5083]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -180721,6 +180722,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex (also insula and insular lobe) is a portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [Wikipedia:INSULA, MESH:D007419, https://orcid.org/0000-0002-4964-5083]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]

```

## Agent Attempts (11)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#331](https://github.com/ai4curation/eval-ont-agent-uberon/pull/331)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25888685131](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25888685131)
- **Workflow run**: [25888685131](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888685131)

#### Agent PR Comment

# PR: Add definitions for insular cortex and Brodmann area 9

## Summary
This PR addresses issue #3448 by adding textual definitions to two previously undefined UBERON terms that are important for neuroscience research, particularly for the SCORCH Project (Single Cell Opioid Response in the Context of HIV).

## Changes Made

### 1. UBERON:0034891 (insular cortex)
**Definition added:**
"The insular cortex is a portion of the cerebral cortex folded deep within the lateral sulcus within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor, somatosensory, and socioemotional functions."

**Metadata added:**
- Contributor: Dana Gabuxda (ORCID: 0000-0002-4964-5083)
- Date: 2026-05-14
- Reference: Wikipedia:Insular_cortex

### 2. UBERON:0013540 (Brodmann (1909) area 9)
**Definition added:**
A comprehensive definition describing Brodmann area 9 as a cytoarchitecturally defined portion of the frontal cortex involved in executive functions. The definition includes detailed cytoarchitectural features including the granular structure and layer organization (layers II-V with specific sublayer characteristics).

**Metadata added:**
- Contributor: Dana Gabuxda (ORCID: 0000-0002-4964-5083)
- Date: 2026-05-14
- Reference: Wikipedia:Brodmann_area_9

## Validation Completed
- ✅ Both terms successfully checked out from the main ontology file
- ✅ Definitions added in proper OBO format
- ✅ Contributor and date metadata included per UBERON standards
- ✅ Definitions checked back into ontology with `obo-checkin.pl`
- ✅ Verified definitions are properly in the serialized ontology file using `obo-grep.pl`

## Notes
- The definitions were based on the suggestions provided in the issue
- Wikipedia was used as reference source as indicated in the original issue
- Both terms had appropriate synonyms and cross-references already in place
- The contributor information was sourced from the issue submission (Dana Gabuxda on behalf of SCORCH Project)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888685131)


#### Agent Issue Comment

Changes completed for issue #3448.

I've added definitions to both requested terms:

1. **UBERON:0034891 (insular cortex)** - Added definition describing the insular cortex as a portion of the cerebral cortex in the lateral sulcus involved in gustatory, sensorimotor, somatosensory, and socioemotional functions.

2. **UBERON:0013540 (Brodmann (1909) area 9)** - Added comprehensive definition with cytoarchitectural details including granular structure and involvement in executive functions such as working memory, planning, and decision-making.

Both terms have been updated with contributor metadata (Dana Gabuxda, ORCID:0000-0002-4964-5083) and date metadata (2026-05-14).

The definitions were based on the suggestions provided in the issue and referenced to Wikipedia as indicated.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25888685131)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..bf16fa9bb 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9 (BA9) is a cytoarchitecturally defined portion of the frontal cortex in humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. The cytoarchitecture is granular due to high concentration of granule cells in layer IV. Layer V is divisible into sublayers 5a and 5b, with layer 5a containing densely distributed medium-size ganglion cells that partially merge with layer IV, and layer 5b clearer and cell-poor. Sublayer 3b of the external pyramidal layer (layer III) contains smaller and sparser pyramidal cells, and the external granular layer (II) is narrow with sparsely distributed granule cells." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,8 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180724,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex is a portion of the cerebral cortex folded deep within the lateral sulcus within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor, somatosensory, and socioemotional functions." [Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180735,6 +180739,8 @@ xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
 
 [Term]
 id: UBERON:0034892

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#300](https://github.com/ai4curation/eval-ont-agent-uberon/pull/300)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25877984265](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25877984265)
- **Workflow run**: [25877984265](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877984265)

#### Agent PR Comment

## Summary

This PR adds text definitions to two previously undefined UBERON terms as requested in issue #3448, submitted on behalf of the SCORCH Project (Single Cell Opioid Response in the Context of HIV).

#### Agent Issue Comment

Thank you for submitting these definition requests for the SCORCH Project!

I have successfully added definitions to both terms as requested:
- UBERON:0034891 (insular cortex) 
- UBERON:0013540 (Brodmann area 9)

Both terms now include comprehensive definitions with proper references (Wikipedia and MeSH), along with metadata crediting Dana Gabuxda as the contributor.

Changes have been committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25877984265)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..1adf922d0 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9, or BA9, refers to a cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156283,7 +156284,11 @@ xref: neuronames:1024 {source="BIRNLEX:1740"}
 xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
+created_by: dragon-ai-agent
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180726,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex (also insula and insular lobe) is a portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [Wikipedia:Insular_cortex, MESH:D000087623]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180734,7 +180740,11 @@ xref: FMA:242223
 xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
 relationship: part_of UBERON:0002022 ! insula
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
+created_by: dragon-ai-agent
 
 [Term]
 id: UBERON:0034892

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#271](https://github.com/ai4curation/eval-ont-agent-uberon/pull/271)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25844169488](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25844169488)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..bf16fa9bb 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9 (BA9) is a cytoarchitecturally defined portion of the frontal cortex in humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. The cytoarchitecture is granular due to high concentration of granule cells in layer IV. Layer V is divisible into sublayers 5a and 5b, with layer 5a containing densely distributed medium-size ganglion cells that partially merge with layer IV, and layer 5b clearer and cell-poor. Sublayer 3b of the external pyramidal layer (layer III) contains smaller and sparser pyramidal cells, and the external granular layer (II) is narrow with sparsely distributed granule cells." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,8 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180724,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex is a portion of the cerebral cortex folded deep within the lateral sulcus within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor, somatosensory, and socioemotional functions." [Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180735,6 +180739,8 @@ xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083 ! Dana Gabuxda
+property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime
 
 [Term]
 id: UBERON:0034892

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#237](https://github.com/ai4curation/eval-ont-agent-uberon/pull/237)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25834709756](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25834709756)
- **Workflow run**: [25834709756](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834709756)

#### Agent PR Comment

## Summary

Addresses issue #3448 by adding textual definitions to two previously
undefined UBERON terms.

### Terms updated

| ID | Name | Source |
| --- | --- | --- |
| `UBERON:0034891` | insular cortex | `Wikipedia:Insular_cortex` |
| `UBERON:0013540` | Brodmann (1909) area 9 | `Wikipedia:Brodmann_area_9` |

Definitions were taken from the text supplied in the issue (suggested by
Dana Gabuxda, ORCID `0000-0002-4964-5083`, as part of the SCORCH
Project — Single Cell Opioid Response in the Context of HIV).

A `term_tracker_item` property linking back to issue
[#3448](https://github.com/obophenotype/uberon/issues/3448) was added to
both terms.

## Rationale / decisions

- **Definition sources**: The issue cited "Wikipedia, MeSH" and
  "Adapted from Wikipedia" as references. I used `Wikipedia:Insular_cortex`
  and `Wikipedia:Brodmann_area_9` as the definition xrefs — both are
  already used in existing xrefs/synonyms on these very terms (matching the
  convention used by neighbouring Brodmann area terms such as
  `UBERON:0013539` Brodmann area 8 and `UBERON:0013541` Brodmann area 10,
  which all use a single `[Wikipedia:Brodmann_area_N]` xref on their
  definitions). I did not add a MeSH xref because I could not verify the
  exact MeSH descriptor ID from the local environment.
- **No structural changes**: The existing `is_a`, `part_of`, synonyms, and
  external xrefs were left untouched — the only additions are the `def`
  line and the `term_tracker_item` property.
- **Process**: Both terms were checked out via `obo-checkout.pl`, edited
  in `terms/`, and checked back in via `obo-checkin.pl`. Note: I was
  unable to run the recommended `robot convert` reserialisation step
  because the `robot` tool is not available in this environment; this can
  be applied as part of the standard release process if needed.

## Checklist

- [x] Read issue #3448 and verified both terms currently lack a `def:`
- [x] Confirmed parent/structural axioms for both terms are appropriate
- [x] Followed the definition-xref convention used by sibling Brodmann
      area terms
- [x] Added `term_tracker_item` linking to the originating issue on both
      terms
- [x] Committed only `src/ontology/uberon-edit.obo`
- [ ] `robot convert` reserialisation — not run (tool unavailable in env)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834709756)


#### Agent Issue Comment

Thank you for the definition suggestions! Both terms have been updated:

- `UBERON:0034891` — insular cortex
- `UBERON:0013540` — Brodmann (1909) area 9

Definitions added (adapted from the suggested text) along with `term_tracker_item` annotations linking back to this issue.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25834709756)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..df3230c9f 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9, or BA9, refers to a cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,7 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180723,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex (also insula and insular lobe) is a portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180735,6 +180738,7 @@ xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0034892

```

### Attempt 5: claude-sonnet-4.5 / copilot

- **Eval PR**: [#196](https://github.com/ai4curation/eval-ont-agent-uberon/pull/196)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25774521112](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25774521112)
- **Workflow run**: [25774521112](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25774521112)

#### Agent PR Comment

# Add definitions for two brain anatomy terms

This PR addresses issue #3448 by adding textual definitions to two previously undefined terms.

#### Agent Issue Comment

Definitions have been added for both terms as requested. Changes committed in PR #<NN>.

Both UBERON:0034891 (insular cortex) and UBERON:0013540 (Brodmann area 9) now have textual definitions with appropriate references and contributor attribution to Dana Gabuzda.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25774521112)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..181a59c81 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -72965,8 +72965,8 @@ id: UBERON:0003532
 name: hindlimb skin
 def: "A zone of skin that is part of a hindlimb [Automatically generated definition]." [OBOL:automatic]
 synonym: "hind limb skin" EXACT [OBOL:automatic]
-synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
 synonym: "lower limb skin" EXACT [FMA:23102]
+synonym: "lower limb skin" EXACT [https://orcid.org/0000-0002-0819-0473]
 synonym: "skin of hind limb" EXACT [OBOL:automatic]
 synonym: "skin of hindlimb" EXACT [OBOL:automatic]
 synonym: "skin of lower extremity" EXACT [OBOL:automatic]
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "Brodmann area 9, or BA9, refers to a cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156283,7 +156284,11 @@ xref: neuronames:1024 {source="BIRNLEX:1740"}
 xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: dcterms-date "2026-05-13T02:32:02.720Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
+created_by: dragon-ai-agent
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180726,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "The insular cortex (also insula and insular lobe) is a portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [MESH:D056129, Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180734,7 +180740,11 @@ xref: FMA:242223
 xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0002022 ! insula
+property_value: dcterms-date "2026-05-13T02:32:02.720Z" xsd:dateTime
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
+created_by: dragon-ai-agent
 
 [Term]
 id: UBERON:0034892

```

### Attempt 6: gemma-4-31b / opencode

- **Eval PR**: [#150](https://github.com/ai4curation/eval-ont-agent-uberon/pull/150)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25743781733](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25743781733)
- **Workflow run**: [25743781733](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25743781733)

#### Agent PR Comment

## Summary of Changes
Added textual definitions and metadata for two previously undefined terms:
- `UBERON:0034891` (insular cortex)
- `UBERON:0013540` (Brodmann (1909) area 9)

## Rationale
The definitions were provided by the user in the issue description, referencing Wikipedia and MeSH.

## Validation and Research
- Verified the existence and current state of both terms using `obo-grep.pl`.
- Validated the suggested definitions against Wikipedia.
- Added required metadata:
    - `dc-contributor`: Added ORCID for Dana Gabuxda.
    - `dcterms-date`: Added timestamp of the edit.
    - `term_tracker_item`: Linked to GH-3448.
- Used `obo-checkout.pl` and `obo-checkin.pl` for safe editing of the ontology.
- Reserialized the ontology using `robot convert` to ensure correct formatting.

## Checklist
- [x] Research and validate definitions and references.
- [x] Checkout terms.
- [x] Apply definitions and metadata.
- [x] Check in terms.
- [x] Reserialize ontology.
- [x] Commit changes.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25743781733)


#### Agent Issue Comment

The definitions for insular cortex (UBERON:0034891) and Brodmann area 9 (UBERON:0013540) have been added as requested. Changes are committed in PR #<NN>.
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25743781733)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..47a42b983 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156283,7 +156284,10 @@ xref: neuronames:1024 {source="BIRNLEX:1740"}
 xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: dcterms-date "2026-05-12T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "GH-3448" xsd:string
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180725,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [MeSH:D000087623, Wikipedia]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180734,7 +180739,10 @@ xref: FMA:242223
 xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0002022 ! insula
+property_value: dcterms-date "2026-05-12T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "GH-3448" xsd:string
 
 [Term]
 id: UBERON:0034892

```

### Attempt 7: gemma-4-31b / opencode

- **Eval PR**: [#107](https://github.com/ai4curation/eval-ont-agent-uberon/pull/107)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25683656249](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25683656249)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..47a42b983 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A cytoarchitecturally defined portion of the frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and plays a role in executive functions such as working memory, planning, inhibition, decision-making, and reasoning. Its cytoarchitecture is referred to as granular due to the concentration of granule cells in layer IV. Its internal pyramidal layer (V) is divisible into two sublayers, an outer layer 5a of densely distributed medium-size ganglion cells that partially merges with layer IV, and an inner, clearer, cell-poor layer 5b; the pyramidal cells of sublayer 3b of the external pyramidal layer (III) are smaller and sparser in distribution; the external granular layer (II) is narrow, with small numbers of sparsely distributed granule cells." [Wikipedia]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156283,7 +156284,10 @@ xref: neuronames:1024 {source="BIRNLEX:1740"}
 xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: dcterms-date "2026-05-12T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "GH-3448" xsd:string
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180725,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A portion of the cerebral cortex folded deep within the lateral sulcus (the fissure separating the temporal lobe from the parietal and frontal lobes) within each hemisphere of the mammalian brain. It is the primary gustatory cortex and is involved in sensorimotor and somatosensory as well as socioemotional functions." [MeSH:D000087623, Wikipedia]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180734,7 +180739,10 @@ xref: FMA:242223
 xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0002022 ! insula
+property_value: dcterms-date "2026-05-12T00:00:00Z" xsd:dateTime
+property_value: term_tracker_item "GH-3448" xsd:string
 
 [Term]
 id: UBERON:0034892

```

### Attempt 8: gpt-5.4 / codex

- **Eval PR**: [#78](https://github.com/ai4curation/eval-ont-agent-uberon/pull/78)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Workflow run**: [25640360028](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640360028)

#### Agent PR Comment

This change resolves issue `#3448` by adding missing textual definitions for two existing Uberon terms:

- `UBERON:0034891` insular cortex
- `UBERON:0013540` Brodmann (1909) area 9

Rationale:
- The issue requested definitions for two currently undefined neuroanatomy terms.
- I kept the new definitions concise and ontology-style, emphasizing structural placement and existing Uberon modeling rather than copying long functional prose from the issue text.
- I added `term_tracker_item` metadata on both terms to link the ontology updates back to the source issue.

References used in the new definitions:
- `UBERON:0034891` cites `FMA:242223` and `PMID:34827532`
- `UBERON:0013540` cites `BIRNLEX:1740`, `FMA:68606`, and `PMID:2768563`

Completed checklist:
- [x] Read the imported issue context
- [x] Inspected both target term stanzas in `src/ontology/uberon-edit.obo`
- [x] Checked parent terms for consistency
- [x] Checked out the target terms into `terms/`
- [x] Added textual definitions and issue tracking metadata
- [x] Checked the terms back into `src/ontology/uberon-edit.obo`
- [x] Reserialized the ontology with `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo`
- [x] Re-read the edited stanzas from the checked-in ontology file
- [x] Committed only the ontology file changes locally

Validation:
- `obo-checkin.pl src/ontology/uberon-edit.obo UBERON:0034891 UBERON:0013540`
- `robot convert -i src/ontology/uberon-edit.obo -f obo -o src/ontology/uberon-edit.obo`

Local commit:
- `ced8dd1` `Add definitions for insular cortex and Brodmann area 9`

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640360028)

#### Agent Issue Comment

Addressed in PR #<NN>.

Added textual definitions and `term_tracker_item` links for:
- `UBERON:0034891` insular cortex
- `UBERON:0013540` Brodmann (1909) area 9

Validation included check-in to `uberon-edit.obo` and OBO reserialization with `robot convert`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25640360028)

#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..d772d4f72 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A Brodmann area that is part of the dorsolateral prefrontal cortex and corresponds to a granular cytoarchitectonically defined region of the frontal cortex in humans and other primates." [BIRNLEX:1740, FMA:68606, PMID:2768563]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,7 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180723,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A cortex of cerebral lobe that forms the cortical part of the insula and lies deep within the lateral sulcus of the cerebral hemisphere." [FMA:242223, PMID:34827532]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180735,6 +180738,7 @@ xref: MA:0000909
 xref: SCTID:369221008
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0034892

```

### Attempt 9: gpt-5.5 / opencode

- **Eval PR**: [#62](https://github.com/ai4curation/eval-ont-agent-uberon/pull/62)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615967010](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615967010)
- **Workflow run**: [25615967010](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615967010)

#### Agent PR Comment

## Summary

This change addresses issue #3448 by adding textual definitions to two previously undefined Uberon terms:

- `UBERON:0034891` insular cortex
- `UBERON:0013540` Brodmann (1909) area 9

## Rationale

The definitions were adapted from the issue request while keeping the wording concise and anatomy-focused. I also added `term_tracker_item` annotations linking both updated terms back to the originating issue.

For `insular cortex`, I added supporting xrefs to `MESH:D000087623` and `Wikipedia:Insular_cortex`, matching the requested MeSH/Wikipedia source basis. `Brodmann (1909) area 9` already had a Wikipedia xref, so its new definition cites `Wikipedia:Brodmann_area_9`.

## Checklist completed

- [x] Read the imported issue context and comments.
- [x] Checked the existing term stanzas for both requested terms.
- [x] Checked existing parent/context terms for consistency.
- [x] Edited terms via `obo-checkout.pl` / `obo-checkin.pl` rather than direct ontology editing.
- [x] Re-serialized `src/ontology/uberon-edit.obo` with ROBOT.
- [x] Validated OBO conversion with `robot convert` to a temporary file.
- [x] Committed only the ontology edit file.

@dragon-ai-agent

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615967010)


#### Agent Issue Comment

Definitions for `insular cortex` (UBERON:0034891) and `Brodmann (1909) area 9` (UBERON:0013540) have been added and committed for PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615967010)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..5b3360060 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A Brodmann area that is a cytoarchitecturally defined region of frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and has granular cytoarchitecture with a well-developed layer IV." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,7 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180723,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A region of cerebral cortex that forms the cortical component of the insula and lies deep within the lateral sulcus, between the temporal lobe and the parietal and frontal lobes." [MESH:D000087623, Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180732,9 +180735,12 @@ xref: DMBA:16058
 xref: EMAPA:35432
 xref: FMA:242223
 xref: MA:0000909
+xref: MESH:D000087623
 xref: SCTID:369221008
+xref: Wikipedia:Insular_cortex
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0034892

```

### Attempt 10: gpt-5.5 / opencode

- **Eval PR**: [#42](https://github.com/ai4curation/eval-ont-agent-uberon/pull/42)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615925524](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615925524)
- **Workflow run**: [25615925524](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615925524)

#### Agent PR Comment

## Summary

Added definitions for the two previously undefined terms requested in issue #3448:

- `UBERON:0034891` insular cortex
- `UBERON:0013540` Brodmann (1909) area 9

## Rationale

The definitions were adapted from the issue-provided source material while keeping them concise and anatomy-focused. The insular cortex definition mirrors the existing logical placement as a cortex of cerebral lobe that is part of the insula. The Brodmann area 9 definition reflects its existing placement under Brodmann area and summarizes the source-provided cytoarchitectural characterization.

Both updated terms were linked back to issue #3448 using `term_tracker_item`.

## Checklist

- Read imported issue context from `__issue_context__.json`.
- Checked the current stanzas for both requested UBERON terms.
- Checked parent/part-of context for consistency.
- Verified the MeSH descriptor for insular cortex as `MESH:D000087623` using the MeSH Browser.
- Checked the referenced Wikipedia source pages for both terms.
- Edited checked-out term stanzas and checked them back into `src/ontology/uberon-edit.obo`.
- Reserialized the ontology with `robot convert`.
- Validated OBO conversion with `robot convert` to a temporary output.
- Ran `git diff --check`.
- Committed only `src/ontology/uberon-edit.obo` locally.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615925524)


#### Agent Issue Comment

Definitions for insular cortex and Brodmann (1909) area 9 have been added and committed locally for PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615925524)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..5b3360060 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A Brodmann area that is a cytoarchitecturally defined region of frontal cortex in the brain of humans and other primates. It contributes to the dorsolateral and medial prefrontal cortex and has granular cytoarchitecture with a well-developed layer IV." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156284,6 +156285,7 @@ xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180723,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A region of cerebral cortex that forms the cortical component of the insula and lies deep within the lateral sulcus, between the temporal lobe and the parietal and frontal lobes." [MESH:D000087623, Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180732,9 +180735,12 @@ xref: DMBA:16058
 xref: EMAPA:35432
 xref: FMA:242223
 xref: MA:0000909
+xref: MESH:D000087623
 xref: SCTID:369221008
+xref: Wikipedia:Insular_cortex
 is_a: UBERON:0016529 ! cortex of cerebral lobe
 relationship: part_of UBERON:0002022 ! insula
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0034892

```

### Attempt 11: gpt-5.5 / codex

- **Eval PR**: [#23](https://github.com/ai4curation/eval-ont-agent-uberon/pull/23)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25615866311](https://github.com/ai4curation/eval-ont-agent-uberon/tree/master/traces/25615866311)
- **Workflow run**: [25615866311](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615866311)

#### Agent PR Comment

## Summary

Added textual definitions for the two previously undefined terms requested in issue #3448:

- `UBERON:0034891` insular cortex
- `UBERON:0013540` Brodmann (1909) area 9

## Rationale

The added definitions are concise anatomical definitions adapted from the sources named in the issue. For `insular cortex`, I verified the current MeSH descriptor and added `MESH:D000087623` plus `Wikipedia:Insular_cortex` as definition/xref sources. For `Brodmann (1909) area 9`, I used the existing `Wikipedia:Brodmann_area_9` source already present on the term.

I also linked both edited terms back to issue #3448 with `term_tracker_item` and added the contributor ORCID from the issue (`https://orcid.org/0000-0002-4964-5083`). The ORCID corresponds to Dana Gabuzda; the issue text appears to contain a minor spelling typo in the surname.

## Checklist

- Read `__issue_context__.json`.
- Checked the existing stanzas with `obo-grep.pl`.
- Checked parent/relationship context for both terms.
- Checked terms out with `obo-checkout.pl`, edited the small term files, then checked them back in with `obo-checkin.pl`.
- Reserialized `src/ontology/uberon-edit.obo` with `robot convert`.
- Validated OBO parsing with `robot convert -i src/ontology/uberon-edit.obo -f obo -o /tmp/uberon-edit-check.obo`.
- Committed only `src/ontology/uberon-edit.obo`.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615866311)


#### Agent Issue Comment

Changes committed in PR #<NN>.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25615866311)


#### Agent Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index d32bd1180..941a29d6e 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -156265,6 +156265,7 @@ is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
 [Term]
 id: UBERON:0013540
 name: Brodmann (1909) area 9
+def: "A Brodmann area that is a cytoarchitecturally defined region of frontal cortex in primates, with a granular layer IV, and that contributes to the dorsolateral and medial prefrontal cortex." [Wikipedia:Brodmann_area_9]
 synonym: "area 9 of Brodmann" EXACT [FMA:68606]
 synonym: "area 9 of Brodmann (guenon)" RELATED [NeuroNames:1024]
 synonym: "area 9 of Brodmann-1909" EXACT [BIRNLEX:1740]
@@ -156283,7 +156284,9 @@ xref: neuronames:1024 {source="BIRNLEX:1740"}
 xref: UMLS:C1272531 {source="BIRNLEX:1740"}
 xref: Wikipedia:Brodmann_area_9
 is_a: UBERON:0013529 {source="NIFSTD"} ! Brodmann area
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0009834 {source="https://orcid.org/0000-0003-3308-6245"} ! dorsolateral prefrontal cortex
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0013541
@@ -180721,6 +180724,7 @@ relationship: part_of UBERON:0016530 {source="DHBA"} ! parietal cortex
 [Term]
 id: UBERON:0034891
 name: insular cortex
+def: "A cortex of cerebral lobe that is part of the insula and is located deep within the lateral sulcus." [MESH:D000087623, Wikipedia:Insular_cortex]
 synonym: "cortex of insula" EXACT [FMA:242223]
 synonym: "gray matter of insula" RELATED [FMA:242223]
 synonym: "ICx" RELATED OMO:0003000 [DHBA:10288]
@@ -180732,9 +180736,13 @@ xref: DMBA:16058
 xref: EMAPA:35432
 xref: FMA:242223
 xref: MA:0000909
+xref: MESH:D000087623
 xref: SCTID:369221008
+xref: Wikipedia:Insular_cortex
 is_a: UBERON:0016529 ! cortex of cerebral lobe
+relationship: dc-contributor https://orcid.org/0000-0002-4964-5083
 relationship: part_of UBERON:0002022 ! insula
+property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3448" xsd:anyURI
 
 [Term]
 id: UBERON:0034892

```
