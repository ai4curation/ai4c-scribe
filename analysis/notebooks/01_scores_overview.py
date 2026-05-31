"""Scores overview analysis for the ontology agent evaluation paper.

Quality-aware. A central methodological finding is that ~half the
curated cases turned out to be unsuitable for automatic scoring
(mis-paired gold, gold leakage, eval-base contamination); these are
flagged ``case_quality: poor`` and summarised FIRST. All agent
comparisons are then restricted to the CLEAR (non-poor) cases, and use
two complementary measures: the metadiff F1 and the reviewer ``outcome``
verdict (the latter is robust where the gold is flawed). Run:

    uv run python analysis/notebooks/01_scores_overview.py > \\
        analysis/notebooks/scores_overview.html
"""

from pathlib import Path

import pandas as pd

from ai4c_scribe.analysis import (
    attach_case_quality,
    failure_mode_counts,
    load_reviews,
    load_scores,
    outcome_distribution,
    pivot_scores,
    reviewer_score,
    rubric_summary,
    summary_by_model,
    summary_by_runtime,
)

STD_AGENTS = [
    "std_claude_op47",
    "std_claude_son45",
    "std_claude_hai45",
    "std_codex_g54",
    "std_opencode_g55",
    "std_opencode_g54",
]

# load_scores() remaps `agent` to short analysis codes (e.g. CC.op47.v3);
# keep the resolved logical handle (std_*) from the raw TSV for coverage.
_scores_path = Path("analysis/scores.tsv")
df = attach_case_quality(load_scores(_scores_path))
df["agent_handle"] = pd.read_csv(_scores_path, sep="\t")["agent"].values
reviews = attach_case_quality(load_reviews())

valid = df[df["case_quality"] != "poor"].copy()
poor = df[df["case_quality"] == "poor"].copy()
valid_reviews = reviews[reviews["case_quality"] != "poor"].copy()

n_cases = df["case"].nunique()
n_valid_cases = valid["case"].nunique()
n_poor_cases = poor["case"].nunique()

print("# Ontology Agent Evaluation — Scores Overview")

# =====================================================================
# Section 0 (FIRST): Case suitability — the headline caveat
# =====================================================================
print("\n## 0. Case Suitability (read this first)\n")
print(
    f"<p>Of <b>{n_cases}</b> curated issue/PR cases, <b>{n_poor_cases}</b> "
    f"({n_poor_cases / n_cases:.0%}) were found <b>unsuitable for automatic "
    f"scoring</b> and are flagged <code>case_quality: poor</code>. They are "
    f"excluded from every comparison below. Only the <b>{n_valid_cases} "
    f"clear cases</b> are used. This is a substantive methodological result: "
    "metadiff F1 against a single gold PR is only meaningful when that PR is "
    "the correct, complete, leak-free resolution of the issue — often it is "
    "not (the issue is split across companion PRs, the gold leaked into the "
    "eval base, or the linked PR does not resolve the stated issue).</p>"
)

case_q = (
    df.drop_duplicates("case")
    .groupby(["ontology", "case_quality"])
    .size()
    .unstack(fill_value=0)
)
print("\n### Case quality by ontology\n")
print(case_q.to_html())

if len(poor):
    reason = (
        poor.drop_duplicates("case")["case_quality_reason"]
        .fillna("(unspecified)")
        .value_counts()
    )
    print("\n### Why cases were ruled unsuitable (poor-case reasons)\n")
    print(reason.to_frame("cases").to_html())

    print("\n### Excluded poor cases & scoring caveats\n")
    pc = poor.drop_duplicates("case")[
        ["ontology", "issue_number", "case_quality_reason", "scoring_caveat"]
    ].sort_values(["ontology", "issue_number"])
    print(pc.to_html(index=False))

# =====================================================================
# Section 1: Coverage of the target agents over CLEAR cases
# =====================================================================
print("\n## 1. Coverage over clear cases\n")
valid_cases_by_ont = valid.groupby("ontology")["case"].nunique()
cov_rows = []
for agent in STD_AGENTS:
    row = {"agent": agent}
    for ont, n_total in valid_cases_by_ont.items():
        n_have = valid[(valid["agent_handle"] == agent) & (valid["ontology"] == ont)][
            "case"
        ].nunique()
        row[ont] = f"{n_have}/{n_total}"
    cov_rows.append(row)
print(pd.DataFrame(cov_rows).set_index("agent").to_html())

# =====================================================================
# Section 2: Headline performance on CLEAR cases — two measures
# =====================================================================
print("\n## 2. Performance on clear cases\n")
print("\n### 2a. Metadiff F1 by model (clear cases)\n")
print(summary_by_model(valid).to_html())
print("\n### Metadiff F1 by runtime (clear cases)\n")
print(summary_by_runtime(valid).to_html())
print(
    "\n<p><i>Sensitivity — F1 by model over ALL cases incl. poor "
    "(do not use for conclusions; shown to demonstrate the distortion):</i>"
    "</p>\n"
)
print(summary_by_model(df).to_html())

