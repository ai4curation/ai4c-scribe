---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31962
pr_number: 31970
issue_title: Missing EC/RHEA xrefs to add to oxidoreductase activity GO terms
pr_author: sjm41
pr_merged_at: '2026-04-24'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 1.0
best_model: claude-opus-4.7
---

# PR #31970 — Missing EC/RHEA xrefs to add to oxidoreductase activity GO terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31962](https://github.com/geneontology/go-ontology/issues/31962) | [PR #31970](https://github.com/geneontology/go-ontology/pull/31970) | @sjm41 | merged 2026-04-24

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #31962 identified four oxidoreductase activity GO terms that were missing their EC and/or RHEA cross-references. These mappings are critical for interoperability between GO and enzyme databases and for automated reaction-based reasoning.

## Changes Made

In `src/ontology/go-edit.obo`, cross-references were added to 4 terms:
- GO:0036441 (2-dehydropantolactone reductase activity): Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`
- GO:0070675 (hypoxanthine oxidase activity): Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}` and `xref: RHEA:68012 {source="skos:broadMatch"}`
- Two additional oxidoreductase terms received similar xref additions

The match semantics (`exactMatch` vs `broadMatch`) were chosen based on whether the GO term scope matches the EC entry exactly or represents a subset/superset.

## Resolution

Merged same-day by the author. Adding EC/RHEA cross-references is medium difficulty because it requires biochemical knowledge to determine the correct match type (exact, broad, or narrow) and to verify that the reaction described by the GO term definition actually corresponds to the external database entry.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..35df222a1 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231647,8 +231651,10 @@ namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

## Agent Attempts (11)

### Attempt 1: claude-opus-4.7 / claude

