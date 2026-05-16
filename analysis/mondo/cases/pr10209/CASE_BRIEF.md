---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9930
pr_number: 10209
issue_title: 'Request to add synonyms to: GRIN-related complex neurodevelopmental
  disorder (MONDO:1060138)'
pr_author: MeeSiing
pr_merged_at: '2026-05-01'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 7
generated_at: '2026-05-15'
best_f1: 0.25
best_model: claude-sonnet-4.5
---

# PR #10209 — Request to add synonyms to: GRIN-related complex neurodevelopmental disorder (MONDO:1060138)

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9930](https://github.com/monarch-initiative/mondo/issues/9930) | [PR #10209](https://github.com/monarch-initiative/mondo/pull/10209) | @MeeSiing | merged 2026-05-01

`synonym_update` `simple` `tightly_scoped` `changes_requested`

## Context

Issue #9930 was a request from NORD (National Organization for Rare Disorders) to add multiple synonyms to MONDO:1060138 (GRIN-related complex neurodevelopmental disorder). The requested synonyms included "GRINopathies", "GRIN-related Encephalopathy", and "GRIN-related Neurodevelopmental Disorder", reflecting terminology used in their rare disease report.

## Changes Made

The PR went through 3 commits: the initial synonym addition, then an update to correct a synonym value, and finally a scope correction. The final result added 4 synonym lines to MONDO:1060138 in mondo-edit.obo. The revisions demonstrate that synonym scope (EXACT vs RELATED vs BROAD) requires careful consideration, particularly when a requested synonym like "GRINopathies" is plural and may warrant RELATED rather than EXACT scope.

## Resolution

Although the individual edits are simple, this case illustrates that synonym requests from external stakeholders may need scope adjustment. The plural form "GRINopathies" could be argued as BROAD or RELATED rather than EXACT. An agent handling such requests needs to evaluate whether requested synonyms truly represent exact equivalence or require scope downgrading based on linguistic or semantic analysis.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..e763e9ddae 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related encephalopathy" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38380699]
+synonym: "GRIN-related neurodevelopmental disorder" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:38727899]
+synonym: "GRINpathies" EXACT [https://orcid.org/0000-0001-9310-0163, PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

## Agent Attempts (7)

### Attempt 1: claude-sonnet-4.5 / copilot

- **Eval PR**: [#519](https://github.com/ai4curation/eval-ont-agent-mondo/pull/519)
- **F1**: 0.250  **Precision**: 0.250  **Recall**: 0.250  **Jaccard**: 0.143

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..b35e5cfcf 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related Encephalopathy" EXACT [PMID:34884460]
+synonym: "GRIN-related Neurodevelopmental Disorder" EXACT [PMID:34884460]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#485](https://github.com/ai4curation/eval-ont-agent-mondo/pull/485)
- **F1**: 0.250  **Precision**: 0.250  **Recall**: 0.250  **Jaccard**: 0.143

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..b35e5cfcf 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related Encephalopathy" EXACT [PMID:34884460]
+synonym: "GRIN-related Neurodevelopmental Disorder" EXACT [PMID:34884460]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#437](https://github.com/ai4curation/eval-ont-agent-mondo/pull/437)
- **F1**: 0.250  **Precision**: 0.250  **Recall**: 0.250  **Jaccard**: 0.143
- **Trace**: [25867667024](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867667024)
- **Workflow run**: [25867667024](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867667024)

#### Agent PR Comment

## Summary

Added three new synonyms to MONDO:1060138 (GRIN-related complex neurodevelopmental disorder) as requested in issue #9930.

## Changes Made

Added the following synonyms with proper PMID citations:

1. **"grinpathies"** [PMID:34884460]
2. **"GRIN-related encephalopathy"** [PMID:33043365, PMID:34560056]
3. **"GRIN-related neurodevelopmental disorder"** [PMID:34560056, PMID:38727899]

## Rationale and Research

### Spelling Verification
The curation team asked about the correct spelling of "GRINopathies" vs "grinpathies". I researched the referenced literature and confirmed that:
- PMID:34884460 (Santos-Gómez et al., 2021) uses **"grinpathies"** (lowercase)
- This spelling is consistent with the medical literature

### Citation Verification
I verified all PMIDs from the issue request:
- **PMID:33043365** - Santos-Gómez et al. "Disease-associated GRIN protein truncating variants trigger NMDA receptor loss-of-function" (Hum Mol Genet, 2021)
- **PMID:34884460** - Santos-Gómez et al. "Paradigmatic de novo variants recapitulate pathophysiological mechanisms underlying GRIN1-related disorder clinical spectrum" (Int J Mol Sci, 2021)
- **PMID:34560056** - Benke et al. "Clinical and therapeutic significance of genetic variation in the GRIN gene family encoding NMDARs" (Neuropharmacology, 2021)
- **PMID:38727899** - Gjerulfsen et al. "Spectrum of NMDA receptor variants in neurodevelopmental disorders and epilepsy" (Methods Mol Biol, 2024)

### Curation Standards
All synonyms follow MONDO curation guidelines:
- ✅ Proper PMID citations included (no empty brackets)
- ✅ Appropriate synonym scope (EXACT)
- ✅ Issue tracker reference updated (IAO:0000233)
- ✅ File normalized using ODK

## Validation

- [x] Checked out term MONDO:1060138 to terms/ directory
- [x] Added synonyms with proper citations
- [x] Updated issue tracker reference to #9930
- [x] Checked in changes to mondo-edit.obo
- [x] Normalized ontology file using `make NORM`
- [x] Verified all synonyms present after normalization

## Notes

The fourth requested synonym "GRIN-related complex neurodevelopmental disorder" was not added as a synonym because it is already the primary term name.

Sources:
- [PMID:34884460 - Paradigmatic De Novo GRIN1 Variants](https://pubmed.ncbi.nlm.nih.gov/34884460/)
- [PMID:33043365 - Disease-associated GRIN protein truncating variants](https://pubmed.ncbi.nlm.nih.gov/33043365/)
- [PMID:34560056 - Clinical and therapeutic significance of GRIN gene family](https://pubmed.ncbi.nlm.nih.gov/34560056/)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867667024)


#### Agent Issue Comment

Thank you for the synonym request! I have added all three synonyms to MONDO:1060138 with proper citations.

Regarding the spelling question from @MeeSiing: Based on the literature (specifically PMID:34884460), the term is spelled **"grinpathies"** (lowercase), not "GRINopathies". I've used this spelling in the update.

The changes have been committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867667024)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..9e9d2c916 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related encephalopathy" EXACT [PMID:33043365, PMID:34560056]
+synonym: "GRIN-related neurodevelopmental disorder" EXACT [PMID:34560056, PMID:38727899]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

### Attempt 4: kimi-k2.6 / opencode

- **Eval PR**: [#245](https://github.com/ai4curation/eval-ont-agent-mondo/pull/245)
- **F1**: 0.250  **Precision**: 0.250  **Recall**: 0.250  **Jaccard**: 0.143
- **Trace**: [25755481888](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755481888)
- **Workflow run**: [25755481888](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755481888)

#### Agent PR Comment

## Summary

Added requested synonyms to **MONDO:1060138** (GRIN-related complex neurodevelopmental disorder) per issue #9930.

## Changes Made

- **Term:** `MONDO:1060138`
- **File modified:** `src/ontology/mondo-edit.obo`
- Added 3 new EXACT synonyms with verified PubMed/DOI citations:
  1. `grinpathies` — [PMID:34884460]
  2. `GRIN-related encephalopathy` — [PMID:33043365, PMID:34560056, PMID:38727899]
  3. `GRIN-related neurodevelopmental disorder` — [PMID:33043365, PMID:34560056, PMID:34884460, PMID:38727899]
- Added term tracker item: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930"`

## Rationale & Decisions

### Synonym sources
All PMIDs were identified by searching PubMed for the exact reference titles provided in the issue:

| Citation in issue | Verified PMID |
|---|---|
| Santos-Gómez A et al. Hum Mol Genet. 2021. | [PMID:33043365](https://pubmed.ncbi.nlm.nih.gov/33043365/) |
| Santos-Gómez A et al. Int J Mol Sci. 2021. | [PMID:34884460](https://pubmed.ncbi.nlm.nih.gov/34884460/) |
| Gjerulfsen CE et al. Methods Mol Biol. 2024. | [PMID:38727899](https://pubmed.ncbi.nlm.nih.gov/38727899/) |
| Benke TA et al. Neuropharmacology. 2021. | [PMID:34560056](https://pubmed.ncbi.nlm.nih.gov/34560056/) |

### Spelling of "grinpathies"
The requester wrote **"GRINopathies"**. Curator @MeeSiing asked for clarification whether it should be **"GRINpathies"** or **"grinpathies"** ([comment](https://github.com/monarch-initiative/mondo/issues/9930#issuecomment-4346308927)). Since no response was received, I checked the primary literature. PMID:34884460 explicitly uses the lowercase form **"grinpathies"** ("GRIN-related disorders (GRD), the so-called grinpathies"). No published source supports the capitalized "GRINopathies" spelling with an intervening "o". Therefore, I added the literature-backed form as the EXACT synonym.

### Why "GRIN-related complex neurodevelopmental disorder" was not added as a synonym
This string is already the exact term name. Adding it as an additional EXACT synonym would be redundant.

## Curation checklist

- [x] Read and understood the issue request
- [x] Verified all PubMed citations provided in the issue
- [x] Checked out term `MONDO:1060138` via `obo-checkout.pl`
- [x] Added synonyms with proper citations (no empty `[]`)
- [x] Added term tracker item for issue #9930
- [x] Checked term back in via `obo-checkin.pl`
- [x] Ran `make NORM` via ODK docker and moved `NORM` to `mondo-edit.obo`
- [x] Verified normalized term looks correct
- [x] Committed only `src/ontology/mondo-edit.obo`

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755481888)


#### Agent Issue Comment

Hi @galyea123 and @MeeSiing,

Thank you for the synonym request. We have added the following synonyms to **MONDO:1060138** "GRIN-related complex neurodevelopmental disorder" in PR #<NN>:

| Synonym | Scope | Citations |
|---|---|---|
| grinpathies | EXACT | PMID:34884460 |
| GRIN-related encephalopathy | EXACT | PMID:33043365, PMID:34560056, PMID:38727899 |
| GRIN-related neurodevelopmental disorder | EXACT | PMID:33043365, PMID:34560056, PMID:34884460, PMID:38727899 |

**Note on "GRINopathies" spelling:** We chose to use the spelling **"grinpathies"** (all-lowercase, no intervening "o") because the published literature (Santos-Gómez et al., Int J Mol Sci 2021, PMID:34884460) explicitly uses this form: *"GRIN-related disorders (GRD), the so-called grinpathies"*. We did not add "GRINopathies" with a capital "G" and an "o" because that spelling could not be verified in the cited literature.

A term tracker item for this issue has also been added to the term.

Please let us know if anything needs adjustment.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755481888)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..676c2154a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,10 +658223,14 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related encephalopathy" EXACT [PMID:33043365, PMID:34560056, PMID:38727899]
+synonym: "GRIN-related neurodevelopmental disorder" EXACT [PMID:33043365, PMID:34560056, PMID:34884460, PMID:38727899]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9063" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9930" xsd:anyURI
 
 [Term]
 id: MONDO:1060139

```

### Attempt 5: claude-haiku-4.5 / claude

- **Eval PR**: [#425](https://github.com/ai4curation/eval-ont-agent-mondo/pull/425)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25844227153](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25844227153)
- **Workflow run**: [25844227153](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25844227153)

#### Agent PR Comment

# PR #<NN> - Add synonyms to MONDO:1060138

#### Agent Issue Comment

# Issue #9930 - Request to add synonyms to GRIN-related complex neurodevelopmental disorder

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..6bc180a79 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,6 +658223,10 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related Encephalopathy" EXACT [PMID:34560056]
+synonym: "GRIN-related Neurodevelopmental Disorder" EXACT [PMID:34884460]
+synonym: "GRINopathies" EXACT [PMID:34884460]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder

```

### Attempt 6: claude-opus-4.7 / claude

- **Eval PR**: [#402](https://github.com/ai4curation/eval-ont-agent-mondo/pull/402)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25818893863](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25818893863)
- **Workflow run**: [25818893863](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818893863)

#### Agent PR Comment

# Add synonyms to GRIN-related complex neurodevelopmental disorder (MONDO:1060138)

Addresses issue [#9930](https://github.com/monarch-initiative/mondo/issues/9930), a request from @galyea123 (NORD) to add several common synonyms for GRIN-related disorders.

#### Agent Issue Comment

Hi @galyea123 and @MeeSiing — the requested synonyms have been added to **GRIN-related complex neurodevelopmental disorder (MONDO:1060138)** in PR #<NN>.

A note on the "GRINopathies" vs "grinpathies" question raised by @MeeSiing: the published literature (e.g., Santos-Gómez et al. 2021, [PMID:34884460](https://pubmed.ncbi.nlm.nih.gov/34884460/)) uses **"grinpathies"** in lowercase. To preserve both the curator/community-facing capitalized form ("GRINopathies") that the NORD report uses and the form found in the primary literature, I added both as RELATED synonyms. If only one is preferred, please let us know and we can remove the other.

Summary of synonyms added:
- "GRIN-related encephalopathy" — RELATED [PMID:34884460]
- "GRIN-related neurodevelopmental disorder" — EXACT [PMID:40374652]
- "GRINopathies" — RELATED [PMID:34884460]
- "grinpathies" — RELATED [PMID:34884460]

"GRIN-related complex neurodevelopmental disorder" is already the term's primary label, so it was not added as a synonym.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818893863)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..5961f2944 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658221,6 +658221,10 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 id: MONDO:1060138
 name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
+synonym: "GRIN-related encephalopathy" RELATED [PMID:34884460]
+synonym: "GRIN-related neurodevelopmental disorder" EXACT [PMID:40374652]
+synonym: "GRINopathies" RELATED [PMID:34884460]
+synonym: "grinpathies" RELATED [PMID:34884460]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
 xref: GARD:0028156 {source="MONDO:GARD"}

```

### Attempt 7: claude-haiku-4.5 / claude

- **Eval PR**: [#299](https://github.com/ai4curation/eval-ont-agent-mondo/pull/299)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25762174549](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25762174549)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..6bc180a79 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658223,6 +658223,10 @@ name: GRIN-related complex neurodevelopmental disorder
 def: "A group of neurological and neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the N-methyl-D-aspartate (NMDA) receptor, including GRIN1, GRIN2A, GRIN2B, and GRIN2D. These disorders are associated with a spectrum of symptoms such as developmental delay, intellectual disability, epilepsy, movement disorders, speech and language impairment, and neuropsychiatric features. The clinical presentation and severity vary depending on the specific gene and mutation involved." [https://orcid.org/0000-0001-9310-0163, PMID:40374652]
 subset: gard_rare {source="GARD:0028156", source="MONDO:GARD"}
 subset: rare
+synonym: "GRIN-related Encephalopathy" EXACT [PMID:34560056]
+synonym: "GRIN-related Neurodevelopmental Disorder" EXACT [PMID:34884460]
+synonym: "GRINopathies" EXACT [PMID:34884460]
+synonym: "grinpathies" EXACT [PMID:34884460]
 xref: GARD:0028156 {source="MONDO:GARD"}
 is_a: MONDO:0003847 {source="PMID:40374652"} ! hereditary disease
 is_a: MONDO:0100038 {source="https://orcid.org/0000-0002-4142-7153"} ! complex neurodevelopmental disorder

```
