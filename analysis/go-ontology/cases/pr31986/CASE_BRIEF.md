# PR #31986 — GO:0102177 24-methylenelophenol methyl oxidase activity

- **Ontology**: go-ontology
- **Repo**: geneontology/go-ontology
- **Issue**: [#31985](https://github.com/geneontology/go-ontology/issues/31985)
- **PR**: [#31986](https://github.com/geneontology/go-ontology/pull/31986)
- **Author**: @sjm41
- **Merged**: 2026-04-27
- **task_type**: reclassification
- **difficulty**: hard
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #31985 identified that GO:0102177 carried an `xref: EC:1.14.18.11` (plant 4-alpha-monomethylsterol monooxygenase) but its name, definition, RHEA cross-reference, MetaCyc cross-reference, and parent term all described a different reaction (an NADH-dependent partial reaction). All five fields needed realignment to match the actual EC:1.14.18.11 reaction.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0102177 was comprehensively realigned:
- Name updated to match EC:1.14.18.11 nomenclature
- Definition rewritten to describe the correct reaction
- RHEA cross-reference corrected
- MetaCyc cross-reference corrected
- Parent `is_a` relationship changed to the appropriate oxidase parent
- Net +2 lines reflecting addition of previously missing xrefs

## Resolution

Merged same-day by the reporting curator (@sjm41). This is a technically demanding correction because it requires reconciling multiple external database identifiers (EC, RHEA, MetaCyc) with the GO term hierarchy to ensure all five aspects of the term (name, def, xrefs, parent) describe the same biochemical reaction.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..a76eab953 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,16 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
+synonym: "24-methylenelophenol methyl oxidase activity" EXACT []
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

## Agent Attempts (7)

### Attempt 1: claude-opus-4.7 / claude

- **Eval PR**: [#352](https://github.com/ai4curation/eval-ont-agent-go/pull/352)
- **F1**: 0.960  **Precision**: 1.000  **Recall**: 0.923  **Jaccard**: 0.923
- **Trace**: [25650709072](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25650709072)
- **Workflow run**: [25650709072](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650709072)

#### Agent PR Comment

## Summary

Aligns `GO:0102177` with its EC mapping (EC:1.14.18.11, "plant 4alpha-monomethylsterol monooxygenase"). The previous metadata combined the EC:1.14.18.11 xref with a partial-reaction RHEA (`RHEA:58872`, which is *part of* RHEA:58868) and a NAD(P)H-donor parent (`GO:0016709`), making the term internally inconsistent. Issue #31985 enumerates the fix.

## Changes to `GO:0102177`

| Field | Before | After |
|---|---|---|
| name | 24-methylenelophenol methyl oxidase activity | 4alpha-monomethylsterol monooxygenase activity |
| def reaction | `24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O` | `24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O` |
| def xref | `[GOC:pz, PMID:11707264, RHEA:58872]` | `[PMID:11707264, RHEA:58868]` |
| RHEA xref | `RHEA:58872` | `RHEA:58868` |
| MetaCyc xref | `MetaCyc:RXN-11930` | `MetaCyc:RXN-19724` |
| is_a | `GO:0016709` (... NAD(P)H as one donor ...) | `GO:0016716` (... another compound as one donor ...) |
| synonyms | — | `"24-methylenelophenol methyl oxidase activity" EXACT []` (preserves old label); `"plant 4alpha-monomethylsterol monooxygenase" RELATED [EC:1.14.18.11]` (EC accepted name) |
| term_tracker_item | (existing #30193) | adds #31985 |

The new axiomatization matches the sibling `GO:0000254` (C-4 methylsterol oxidase activity, EC:1.14.18.9), which uses the same Fe(II)/Fe(III)-[cytochrome b5] reaction template and parent.

## Rationale notes

- EC:1.14.18.11 (`plant 4alpha-monomethylsterol monooxygenase`) corresponds to the overall three-step oxidation methyl → hydroxymethyl → formyl → carboxyl, i.e. RHEA:58868. RHEA:58872 is only the first sub-step (methyl → hydroxymethyl) and is annotated in RHEA as `part_of RHEA:58868`, so it is not the right def xref for an EC:1.14.18.11-equivalent class.
- The parent shift from `GO:0016709` to `GO:0016716` reflects that the actual electron donor is reduced cytochrome b5, not NAD(P)H — so the NAD(P)H-donor branch was the wrong superclass.
- The old name is kept as an EXACT synonym so downstream tooling can still resolve it.

## Checklist

- [x] PLAN — issue intent unambiguous (five explicit task bullets); plan executed as listed
- [x] PRE-VALIDATION — no pre-existing edit-file errors detected; ran `robot convert` cleanly
- [N/A] RESEARCH — no literature search needed; reaction details supplied in the issue and cross-checked against RHEA:58868 / EC:1.14.18.11 / MetaCyc:RXN-19724 references and the sibling `GO:0000254` pattern
- [x] TERM-SEARCH — confirmed `GO:0016716` exists and is the correct parent; confirmed no other ontology references to `GO:0102177`
- [x] DESIGN-PATTERNS — followed the catalytic-activity / cytochrome-b5 monooxygenase pattern established by `GO:0000254` (sibling under EC:1.14.18.x)
- [x] EDITS — used `obo-checkout.pl` / `obo-checkin.pl`; no direct edits to `go-edit.obo`
- [x] RELATIONSHIPS — single `is_a` to `GO:0016716`; no logical definition added (none exists for the sibling either; matches reaction-skill guidance of single-source-of-truth via RHEA def xref)
- [x] SPECIALIZED-EDITS / reaction skill — RHEA `skos:exactMatch`, EC `skos:exactMatch`, MetaCyc unqualified (mirrors `GO:0000254`); single source of truth `RHEA:58868` in def xref
- [N/A] chemical-entity skill — no CHEBI ID changes
- [N/A] taxon-constraint skill — no taxon constraint changes
- [N/A] term-obsoletion skill — term not obsoleted
- [x] METADATA — not a new term, so `created_by` / `creation_date` not added; added `term_tracker_item` for #31985; namespace preserved
- [x] AUTOMATED-VALIDATION — `robot convert` syntactic check passes; all 16 SPARQL violation queries from `travis_build` pass; ELK reasoning runs without unsat classes
- [x] REFERENCE-VALIDATION — `PMID:11707264` was already on the term and is retained; no new PMIDs introduced
- [x] CHANGES-COMMITTED — `src/ontology/go-edit.obo` only
- [x] ISSUE-ALIGNMENT — every bullet in the issue task list is addressed

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650709072)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Applied all five tasks from the issue:

- Renamed `GO:0102177` to **4alpha-monomethylsterol monooxygenase activity** (matching EC:1.14.18.11).
- Replaced the definition with the full EC:1.14.18.11 / RHEA:58868 reaction (cytochrome b5 form, 3 O2).
- Updated def xrefs to `[PMID:11707264, RHEA:58868]` (dropped the unnecessary `GOC:pz`).
- Updated the RHEA xref from `RHEA:58872` to `RHEA:58868`, and the MetaCyc xref from `RXN-11930` to `RXN-19724`.
- Reparented under `GO:0016716` (oxidoreductase activity, acting on paired donors, ... another compound as one donor ...), the parent appropriate to EC:1.14.18.- rather than the NAD(P)H-donor class.
- Kept `24-methylenelophenol methyl oxidase activity` as an EXACT synonym and added `plant 4alpha-monomethylsterol monooxygenase` (the EC accepted name) as a RELATED synonym.

The three Arabidopsis SMO1-3/SMO2-1/SMO2-2 IEA annotations propagated via EC:1.14.18.11 remain valid; only the GO term metadata changes.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25650709072)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..30d280f46 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,17 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
+synonym: "24-methylenelophenol methyl oxidase activity" EXACT []
+synonym: "plant 4alpha-monomethylsterol monooxygenase" RELATED [EC:1.14.18.11]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#494](https://github.com/ai4curation/eval-ont-agent-go/pull/494)
- **F1**: 0.957  **Precision**: 0.917  **Recall**: 1.000  **Jaccard**: 0.917
- **Trace**: [25888578585](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25888578585)
- **Workflow run**: [25888578585](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888578585)

#### Agent PR Comment

# Update GO:0102177 to align with EC:1.14.18.11

#### Agent Issue Comment

All requested changes to GO:0102177 have been completed and committed in PR #<NN>.

The term now correctly aligns with EC:1.14.18.11 (plant 4alpha-monomethylsterol monooxygenase) by:
- Using the correct RHEA reaction (RHEA:58868 instead of the partial reaction RHEA:58872)
- Updating the name and definition to match the EC nomenclature
- Using the appropriate parent term (GO:0016716 for EC:1.14.18.-)
- Correcting the MetaCyc xref to RXN-19724

The three IEA annotations via EC:1.14.18.11 for Arabidopsis Methylsterol monooxygenase proteins should now be correctly mapped to the updated term.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25888578585)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..4a660c768 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,15 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#424](https://github.com/ai4curation/eval-ont-agent-go/pull/424)
- **F1**: 0.957  **Precision**: 0.917  **Recall**: 1.000  **Jaccard**: 0.917
- **Trace**: [25775057140](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25775057140)

#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..4a660c768 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,15 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

### Attempt 4: kimi-k2.6 / opencode

- **Eval PR**: [#283](https://github.com/ai4curation/eval-ont-agent-go/pull/283)
- **F1**: 0.957  **Precision**: 0.917  **Recall**: 1.000  **Jaccard**: 0.917
- **Trace**: [25646712433](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646712433)
- **Workflow run**: [25646712433](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646712433)

#### Agent PR Comment

## Summary

This PR updates GO:0102177 to align the term with its EC:1.14.18.11 and RHEA:58868 references, as requested in issue #31985.

### Changes to GO:0102177

| Property | Before | After |
|----------|--------|-------|
| **name** | 24-methylenelophenol methyl oxidase activity | 4alpha-monomethylsterol monooxygenase activity |
| **definition** | Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O. [GOC:pz, PMID:11707264, RHEA:58872] | Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O. [PMID:11707264, RHEA:58868] |
| **EC xref** | EC:1.14.18.11 {exactMatch} | EC:1.14.18.11 {exactMatch} |
| **RHEA xref** | RHEA:58872 {exactMatch} | RHEA:58868 {exactMatch} |
| **MetaCyc xref** | MetaCyc:RXN-11930 | MetaCyc:RXN-19724 |
| **is_a parent** | GO:0016709 | GO:0016716 |
| **term_tracker_item** | #30193 | #30193, #31985 |

### Rationale

The existing term name, definition, RHEA xref, MetaCyc xref, and parent did not match the assigned EC number (1.14.18.11). The RHEA:58872 xref was only a partial ("part of") reaction of the full EC-catalyzed reaction RHEA:58868. Updating to RHEA:58868 captures the complete reaction catalyzed by this enzyme, consistent with EC:1.14.18.11. The new name, definition, and MetaCyc xref were derived from the EC and RHEA entries directly.

The parent was moved from GO:0016709 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen) to GO:0016716 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen), reflecting that EC:1.14.18.- uses a cytochrome b5/Fe donor system rather than NAD(P)H.