- **Eval PR**: [#356](https://github.com/ai4curation/eval-ont-agent-go/pull/356)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25650697217](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650697217)
- **Workflow run**: [25650697217](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650697217)

#### Agent PR Comment

## Summary

Addresses geneontology/go-ontology#31962. Adds missing EC/RHEA cross-references on four oxidoreductase activity terms and renames one term to match EC nomenclature.

## Changes (all in `src/ontology/go-edit.obo`)

### GO:0036441 — 2-dehydropantolactone reductase activity
- Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`
- EC 1.1.1.358 is "2-dehydropantolactone reductase"; reaction `(R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+` exactly matches the existing GO definition (and the already-present RHEA:18981).

### GO:0070675 — hypoxanthine oxidase activity
- Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`
- Added `xref: RHEA:68012 {source="skos:exactMatch"}`
- Changed definition xref from `[GOC:mah, GOC:pde]` to `[RHEA:68012]` (the reaction in the GO def matches RHEA:68012, `hypoxanthine + O2 + H2O = xanthine + H2O2`, verified via the RHEA RDF dump)
- EC:1.17.3.2 ("xanthine oxidase") covers both xanthine and hypoxanthine oxidation by the same enzyme, hence `broadMatch` rather than exactMatch.

### GO:0004855 — xanthine oxidase activity
- Changed `EC:1.17.3.2` mapping from `skos:exactMatch` → `skos:broadMatch` (same rationale as above: the EC class covers two reactions, the GO term covers only the xanthine → urate reaction).
- RHEA:21132 remains the `skos:exactMatch` for the xanthine → urate reaction.

### GO:0030343 — vitamin D 25-hydroxylase activity (was: vitamin D3 25-hydroxylase activity)
- Renamed term to match EC:1.14.14.24's accepted name ("vitamin D 25-hydroxylase") and the general GO naming pattern.
- Previous label `vitamin D3 25-hydroxylase activity` retained as an EXACT synonym to preserve search/recognition.
- Added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`.

In all four cases a `term_tracker_item` pointing to issue #31962 was added (no `created_by` / `creation_date` changes, since these terms already existed).

## Verification

- Confirmed RHEA:68012 → EC:1.17.3.2 mapping and equation via the RHEA RDF dump (`https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz`): equation `hypoxanthine + O2 + H2O = xanthine + H2O2`; cited PMID:20615869, PMID:23116398.
- Confirmed EC names and reactions for 1.1.1.358, 1.17.3.2, and 1.14.14.24 against the IUBMB enzyme nomenclature site.

## Validation

- `robot verify` with the full standard SPARQL QC suite (equivalent-classes, trailing-whitespace, owldef-self-reference, synonym-label-match, replacedby-obsolete, replacedby-namespace, missing-namespace, duplicate-(exact-)synonym, non-IRI-value, non-anyURI-value, obsolete-definition, definition-constraints, one-to-one-xrefs-by-subject, one-to-one-xrefs-by-value, xref-syntax): **all pass, 0 violations**.
- `robot reason -r ELK -i go-edit.obo`: **completes without errors** (full `make travis_build` was not run because the local sandbox lacks parts of the build chain, but the syntactic and reasoning checks above cover the categories most likely to be perturbed by xref/label edits).

## Checklist

- [x] PLAN: Issue analyzed; intent (add EC/RHEA xrefs and one rename) is unambiguous; no clarification needed.
- [x] PRE-VALIDATION: SPARQL QC + ELK reasoning pass on the pristine file.
- [N/A] RESEARCH: Not required — issue specified the exact EC/RHEA IDs to add. External IDs cross-checked against IUBMB and RHEA's own RDF.
- [x] TERM-SEARCH: All four target terms located via `obo-grep.pl`; no name collisions (only the obsolete "obsolete vitamin D 25-hydroxylase activity" stanza shares the stem, which is expected).
- [N/A] DESIGN-PATTERNS: No new term construction or logical definition changes; pure metadata edits.
- [x] EDITS: Used `obo-checkout.pl` → edit in `terms/` → `obo-checkin.pl` workflow.
- [x] RELATIONSHIPS: Unchanged.
- [x] SPECIALIZED-EDITS: /mapping skill consulted (skos predicates assigned per the broader-EC / exact-RHEA pattern; broadMatch chosen because EC:1.17.3.2 groups two distinct reactions).
- [x] METADATA: No `created_by`/`creation_date` touched on these legacy terms; added `term_tracker_item` for #31962.
- [x] AUTOMATED-VALIDATION: robot SPARQL QC + ELK reasoning.
- [x] REFERENCE-VALIDATION: No PMIDs introduced. EC/RHEA IDs verified against authoritative sources.
- [x] CHANGES-COMMITTED: Single commit on `src/ontology/go-edit.obo`.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650697217)


#### Agent Issue Comment

All four requested xref/name updates committed in PR #<NN>.

Summary:
- GO:0036441 now carries `EC:1.1.1.358` as `skos:exactMatch`.
- GO:0070675 now carries `EC:1.17.3.2` as `skos:broadMatch` and `RHEA:68012` as `skos:exactMatch`; the definition xref has been switched to `RHEA:68012`.
- GO:0004855 `EC:1.17.3.2` xref relaxed from `exactMatch` to `broadMatch` (the EC covers both xanthine and hypoxanthine oxidation, so it is broader than the single-reaction GO term).
- GO:0030343 renamed from "vitamin D3 25-hydroxylase activity" to "vitamin D 25-hydroxylase activity" to match the EC and other similar GO terms; `EC:1.14.14.24` added as `skos:exactMatch`. The previous label retained as an exact synonym.

Ontology validates with the standard SPARQL QC checks and ELK reasoning.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650697217)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..33b21057d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231645,10 +231649,12 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

### Attempt 2: kimi-k2.6 / opencode

- **Eval PR**: [#280](https://github.com/ai4curation/eval-ont-agent-go/pull/280)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Trace**: [25646702351](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646702351)
- **Workflow run**: [25646702351](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646702351)

#### Agent PR Comment

This PR addresses #31962 by adding the missing EC and RHEA cross-references and adjusting one term name as requested.

### Changes made

| Term | Action |
|------|--------|
| **GO:0036441** | Added `EC:1.1.1.358` as `skos:exactMatch` xref. |
| **GO:0070675** | Updated definition xref to `RHEA:68012`; added `RHEA:68012` (`skos:exactMatch`) and `EC:1.17.3.2` (`skos:broadMatch`) xrefs. |
| **GO:0004855** | Changed existing `EC:1.17.3.2` xref from `skos:exactMatch` → `skos:broadMatch`. |
| **GO:0030343** | Renamed to **vitamin D 25-hydroxylase activity**; added *vitamin D3 25-hydroxylase activity* as exact synonym; added `EC:1.14.14.24` as `skos:exactMatch` xref. |

All affected terms were given a `term_tracker_item` property pointing to issue #31962.

### Rationale

* **skos relations** were chosen based on the issue request (exact/broad) and on existing GO curation practice for EC xrefs.
* The rename of GO:0030343 aligns the primary label with the EC nomenclature (EC 1.14.14.24 = *vitamin D 25-hydroxylase*) and with patterns of sibling GO hydroxylase terms, while keeping the substrate-specific name as an exact synonym so that existing annotations remain fully valid.
* The definition xref for GO:0070675 was switched from GOC curators to the newly added RHEA identifier because the issue explicitly asked to “use as def xref”.

### Checklist

- [x] Verified that EC/RHEA identifiers are syntactically correct.
- [x] Checked out terms individually in `terms/` and performed edits via `obo-checkout.pl` / `obo-checkin.pl` (no direct mega-file editing).
- [x] Confirmed the correct use of `skos:exactMatch` vs. `skos:broadMatch` per the issue.
- [x] Updated `term_tracker_item` for all changed terms.
- [x] Ran `robot verify` with the full SPARQL QC suite – **0 violations**.
- [x] Ran `robot reason` with ELK – **no unsatisfiable classes**.

### Files changed

* `src/ontology/go-edit.obo` (+12 / −3 lines)

### Note on validation

Full `make travis_build` could not be run because the local environment is missing the `amm` (Ammonite) dependency required by the Makefile. However, the equivalent `robot verify` and `robot reason` checks, which constitute the core of the build pipeline, completed successfully, so the ontology is functionally valid.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646702351)


#### Agent Issue Comment

Hi all, following up on the checklist in the issue description, I have implemented the requested changes locally and they are included in PR #<NN>.

**Summary of changes:**

1. **GO:0036441** — Added `EC:1.1.1.358` as a `skos:exactMatch` xref.
2. **GO:0070675** — Replaced the definition reference with `RHEA:68012`, added `RHEA:68012` as a `skos:exactMatch` xref, and added `EC:1.17.3.2` as a `skos:broadMatch` xref.
3. **GO:0004855** — Switched the existing `EC:1.17.3.2` xref from `skos:exactMatch` to `skos:broadMatch`.
4. **GO:0030343** — Renamed to **vitamin D 25-hydroxylase activity**, retained the old name *vitamin D3 25-hydroxylase activity* as an exact synonym, and added `EC:1.14.14.24` as a `skos:exactMatch` xref.

All four terms now have a `term_tracker_item` property linking back to this issue. A full set of SPARQL QC checks and an ELK reasoning pass were performed successfully with no errors.

If any reviewer spots an issue, just let me know!

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646702351)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..35df222a1 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231647,8 +231651,10 @@ namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

### Attempt 3: gpt-5.4 / codex

- **Eval PR**: [#187](https://github.com/ai4curation/eval-ont-agent-go/pull/187)
- **F1**: 1.000  **Precision**: 1.000  **Recall**: 1.000  **Jaccard**: 1.000
- **Workflow run**: [25640335244](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640335244)

#### Agent PR Comment

This PR addresses issue #31962 by updating four existing oxidoreductase activity terms with the requested EC/RHEA cross-references and one label adjustment.

Changes made:
- `GO:0036441 2-dehydropantolactone reductase activity`
  - added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`
- `GO:0070675 hypoxanthine oxidase activity`
  - changed definition provenance to `RHEA:68012`
  - added `xref: RHEA:68012 {source="skos:exactMatch"}`
  - added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`
- `GO:0004855 xanthine oxidase activity`
  - changed `xref: EC:1.17.3.2` from `skos:exactMatch` to `skos:broadMatch`
- `GO:0030343 vitamin D 25-hydroxylase activity`
  - renamed from `vitamin D3 25-hydroxylase activity`
  - added exact synonym `vitamin D3 25-hydroxylase activity`
  - added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`

Rationale:
- `EC:1.1.1.358` is the unspecific 2-dehydropantolactone reductase EC entry and matches the parent GO term `GO:0036441`.
- `EC:1.17.3.2 xanthine oxidase` covers both xanthine and hypoxanthine oxidation, so `broadMatch` is more accurate than `exactMatch` for the substrate-specific GO terms.
- `RHEA:68012` exactly matches the current hypoxanthine oxidase reaction text, so it is appropriate both as an exact xref and as definition provenance.
- `EC:1.14.14.24` uses the accepted name `vitamin D 25-hydroxylase`, while listing `vitamin D3 25-hydroxylase` as an alternative name; the GO label was aligned accordingly and the old wording was preserved as a synonym.

Validation and support:
- checked current stanzas with `obo-grep.pl`
- followed checkout/checkin workflow with `obo-checkout.pl` and `obo-checkin.pl`
- validated external identifiers against official EC/RHEA records in `RESEARCH.md`
- documented precedent/pattern notes in `DESIGN_PATTERNS.md`
- `make travis_build` passed before changes
- `make travis_build` passed after changes

Checklist:
- [x] PLAN: The issue and all its context has been analyzed, the intent is clear, and a plan for addressing it has been created
- [x] PRE-VALIDATION: Current state of the ontology validates prior to any changes
- [x] RESEARCH: Reference validation performed in `RESEARCH.md`; literature research not needed for this xref curation task
- [x] TERM-SEARCH: Relevant GO terms were consulted in `src/ontology/go-edit.obo`
- [x] DESIGN-PATTERNS: Existing design precedent documented in `DESIGN_PATTERNS.md`
- [x] EDITS: Correct checkout/checkin procedure used via `terms/`
- [x] RELATIONSHIPS: No relationship or logical axiom changes were needed; existing structure preserved
- [x] SPECIALIZED-EDITS: `/reaction` skill applied for catalytic activity EC/RHEA handling
- [x] METADATA: Added `term_tracker_item` links for issue `#31962`; no `created_by`/`creation_date` changes on existing terms
- [x] AUTOMATED-VALIDATION: Ontology validates with `make travis_build` after changes
- [x] REFERENCE-VALIDATION: Added/updated EC and RHEA references were validated against official source records
- [x] CHANGES-COMMITTED
- [x] RELEVANT-FILES: committed `src/ontology/go-edit.obo` only
- [x] ACCURACY: mappings and label changes match the referenced EC/RHEA entries
- [x] ISSUE-ALIGNMENT: changes match the scope of issue #31962
- [x] PR is created or amended
- [x] Communicate high level summary of changes on original issue(s), and any requests for further info
- [x] Communicated on PR detailed description of changes made, and rationale. Include checklists.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640335244)


#### Agent Issue Comment

Addressed in PR #<NN>.

Summary:
- added `EC:1.1.1.358` as `exactMatch` to `GO:0036441`
- changed `EC:1.17.3.2` to `broadMatch` on both `GO:0070675` and `GO:0004855`, and added `RHEA:68012` plus RHEA-based definition provenance to `GO:0070675`
- added `EC:1.14.14.24` to `GO:0030343` and renamed it to `vitamin D 25-hydroxylase activity`, retaining the old `vitamin D3` wording as a synonym

`make travis_build` passed before and after the edit.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640335244)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..33b21057d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231645,10 +231649,12 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 1.0  **precision**: 1.0  **recall**: 1.0

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/187
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 187 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully addressed issue #31962 by making the same substantive enzyme cross-reference and naming repairs as the human PR across `GO:0004855`, `GO:0030343`, `GO:0036441`, and `GO:0070675`. The metadiff F1/precision/recall of 1.0 accurately reflects the quality: the only visible differences from the human diff are xref ordering/context differences in the OBO stanzas, not semantic differences.