print(
    "\n### 2b. Reviewer outcome score (clear cases)\n"
    "<p>Reviewer verdict mapped success=1.0, partial_success=0.5, "
    "failure/no_output=0.0. Robust where F1 is not (a reviewer can credit "
    "an agent that correctly resolved a flawed-gold issue). The free-text "
    "<code>agent</code> field in review files is unreliable (reviewers wrote "
    "62 variant labels), so the canonical agent is recovered by joining each "
    "review to the scored run on (ontology, eval_repo_pr).</p>\n"
)
# Recover the canonical resolved agent per reviewed PR from the scores.
_pr_agent = (
    df.dropna(subset=["eval_repo_pr"])
    .assign(eval_repo_pr=lambda x: x["eval_repo_pr"].astype("Int64"))
    .drop_duplicates(["ontology", "eval_repo_pr"])
    .set_index(["ontology", "eval_repo_pr"])["agent_handle"]
)
vr2 = valid_reviews.copy()
if "eval_repo_pr" in vr2.columns:
    vr2["eval_repo_pr"] = pd.to_numeric(vr2["eval_repo_pr"], errors="coerce").astype(
        "Int64"
    )
    vr2["canonical_agent"] = vr2.set_index(["ontology", "eval_repo_pr"]).index.map(
        _pr_agent
    )
ag_rs = reviewer_score(vr2[vr2.get("canonical_agent").notna()], by="canonical_agent")
if len(ag_rs):
    print("\n#### By agent (canonical, joined from scores)\n")
    print(ag_rs.sort_values("mean_score", ascending=False).to_html())
print("\n#### By runtime\n")
rt_rs = reviewer_score(valid_reviews, by="runtime")
if len(rt_rs):
    print(rt_rs.sort_values("mean_score", ascending=False).to_html())

# =====================================================================
# Section 3: Pivots / ablation (clear cases)
# =====================================================================
print("\n## 3. Slices (clear cases)\n")
print("\n### Mean F1: Ontology x Model\n")
print(pivot_scores(valid, rows="ontology", cols="model").to_html(na_rep="—"))
print("\n### Mean F1: Difficulty x Model\n")
print(pivot_scores(valid, rows="difficulty", cols="model").to_html(na_rep="—"))
print("\n### Mean F1: Task Type x Runtime\n")
print(pivot_scores(valid, rows="case_type", cols="runtime").to_html(na_rep="—"))

ablation = valid[
    valid["agent_config_tag"].isin(
        ["v8", "v8-noskills", "v9", "v2", "v2-noskills", "v3"]
    )
]
print("\n### Skills Ablation\n")
print(
    pivot_scores(ablation, rows="agent_config_tag", cols="runtime").to_html(na_rep="—")
)

# =====================================================================
# Section 4: Qualitative reviews detail
# =====================================================================
if len(valid_reviews):
    print("\n## 4. Qualitative Reviews (clear cases)\n")
    n_scored = (
        valid_reviews["outcome"].notna().sum() if "outcome" in valid_reviews else 0
    )
    print(
        f"<p>{len(valid_reviews)} review files on clear cases "
        f"({n_scored} with an outcome verdict).</p>\n"
    )
    if "_file" in valid_reviews.columns:
        vr = valid_reviews.copy()
        vr["reviewer"] = vr["_file"].str.extract(r"-([a-z]+)-(?:complete|stub)\.md$")
        print("\n### Reviews by ontology and reviewer\n")
        print(pd.crosstab(vr["ontology"], vr["reviewer"].fillna("?")).to_html())

    print("\n### Outcome distribution by model\n")
    od = outcome_distribution(valid_reviews)
    if od is not None:
        print(od.to_html())

    print("\n### Failure modes (frequency across clear-case reviews)\n")
    fm = failure_mode_counts(valid_reviews)
    if fm is not None:
        print(fm.to_frame("count").to_html())

    rs = rubric_summary(valid_reviews)
    if rs is not None and len(rs):
        print("\n### 1-5 rubric (only a few reviews carry this)\n")
        print(rs.to_html())

# =====================================================================
# Section 5: All clear-case scored runs
# =====================================================================
print("\n## 5. All clear-case scored runs\n")
cols = [
    "ontology",
    "issue_number",
    "case_type",
    "difficulty",
    "agent",
    "model",
    "runtime",
    "f1",
    "precision",
    "recall",
]
print(
    valid[cols]
    .sort_values(["ontology", "issue_number", "model"])
    .to_html(index=False, float_format="%.3f")
)