### Checklist

- [x] Issue analyzed and intent is clear
- [x] Term checked out using obo-checkout.pl
- [x] Edits made in terms/GO_0102177.obo
- [x] Term checked in using obo-checkin.pl
- [x] All SPARQL QC checks pass (16/16 PASS)
- [x] ELK reasoning completes without error
- [x] Only src/ontology/go-edit.obo was modified and committed
- [x] term_tracker_item added for issue #31985

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646712433)


#### Agent Issue Comment

Hi,

All requested updates to GO:0102177 have been made and are committed in PR #<NN>.

Summary of changes:
- Name updated to '4alpha-monomethylsterol monooxygenase activity' to match EC:1.14.18.11
- Definition and reaction updated to the full RHEA:58868 reaction
- RHEA xref updated to RHEA:58868 (exactMatch)
- MetaCyc xref updated to MetaCyc:RXN-19724
- Parent changed from GO:0016709 to GO:0016716 (EC:1.14.18.-)
- Removed GOC:pz from definition references

Thanks for the detailed report and checklist — it made the edits very straightforward.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646712433)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..4a660c768 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,14 +440991,15 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31985" xsd:anyURI
 
 [Term]
 id: GO:0102178

```

### Attempt 5: claude-sonnet-4.5 / claude

- **Eval PR**: [#479](https://github.com/ai4curation/eval-ont-agent-go/pull/479)
- **F1**: 0.909  **Precision**: 0.833  **Recall**: 1.000  **Jaccard**: 0.833
- **Trace**: [25847343953](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25847343953)
- **Workflow run**: [25847343953](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847343953)

#### Agent PR Comment

# Fix GO:0102177 to align with EC:1.14.18.11

## Summary

Corrected GO:0102177 to properly represent plant 4alpha-monomethylsterol monooxygenase activity (EC:1.14.18.11). The term previously referenced RHEA:58872, which represents only one step of a three-step oxidation process. EC:1.14.18.11 maps to RHEA:58868, the complete reaction.

## Changes Made

**GO:0102177**

- **Name:** `24-methylenelophenol methyl oxidase activity` → `4alpha-monomethylsterol monooxygenase activity`
  - Updated to match EC:1.14.18.11 accepted name

- **Definition:** Updated from incorrect NADH-dependent partial reaction to complete cytochrome b5-dependent three-step oxidation:
  - Old: `Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O.`
  - New: `Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O.`
  - Also corrected substrate name: methylenelophenol → methylidenelophenol

- **Definition provenance:** Removed GOC:pz, retained PMID:11707264, updated to RHEA:58868

- **RHEA xref:** `RHEA:58872` → `RHEA:58868`

- **MetaCyc xref:** `RXN-11930` → `RXN-19724`

- **Parent term:** `GO:0016709` → `GO:0016716`
  - Changed from "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor"
  - To "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor" (EC:1.14.18.-)
  - This correctly reflects that cytochrome b5, not NAD(P)H, serves as electron donor

## Biological Justification

Plant 4alpha-monomethylsterol monooxygenase (SMO) catalyzes three successive oxidation steps of the 4alpha-methyl group on sterol intermediates:
1. Methyl → hydroxymethyl (RHEA:58872 - the partial reaction)
2. Hydroxymethyl → aldehyde 
3. Aldehyde → carboxyl (complete product in RHEA:58868)

The enzyme uses cytochrome b5 as electron donor and is essential for plant sterol biosynthesis. PMID:11707264 describes the functional identification of Arabidopsis SMO1 and SMO2 genes.

## Validation Checklist

- [x] **PLAN:** Issue analyzed, intent clear, plan created
- [x] **PRE-VALIDATION:** Ontology structure verified before changes
- [x] **RESEARCH:** References validated
  - PMID:11707264 confirmed (Darnet et al., 2001 - Arabidopsis SMO functional identification)
  - EC:1.14.18.11 verified (plant 4alpha-monomethylsterol monooxygenase)
  - RHEA:58868 vs RHEA:58872 relationship confirmed
- [x] **TERM-SEARCH:** Located GO:0102177 and new parent GO:0016716
- [x] **DESIGN-PATTERNS:** N/A (metadata correction, not structural change)
- [x] **EDITS:** Proper checkout/checkin procedure followed
- [x] **RELATIONSHIPS:** Parent relationship corrected to GO:0016716 (EC:1.14.18.-)
- [x] **SPECIALIZED-EDITS:** N/A (no obsoletion, chemical entity, or taxon constraints)
- [x] **METADATA:** All metadata preserved appropriately
  - EC:1.14.18.11 xref retained
  - term_tracker_item preserved (links to #30193)
  - Definition now has proper provenance
- [x] **AUTOMATED-VALIDATION:** OBO syntax verified
- [x] **REFERENCE-VALIDATION:** PMID:11707264 validated via linkml-reference-validator
- [x] **CHANGES-COMMITTED:**
  - [x] **RELEVANT-FILES:** Only src/ontology/go-edit.obo modified
  - [x] **ACCURACY:** Changes align with EC, RHEA, and literature
  - [x] **ISSUE-ALIGNMENT:** All requested tasks from issue #31985 completed
  - [x] **PR:** Created with detailed description
  - [x] **COMMUNICATION:** Issue updated with summary

## Testing

Basic OBO syntax validation confirmed file integrity (48,306 terms counted, proper format-version header, well-formed structure).

Note: Full travis_build could not be completed due to missing build dependencies (amm) in the evaluation environment, but core validations passed.

## Addresses

Issue #31985

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847343953)


#### Agent Issue Comment

All requested changes have been implemented and committed in PR #<NN>.

GO:0102177 has been corrected to properly align with EC:1.14.18.11 (plant 4alpha-monomethylsterol monooxygenase), including:
- Name updated to match EC accepted name
- Definition updated to reflect the complete RHEA:58868 reaction 
- RHEA xref changed from 58872 to 58868
- MetaCyc xref updated to RXN-19724
- Parent changed to GO:0016716 (EC:1.14.18.-)

The term now correctly represents the complete three-step oxidation reaction using cytochrome b5 as electron donor, rather than the partial reaction previously referenced.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25847343953)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..6ab6948f4 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,13 +440991,13 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]

```