## Strengths

- Correctly changed `GO:0004855` `xanthine oxidase activity` from `EC:1.17.3.2 {source="skos:exactMatch"}` to `skos:broadMatch`, matching the issue's instruction that this EC maps broadly to both xanthine and hypoxanthine oxidase activities.
- Correctly updated `GO:0070675` `hypoxanthine oxidase activity` by adding `EC:1.17.3.2 {source="skos:broadMatch"}`, adding `RHEA:68012 {source="skos:exactMatch"}`, and replacing the definition xrefs with `[RHEA:68012]`.
- Correctly added `EC:1.1.1.358 {source="skos:exactMatch"}` to `GO:0036441` `2-dehydropantolactone reductase activity`.
- Correctly renamed `GO:0030343` from `vitamin D3 25-hydroxylase activity` to `vitamin D 25-hydroxylase activity`, preserved the old label as an exact synonym, and added `EC:1.14.14.24 {source="skos:exactMatch"}`.
- Added `term_tracker_item` annotations for issue #31962 to each touched term, consistent with the human PR.


## Issues

No substantive issues found. The agent placed the new EC xrefs before existing xrefs in `GO:0030343` and `GO:0036441`, whereas the human PR placed them after existing xrefs; this is a minor ordering/style difference only.

### Attempt 4: claude-sonnet-4.5 / copilot

- **Eval PR**: [#392](https://github.com/ai4curation/eval-ont-agent-go/pull/392)
- **F1**: 0.900  **Precision**: 0.900  **Recall**: 0.900  **Jaccard**: 0.818
- **Trace**: [25752375301](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25752375301)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..e2fcf9c64 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,10 +48957,11 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]
@@ -165190,13 +165191,16 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT []
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
 
 [Term]
@@ -231645,9 +231649,11 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde, RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

### Attempt 5: gemma-4-31b / opencode

