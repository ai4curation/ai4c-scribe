# PR #10126 — Request for new term Southern tick-associated rash illness

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9873](https://github.com/monarch-initiative/mondo/issues/9873)
- **PR**: [#10126](https://github.com/monarch-initiative/mondo/pull/10126)
- **Author**: @katiermullen
- **Merged**: 2026-04-17
- **task_type**: new_term
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: changes_requested
- **scoping_notes**: PR adds a single new disease term with definition, synonyms, and cross-references.

## Context

A user requested a new Mondo term for Southern tick-associated rash illness (STARI), also known as Masters disease. STARI is an infectious disease transmitted by the lone star tick (Amblyomma americanum) that presents with an erythema migrans-like rash similar to Lyme disease but with a distinct etiology. The request (issue #9873) included exact synonyms (STARI, Masters disease), a proposed definition with PubMed references, and cross-references to NCIT:C128427 and SNOMED:444100007.

## Changes Made

The PR added 13 lines to `src/ontology/mondo-edit.obo` introducing a new term stanza classified under MONDO:0025294 "tick-borne infectious disease." The 8 commits reflect review iteration: the initial submission received a CHANGES_REQUESTED review from a senior curator asking for an updated definition, after which the definition was revised and the PR was approved. Cross-references to NCIT and SNOMED were included for interoperability.

## Resolution

Medium difficulty because while the new term follows standard Mondo patterns, the definition required iteration based on reviewer feedback. An agent would need to construct the term stanza with the correct parent classification, parse the user-provided synonyms and cross-references, and be able to revise the definition in response to curator feedback. The review cycle (changes requested then approved) is representative of typical NTR workflows.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f5..45dbc41774 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -619475,6 +619475,19 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
 
+[Term]
+id: MONDO:1010205
+name: southern tick-associated rash illness
+def: "A tick-borne infectious disease transmitted by the lone star tick, Amblyomma americanum, and causing an erythema migrans–like rash with or without mild constitutional symptoms." [https://orcid.org/0000-0001-5705-7831, PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:18452807]
+synonym: "STARI" EXACT ABBREVIATION [PMID:18452807]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:1010206
 name: meningeal neoplasm, non-human animal

```

## Agent Attempts (9)

### Attempt 1: gpt-5.4 / codex

- **Eval PR**: [#173](https://github.com/ai4curation/eval-ont-agent-mondo/pull/173)
- **F1**: 0.640  **Precision**: 0.667  **Recall**: 0.615  **Jaccard**: 0.471
- **Workflow run**: [25640353208](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353208)

#### Agent PR Comment

Implemented issue #9873 by adding a new MONDO term:

- `MONDO:7770018` southern tick-associated rash illness

Rationale:

- The requested disease was not already present in `src/ontology/mondo-edit.obo`.
- The term was added under `MONDO:0025294` tick-borne infectious disease, which is the conservative parent supported by the issue request and the literature.
- I did not assert a specific infectious agent because the current evidence remains unsettled; instead I modeled the known vector with `transmitted_by NCBITaxon:6943 ! Amblyomma americanum`.
- I added the requested exact synonyms `STARI` and `Masters disease`, and added the requested external mappings to `NCIT:C128427` and `SCTID:444100007`.
- I linked the term back to the source issue and used the ORCID supplied in the issue for creator attribution.

Validation and background checks completed:

- Confirmed the term label and synonyms were not already present in MONDO.
- Verified the requested parent term exists and is appropriate.
- Checked supporting literature for STARI, including `PMID:36116832`, `PMID:17028220`, and `PMID:19522220`.
- Ran syntax validation with:
  `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`
- Ran normalization with local tooling:
  `cd src/ontology && make NORM && mv NORM mondo-edit.obo`

Notes:

- The issue body listed `PMID:40267428`, but I could not verify that identifier as a PubMed record for STARI, so I did not use it in the stanza.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353208)


#### Agent Issue Comment

Added a new MONDO term for `southern tick-associated rash illness` with exact synonyms `STARI` and `Masters disease`, mapped to `NCIT:C128427` and `SCTID:444100007`, under `MONDO:0025294` tick-borne infectious disease.

Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353208)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..56f050a59 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,20 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: southern tick-associated rash illness
+def: "A tick-borne infectious disease characterized by an expanding erythema migrans-like rash and other acute manifestations similar to Lyme disease that occurs following the bite of the lone star tick, Amblyomma americanum." [PMID:36116832]
+subset: ncit {source="NCIT:C128427"}
+synonym: "Masters disease" EXACT [PMID:17028220]
+synonym: "STARI" EXACT ABBREVIATION [PMID:36116832]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="PMID:36116832"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:36116832"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#463](https://github.com/ai4curation/eval-ont-agent-mondo/pull/463)
- **F1**: 0.522  **Precision**: 0.500  **Recall**: 0.545  **Jaccard**: 0.353
- **Trace**: [25867839011](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867839011)
- **Workflow run**: [25867839011](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867839011)

#### Agent PR Comment

## Summary

This PR adds a new term for Southern tick-associated rash illness in response to issue #9873.

## Changes Made

- **Added MONDO:7770018**: Southern tick-associated rash illness
  - Label: Southern tick-associated rash illness
  - Synonyms: 
    - "STARI" (EXACT) [PMID:19522220]
    - "Masters disease" (EXACT) [PMID:19522220]
  - Definition: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
  - Parent: MONDO:0025294 (tick-borne infectious disease)
  - Cross-references:
    - NCIT:C128427 (equivalentTo)
    - SCTID:444100007 (equivalentTo)
  - Creator: https://orcid.org/0000-0001-5705-7831
  - Issue tracker: https://github.com/monarch-initiative/mondo/issues/9873

## Validation Performed

- ✅ Verified parent term MONDO:0025294 exists and is appropriate
- ✅ Assigned next available MONDO:777xxxx ID (MONDO:7770018)
- ✅ Validated syntax using robot convert
- ✅ Normalized the ontology file using make NORM
- ✅ Verified term is properly integrated into normalized file

## Rationale

Southern tick-associated rash illness (STARI) is a well-documented tick-borne infectious disease transmitted by the lone star tick (*Amblyomma americanum*). The disease presents with acute manifestations similar to Lyme disease but has a distinct vector and geographic distribution. The term has been properly classified under tick-borne infectious diseases with appropriate references to the scientific literature and standard medical terminologies (NCIT and SNOMED).

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867839011)


#### Agent Issue Comment

Thank you for the new term request! I have successfully added the term for Southern tick-associated rash illness.

The new term has been created as **MONDO:7770018** with:
- Label: Southern tick-associated rash illness
- Synonyms: STARI, Masters disease (both EXACT)
- Definition with all three PMIDs cited (PMID:19522220, PMID:36116832, PMID:40267428)
- Parent term: MONDO:0025294 (tick-borne infectious disease)
- Cross-references to NCIT:C128427 and SCTID:444100007
- Proper creator attribution to your ORCID

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867839011)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..840b4ddbb 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,18 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:19522220]
+synonym: "STARI" EXACT [PMID:19522220]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 ! tick-borne infectious disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 3: claude-haiku-4.5 / claude

- **Eval PR**: [#476](https://github.com/ai4curation/eval-ont-agent-mondo/pull/476)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25888781147](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25888781147)
- **Workflow run**: [25888781147](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25888781147)

#### Agent PR Comment

# PR Implementation Summary: Southern tick-associated rash illness (MONDO:7770018)

#### Agent Issue Comment

# Issue Resolution Summary

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..f6ffe2584 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+namespace: infectious_disease
+def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:19522220]
+synonym: "STARI" EXACT ABBREVIATION [PMID:36116832]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SNOMED:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 4: claude-haiku-4.5 / claude

- **Eval PR**: [#422](https://github.com/ai4curation/eval-ont-agent-mondo/pull/422)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25844283237](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25844283237)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..f6ffe2584 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+namespace: infectious_disease
+def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:19522220]
+synonym: "STARI" EXACT ABBREVIATION [PMID:36116832]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SNOMED:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#77](https://github.com/ai4curation/eval-ont-agent-mondo/pull/77)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615976782](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615976782)
- **Workflow run**: [25615976782](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615976782)

#### Agent PR Comment

## Summary

Added a new MONDO term for **Southern tick-associated rash illness** (`MONDO:7770018`) to address issue #9873.

#### Agent Issue Comment

Added the requested new term for Southern tick-associated rash illness. Changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615976782)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..02b16b1a6 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "A tick-borne infectious disease with acute manifestations similar to Lyme disease, characterized by an erythema migrans-like rash at the site of a lone star tick (Amblyomma americanum) bite." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:19522220]
+synonym: "STARI" EXACT ABBREVIATION [PMID:19522220, PMID:36116832, PMID:40267428]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#58](https://github.com/ai4curation/eval-ont-agent-mondo/pull/58)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615934346](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615934346)
- **Workflow run**: [25615934346](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615934346)

#### Agent PR Comment

## Summary

Added a new MONDO term for Southern tick-associated rash illness (`MONDO:7770018`) as a child of tick-borne infectious disease (`MONDO:0025294`).

## Rationale

The requested concept is supported by the cited publications and by equivalent external records in NCIT (`NCIT:C128427`) and SNOMED CT (`SCTID:444100007`). The term includes the requested exact synonyms `STARI` and `Masters disease`, equivalent xrefs, the requested issue tracker link, and a vector relationship to the lone star tick (`NCBITaxon:6943`).

## Completed Checklist

- Reviewed issue #9873 context.
- Checked for existing duplicate MONDO content using `obo-grep.pl`.
- Confirmed requested parent `MONDO:0025294` exists and is appropriate.
- Validated PMIDs `19522220`, `36116832`, and `40267428` through PubMed pages because `aurelian` was unavailable locally.
- Validated `NCIT:C128427` and `SCTID:444100007` via public ontology pages.
- Used the `terms/` OBO stanza plus `obo-checkin.pl` workflow to update `src/ontology/mondo-edit.obo`.
- Ran local normalization with `make NORM` and replaced `mondo-edit.obo` with the normalized output.
- Ran syntax validation with `robot convert`.
- Ran ELK reasoning validation with `robot reason`.

## Notes

The standard ODK Docker wrapper could not be used because Docker is not installed in this environment, but the local `make NORM`, `robot convert`, and `robot reason` validations completed successfully.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615934346)


#### Agent Issue Comment

Added Southern tick-associated rash illness as `MONDO:7770018`; changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615934346)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..02b16b1a6 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "A tick-borne infectious disease with acute manifestations similar to Lyme disease, characterized by an erythema migrans-like rash at the site of a lone star tick (Amblyomma americanum) bite." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [PMID:19522220]
+synonym: "STARI" EXACT ABBREVIATION [PMID:19522220, PMID:36116832, PMID:40267428]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 7: claude-opus-4.7 / claude

- **Eval PR**: [#388](https://github.com/ai4curation/eval-ont-agent-mondo/pull/388)
- **F1**: 0.417  **Precision**: 0.417  **Recall**: 0.417  **Jaccard**: 0.263
- **Trace**: [25817732019](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25817732019)
- **Workflow run**: [25817732019](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817732019)

#### Agent PR Comment

# New term: Southern tick-associated rash illness (MONDO:7770018)

Resolves issue #9873.

## Summary

Adds a new MONDO term for **Southern tick-associated rash illness (STARI)**, as requested.

## Stanza added

```
[Term]
id: MONDO:7770018
name: Southern tick-associated rash illness
def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
synonym: "Masters disease" EXACT [https://orcid.org/0000-0001-5705-7831]
synonym: "STARI" EXACT ABBREVIATION [https://orcid.org/0000-0001-5705-7831]
xref: NCIT:C128427 {source="MONDO:equivalentTo"}
xref: SCTID:444100007 {source="MONDO:equivalentTo"}
is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
relationship: transmitted_by NCBITaxon:6943 {source="https://orcid.org/0000-0001-5705-7831"} ! Amblyomma americanum
property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
```

## Rationale and decisions

- **MONDO ID**: Used the next free 777xxxx ID. `MONDO:7770017` was the highest existing 777-range ID, so `MONDO:7770018` was selected. Verified with `grep id: MONDO:777 src/ontology/mondo-edit.obo`.
- **Parent term**: `MONDO:0025294` (tick-borne infectious disease), as requested in the issue. Confirmed the parent term exists and is appropriately scoped.
- **Duplicate check**: Searched the edit file for `STARI`, `Southern tick`, `Masters`, and `Amblyomma`. No pre-existing STARI term was found.
- **Synonyms**: Both `STARI` and `Masters disease` set to `EXACT` per the issue. `STARI` additionally annotated as `ABBREVIATION`. Synonyms cite the submitter's ORCID since the issue did not supply a separate citation for them.
- **Vector relationship**: Added `transmitted_by NCBITaxon:6943` (Amblyomma americanum) so the lone star tick assertion from the definition is captured as a logical axiom, consistent with how other Amblyomma-borne diseases are structured (e.g. MONDO:0000232 Flinders island spotted fever, MONDO:0000234 Rickettsia parkeri spotted fever). The NCBITaxon ID was looked up via existing usage in the edit file.
- **Xrefs**: `NCIT:C128427` and `SCTID:444100007` (issue used `SNOMED:` prefix, but MONDO consistently uses `SCTID:` for SNOMED CT — confirmed by `grep -c 'xref: SCTID:' src/ontology/mondo-edit.obo` returning 18067 hits vs. 0 for `SNOMED:`). Both qualified with `source="MONDO:equivalentTo"`.
- **Definition references**: All three PMIDs from the issue retained in the definition reference list.
- **Provenance**: `dcterms:creator` set to the submitter ORCID and `IAO:0000233` (term_tracker_item) set to the issue URL.

## Checklist

- [x] Confirmed parent `MONDO:0025294` exists
- [x] Verified no duplicate STARI / Southern tick-associated rash illness term exists
- [x] Confirmed `MONDO:7770018` is unused
- [x] Verified `NCBITaxon:6943` is the established label-bearing ID for *Amblyomma americanum* in this ontology
- [x] Used `SCTID:` prefix for SNOMED, matching repo convention
- [x] Added `term_tracker_item` linking back to issue #9873
- [x] Added creator ORCID

## Limitations / things I could not do

- **PMID fetch**: `aurelian` was not installed in this environment, so I was unable to retrieve the full text of PMID:19522220, PMID:36116832, or PMID:40267428 to independently confirm they support the definition. The PMIDs were taken at face value from the issue.
- **NORM step**: `sh run.sh make NORM` requires Docker, which is not available in this environment, so the file was not re-serialized. The new stanza was inserted by `obo-checkin.pl` and a stray duplicated OBO header that the script preserved from the per-term file was removed manually; the resulting diff is a single contiguous `[Term]` block.
- **`robot convert` validation**: Same Docker constraint; the syntactic shape of the stanza was checked by visual inspection against neighboring terms.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817732019)


#### Agent Issue Comment

New term added in PR #<NN>.

- ID: `MONDO:7770018`
- Label: Southern tick-associated rash illness
- Parent: `MONDO:0025294` tick-borne infectious disease
- Synonyms: STARI (EXACT, ABBREVIATION), Masters disease (EXACT)
- Xrefs: NCIT:C128427, SCTID:444100007
- Vector relationship: `transmitted_by NCBITaxon:6943` (Amblyomma americanum)
- Definition references: PMID:19522220, PMID:36116832, PMID:40267428
- Creator ORCID: https://orcid.org/0000-0001-5705-7831

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817732019)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..33c1d109a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [https://orcid.org/0000-0001-5705-7831]
+synonym: "STARI" EXACT ABBREVIATION [https://orcid.org/0000-0001-5705-7831]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="https://orcid.org/0000-0001-5705-7831"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 8: kimi-k2.6 / opencode

- **Eval PR**: [#281](https://github.com/ai4curation/eval-ont-agent-mondo/pull/281)
- **F1**: 0.417  **Precision**: 0.417  **Recall**: 0.417  **Jaccard**: 0.263
- **Trace**: [25755668841](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755668841)
- **Workflow run**: [25755668841](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755668841)

#### Agent PR Comment

## Summary

Added a new MONDO term **Southern tick-associated rash illness (MONDO:7770018)** in response to issue #9873.

### Changes Made

In `src/ontology/mondo-edit.obo`, added the following stanza:

```obo
[Term]
id: MONDO:7770018
name: Southern tick-associated rash illness
def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [https://orcid.org/0000-0001-5705-7831, PMID:19522220, PMID:36116832, PMID:40267428]
synonym: "Masters disease" EXACT [https://orcid.org/0000-0001-5705-7831]
synonym: "STARI" EXACT ABBREVIATION [https://orcid.org/0000-0001-5705-7831]
xref: NCIT:C128427 {source="MONDO:equivalentTo"}
xref: SCTID:444100007 {source="MONDO:equivalentTo"}
is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
relationship: transmitted_by NCBITaxon:6943 {source="PMID:36116832"} ! Amblyomma americanum
property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
```

### Rationale and Validation

- **New ID**: Assigned `MONDO:7770018`, the next available ID in the new-term range (`MONDO:7770001`–`MONDO:7770017` were already in use).
- **Parent term**: The requester specified `MONDO:0025294` *tick-borne infectious disease*. This was confirmed in the ontology and is consistent with the textual definition of the parent, which covers diseases transmitted by ticks in the families Ixodidae and Argasidae. *Amblyomma americanum* belongs to family Ixodidae.
- **PMID validation**: All three PMIDs were verified via NCBI E-utilities:
  - PMID:19522220 — "[STARI--a new tick borne spirochetosis]" (2009)
  - PMID:36116832 — "Early Lyme Disease (Erythema Migrans) and Its Mimics (Southern Tick-Associated Rash Illness and Tick-Associated Rash Illness)" (2022)
  - PMID:40267428 — "Southern Tick-Associated Rash Illness" in NEJM (2025)
- **External xrefs**: `NCIT:C128427` and `SCTID:444100007` were confirmed via web lookup (BioPortal/NCIT). SNOMED CT lists both "STARI" and "Masters disease" as synonyms.
- **Relationship**: Added `relationship: transmitted_by NCBITaxon:6943` because the vector (*Amblyomma americanum*) is specific to this disease and is already present in the ontology. This follows the same pattern used for other tick-borne diseases in MONDO (e.g., human granulocytic anaplasmosis).
- **ORCID attribution**: The requester's ORCID (`https://orcid.org/0000-0001-5705-7831`) is cited as the definition source, synonym source, parent source, and term creator.
- **Syntax validation**: Ran `robot convert` via the ODK docker image; conversion completed without errors.
- **Normalization**: Ran `make NORM` via ODK and replaced `mondo-edit.obo` with the normalized file.

### Checklist

- [x] Verified term does not already exist in MONDO
- [x] Checked for ID clashes in `MONDO:777` range
- [x] Validated PMIDs via NCBI E-utilities
- [x] Confirmed external xrefs (NCIT, SNOMED CT)
- [x] Selected appropriate parent term
- [x] Added required metadata (definition, synonyms, xrefs, creator, tracker item)
- [x] Ran `make NORM` for serialization normalization
- [x] Ran `robot convert` for syntax validation
- [x] Committed changes

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755668841)


#### Agent Issue Comment

New term "Southern tick-associated rash illness" has been added as **MONDO:7770018** and committed in PR #<NN>.

The term includes:
- Exact synonyms: STARI, Masters disease
- Definition sourced from the requester and supported by PMID:19522220, PMID:36116832, and PMID:40267428
- Xrefs: NCIT:C128427 and SCTID:444100007 (SNOMED CT)
- Parent: MONDO:0025294 *tick-borne infectious disease*
- Vector relationship: transmitted by *Amblyomma americanum* (NCBITaxon:6943)

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755668841)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..e9f85ec11 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,19 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "An infectious disease causing acute manifestations similar to those of Lyme disease. Its vector is the lone star tick, Amblyomma americanum." [https://orcid.org/0000-0001-5705-7831, PMID:19522220, PMID:36116832, PMID:40267428]
+synonym: "Masters disease" EXACT [https://orcid.org/0000-0001-5705-7831]
+synonym: "STARI" EXACT ABBREVIATION [https://orcid.org/0000-0001-5705-7831]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:36116832"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 9: gpt-5.5 / codex

- **Eval PR**: [#40](https://github.com/ai4curation/eval-ont-agent-mondo/pull/40)
- **F1**: 0.400  **Precision**: 0.417  **Recall**: 0.385  **Jaccard**: 0.250
- **Trace**: [25615870415](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615870415)
- **Workflow run**: [25615870415](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615870415)

#### Agent PR Comment

## Summary

Added a new MONDO term for Southern tick-associated rash illness:

- `MONDO:7770018` Southern tick-associated rash illness
- Parent: `MONDO:0025294` tick-borne infectious disease
- Definition cites `NCIT:C128427`, `PMID:19522220`, `PMID:36116832`, and `PMID:40267428`
- Exact synonyms: `STARI` and `Masters disease`, with cited sources
- Xrefs: `NCIT:C128427` and `SCTID:444100007`
- Added `transmitted_by NCBITaxon:6943` for the lone star tick, `Amblyomma americanum`
- Added the requester ORCID as creator and linked the GitHub issue as the tracker item

#### Agent Issue Comment

Added Southern tick-associated rash illness as MONDO:7770018. Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615870415)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index f1c7c0e8f..d9f233bea 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -658378,6 +658378,20 @@ intersection_of: MONDO:0005583 ! non-human animal disease
 intersection_of: MONDO:0700097 MONDO:7770011 ! cross-species analog disease by molecular mechanism
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10127" xsd:anyURI
 
+[Term]
+id: MONDO:7770018
+name: Southern tick-associated rash illness
+def: "A tick-borne infectious disease characterized by acute manifestations similar to Lyme disease, particularly erythema migrans-like rash, following a bite from the lone star tick, Amblyomma americanum." [NCIT:C128427, PMID:19522220, PMID:36116832, PMID:40267428]
+subset: ncit {source="NCIT:C128427"}
+synonym: "Masters disease" EXACT [PMID:19522220, SCTID:444100007]
+synonym: "STARI" EXACT ABBREVIATION [PMID:19522220, PMID:36116832, PMID:40267428, SCTID:444100007]
+xref: NCIT:C128427 {source="MONDO:equivalentTo"}
+xref: SCTID:444100007 {source="MONDO:equivalentTo"}
+is_a: MONDO:0025294 {source="NCIT:C128427", source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! tick-borne infectious disease
+relationship: transmitted_by NCBITaxon:6943 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428"} ! Amblyomma americanum
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5705-7831
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```