### Attempt 6: claude-haiku-4.5 / claude

- **Eval PR**: [#409](https://github.com/ai4curation/eval-ont-agent-go/pull/409)
- **F1**: 0.909  **Precision**: 0.833  **Recall**: 1.000  **Jaccard**: 0.833
- **Trace**: [25761773926](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25761773926)
- **Workflow run**: [25761773926](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761773926)

#### Agent PR Comment

# GO:0102177 Correction - xrefs and reaction definition

## Changes Made

Updated GO:0102177 to correct mismatched external references and provide the accurate enzyme reaction.

### Term Name
- **Before:** 24-methylenelophenol methyl oxidase activity
- **After:** 4alpha-monomethylsterol monooxygenase activity
- **Reason:** Updated to match the official EC:1.14.18.11 nomenclature

### Reaction Definition
- **Before:** Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O
- **After:** Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O
- **Reason:** Updated to the correct EC:1.14.18.11 reaction with proper cofactors and products

### Definition References
- **Before:** [GOC:pz, PMID:11707264, RHEA:58872]
- **After:** [PMID:11707264, RHEA:58868]
- **Reason:** Removed GOC:pz and updated RHEA reference to the correct parent reaction RHEA:58868

### RHEA Cross-reference
- **Before:** RHEA:58872
- **After:** RHEA:58868
- **Reason:** Corrected to the main reaction that encompasses the correct catalytic mechanism

### MetaCyc Cross-reference
- **Before:** MetaCyc:RXN-11930
- **After:** MetaCyc:RXN-19724
- **Reason:** Updated to match the correct enzyme reaction in MetaCyc

### Parent Class
- **Before:** GO:0016709 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen)
- **After:** GO:0016716 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen)
- **Reason:** Updated to match EC:1.14.18.- classification, as the enzyme uses cytochrome b5 as the other donor, not NAD(P)H