- **Eval PR**: [#535](https://github.com/ai4curation/eval-ont-agent-go/pull/535)
- **F1**: 0.842  **Precision**: 0.800  **Recall**: 0.889  **Jaccard**: 0.727

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..226dc1027 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,7 +48957,7 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
@@ -165190,12 +165190,13 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
+xref: EC:1.14.14.24
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
 
@@ -231647,6 +231648,7 @@ namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -382391,13 +382393,15 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z

```

### Attempt 6: gemma-4-31b / opencode

- **Eval PR**: [#518](https://github.com/ai4curation/eval-ont-agent-go/pull/518)
- **F1**: 0.842  **Precision**: 0.800  **Recall**: 0.889  **Jaccard**: 0.727

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..226dc1027 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,7 +48957,7 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
@@ -165190,12 +165190,13 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
+xref: EC:1.14.14.24
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
 
@@ -231647,6 +231648,7 @@ namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 created_by: bf
@@ -382391,13 +382393,15 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#154](https://github.com/ai4curation/eval-ont-agent-go/pull/154)
- **F1**: 0.818  **Precision**: 0.900  **Recall**: 0.750  **Jaccard**: 0.692
- **Workflow run**: [25633611305](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633611305)

#### Agent PR Comment

## Summary

Addressed issue #31962 by updating catalytic activity xrefs and related metadata in `src/ontology/go-edit.obo`:

- `GO:0036441 2-dehydropantolactone reductase activity`
  - Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`.
  - Added term tracker link for issue #31962.
- `GO:0070675 hypoxanthine oxidase activity`
  - Replaced the definition provenance with `RHEA:68012`, matching the exact hypoxanthine oxidation reaction.
  - Added `xref: RHEA:68012 {source="skos:exactMatch"}`.
  - Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`.
  - Added term tracker link for issue #31962.
- `GO:0004855 xanthine oxidase activity`
  - Changed the EC xref predicate from `skos:exactMatch` to `skos:broadMatch` as requested.
  - Updated definition provenance from EC to the existing exact RHEA reaction, `RHEA:21132`.
  - Added term tracker link for issue #31962.
- `GO:0030343 vitamin D3 25-hydroxylase activity`
  - Renamed to `vitamin D 25-hydroxylase activity` to align with EC:1.14.14.24.
  - Preserved the previous label as an exact synonym: `vitamin D3 25-hydroxylase activity`.
  - Added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`.
  - Added term tracker link for issue #31962.

## Rationale

RHEA provides exact reaction-level identifiers for the GO molecular functions, so RHEA is used as exact mapping and definition provenance where applicable. EC:1.17.3.2 is broader than either the xanthine-only or hypoxanthine-only GO activities, so the xref predicate was set to `skos:broadMatch` on both terms. EC:1.14.14.24 has accepted name `vitamin D 25-hydroxylase`, supporting the requested GO label change.

`runoak` lookup was attempted for EC/RHEA checks, but failed in this environment because of a Python dependency error. I verified the IDs instead using the local RHEA RDF resource and ENZYME/ExPASy EC pages.

## Validation

- Pre-validation: `cd src/ontology && make travis_build` passed before edits.
- Post-edit validation: `cd src/ontology && make travis_build` passed after edits.

## Checklist

- [x] PLAN: Issue context reviewed; requested xref/name/provenance changes were clear.
- [x] PRE-VALIDATION: Current ontology validated before changes with `make travis_build`.
- [x] RESEARCH: External reaction/enzyme IDs checked; no new literature citations introduced.
- [x] TERM-SEARCH: Existing GO terms inspected with `obo-grep.pl`.
- [x] DESIGN-PATTERNS: Existing catalytic activity mapping/definition pattern reviewed; no new logical definitions needed.
- [x] EDITS: Used `obo-checkout.pl`, edited term files under `terms/`, then used `obo-checkin.pl`.
- [x] RELATIONSHIPS: No relationship changes required; existing parents/relationships retained.
  - [x] Logical definitions: N/A, no `intersection_of` edits.
  - [x] Relationships conform to existing MF catalytic activity terms.
  - [x] `is_a` not over-asserted; existing `is_a` links retained.
- [x] SPECIALIZED-EDITS: Reaction and mapping guidance applied for EC/RHEA xrefs.
  - [x] Term obsoletion: N/A.
  - [x] Chemical entity: N/A, no CHEBI edits made.
  - [x] Reaction: EC/RHEA IDs checked and SKOS predicates applied.
  - [x] Taxon constraints: N/A.
- [x] METADATA: Added issue #31962 term tracker links to modified terms; did not alter `created_by`/`creation_date` on existing terms.
- [x] AUTOMATED-VALIDATION: `make travis_build` passed after changes.
- [x] REFERENCE-VALIDATION: No new PMID/reference IDs introduced; RHEA/EC IDs validated via local RHEA RDF and ENZYME/ExPASy.
- [x] CHANGES-COMMITTED: Local commit created: `2d38ff8 Add oxidoreductase EC and RHEA xrefs`.
  - [x] RELEVANT-FILES: Committed only `src/ontology/go-edit.obo`.
  - [x] ACCURACY: Changes align with RHEA reaction equations and EC accepted names/comments.
  - [x] ISSUE-ALIGNMENT: Changes address all four requested bullets in issue #31962.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633611305)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Summary:
- Added EC:1.1.1.358 exactMatch to GO:0036441.
- Added EC:1.17.3.2 broadMatch xrefs to GO:0070675 and GO:0004855; added RHEA:68012 exactMatch and definition provenance to GO:0070675.
- Updated GO:0030343 label to `vitamin D 25-hydroxylase activity`, retained `vitamin D3 25-hydroxylase activity` as an exact synonym, and added EC:1.14.14.24 exactMatch.

Validation passed with `cd src/ontology && make travis_build`.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633611305)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..5cf0615cf 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48949,7 +48949,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0004855
 name: xanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [EC:1.17.3.2]
+def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [RHEA:21132]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231645,10 +231649,12 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

#### Review by gpt-5

**outcome**: success  **f1**: 0.818  **precision**: 0.9  **recall**: 0.75

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/154
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 154 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed all four requested oxidoreductase xref/name repairs from issue #31962: GO:0036441, GO:0004855, GO:0070675, and GO:0030343 were all updated in the intended direction. The metadiff score of 0.818 is a fair reflection of small line-level differences from the human PR, but it slightly under-rates the substantive quality because the agent completed the requested edits and its main extra change is defensible.

## Strengths

- Correctly added `EC:1.1.1.358 {source="skos:exactMatch"}` to `GO:0036441` 2-dehydropantolactone reductase activity.
- Correctly changed `GO:0004855` xanthine oxidase activity from `EC:1.17.3.2 {source="skos:exactMatch"}` to `skos:broadMatch`, matching the issue's instruction to make that EC mapping broad.
- Correctly added both `EC:1.17.3.2 {source="skos:broadMatch"}` and `RHEA:68012 {source="skos:exactMatch"}` to `GO:0070675` hypoxanthine oxidase activity, and changed the definition xref to `RHEA:68012` as explicitly requested.
- Correctly renamed `GO:0030343` from "vitamin D3 25-hydroxylase activity" to "vitamin D 25-hydroxylase activity", retained the old label as an exact synonym, and added `EC:1.14.14.24 {source="skos:exactMatch"}`.
- Added `term_tracker_item` annotations for issue #31962 on the touched terms, consistent with the human PR.

## Issues

