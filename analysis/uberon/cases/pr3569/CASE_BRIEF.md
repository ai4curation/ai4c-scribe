---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3457
pr_number: 3569
issue_title: Track the addition of VCCF vasculature terms here
pr_author: ar-ibrahim
pr_merged_at: '2025-07-03'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: vascular-anatomy
best_f1: 0.626
best_model: gpt-5.5
---

# PR #3569 — Track the addition of VCCF vasculature terms here

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3457](https://github.com/obophenotype/uberon/issues/3457) | [PR #3569](https://github.com/obophenotype/uberon/pull/3569) | @ar-ibrahim | merged 2025-07-03

`new_term` `medium` `tightly_scoped` `changes_requested`

## Context

Issue #3457 tracked the addition of vasculature terms from the Vasculature Common Coordinate Framework (VCCF) into Uberon. This was the fifth PR in a series (following PRs #3497, #3513, #3559, #3566) adding batches of arterial and venous terms. Seven new terms were added in this installment.

## Changes Made

The PR added four new entries to the artery_and_arteriole_pattern.tsv and three to the vein_and_venule_pattern.tsv DOSDP pattern data files. The definitions.owl file was updated with 106 new lines containing the generated logical definitions and annotations for the new vasculature terms, linking them to their anatomical regions via supplies/drains relationships.

## Resolution

Medium difficulty. An agent would need to understand the DOSDP (Dead Simple OWL Design Patterns) framework used for systematic vasculature term creation, populate the correct pattern data TSV files with appropriate anatomical region references, and ensure the generated OWL definitions are consistent with existing vasculature terms. The six commits and multi-PR series suggest iterative review feedback across the batch import effort.

## Human Diff

```diff
diff --git a/src/patterns/data/default/artery_and_arteriole_pattern.tsv b/src/patterns/data/default/artery_and_arteriole_pattern.tsv
index 99c0d40d4..673c706b3 100644
--- a/src/patterns/data/default/artery_and_arteriole_pattern.tsv
+++ b/src/patterns/data/default/artery_and_arteriole_pattern.tsv
@@ -54,3 +54,7 @@ UBERON:8920043	retroduodenal artery	FMA:61437	UBERON:0001637	UBERON:0000916	An a
 UBERON:8920044	supraduodenal artery	FMA:70438	UBERON:0001637	UBERON:0000916	An artery that branches from the gastroduodenal artery and supplies the superior, right, and anterior surfaces of the first part of the duodenum, extending into the second part.	https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/supraduodenal-artery/22976|wikipedia:Supraduodenal_artery			UBERON:0010132	UBERON:0002114	https://orcid.org/0000-0001-6757-4744	2025-06-16T09:40:19Z
 UBERON:8920045	right gastric artery	FMA:14776	UBERON:0001637	UBERON:0000916	An artery that branches from the proper hepatic artery and supplies the right side of the lesser curvature of the stomach and adjacent anterior and posterior surfaces.	wikipedia:Right_gastric_artery|https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/right-gastric-artery/19347			UBERON:0015480	UBERON:0001163	https://orcid.org/0000-0001-6757-4744	2025-06-16T09:40:19Z
 UBERON:8920046	short gastric artery	FMA:14794	UBERON:0001637	UBERON:0000916	An artery that branches from the splenic artery and supplies the fundus of the stomach on the side of the greater curvature of the stomach.	wikipedia:Short_gastric_arteries|https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/short-gastric-arteries/24632			UBERON:0001194	UBERON:0001160	https://orcid.org/0000-0001-6757-4744	2025-06-16T09:40:19Z
+UBERON:8920049	lobar artery of spleen		UBERON:0001637	UBERON:0000916	An artery that branches from the splenic artery at the splenic hilum at which it divides into one or two terminal branches supplying a lobe of the spleen.	PMID:26217091	splenic lobar artery	PMID:26217091	UBERON:0001194	UBERON:0002106	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
+UBERON:8920050	esophageal branches of left gastric artery	FMA:70431	UBERON:0001637	UBERON:0000916	An artery that branches from the left gastric artery and supplies the abdominal esophagus.	wikipedia:Esophageal_branches_of_left_gastric_artery|https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/esophageal-branches-of-left-gastric-artery/20285	Esophageal part of left gastric artery	FMA:70431	UBERON:0001192	UBERON:0001043	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
+UBERON:8920051	posterior scrotal artery	FMA:20853	UBERON:0001637	UBERON:0002355	An artery that branches from the internal pudendal artery and supplies the scrotum.	wikipedia:Posterior_scrotal_arteries			UBERON:0007315	UBERON:0001300	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
+UBERON:8920052	vaginal artery	FMA:18832	UBERON:0001637	UBERON:0002355	An artery that branches from the internal iliac artery and supplies the lower vagina and fundus of the bladder.	wikipedia:Vaginal_artery|https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/vaginal-artery-right/20364			UBERON:0001309	UBERON:0000996|UBERON:0006082	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
diff --git a/src/patterns/data/default/vein_and_venule_pattern.tsv b/src/patterns/data/default/vein_and_venule_pattern.tsv
index 2de6d4c8c..c22cb302e 100644
--- a/src/patterns/data/default/vein_and_venule_pattern.tsv
+++ b/src/patterns/data/default/vein_and_venule_pattern.tsv
@@ -53,3 +53,6 @@ UBERON:8920030	anterior inferior pancreaticoduodenal vein		UBERON:0011383	UBERON
 UBERON:8920031	posterior inferior pancreaticoduodenal vein		UBERON:0011383	UBERON:0000916	A vein that is a tributary of the superior mesenteric vein. It drains the dorsal surface of the second and third portion of the duodenum and the dorsal surface of the head and uncinate process of the pancreas.	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/posterior-inferior-pancreaticoduodenal-vein/16750|ISBN:0702052302				UBERON:0001138		UBERON:0002114|UBERON:0001069|UBERON:0010373	https://orcid.org/0000-0001-6757-4744	2025-05-14T14:34:54Z
 UBERON:8920047	left gastroepiploic vein	FMA:15390	UBERON:0001638	UBERON:0000916	A vein that is a tributary of the splenic vein and drains the anterior and posterior body of the stomach and greater omentum.	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/left-gastroomental-vein/16519|wikipedia:Left_gastroepiploic_vein	Left gastro-omental vein	FMA:15390		UBERON:0003713		UBERON:0001161|UBERON:0005448	https://orcid.org/0000-0001-6757-4744	2025-06-16T09:40:19Z
 UBERON:8920048	right gastroepiploic vein	FMA:15397	UBERON:0001638	UBERON:0000916	A vein that is a tributary of the superior mesenteric vein and drains the greater omentum and distal body and antrum of the stomach.	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/right-gastroomental-vein/21003|https://en.wikipedia.org/wiki/Right_gastroepiploic_vein	Right gastroepiploic vein	FMA:15397		UBERON:0001138		UBERON:0001161|UBERON:0005448|UBERON:0001165	https://orcid.org/0000-0001-6757-4744	2025-06-16T09:40:19Z
+UBERON:8920053	superior rectal vein	FMA:15393	UBERON:0001638	UBERON:0002355	A vein that is a tributary of the inferior mesenteric vein and drains the upper two thirds of the rectum and upper anal canal.	wikipedia:Superior_rectal_vein|https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/superior-anorectal-vein/24829	Superior Anorectal Vein	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/superior-anorectal-vein/24829		UBERON:0001215		UBERON:0001052|UBERON:0000159	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
+UBERON:8920054	inferior rectal vein	FMA:21242	UBERON:0001638	UBERON:0002355	A vein that is a tributary of the internal pudendal vein and drains the lower third of the rectum and anal canal.	wikipedia:Inferior_rectal_veins|https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/inferior-anorectal-veins/18814	Inferior Anorectal Veins	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/inferior-anorectal-veins/18814		UBERON:0018252		UBERON:0001052|UBERON:0000159	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
+UBERON:8920055	posterior scrotal vein	FMA:21254	UBERON:0001638	UBERON:0002355	A vein that is a tributary of the internal pudendal vein and drains the skin and fascial layers of the posterior scrotum.	https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/posterior-scrotal-veins-left/25245				UBERON:0018252		UBERON:0001300	https://orcid.org/0000-0001-6757-4744	2025-06-23T11:57:25Z
diff --git a/src/patterns/definitions.owl b/src/patterns/definitions.owl
index c05827054..b7e402b10 100644
--- a/src/patterns/definitions.owl
+++ b/src/patterns/definitions.owl
@@ -7,13 +7,14 @@ Prefix(rdfs:=<http://www.w3.org/2000/01/rdf-schema#>)
 
 
 Ontology(<http://purl.obolibrary.org/obo/uberon/patterns/definitions.owl>
-<http://purl.obolibrary.org/obo/uberon/releases/2025-06-26/patterns/definitions.owl>
-Annotation(owl:versionInfo "2025-06-26")
+<http://purl.obolibrary.org/obo/uberon/releases/2025-06-30/patterns/definitions.owl>
+Annotation(owl:versionInfo "2025-06-30")
 
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000004>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000007>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000033>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000117>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000159>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000388>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000915>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000916>))
@@ -23,6 +24,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000974>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000976>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000985>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000995>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0000996>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001043>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001052>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001069>))
@@ -49,12 +51,16 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001163>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001165>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001174>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001184>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001192>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001194>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001195>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001197>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001215>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001225>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001264>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001281>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001300>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001309>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001310>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001312>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0001317>))
@@ -113,6 +119,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002080>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002084>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002094>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002103>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002106>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002107>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002113>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0002114>))
@@ -150,6 +157,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0005168>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0005448>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0005462>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0005616>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006082>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006533>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006562>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006634>))
@@ -157,6 +165,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006665>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006801>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0006958>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0007157>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0007315>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008200>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008874>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0008952>))
@@ -189,6 +198,7 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0016405>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0016454>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0016455>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0017717>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0018252>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0018561>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0018562>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_0018568>))
@@ -379,6 +389,13 @@ Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920045>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920046>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920047>))
 Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920048>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920049>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920050>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920051>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920052>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920053>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920054>))
+Declaration(Class(<http://purl.obolibrary.org/obo/UBERON_8920055>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/BFO_0000050>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/BSPO_0000120>))
 Declaration(ObjectProperty(<http://purl.obolibrary.org/obo/BSPO_0000121>))
@@ -2332,5 +2349,92 @@ SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920048> ObjectIntersectionOf(
 SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920048> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0000916>))
 SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920048> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002376> <http://purl.obolibrary.org/obo/UBERON_0001138>))
 
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920049> (lobar artery of spleen)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PMID:26217091") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920049> "An artery that branches from the splenic artery at the splenic hilum at which it divides into one or two terminal branches supplying a lobe of the spleen.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920049> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920049> "2025-06-23T11:57:25Z")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PMID:26217091") <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/UBERON_8920049> "splenic lobar artery")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920049> "lobar artery of spleen")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920049> <http://purl.obolibrary.org/obo/UBERON_0001637>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920049> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0000916>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920049> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002252> <http://purl.obolibrary.org/obo/UBERON_0001194>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920049> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020101> <http://purl.obolibrary.org/obo/UBERON_0002106>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920050> (esophageal branches of left gastric artery)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/esophageal-branches-of-left-gastric-artery/20285") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "wikipedia:Esophageal_branches_of_left_gastric_artery") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920050> "An artery that branches from the left gastric artery and supplies the abdominal esophagus.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920050> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920050> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920050> "FMA:70431")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "FMA:70431") <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/UBERON_8920050> "Esophageal part of left gastric artery")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920050> "esophageal branches of left gastric artery")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920050> <http://purl.obolibrary.org/obo/UBERON_0001637>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920050> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0000916>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920050> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002252> <http://purl.obolibrary.org/obo/UBERON_0001192>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920050> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020101> <http://purl.obolibrary.org/obo/UBERON_0001043>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920051> (posterior scrotal artery)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "wikipedia:Posterior_scrotal_arteries") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920051> "An artery that branches from the internal pudendal artery and supplies the scrotum.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920051> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920051> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920051> "FMA:20853")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920051> "posterior scrotal artery")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920051> <http://purl.obolibrary.org/obo/UBERON_0001637>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920051> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0002355>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920051> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002252> <http://purl.obolibrary.org/obo/UBERON_0007315>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920051> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020101> <http://purl.obolibrary.org/obo/UBERON_0001300>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920052> (vaginal artery)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/vaginal-artery-right/20364") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "wikipedia:Vaginal_artery") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920052> "An artery that branches from the internal iliac artery and supplies the lower vagina and fundus of the bladder.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920052> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920052> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920052> "FMA:18832")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920052> "vaginal artery")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920052> <http://purl.obolibrary.org/obo/UBERON_0001637>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920052> ObjectIntersectionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020101> <http://purl.obolibrary.org/obo/UBERON_0000996>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020101> <http://purl.obolibrary.org/obo/UBERON_0006082>)))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920052> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0002355>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920052> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002252> <http://purl.obolibrary.org/obo/UBERON_0001309>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920053> (superior rectal vein)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/superior-anorectal-vein/24829") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "wikipedia:Superior_rectal_vein") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920053> "A vein that is a tributary of the inferior mesenteric vein and drains the upper two thirds of the rectum and upper anal canal.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920053> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920053> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920053> "FMA:15393")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/superior-anorectal-vein/24829") <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/UBERON_8920053> "Superior Anorectal Vein")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920053> "superior rectal vein")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920053> <http://purl.obolibrary.org/obo/UBERON_0001638>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920053> ObjectIntersectionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020102> <http://purl.obolibrary.org/obo/UBERON_0000159>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020102> <http://purl.obolibrary.org/obo/UBERON_0001052>)))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920053> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0002355>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920053> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002376> <http://purl.obolibrary.org/obo/UBERON_0001215>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920054> (inferior rectal vein)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/inferior-anorectal-veins/18814") Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "wikipedia:Inferior_rectal_veins") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920054> "A vein that is a tributary of the internal pudendal vein and drains the lower third of the rectum and anal canal.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920054> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920054> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920054> "FMA:21242")
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/inferior-anorectal-veins/18814") <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> <http://purl.obolibrary.org/obo/UBERON_8920054> "Inferior Anorectal Veins")
+AnnotationAssertion(rdfs:label <http://purl.obolibrary.org/obo/UBERON_8920054> "inferior rectal vein")
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920054> <http://purl.obolibrary.org/obo/UBERON_0001638>)
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920054> ObjectIntersectionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020102> <http://purl.obolibrary.org/obo/UBERON_0000159>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0020102> <http://purl.obolibrary.org/obo/UBERON_0001052>)))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920054> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/UBERON_0002355>))
+SubClassOf(<http://purl.obolibrary.org/obo/UBERON_8920054> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002376> <http://purl.obolibrary.org/obo/UBERON_0018252>))
+
+# Class: <http://purl.obolibrary.org/obo/UBERON_8920055> (posterior scrotal vein)
+
+AnnotationAssertion(Annotation(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> "https://www.elsevier.com/resources/anatomy/cardiovascular-system/veins/posterior-scrotal-veins-left/25245") <http://purl.obolibrary.org/obo/IAO_0000115> <http://purl.obolibrary.org/obo/UBERON_8920055> "A vein that is a tributary of the internal pudendal vein and drains the skin and fascial layers of the posterior scrotum.")
+AnnotationAssertion(<http://purl.org/dc/terms/contributor> <http://purl.obolibrary.org/obo/UBERON_8920055> <https://orcid.org/0000-0001-6757-4744>)
+AnnotationAssertion(<http://purl.org/dc/terms/date> <http://purl.obolibrary.org/obo/UBERON_8920055> "2025-06-23T11:57:25Z")
+AnnotationAssertion(<http://www.geneontology.org/formats/oboInOwl#hasDbXref> <http://purl.obolibrary.org/obo/UBERON_8920055> "FMA:21254")
... (10 more lines truncated)
```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.626 | 0.604 | 0.649 | [#34](https://github.com/ai4curation/eval-ont-agent-uberon/pull/34) | [attempt](attempts/pr34.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#323](https://github.com/ai4curation/eval-ont-agent-uberon/pull/323) | [attempt](attempts/pr323.md) |
| 3 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#253](https://github.com/ai4curation/eval-ont-agent-uberon/pull/253) | [attempt](attempts/pr253.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#189](https://github.com/ai4curation/eval-ont-agent-uberon/pull/189) | [attempt](attempts/pr189.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#93](https://github.com/ai4curation/eval-ont-agent-uberon/pull/93) | [attempt](attempts/pr93.md) |
| 6 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#71](https://github.com/ai4curation/eval-ont-agent-uberon/pull/71) | [attempt](attempts/pr71.md) |
| 7 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | [#54](https://github.com/ai4curation/eval-ont-agent-uberon/pull/54) | [attempt](attempts/pr54.md) |