## Validation

The OBO format has been verified to be syntactically correct. The term structure follows GO conventions with proper metadata and cross-references.

## Checklist

- [x] PLAN: Issue analyzed and approach determined
- [x] TERM-SEARCH: Current term state verified
- [x] EDITS: Corrections made using proper checkout/checkin procedure
- [x] RELATIONSHIPS: Parent class updated appropriately
- [x] METADATA: Term tracker item reference maintained
- [x] CHANGES-COMMITTED: Changes committed with detailed message
- [x] ISSUE-ALIGNMENT: All requested corrections from issue #31985 completed

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761773926)


#### Agent Issue Comment

Completed all requested corrections to GO:0102177. Changes committed to PR #<NN>.

Summary of changes:
- Renamed term to '4alpha-monomethylsterol monooxygenase activity' to match EC nomenclature
- Updated reaction definition to the correct EC:1.14.18.11 reaction
- Corrected RHEA xref from RHEA:58872 to RHEA:58868
- Updated MetaCyc xref to RXN-19724
- Corrected parent class to GO:0016716

All external references (EC, RHEA, MetaCyc) are now consistent with each other and aligned with the enzyme classification.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25761773926)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..6ab6948f4 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,13 +440991,13 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O." [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]

```

### Attempt 7: gemma-4-31b / opencode

- **Eval PR**: [#253](https://github.com/ai4curation/eval-ont-agent-go/pull/253)
- **F1**: 0.818  **Precision**: 0.750  **Recall**: 0.900  **Jaccard**: 0.692
- **Trace**: [25646664474](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646664474)
- **Workflow run**: [25646664474](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646664474)

#### Agent PR Comment

## Summary of Changes
Updated GO:0102177 to align with EC:1.14.18.11 and RHEA:58868.

### Changes Made:
- **Name**: Changed from `24-methylenelophenol methyl oxidase activity` to `4alpha-monomethylsterol monooxygenase activity`.
- **Definition**: Updated to "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O".
- **Definition Xrefs**: Removed `GOC:pz` and updated `RHEA:58872` to `RHEA:58868`.
- **Xrefs**:
  - Updated `MetaCyc:RXN-11930` to `MetaCyc:RXN-19724`.
  - Updated `RHEA:58872` to `RHEA:58868`.
- **Parent**: Changed `is_a` from `GO:0016709` to `GO:0016716`.

### Rationale:
The previous name, definition, and parent were inconsistent with the linked EC and RHEA entries. The updates ensure that GO:0102177 correctly describes the activity of plant 4alpha-monomethylsterol monooxygenase, consistent with the biochemical data from RHEA:58868 and EC:1.14.18.11.

### Checklist:
- [x] Update name to match EC
- [x] Update definition to reflect RHEA:58868 reaction
- [x] Update MetaCyc xref
- [x] Update RHEA xref
- [x] Update parent GO term
- [x] Removed unnecessary GOC:pz definition xref

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646664474)


#### Agent Issue Comment

Changes committed in PR #<NN>
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/go-ontology-agent-config@v9:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646664474)


#### Agent Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index dd6593ace..fd873777a 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -440991,13 +440991,13 @@ replaced_by: GO:0000253
 
 [Term]
 id: GO:0102177
-name: 24-methylenelophenol methyl oxidase activity
+name: 4alpha-monomethylsterol monooxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: 24-methylenelophenol + O2 + NADH + H+ = 4alpha-hydroxymethyl-ergosta-7,24(241)-dien-3beta-ol + NAD + H2O." [GOC:pz, PMID:11707264, RHEA:58872]
+def: "Catalysis of the reaction: 24-methylidenelophenol + 6 Fe(II)-[cytochrome b5] + 3 O2 + 5 H+ = 4alpha-carboxy-ergosta-7,24(24(1))-dien-3beta-ol + 6 Fe(III)-[cytochrome b5] + 4 H2O" [PMID:11707264, RHEA:58868]
 xref: EC:1.14.18.11 {source="skos:exactMatch"}
-xref: MetaCyc:RXN-11930
-xref: RHEA:58872 {source="skos:exactMatch"}
-is_a: GO:0016709 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
+xref: MetaCyc:RXN-19724
+xref: RHEA:58868 {source="skos:exactMatch"}
+is_a: GO:0016716 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, another compound as one donor, and incorporation of one atom of oxygen
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
 
 [Term]

```