- Minor scope difference: the agent also changed the definition xref for `GO:0004855` from `EC:1.17.3.2` to `RHEA:21132`. The issue only explicitly requested using a RHEA definition xref for `GO:0070675`, and the human PR did not make this change. However, because `EC:1.17.3.2` was being demoted to `skos:broadMatch` and `RHEA:21132` is already the exact reaction xref on `GO:0004855`, this looks like a defensible cleanup rather than a harmful edit.
- Minor provenance/style difference: for the restored synonym "vitamin D3 25-hydroxylase activity" on `GO:0030343`, the agent used `[EC:1.14.14.24]` as the synonym source, whereas the human PR used an empty source list. This is unlikely to affect ontology semantics, but the human version is more conservative because the EC label being matched is the broader "vitamin D 25-hydroxylase" name.

### Attempt 8: gpt-5.5 / opencode

- **Eval PR**: [#134](https://github.com/ai4curation/eval-ont-agent-go/pull/134)
- **F1**: 0.818  **Precision**: 0.900  **Recall**: 0.750  **Jaccard**: 0.692

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..5cf0615cf 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48949,7 +48949,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0004855
 name: xanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [EC:1.17.3.2]
+def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [RHEA:21132]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231645,10 +231649,12 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.818  **precision**: 0.9  **recall**: 0.75

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/134
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 134 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#31962` by making the requested EC/RHEA xref repairs on all four oxidoreductase activity terms: `GO:0036441`, `GO:0070675`, `GO:0004855`, and `GO:0030343`. The metadiff F1 of 0.818 under-represents the practical quality, because the differences from the human PR are a defensible extra definition-xref cleanup on `GO:0004855` and a minor synonym-provenance difference on `GO:0030343`, not missed core work. Overall this is a successful solution with small scope/style deviations.


## Strengths

- Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}` to `GO:0036441` `2-dehydropantolactone reductase activity`, matching the issue and the human PR.
- Correctly handled `GO:0070675` `hypoxanthine oxidase activity`: added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`, added `xref: RHEA:68012 {source="skos:exactMatch"}`, and replaced the definition xrefs `[GOC:mah, GOC:pde]` with `[RHEA:68012]`.
- Correctly changed the existing `GO:0004855` `xanthine oxidase activity` mapping for `EC:1.17.3.2` from `skos:exactMatch` to `skos:broadMatch`, reflecting the issue's instruction that this EC class is broader than the individual GO reaction.
- Correctly renamed `GO:0030343` from `vitamin D3 25-hydroxylase activity` to `vitamin D 25-hydroxylase activity`, preserved the previous label as an exact synonym, and added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`.
- Added `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI` to every term it touched, consistent with the human PR.


## Issues

- Minor scope difference: the agent also changed the definition xref on `GO:0004855` from `[EC:1.17.3.2]` to `[RHEA:21132]`. This was not explicitly requested and was not done in the human PR, but it is ontologically defensible because `RHEA:21132` is already the exact reaction xref for that term while `EC:1.17.3.2` was being downgraded to a broad match.
- Minor style/provenance difference: for the preserved old label on `GO:0030343`, the agent used `synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]`, while the human PR used `EXACT []`. This is unlikely to break anything, but it makes an extra synonym provenance assertion beyond the reference solution.
- No substantive missing requirement, wrong term, or syntax problem was found.

### Attempt 9: gpt-5.5 / codex

- **Eval PR**: [#126](https://github.com/ai4curation/eval-ont-agent-go/pull/126)
- **F1**: 0.818  **Precision**: 0.900  **Recall**: 0.750  **Jaccard**: 0.692
- **Workflow run**: [25633559640](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633559640)

#### Agent PR Comment

# Summary

Addressed issue #31962 by updating EC/RHEA mappings and reaction provenance on four existing molecular function catalytic activity terms.

Changes made in `src/ontology/go-edit.obo`:

* GO:0036441 `2-dehydropantolactone reductase activity`
  - Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`.
  - Added the issue #31962 `term_tracker_item`.
* GO:0070675 `hypoxanthine oxidase activity`
  - Replaced definition provenance with `RHEA:68012`.
  - Added `xref: RHEA:68012 {source="skos:exactMatch"}`.
  - Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`.
  - Added the issue #31962 `term_tracker_item`.
* GO:0004855 `xanthine oxidase activity`
  - Changed `EC:1.17.3.2` from `skos:exactMatch` to `skos:broadMatch`.
  - Updated definition provenance from `EC:1.17.3.2` to exact reaction source `RHEA:21132`.
  - Added the issue #31962 `term_tracker_item`.
* GO:0030343
  - Renamed from `vitamin D3 25-hydroxylase activity` to `vitamin D 25-hydroxylase activity`.
  - Added `vitamin D3 25-hydroxylase activity` as an exact synonym.
  - Added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`.
  - Added the issue #31962 `term_tracker_item`.

# Rationale

The EC and RHEA records support the requested mapping predicates. EC:1.17.3.2 describes xanthine oxidase as an enzyme class with xanthine as the primary reaction and notes activity on hypoxanthine and other substrates, so it is broader than each individual GO reaction term. RHEA:68012 and RHEA:21132 match the specific hypoxanthine-to-xanthine and xanthine-to-urate reactions, respectively, and are therefore exact reaction sources.

EC:1.14.14.24 uses the accepted name `vitamin D 25-hydroxylase`, with `vitamin D3 25-hydroxylase` as another name, so the GO label was updated while preserving the former label as a synonym.

# Validation

Baseline validation before edits:

* `cd src/ontology && make travis_build` passed.

Post-change validation:

* `cd src/ontology && make travis_build` passed.

Note: `runoak` was unavailable due to an installed OAK/LinkML dependency mismatch, so external IDs were checked against IUBMB Enzyme Nomenclature, Expasy ENZYME, and Rhea pages. A temporary `RESEARCH.md` with source notes and `DESIGN_PATTERNS.md` with pattern notes were created and left uncommitted.

# Checklist

