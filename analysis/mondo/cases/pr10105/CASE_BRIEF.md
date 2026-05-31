---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9864
pr_number: 10105
issue_title: Request for new term SYCE1-related gametogenic failure
pr_author: MeeSiing
pr_merged_at: '2026-03-31'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
best_f1: 0.56
best_model: claude-sonnet-4.5
---

# PR #10105 — Request for new term SYCE1-related gametogenic failure

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9864](https://github.com/monarch-initiative/mondo/issues/9864) | [PR #10105](https://github.com/monarch-initiative/mondo/pull/10105) | @MeeSiing | merged 2026-03-31

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #9864 requested a new term for "SYCE1-related gametogenic failure" describing a condition where variants in SYCE1 (synaptonemal complex central element protein 1) cause varying gametogenic phenotypes in both 46,XY and 46,XX individuals, ranging from spermatogenic failure to premature ovarian insufficiency.

## Changes Made

The PR created MONDO:1060214 with 12 additions to mondo-edit.obo: the term ID, label, definition referencing the gametogenic failure phenotype, ClinGen preferred label as exact synonym, logical definition (likely using the gene-related disease pattern linking to SYCE1), parent classification under gametogenic failure, and appropriate cross-references. The curator noted that child terms were not requested and would be handled by the reasoner.

## Resolution

Moderate difficulty because new term creation requires understanding of Mondo's DOSDP patterns, correct parent placement, and logical definition construction. The curator needed to craft a definition that captures the variable expressivity (both male and female presentations) and set up the logical axiom so the reasoner can infer additional classification. An agent would need knowledge of Mondo's term creation SOP and gene-disease patterns.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e49..d7a85ffe7b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665193,6 +665193,18 @@ is_a: MONDO:0006949 {source="PMID:29859199", source="https://orcid.org/0000-0001
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9849" xsd:anyURI
 
+[Term]
+id: MONDO:1060214
+name: SYCE1-related gametogenic failure
+def: "An infertility disorder caused by variation in the SYCE1 gene. Affected males may present with non-obstructive azoospermia due to maturation arrest or meiotic failure, while affected females may present with primary ovarian insufficiency." [https://clinicalgenome.org/affiliation/40073/, PMID:32402064, PMID:35718780]
+synonym: "SYCE1-related gametogenic failure" EXACT [https://clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005047 {source="https://clinicalgenome.org/affiliation/40073/"} ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="PMID:32402064", source="PMID:35718780", source="https://clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.560 | 0.636 | 0.500 | `26f35cc` | [#334](https://github.com/ai4curation/eval-ont-agent-mondo/pull/334) | [attempt](attempts/pr334.md) |
| 2 | claude-haiku-4.5 | claude | 0.545 | 0.545 | 0.545 | `c34a302` | [#603](https://github.com/ai4curation/eval-ont-agent-mondo/pull/603) | [attempt](attempts/pr603.md) |
| 3 | claude-haiku-4.5 | claude | 0.545 | 0.545 | 0.545 | `c34a302` | [#512](https://github.com/ai4curation/eval-ont-agent-mondo/pull/512) | [attempt](attempts/pr512.md) |
| 4 | gpt-5.5 | opencode | 0.545 | 0.545 | 0.545 | `d3e5461` | [#133](https://github.com/ai4curation/eval-ont-agent-mondo/pull/133) | [attempt](attempts/pr133.md) |
| 5 | gpt-5.5 | opencode | 0.545 | 0.545 | 0.545 | `d3e5461` | [#118](https://github.com/ai4curation/eval-ont-agent-mondo/pull/118) | [attempt](attempts/pr118.md) |
| 6 | claude-sonnet-4.5 | claude | 0.462 | 0.545 | 0.400 | `e400572` | [#454](https://github.com/ai4curation/eval-ont-agent-mondo/pull/454) | [attempt](attempts/pr454.md) |
| 7 | gpt-5.5 | codex | 0.455 | 0.455 | 0.455 | `7920413` | [#98](https://github.com/ai4curation/eval-ont-agent-mondo/pull/98) | [attempt](attempts/pr98.md) |
| 8 | gpt-5.4 | opencode | 0.435 | 0.455 | 0.417 | `c0ea8e5` | [#734](https://github.com/ai4curation/eval-ont-agent-mondo/pull/734) | [attempt](attempts/pr734.md) |
| 9 | gpt-5.4 | opencode | 0.435 | 0.455 | 0.417 | `c0ea8e5` | [#678](https://github.com/ai4curation/eval-ont-agent-mondo/pull/678) | [attempt](attempts/pr678.md) |
| 10 | gpt-5.4 | codex | 0.417 | 0.455 | 0.385 | `fdc4958` | [#172](https://github.com/ai4curation/eval-ont-agent-mondo/pull/172) | [attempt](attempts/pr172.md) |
| 11 | claude-opus-4.7 | claude | 0.381 | 0.364 | 0.400 | `4333d77` | [#374](https://github.com/ai4curation/eval-ont-agent-mondo/pull/374) | [attempt](attempts/pr374.md) |
| 12 | kimi-k2.6 | opencode | 0.348 | 0.364 | 0.333 | `017ace4` | [#279](https://github.com/ai4curation/eval-ont-agent-mondo/pull/279) | [attempt](attempts/pr279.md) |