* [x] PLAN: Issue #31962 and its context were analyzed; requested edits were clear.
* [x] PRE-VALIDATION: Current ontology validated before edits with `make travis_build`.
* [x] RESEARCH: External EC/RHEA records were checked; notes recorded in `RESEARCH.md`.
* [x] TERM-SEARCH: Existing GO target terms and related xrefs were checked with `obo-grep.pl`.
* [x] DESIGN-PATTERNS: Catalytic activity precedent and mapping style were reviewed; no logical definitions were added.
* [x] EDITS: Terms were edited via `obo-checkout.pl`, files in `terms/`, and `obo-checkin.pl`.
* [x] RELATIONSHIPS: Existing `is_a` and `part_of` relationships were retained; no new relationships or logical definitions were needed.
* [x] SPECIALIZED-EDITS: `/mapping` and `/reaction` workflows applied. Term obsoletion, taxon constraints, and chemical entity changes were N/A.
* [x] METADATA: Added issue #31962 `term_tracker_item` links to modified terms; no creation metadata was added to existing terms.
* [x] AUTOMATED-VALIDATION: Post-change `make travis_build` passed.
* [x] REFERENCE-VALIDATION: New RHEA/EC identifiers were checked against external source pages; no PMIDs were introduced.
* [x] CHANGES-COMMITTED: Committed only `src/ontology/go-edit.obo` locally.
* [x] ACCURACY: Mapping predicates reflect the scope of the EC entries and exact RHEA reactions.
* [x] ISSUE-ALIGNMENT: Changes match the requested mappings and label update for issue #31962.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633559640)

#### Agent Issue Comment

Changes committed in PR #<NN>.

Implemented the requested EC/RHEA mapping updates for GO:0036441, GO:0070675, GO:0004855, and GO:0030343. GO:0030343 has also been renamed to `vitamin D 25-hydroxylase activity` as requested.

Validation passed with `cd src/ontology && make travis_build`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25633559640)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..5cf0615cf 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48949,7 +48949,7 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 id: GO:0004855
 name: xanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [EC:1.17.3.2]
+def: "Catalysis of the reaction: xanthine + H2O + O2 = urate + H2O2." [RHEA:21132]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
@@ -48957,11 +48957,12 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0004856
@@ -165190,14 +165191,17 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
 relationship: part_of GO:0036378 ! calcitriol biosynthetic process from calciol
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 
 [Term]
 id: GO:0030345
@@ -231645,10 +231649,12 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: bf
 creation_date: 2013-09-30T16:26:27Z
 
@@ -382391,14 +382397,17 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962" xsd:anyURI
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z
 

```

#### Review by gpt-5.5

**outcome**: success  **f1**: 0.818  **precision**: 0.9  **recall**: 0.75

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/126
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 126 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly addressed issue `#31962` by adding or adjusting the requested EC/RHEA xrefs on all four oxidoreductase activity terms: `GO:0036441`, `GO:0070675`, `GO:0004855`, and `GO:0030343`. The metadiff F1 of 0.818 under-represents the practical quality, because the mismatches are mostly ordering/provenance differences plus one defensible extra definition-xref cleanup on `GO:0004855`. The agent's solution is substantively equivalent to the human PR and arguably improves one pre-existing provenance inconsistency.


## Strengths

- Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}` to `GO:0036441` `2-dehydropantolactone reductase activity`, matching the issue and human PR.
- Correctly handled `GO:0070675` `hypoxanthine oxidase activity`: added `EC:1.17.3.2` as `skos:broadMatch`, added `RHEA:68012` as `skos:exactMatch`, and changed the definition xref from local curator xrefs to `[RHEA:68012]`.
- Correctly changed the existing `GO:0004855` `xanthine oxidase activity` EC mapping from `skos:exactMatch` to `skos:broadMatch`, reflecting that `EC:1.17.3.2` covers a broader enzyme activity than the single xanthine-to-urate GO reaction.
- Correctly renamed `GO:0030343` from `vitamin D3 25-hydroxylase activity` to `vitamin D 25-hydroxylase activity`, preserved the old label as an exact synonym, and added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`.
- Added the `term_tracker_item` for `https://github.com/geneontology/go-ontology/issues/31962` to every touched term, as the human PR did.
- The agent's PR notes show appropriate methodology: it checked the EC/RHEA scope, recognized why `EC:1.17.3.2` should be broad for both `GO:0004855` and `GO:0070675`, and ran ontology validation.


## Issues

- Minor scope difference: the agent also changed the definition xref on `GO:0004855` from `[EC:1.17.3.2]` to `[RHEA:21132]`. This was not explicitly requested and was not done in the human PR, but it is ontologically defensible because `RHEA:21132` is already an exact reaction xref for that term while `EC:1.17.3.2` was being downgraded to a broad match.
- Minor style/provenance difference: for the preserved `GO:0030343` old-label synonym, the agent used `synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]`, while the human PR used an empty synonym xref list. This is unlikely to be harmful, but it is an extra assertion of synonym provenance relative to the reference solution.
- No substantive missing requirement or wrong term was found.

### Attempt 10: claude-sonnet-4.5 / claude

- **Eval PR**: [#480](https://github.com/ai4curation/eval-ont-agent-go/pull/480)
- **F1**: 0.778  **Precision**: 0.700  **Recall**: 0.875  **Jaccard**: 0.636
- **Trace**: [25847303086](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847303086)
- **Workflow run**: [25847303086](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847303086)

#### Agent PR Comment

# Add EC and RHEA xrefs to oxidoreductase activity terms

This PR addresses issue #31962 by adding missing EC and RHEA cross-references to four oxidoreductase activity GO terms and updating mapping predicates to ensure semantic accuracy.

## Changes Made

### 1. GO:0036441 (2-dehydropantolactone reductase activity)
**Change:** Added `xref: EC:1.1.1.358 {source="skos:exactMatch"}`

**Rationale:** EC:1.1.1.358 (2-dehydropantolactone reductase) precisely matches this GO term, both referring to the enzyme that catalyzes the reduction of 2-dehydropantolactone to pantolactone in pantothenate (vitamin B5) biosynthesis. The reaction definitions align exactly.

### 2. GO:0070675 (hypoxanthine oxidase activity)
**Changes:** 
- Added `xref: EC:1.17.3.2 {source="skos:broadMatch"}`
- Added `xref: RHEA:68012 {source="skos:exactMatch"}`
- Added RHEA:68012 to definition provenance

**Rationale:** 
- EC:1.17.3.2 (xanthine oxidase) encompasses both hypoxanthine→xanthine AND xanthine→urate oxidation reactions, making it broader than GO:0070675 which specifically describes only hypoxanthine oxidation. Therefore, broadMatch is the appropriate predicate.
- RHEA:68012 describes the specific reaction "hypoxanthine + O2 + H2O = xanthine + H2O2", which exactly matches the GO term definition, warranting exactMatch.
- Including RHEA:68012 in the definition provenance provides direct linkage to the precise reaction equation.

### 3. GO:0004855 (xanthine oxidase activity)
**Change:** Modified `xref: EC:1.17.3.2` from `skos:exactMatch` to `skos:broadMatch`

**Rationale:** EC:1.17.3.2 catalyzes both steps of purine catabolism (hypoxanthine→xanthine and xanthine→urate), while GO:0004855 specifically describes only the xanthine→urate reaction. The EC term has broader scope than the GO term, making broadMatch more semantically accurate than exactMatch. This change aligns the mapping with GO:0070675 for consistency.

### 4. GO:0030343 (vitamin D 25-hydroxylase activity)
**Changes:**
- Added `xref: EC:1.14.14.24 {source="skos:exactMatch"}`
- Renamed from "vitamin D3 25-hydroxylase activity" to "vitamin D 25-hydroxylase activity"

**Rationale:** 
- EC:1.14.14.24 (vitamin D 25-hydroxylase) precisely matches this GO term's function.
- The name change reflects that the enzyme hydroxylates both vitamin D2 (ergocalciferol) and vitamin D3 (cholecalciferol), not just D3. This aligns with EC nomenclature and matches similar GO terms. The existing synonym "cholecalciferol 25-hydroxylase activity" is retained for D3-specific searches.

## Verification and Validation

### External Term Verification
All EC and RHEA identifiers were verified through:
- **BRENDA Enzyme Database**: Confirmed all EC numbers and enzymatic functions
- **ExPASy ENZYME Database**: Cross-referenced EC classifications
- **RHEA Reaction Database**: Verified RHEA:68012 reaction equation via runoak
- **Literature**: 
  - PMID:32893671 - "New insights into purine metabolism in metabolic diseases: role of xanthine oxidoreductase activity" (Furuhashi M, 2020)
  - PMID:26443589 - "Biosynthesis of Pantothenic Acid and Coenzyme A" (Leonardi R, Jackowski S, 2007)
  - PMID:23243306 - "PanG, a new ketopantoate reductase involved in pantothenate synthesis" (Miller CN et al., 2013)

### runoak Verification Results
```
EC:1.1.1.358 ! 2-dehydropantolactone reductase
EC:1.17.3.2 ! xanthine oxidase
RHEA:68012 ! hypoxanthine + O2 + H2O = xanthine + H2O2
EC:1.14.14.24 ! vitamin D 25-hydroxylase
```

### Mapping Predicate Selection
Mapping predicates (exactMatch vs broadMatch) were assigned following GO mapping conventions:
- **exactMatch**: Used when the GO term and external term have identical or nearly identical scope
- **broadMatch**: Used when the external term has broader scope than the GO term

The semantic analysis considered:
- Reaction participants and stoichiometry
- Substrate and product specificity
- Enzymatic activity scope
- Alignment with existing GO mapping patterns

## Checklist

### Planning and Research
- [x] PLAN: Issue analyzed and comprehensive plan created
- [x] PRE-VALIDATION: Current ontology state validated before changes
- [x] RESEARCH: Background research performed on EC and RHEA terms
- [x] TERM-SEARCH: All four GO terms located and current state examined
- [x] EXTERNAL-LOOKUP: EC and RHEA IDs verified via external lookups
- [x] DESIGN-PATTERNS: N/A - No logical definitions or design patterns involved
- [x] MAPPING-SKILL: Mapping conventions consulted for proper xref format

### Edits and Relationships
- [x] EDITS: Terms checked out, edited, and checked in using obo-checkout/checkin
- [x] RELATIONSHIPS: N/A - Only xrefs added, no relationship changes
- [x] SPECIALIZED-EDITS: N/A - No obsoletion, chemicals, reactions, or taxon constraints

### Metadata and Validation
- [x] METADATA: Existing metadata preserved; no created_by/creation_date added (editing existing terms)
- [x] AUTOMATED-VALIDATION: Syntax validation performed
- [x] REFERENCE-VALIDATION: All RHEA and EC references verified against authoritative databases

### Commit and Documentation
- [x] CHANGES-COMMITTED:
  - [x] RELEVANT-FILES: Only src/ontology/go-edit.obo committed
  - [x] ACCURACY: Changes are biologically accurate and verified through literature
  - [x] ISSUE-ALIGNMENT: Changes fully address issue #31962 requests
  - [x] PR created with detailed description
  - [x] Communication prepared for original issue
  - [x] Detailed rationale and checklists included

## Background Research

Complete research documentation is available in RESEARCH.md (not committed, as per workflow). Key findings:

**EC:1.1.1.358** catalyzes 2-dehydropantolactone reduction in the alternative pantothenate biosynthesis pathway, present in multiple organisms.

**EC:1.17.3.2** (xanthine oxidase/XOR) is a rate-limiting enzyme in purine metabolism, catalyzing both hypoxanthine→xanthine and xanthine→uric acid oxidation. It exists in two forms (xanthine dehydrogenase and xanthine oxidase) and plays important roles in metabolic diseases.

**RHEA:68012** represents the specific hypoxanthine oxidation reaction, a subset of xanthine oxidase activity.

**EC:1.14.14.24** (CYP2R1 in humans) catalyzes the first step of vitamin D activation, hydroxylating both D2 and D3 forms at the 25 position to produce calcidiol.

## Notes

- No new terms were created; only existing term annotations were updated
- All changes follow GO mapping conventions and semantic web best practices
- Mapping predicate changes ensure consistency across related terms
- The vitamin D term rename improves accuracy and aligns with EC nomenclature

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847303086)


#### Agent Issue Comment

All requested EC and RHEA xrefs have been added to the oxidoreductase activity terms. Changes committed in PR #<NN>.

**Summary of changes:**
- GO:0036441: Added EC:1.1.1.358 (exactMatch)
- GO:0070675: Added EC:1.17.3.2 (broadMatch) and RHEA:68012 (exactMatch, also added to definition)
- GO:0004855: Changed EC:1.17.3.2 from exactMatch to broadMatch
- GO:0030343: Added EC:1.14.14.24 (exactMatch) and renamed to "vitamin D 25-hydroxylase activity"

All external terms were verified through authoritative databases (BRENDA, ExPASy, RHEA) and relevant literature. Mapping predicates were assigned based on semantic scope analysis.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847303086)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..e7a41e706 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,7 +48957,7 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
@@ -165190,10 +165190,11 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
@@ -231645,6 +231646,7 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
@@ -382391,7 +382393,9 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde, RHEA:68012]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]

```

### Attempt 11: claude-haiku-4.5 / claude

- **Eval PR**: [#214](https://github.com/ai4curation/eval-ont-agent-go/pull/214)
- **F1**: 0.778  **Precision**: 0.700  **Recall**: 0.875  **Jaccard**: 0.636
- **Workflow run**: [25640385644](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640385644)

#### Agent PR Comment

# Changes to Address Issue #31962

#### Agent Issue Comment

All requested changes have been completed and committed.

The following EC and RHEA xrefs have been added to the four oxidoreductase activity terms as specified in the issue:

- GO:0036441 (2-dehydropantolactone reductase activity): Added EC:1.1.1.358 as exactMatch
- GO:0070675 (hypoxanthine oxidase activity): Added EC:1.17.3.2 as broadMatch and RHEA:68012 as exactMatch; updated definition to include RHEA:68012 reference
- GO:0004855 (xanthine oxidase activity): Changed EC:1.17.3.2 from exactMatch to broadMatch
- GO:0030343 (vitamin D3 25-hydroxylase activity): Added EC:1.14.14.24 as exactMatch and updated term name to "vitamin D 25-hydroxylase activity" to align with EC nomenclature

All external identifiers (EC:1.1.1.358, EC:1.17.3.2, EC:1.14.14.24, and RHEA:68012) have been verified to exist in their respective external ontologies.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25640385644)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index b2469c260..7062b7e0c 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -48957,7 +48957,7 @@ synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
 synonym: "xanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine:xanthine oxidase activity" RELATED [EC:1.17.3.2]
-xref: EC:1.17.3.2 {source="skos:exactMatch"}
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
 xref: MetaCyc:XANTHINE-OXIDASE-RXN
 xref: RHEA:21132 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
@@ -165190,10 +165190,11 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0030343
-name: vitamin D3 25-hydroxylase activity
+name: vitamin D 25-hydroxylase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: calciol (vitamin D3) + reduced [NADPH--hemoprotein reductase] + O2 = calcidiol + oxidized [NADPH--hemoprotein reductase] + H2O + H+." [RHEA:32903]
 synonym: "cholecalciferol 25-hydroxylase activity" EXACT []
+xref: EC:1.14.14.24 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-9829
 xref: RHEA:32903 {source="skos:exactMatch"}
 is_a: GO:0008395 ! steroid hydroxylase activity
@@ -231645,6 +231646,7 @@ id: GO:0036441
 name: 2-dehydropantolactone reductase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: (R)-pantolactone + NADP+ = 2-dehydropantolactone + NADPH + H+." [RHEA:18981]
+xref: EC:1.1.1.358 {source="skos:exactMatch"}
 xref: KEGG_REACTION:R03155
 xref: RHEA:18981 {source="skos:exactMatch"}
 is_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
@@ -382391,13 +382393,15 @@ creation_date: 2009-05-29T01:02:13Z
 id: GO:0070675
 name: hypoxanthine oxidase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde]
+def: "Catalysis of the reaction: hypoxanthine + H2O + O2 = xanthine + H2O2." [GOC:mah, GOC:pde, RHEA:68012]
 synonym: "hypoxanthine-xanthine oxidase activity" BROAD [EC:1.17.3.2]
 synonym: "hypoxanthine:O2 oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "hypoxanthine:oxygen oxidoreductase activity" RELATED [EC:1.17.3.2]
 synonym: "schardinger enzyme" RELATED [EC:1.17.3.2]
 synonym: "Schardinger enzyme activity" RELATED [EC:1.17.3.2]
 synonym: "xanthine oxidoreductase activity" BROAD [EC:1.17.3.2]
+xref: EC:1.17.3.2 {source="skos:broadMatch"}
+xref: RHEA:68012 {source="skos:exactMatch"}
 is_a: GO:0016727 ! oxidoreductase activity, acting on CH or CH2 groups, oxygen as acceptor
 created_by: mah
 creation_date: 2009-05-29T01:12:55Z

```

#### Review by gpt-5

**outcome**: partial_success  **f1**: 0.778  **precision**: 0.7  **recall**: 0.875

**Failure modes**: under_editing, missed_requirement

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/214
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31962 --repo geneontology/go-ontology
    gh pr diff 31970 --repo geneontology/go-ontology
    gh pr diff 214 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the main issue by adding the requested EC/RHEA mappings and renaming `GO:0030343`, so the core ontology repair is mostly correct. The metadiff F1 of 0.778 is a fair signal of a near miss: the agent matched the explicit xref changes but missed the human PR's synonym preservation and tracker metadata, and handled one definition xref less cleanly than the reference patch.


## Strengths

- Correctly changed `GO:0004855` xanthine oxidase activity so `EC:1.17.3.2` is `skos:broadMatch` rather than `skos:exactMatch`, as requested.
- Correctly added `EC:1.1.1.358` as an exact xref to `GO:0036441` 2-dehydropantolactone reductase activity.
- Correctly renamed `GO:0030343` from "vitamin D3 25-hydroxylase activity" to "vitamin D 25-hydroxylase activity" and added `EC:1.14.14.24` as an exact xref.
- Correctly added both requested mappings to `GO:0070675` hypoxanthine oxidase activity: `EC:1.17.3.2` as `skos:broadMatch` and `RHEA:68012` as `skos:exactMatch`.
- Did use `RHEA:68012` as a definition xref for `GO:0070675`, satisfying the issue's explicit "use as def xref" request in substance.


## Issues

- When renaming `GO:0030343`, the agent did not preserve the old primary label "vitamin D3 25-hydroxylase activity" as an exact synonym. The human PR adds this synonym, which is important because the old name remains a valid search/access label after the broader "vitamin D" name change.
- The agent did not add `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31962"` to the touched terms. The human PR adds it to `GO:0004855`, `GO:0030343`, `GO:0036441`, and `GO:0070675`; this is not central to the xref semantics but is standard traceability metadata for the edit.
- For `GO:0070675`, the agent changed the definition xrefs to `[GOC:mah, GOC:pde, RHEA:68012]`, whereas the human PR replaced the older curator xrefs with `[RHEA:68012]`. Keeping the GOC xrefs is not obviously invalid, but the reference solution more clearly points the reaction definition to the exact RHEA reaction source.
