"""Generate a static HTML gallery browser for evaluation case studies.

Walks an analysis directory tree containing case study METADATA.md files,
human/agent diffs, scores TSV, and review files. Produces a single
self-contained HTML file for browsing cases in a sidebar + detail layout.
"""

import csv
import json
import re
import subprocess
from pathlib import Path

import yaml


def _parse_frontmatter_and_body(text: str) -> tuple[dict, str]:
    """Split markdown into YAML frontmatter dict and body string.

    >>> fm, body = _parse_frontmatter_and_body("---\\nk: v\\n---\\nHello\\n")
    >>> fm
    {'k': 'v'}
    >>> body.strip()
    'Hello'
    """
    parts = text.split("---", 2)
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2] if len(parts) > 2 else ""
    return frontmatter, body


def _load_scores(scores_path: Path) -> list[dict]:
    """Load scores.tsv into a list of dicts.

    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.tsv', delete=False) as f:
    ...     _ = f.write("ontology\\tpr_number\\teval_repo_pr\\tf1\\n")
    ...     _ = f.write("ont1\\t100\\t10\\t0.8\\n")
    >>> rows = _load_scores(Path(f.name))
    >>> rows[0]['pr_number']
    '100'
    >>> os.unlink(f.name)
    """
    with open(scores_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def _discover_ontologies(analysis_dir: Path) -> list[str]:
    """Find subdirectories that contain a cases/ folder.

    >>> import tempfile
    >>> with tempfile.TemporaryDirectory() as tmp:
    ...     (Path(tmp) / "ont1" / "cases").mkdir(parents=True)
    ...     (Path(tmp) / "ont2" / "cases").mkdir(parents=True)
    ...     (Path(tmp) / "scripts").mkdir()
    ...     sorted(_discover_ontologies(Path(tmp)))
    ['ont1', 'ont2']
    """
    return sorted(
        d.name for d in analysis_dir.iterdir()
        if d.is_dir() and (d / "cases").is_dir()
    )


from typing import Optional


def _truncate_diff(text: Optional[str], max_lines: int) -> Optional[str]:
    """Truncate a diff to *max_lines* lines, appending a notice if trimmed.

    >>> _truncate_diff(None, 10) is None
    True
    >>> _truncate_diff("a\\nb\\nc", 2)
    'a\\nb\\n... (1 more lines truncated)'
    >>> _truncate_diff("a\\nb", 5)
    'a\\nb'
    """
    if text is None or max_lines <= 0:
        return text
    lines = text.split("\n")
    if len(lines) <= max_lines:
        return text
    truncated = "\n".join(lines[:max_lines])
    remaining = len(lines) - max_lines
    return f"{truncated}\n... ({remaining} more lines truncated)"


def _parse_eval_pr_body(body: str) -> dict:
    """Extract structured sections from an eval repo PR body.

    >>> d = _parse_eval_pr_body("foo\\n## Agent Response - PR Comments\\nHello world\\n## Agent Response - Issue Comments\\nBye")
    >>> d["pr_comment"]
    'Hello world'
    >>> d["issue_comment"]
    'Bye'
    """
    result: dict = {"pr_comment": None, "issue_comment": None,
                    "workflow_run": None, "trace_url": None}
    # Extract agent PR comment section
    m = re.search(
        r"## Agent Response - PR Comments\n(.*?)(?=\n## |\Z)",
        body, re.DOTALL,
    )
    if m:
        result["pr_comment"] = m.group(1).strip()
    # Extract agent issue comment section
    m = re.search(
        r"## Agent Response - Issue Comments\n(.*?)(?=\n## |\Z)",
        body, re.DOTALL,
    )
    if m:
        result["issue_comment"] = m.group(1).strip()
    # Extract workflow run URL
    runs = re.findall(r"actions/runs/(\d+)\)", body)
    if runs:
        result["workflow_run"] = runs[0]
    return result


def _parse_trace_from_comments(comments: list[dict]) -> Optional[str]:
    """Extract trace URL from PR comments.

    >>> _parse_trace_from_comments([{"body": "Traces: [traces/123](https://github.com/org/repo/tree/master/traces/123)"}])
    'https://github.com/org/repo/tree/master/traces/123'
    """
    for c in comments:
        m = re.search(r"\[traces/\d+\]\((https://[^)]+)\)", c.get("body", ""))
        if m:
            return m.group(1)
    return None


def _fetch_trace_file(eval_repo: str, run_id: str, filename: str) -> Optional[str]:
    """Fetch a file from the traces directory on master via gh API."""
    result = subprocess.run(
        ["gh", "api",
         f"repos/ai4curation/{eval_repo}/contents/traces/{run_id}/{filename}",
         "--jq", ".content"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    import base64
    return base64.b64decode(result.stdout.strip()).decode("utf-8", errors="replace")


def fetch_eval_pr_data(
    eval_repo: str,
    eval_repo_pr: int,
    cache_dir: Path,
) -> Optional[dict]:
    """Fetch eval PR body+comments via gh CLI and cache the parsed result.

    Returns cached data if available. On fetch, parses the PR body into
    structured sections (agent PR comment, issue comment, workflow run,
    trace URL). Also fetches PR_COMMENTS.md and ISSUE_COMMENTS.md from
    the traces directory when available.
    """
    cache_path = cache_dir / f"pr{eval_repo_pr}.json"
    if cache_path.exists():
        return json.loads(cache_path.read_text())

    full_repo = f"ai4curation/{eval_repo}"
    result = subprocess.run(
        ["gh", "pr", "view", str(eval_repo_pr), "--repo", full_repo,
         "--json", "body,comments,url"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None

    raw = json.loads(result.stdout)
    parsed = _parse_eval_pr_body(raw.get("body", ""))
    parsed["eval_pr_url"] = raw.get("url", "")
    trace_url = _parse_trace_from_comments(raw.get("comments", []))
    if trace_url:
        parsed["trace_url"] = trace_url

    # Fetch trace files (PR_COMMENTS.md, ISSUE_COMMENTS.md) if we have a run ID
    run_id = parsed.get("workflow_run")
    if run_id:
        pr_comments_md = _fetch_trace_file(eval_repo, run_id, "PR_COMMENTS.md")
        if pr_comments_md:
            parsed["pr_comment"] = pr_comments_md
        issue_comments_md = _fetch_trace_file(eval_repo, run_id, "ISSUE_COMMENTS.md")
        if issue_comments_md:
            parsed["issue_comment"] = issue_comments_md

    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(parsed, indent=2))
    return parsed


def fetch_all_eval_pr_data(analysis_dir: Path, *, force: bool = False) -> int:
    """Fetch and cache eval PR data for all scored runs.

    Args:
        analysis_dir: Analysis directory.
        force: Re-fetch even if cached.

    Returns the number of PRs fetched.
    """
    eval_repos: dict[str, str] = {}
    try:
        from ai4c_scribe.scoring import EVAL_REPOS
        for ont, cfg in EVAL_REPOS.items():
            eval_repos[ont] = cfg["eval_repo"]
    except ImportError:
        return 0

    fetched = 0
    for ont_name in _discover_ontologies(analysis_dir):
        if ont_name not in eval_repos:
            continue
        scores_path = analysis_dir / ont_name / "results" / "scores.tsv"
        if not scores_path.exists():
            continue
        cache_dir = analysis_dir / ont_name / "results" / "pr_data"
        for row in _load_scores(scores_path):
            eval_pr = int(row["eval_repo_pr"])
            cache_path = cache_dir / f"pr{eval_pr}.json"
            if cache_path.exists() and not force:
                continue
            if force and cache_path.exists():
                cache_path.unlink()
            result = fetch_eval_pr_data(eval_repos[ont_name], eval_pr, cache_dir)
            if result:
                fetched += 1
    return fetched


def collect_gallery_data(analysis_dir: Path, *, max_diff_lines: int = 200) -> dict:
    """Walk the analysis directory and assemble gallery data.

    Args:
        analysis_dir: Path containing ``{ont}/cases/`` and optionally
            ``{ont}/results/`` subdirectories.
        max_diff_lines: Maximum lines per diff to embed. 0 for unlimited.

    Returns:
        Dict with ``ontologies`` key mapping ontology names to their cases,
        each case containing metadata, narrative, diffs, and agent attempts.
    """
    ontologies: dict[str, dict] = {}

    for ont_name in _discover_ontologies(analysis_dir):
        ont_dir = analysis_dir / ont_name
        cases_dir = ont_dir / "cases"
        results_dir = ont_dir / "results"

        # Load scores.tsv if it exists — keyed by (pr_number -> list of attempts)
        scores_by_pr: dict[int, list[dict]] = {}
        scores_path = results_dir / "scores.tsv"
        if scores_path.exists():
            for row in _load_scores(scores_path):
                pr_num = int(row["pr_number"])
                scores_by_pr.setdefault(pr_num, []).append(row)

        # Load each case
        cases = []
        for case_dir in sorted(cases_dir.iterdir()):
            metadata_path = case_dir / "METADATA.md"
            if not metadata_path.exists():
                continue

            text = metadata_path.read_text()
            frontmatter, body = _parse_frontmatter_and_body(text)
            pr_number = int(frontmatter["pr_number"])

            # Human diff
            human_diff_path = results_dir / "diffs" / "human" / f"pr{pr_number}.diff"
            human_diff = _truncate_diff(
                human_diff_path.read_text() if human_diff_path.exists() else None,
                max_diff_lines,
            )

            # Agent attempts — joined via scores.tsv
            agent_attempts = []
            for score_row in scores_by_pr.get(pr_number, []):
                eval_pr = int(score_row["eval_repo_pr"])

                # Agent diff
                agent_diff_path = results_dir / "diffs" / "agent" / f"pr{eval_pr}.diff"
                agent_diff = _truncate_diff(
                    agent_diff_path.read_text() if agent_diff_path.exists() else None,
                    max_diff_lines,
                )

                # Review files — collect ALL matching pr{eval_pr}-*.md
                reviews: list[dict] = []
                reviews_dir = results_dir / "reviews"
                if reviews_dir.exists():
                    for review_path in sorted(reviews_dir.glob(f"pr{eval_pr}-*.md")):
                        raw = review_path.read_text()
                        rfm, rbody = _parse_frontmatter_and_body(raw)
                        # Serialize dates in review frontmatter
                        for k in list(rfm.keys()):
                            if hasattr(rfm[k], "isoformat"):
                                rfm[k] = rfm[k].isoformat()
                        reviews.append({
                            "filename": review_path.name,
                            "frontmatter": rfm,
                            "body_md": rbody,
                        })

                # Cached eval PR data (agent comments, trace, workflow run)
                pr_data_path = results_dir / "pr_data" / f"pr{eval_pr}.json"
                pr_data = json.loads(pr_data_path.read_text()) if pr_data_path.exists() else {}

                agent_attempts.append({
                    "eval_repo_pr": eval_pr,
                    "model": score_row.get("model", ""),
                    "runtime": score_row.get("runtime", ""),
                    "agent_config_tag": score_row.get("agent_config_tag", ""),
                    "agent": score_row.get("agent", ""),
                    "f1": float(score_row.get("f1", 0)),
                    "precision": float(score_row.get("precision", 0)),
                    "recall": float(score_row.get("recall", 0)),
                    "jaccard": float(score_row.get("jaccard", 0)),
                    "diff": agent_diff,
                    "reviews": reviews,
                    "pr_comment": pr_data.get("pr_comment"),
                    "issue_comment": pr_data.get("issue_comment"),
                    "trace_url": pr_data.get("trace_url"),
                    "workflow_run": pr_data.get("workflow_run"),
                })

            # Serialize dates to strings for JSON
            metadata = dict(frontmatter)
            for key in ("issue_created_at", "pr_merged_at", "curated_at",
                        "issue_closed_at"):
                if key in metadata and hasattr(metadata[key], "isoformat"):
                    metadata[key] = metadata[key].isoformat()

            cases.append({
                "pr_number": pr_number,
                "case_dir": case_dir.name,
                "ontology": ont_name,
                "metadata": metadata,
                "narrative_md": body,
                "human_diff": human_diff,
                "agent_attempts": agent_attempts,
            })

        ontologies[ont_name] = {"cases": cases}

    # Include eval repo config for constructing GitHub links
    eval_repos: dict[str, dict] = {}
    try:
        from ai4c_scribe.scoring import EVAL_REPOS
        for ont, cfg in EVAL_REPOS.items():
            eval_repos[ont] = {
                "eval_repo": cfg.get("eval_repo", ""),
                "source_repo": cfg.get("source_repo", ""),
            }
    except ImportError:
        pass

    return {"ontologies": ontologies, "eval_repos": eval_repos}


def format_case_brief(case: dict, eval_repos: dict) -> str:
    """Format a single case dict as a markdown case brief.

    The brief includes YAML frontmatter with all metadata, followed by
    a human-readable markdown body with narrative, diffs, and attempts.

    Args:
        case: A case dict from ``collect_gallery_data()``.
        eval_repos: The ``eval_repos`` dict from gallery data.

    Returns:
        Markdown string with YAML frontmatter.
    """
    from datetime import date as date_type

    m = case["metadata"]
    ont = case["ontology"]
    repo = m.get("repo", "")
    pr_num = case["pr_number"]
    issue_num = m.get("issue_number", "")
    eval_cfg = eval_repos.get(ont, {})

    # Build frontmatter
    fm: dict = {
        "ontology": ont,
        "repo": repo,
        "issue_number": issue_num,
        "pr_number": pr_num,
        "issue_title": m.get("issue_title", ""),
        "pr_author": m.get("pr_author", ""),
        "pr_merged_at": m.get("pr_merged_at"),
        "task_type": m.get("task_type"),
        "difficulty": m.get("difficulty"),
        "scoping": m.get("scoping"),
        "scope": m.get("scope"),
        "review_outcome": m.get("review_outcome"),
        "num_agent_attempts": len(case.get("agent_attempts", [])),
        "generated_at": date_type.today().isoformat(),
    }
    # Optional fields
    for field in ("eval_suitability", "eval_suitability_notes",
                   "diff_noise", "diff_noise_notes",
                   "scoping_notes", "domain_area"):
        val = m.get(field)
        if val:
            fm[field] = val
    # Agent summary
    attempts = case.get("agent_attempts", [])
    if attempts:
        best = max(attempts, key=lambda a: a.get("f1", 0))
        fm["best_f1"] = round(best["f1"], 3)
        fm["best_model"] = best.get("model", "")

    fm_yaml = yaml.dump(fm, default_flow_style=False, sort_keys=False, allow_unicode=True).strip()

    lines = []
    lines.append("---")
    lines.append(fm_yaml)
    lines.append("---")
    lines.append("")
    lines.append(f"# PR #{pr_num} — {m.get('issue_title', '')}")
    lines.append("")
    lines.append(f"**{ont}** | [{repo}](https://github.com/{repo}) | "
                 f"[Issue #{issue_num}](https://github.com/{repo}/issues/{issue_num}) | "
                 f"[PR #{pr_num}](https://github.com/{repo}/pull/{pr_num}) | "
                 f"@{m.get('pr_author', '')} | merged {m.get('pr_merged_at', '?')}")
    lines.append("")
    badge_fields = ["task_type", "difficulty", "scoping", "review_outcome",
                    "eval_suitability", "diff_noise"]
    badges = [f"`{m[f]}`" for f in badge_fields if m.get(f)]
    if badges:
        lines.append(" ".join(badges))
        lines.append("")

    # Narrative
    narrative = case.get("narrative_md", "").strip()
    if narrative:
        lines.append(narrative)
        lines.append("")

    # Human diff
    human_diff = case.get("human_diff")
    if human_diff:
        lines.append("## Human Diff")
        lines.append("")
        lines.append("```diff")
        lines.append(human_diff)
        lines.append("```")
        lines.append("")

    # Agent attempts
    attempts = case.get("agent_attempts", [])
    if attempts:
        lines.append(f"## Agent Attempts ({len(attempts)})")
        lines.append("")
        sorted_attempts = sorted(attempts, key=lambda a: a.get("f1", 0), reverse=True)
        for i, a in enumerate(sorted_attempts, 1):
            eval_pr = a.get("eval_repo_pr", "")
            eval_repo = eval_cfg.get("eval_repo", "")
            eval_pr_url = f"https://github.com/ai4curation/{eval_repo}/pull/{eval_pr}" if eval_repo else ""

            lines.append(f"### Attempt {i}: {a.get('model', '?')} / {a.get('runtime', '?')}")
            lines.append("")
            lines.append(f"- **Eval PR**: {f'[#{eval_pr}]({eval_pr_url})' if eval_pr_url else f'#{eval_pr}'}")
            lines.append(f"- **F1**: {a.get('f1', 0):.3f}  **Precision**: {a.get('precision', 0):.3f}  **Recall**: {a.get('recall', 0):.3f}  **Jaccard**: {a.get('jaccard', 0):.3f}")
            trace_url = a.get("trace_url")
            if trace_url:
                lines.append(f"- **Trace**: [{trace_url.split('/')[-1]}]({trace_url})")
            workflow_run = a.get("workflow_run")
            if workflow_run and eval_repo:
                lines.append(f"- **Workflow run**: [{workflow_run}](https://github.com/ai4curation/{eval_repo}/actions/runs/{workflow_run})")
            lines.append("")

            # Agent PR comment
            if a.get("pr_comment"):
                lines.append("#### Agent PR Comment")
                lines.append("")
                lines.append(a["pr_comment"])
                lines.append("")

            # Agent issue comment
            if a.get("issue_comment"):
                lines.append("#### Agent Issue Comment")
                lines.append("")
                lines.append(a["issue_comment"])
                lines.append("")

            # Agent diff
            if a.get("diff"):
                lines.append("#### Agent Diff")
                lines.append("")
                lines.append("```diff")
                lines.append(a["diff"])
                lines.append("```")
                lines.append("")

            # Reviews
            for review in a.get("reviews", []):
                reviewer = review.get("frontmatter", {}).get("reviewed_by", "unknown")
                lines.append(f"#### Review by {reviewer}")
                lines.append("")
                fm = review.get("frontmatter", {})
                pills = []
                for k in ("outcome", "f1", "precision", "recall", "overall",
                           "instruction_following", "correctness", "completeness"):
                    if k in fm:
                        pills.append(f"**{k}**: {fm[k]}")
                if pills:
                    lines.append("  ".join(pills))
                    lines.append("")
                failure_modes = fm.get("failure_modes")
                if failure_modes:
                    lines.append(f"**Failure modes**: {', '.join(failure_modes) if isinstance(failure_modes, list) else failure_modes}")
                    lines.append("")
                body = review.get("body_md", "").strip()
                if body:
                    lines.append(body)
                    lines.append("")

    return "\n".join(lines)


def generate_case_briefs(analysis_dir: Path, *, max_diff_lines: int = 200) -> list[Path]:
    """Generate CASE_BRIEF.md files for all cases in the analysis directory.

    Each brief is written to ``{ont}/cases/pr{N}/CASE_BRIEF.md``.

    Args:
        analysis_dir: Analysis directory.
        max_diff_lines: Maximum diff lines to include.

    Returns:
        List of paths to generated files.
    """
    data = collect_gallery_data(analysis_dir, max_diff_lines=max_diff_lines)
    eval_repos = data.get("eval_repos", {})
    generated = []

    for ont_name, ont_data in data["ontologies"].items():
        for case in ont_data["cases"]:
            case_dir_name = case.get("case_dir", f"pr{case['pr_number']}")
            brief_path = analysis_dir / ont_name / "cases" / case_dir_name / "CASE_BRIEF.md"
            brief_md = format_case_brief(case, eval_repos)
            brief_path.write_text(brief_md, encoding="utf-8")
            generated.append(brief_path)

    return generated


GALLERY_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI4C Scribe Gallery</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; height: 100vh; display: flex; overflow: hidden; background: #f5f5f5; color: #222; }
#sidebar { width: 300px; flex-shrink: 0; background: #1e1e2e; color: #cdd6f4; display: flex; flex-direction: column; overflow: hidden; }
#filter-wrap { padding: 10px; border-bottom: 1px solid #313244; }
#filter { width: 100%; padding: 6px 10px; border-radius: 6px; border: 1px solid #45475a; background: #313244; color: #cdd6f4; font-size: 13px; }
#filter:focus { outline: 2px solid #89b4fa; }
#sidebar-list { overflow-y: auto; flex: 1; }
.ont-group {}
.ont-header { cursor: pointer; padding: 8px 12px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #a6adc8; display: flex; align-items: center; gap: 6px; user-select: none; }
.ont-header:hover { background: #313244; }
.ont-arrow { transition: transform 0.15s; display: inline-block; }
.ont-header.collapsed .ont-arrow { transform: rotate(-90deg); }
.ont-count { background: #45475a; border-radius: 10px; padding: 1px 7px; font-size: 11px; margin-left: auto; }
.ont-cases { }
.ont-header.collapsed + .ont-cases { display: none; }
.case-item { padding: 8px 12px 8px 20px; cursor: pointer; display: flex; align-items: flex-start; gap: 8px; border-bottom: 1px solid #181825; }
.case-item:hover { background: #313244; }
.case-item.active { background: #45475a; }
.diff-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; margin-top: 4px; }
.dot-simple { background: #a6e3a1; }
.dot-medium { background: #f9e2af; }
.dot-hard { background: #f38ba8; }
.dot-unknown { background: #6c7086; }
.case-info { min-width: 0; }
.case-pr { font-size: 11px; font-family: monospace; color: #89b4fa; }
.case-title { font-size: 12px; color: #cdd6f4; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

#detail { flex: 1; overflow-y: auto; padding: 24px; }
#detail-placeholder { color: #999; font-size: 15px; margin-top: 60px; text-align: center; }
#detail-content { display: none; max-width: 900px; margin: 0 auto; }
.detail-header { margin-bottom: 16px; }
.detail-title { font-size: 20px; font-weight: 700; margin-bottom: 6px; }
.gh-links { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 10px; font-size: 12px; }
.gh-links a { color: #0369a1; text-decoration: none; }
.gh-links a:hover { text-decoration: underline; }
.badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.badge { font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 12px; }
.badge-task_type { background: #dbeafe; color: #1d4ed8; }
.badge-difficulty-simple { background: #dcfce7; color: #15803d; }
.badge-difficulty-medium { background: #fef9c3; color: #a16207; }
.badge-difficulty-hard { background: #fee2e2; color: #b91c1c; }
.badge-difficulty { background: #f0fdf4; color: #166534; }
.badge-scoping { background: #ede9fe; color: #6d28d9; }
.badge-review_outcome { background: #fce7f3; color: #be185d; }
.badge-author { background: #f0f9ff; color: #0369a1; }
.narrative { line-height: 1.7; font-size: 14px; margin-bottom: 24px; }
.narrative h1, .narrative h2, .narrative h3 { margin: 12px 0 6px; }
.narrative p { margin-bottom: 8px; }
.narrative code { background: #f4f4f5; padding: 1px 4px; border-radius: 3px; font-family: monospace; }
.narrative pre { background: #f4f4f5; padding: 10px; border-radius: 6px; overflow-x: auto; }
.collapsible { border: 1px solid #e4e4e7; border-radius: 8px; margin-bottom: 16px; }
.collapsible-header { padding: 10px 14px; cursor: pointer; font-weight: 600; font-size: 13px; display: flex; align-items: center; justify-content: space-between; user-select: none; background: #fafafa; border-radius: 8px; }
.collapsible-header:hover { background: #f4f4f5; }
.collapsible-header .arrow { transition: transform 0.15s; }
.collapsible-header.open .arrow { transform: rotate(90deg); }
.collapsible-body { display: none; padding: 12px; border-top: 1px solid #e4e4e7; }
.collapsible-header.open + .collapsible-body { display: block; }
.diff-view { font-family: monospace; font-size: 12px; line-height: 1.5; overflow-x: auto; white-space: pre; }
.diff-view .d-add { color: #15803d; background: #f0fdf4; display: block; }
.diff-view .d-del { color: #b91c1c; background: #fff1f2; display: block; }
.diff-view .d-hunk { color: #1d4ed8; display: block; }
.diff-view .d-ctx { display: block; color: #555; }
.attempt-card { border: 1px solid #e4e4e7; border-radius: 6px; margin-bottom: 12px; }
.attempt-header { padding: 8px 12px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; background: #fafafa; border-radius: 6px; }
.attempt-model { font-weight: 600; font-size: 13px; }
.attempt-runtime { font-size: 12px; color: #666; }
.attempt-eval-link { font-size: 11px; color: #0369a1; text-decoration: none; }
.attempt-eval-link:hover { text-decoration: underline; }
.score-pill { font-size: 11px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }
.pill-green { background: #dcfce7; color: #15803d; }
.pill-amber { background: #fef9c3; color: #a16207; }
.pill-red { background: #fee2e2; color: #b91c1c; }
.attempt-expander { font-size: 11px; color: #888; cursor: pointer; margin-left: auto; }
.attempt-expander:hover { color: #333; }
.attempt-body { display: none; padding: 10px 12px; border-top: 1px solid #e4e4e7; }
.attempt-body.open { display: block; }
.attempt-section-title { font-size: 12px; font-weight: 600; color: #555; margin-bottom: 4px; margin-top: 10px; }
.attempt-section-title:first-child { margin-top: 0; }
.review-block { margin-bottom: 16px; }
.review-block + .review-block { border-top: 1px solid #e4e4e7; padding-top: 12px; }
.review-meta { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 8px; }
.review-meta-pill { font-size: 10px; font-weight: 600; padding: 1px 6px; border-radius: 8px; background: #f4f4f5; color: #555; border: 1px solid #e4e4e7; }
.review-meta-pill.outcome-success { background: #dcfce7; color: #15803d; border-color: #bbf7d0; }
.review-meta-pill.outcome-partial { background: #fef9c3; color: #a16207; border-color: #fde68a; }
.review-meta-pill.outcome-failure { background: #fee2e2; color: #b91c1c; border-color: #fecaca; }
.review-reviewer { font-size: 12px; font-weight: 600; color: #374151; margin-bottom: 4px; }
.review-md { font-size: 13px; line-height: 1.6; }
.review-md p { margin-bottom: 6px; }
.no-diff { font-size: 12px; color: #999; font-style: italic; }
.attempt-link { font-size: 11px; color: #89b4fa; text-decoration: none; margin-left: 4px; }
.attempt-link:hover { text-decoration: underline; }
.agent-comment { font-size: 13px; border-left: 3px solid #ddd; padding-left: 12px; margin-bottom: 12px; }
</style>
</head>
<body>

<div id="sidebar">
  <div id="filter-wrap">
    <input id="filter" type="text" placeholder="Filter cases..." autocomplete="off">
  </div>
  <div id="sidebar-list"></div>
</div>

<div id="detail">
  <div id="detail-placeholder">Select a case from the sidebar.</div>
  <div id="detail-content">
    <div class="detail-header">
      <div class="detail-title" id="d-title"></div>
      <div class="gh-links" id="d-gh-links"></div>
      <div class="badges" id="d-badges"></div>
    </div>
    <div class="narrative" id="d-narrative"></div>
    <div class="collapsible" id="d-human-diff-wrap">
      <div class="collapsible-header" id="d-human-diff-toggle">
        <span>Human Diff</span><span class="arrow">&#9654;</span>
      </div>
      <div class="collapsible-body">
        <div class="diff-view" id="d-human-diff"></div>
      </div>
    </div>
    <div class="collapsible" id="d-attempts-wrap">
      <div class="collapsible-header" id="d-attempts-toggle">
        <span>Agent Attempts</span><span class="arrow">&#9654;</span>
      </div>
      <div class="collapsible-body" id="d-attempts-body">
      </div>
    </div>
  </div>
</div>

<script>
(function() {
  var galleryData = __GALLERY_DATA__;

  // Build flat list of cases for navigation
  const allCases = [];
  const ontNames = Object.keys(galleryData.ontologies);
  ontNames.forEach(function(ont) {
    galleryData.ontologies[ont].cases.forEach(function(c) {
      allCases.push({ont: ont, c: c});
    });
  });

  let activeIdx = -1;

  // --- Sidebar rendering ---
  const sidebarList = document.getElementById('sidebar-list');

  function difficultyClass(d) {
    if (d === 'simple') return 'dot-simple';
    if (d === 'medium') return 'dot-medium';
    if (d === 'hard') return 'dot-hard';
    return 'dot-unknown';
  }

  function truncate(s, n) {
    if (!s) return '';
    return s.length > n ? s.slice(0, n) + '...' : s;
  }

  function renderSidebar(filter) {
    sidebarList.innerHTML = '';
    const q = (filter || '').toLowerCase();
    ontNames.forEach(function(ont) {
      const cases = galleryData.ontologies[ont].cases.filter(function(c) {
        if (!q) return true;
        const t = ((c.metadata.issue_title || '') + ' pr' + c.pr_number).toLowerCase();
        return t.indexOf(q) !== -1;
      });
      if (cases.length === 0) return;

      const group = document.createElement('div');
      group.className = 'ont-group';

      const header = document.createElement('div');
      header.className = 'ont-header';
      header.innerHTML = '<span class="ont-arrow">&#9660;</span><span>' + ont + '</span><span class="ont-count">' + cases.length + '</span>';
      header.addEventListener('click', function() {
        header.classList.toggle('collapsed');
      });
      group.appendChild(header);

      const casesEl = document.createElement('div');
      casesEl.className = 'ont-cases';
      cases.forEach(function(c) {
        const flatIdx = allCases.findIndex(function(x) { return x.ont === ont && x.c.pr_number === c.pr_number; });
        const item = document.createElement('div');
        item.className = 'case-item' + (flatIdx === activeIdx ? ' active' : '');
        item.dataset.idx = flatIdx;
        const dot = difficultyClass(c.metadata.difficulty);
        item.innerHTML =
          '<span class="diff-dot ' + dot + '"></span>' +
          '<span class="case-info"><span class="case-pr">PR #' + c.pr_number + '</span><br>' +
          '<span class="case-title">' + escHtml(truncate(c.metadata.issue_title || '', 40)) + '</span></span>';
        item.addEventListener('click', function() {
          selectCase(flatIdx);
        });
        casesEl.appendChild(item);
      });
      group.appendChild(casesEl);
      sidebarList.appendChild(group);
    });
  }

  function escHtml(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  // --- Detail pane ---
  function renderDiff(text) {
    if (!text) return '<span class="no-diff">No diff available.</span>';
    const lines = text.split('\\n');
    return lines.map(function(line) {
      if (line.startsWith('+') && !line.startsWith('+++')) return '<span class="d-add">' + escHtml(line) + '</span>';
      if (line.startsWith('-') && !line.startsWith('---')) return '<span class="d-del">' + escHtml(line) + '</span>';
      if (line.startsWith('@@')) return '<span class="d-hunk">' + escHtml(line) + '</span>';
      return '<span class="d-ctx">' + escHtml(line) + '</span>';
    }).join('');
  }

  function renderMarkdown(md) {
    if (typeof marked !== 'undefined') {
      return marked.parse(md || '');
    }
    return (md || '').replace(/\\n/g, '<br>');
  }

  function pillClass(score) {
    if (score >= 0.7) return 'pill-green';
    if (score >= 0.4) return 'pill-amber';
    return 'pill-red';
  }

  function outcomePillClass(outcome) {
    if (!outcome) return '';
    const o = outcome.toLowerCase();
    if (o === 'success' || o === 'full_success') return 'outcome-success';
    if (o === 'partial_success' || o === 'partial') return 'outcome-partial';
    if (o === 'failure' || o === 'fail') return 'outcome-failure';
    return '';
  }

  function reviewerFromFilename(filename) {
    // e.g. pr10-claudecode-complete.md -> claudecode-complete
    const m = filename.match(/^pr\\d+[-_](.+)\\.md$/);
    return m ? m[1] : filename;
  }

  function renderReviews(reviews, abody) {
    if (!reviews || reviews.length === 0) return;
    const secTitle = document.createElement('div');
    secTitle.className = 'attempt-section-title';
    secTitle.textContent = reviews.length === 1 ? 'Review' : 'Reviews (' + reviews.length + ')';
    abody.appendChild(secTitle);

    reviews.forEach(function(review) {
      const block = document.createElement('div');
      block.className = 'review-block';

      // Reviewer name
      const fm = review.frontmatter || {};
      const reviewerName = fm.reviewed_by || reviewerFromFilename(review.filename || '');
      if (reviewerName) {
        const rr = document.createElement('div');
        rr.className = 'review-reviewer';
        rr.textContent = 'Reviewer: ' + reviewerName;
        block.appendChild(rr);
      }

      // Frontmatter pills
      const metaRow = document.createElement('div');
      metaRow.className = 'review-meta';

      const pillFields = ['outcome', 'f1', 'precision', 'recall', 'jaccard', 'failure_modes'];
      pillFields.forEach(function(field) {
        const val = fm[field];
        if (val === null || val === undefined || val === '') return;
        const pill = document.createElement('span');
        pill.className = 'review-meta-pill';
        if (field === 'outcome') {
          pill.classList.add(outcomePillClass(val));
          pill.textContent = String(val);
        } else if (typeof val === 'number') {
          pill.className += ' ' + pillClass(val);
          pill.textContent = field.toUpperCase() + ' ' + val.toFixed(2);
        } else if (Array.isArray(val)) {
          pill.textContent = field + ': ' + val.join(', ');
        } else {
          pill.textContent = field + ': ' + String(val);
        }
        metaRow.appendChild(pill);
      });
      block.appendChild(metaRow);

      // Body markdown
      if (review.body_md && review.body_md.trim()) {
        const rv = document.createElement('div');
        rv.className = 'review-md';
        rv.innerHTML = renderMarkdown(review.body_md);
        block.appendChild(rv);
      }

      abody.appendChild(block);
    });
  }

  function getEvalRepo(ontology) {
    const cfg = galleryData.eval_repos && galleryData.eval_repos[ontology];
    return cfg ? cfg.eval_repo : null;
  }

  function renderAttempts(attempts, ontology) {
    const body = document.getElementById('d-attempts-body');
    body.innerHTML = '';
    if (!attempts || attempts.length === 0) {
      body.innerHTML = '<span class="no-diff">No agent attempts.</span>';
      return;
    }
    const sorted = attempts.slice().sort(function(a, b) { return b.f1 - a.f1; });
    const evalRepo = getEvalRepo(ontology);

    sorted.forEach(function(a) {
      const card = document.createElement('div');
      card.className = 'attempt-card';

      const header = document.createElement('div');
      header.className = 'attempt-header';

      const modelSpan = document.createElement('span');
      modelSpan.className = 'attempt-model';
      modelSpan.textContent = a.model || '(unknown model)';
      header.appendChild(modelSpan);

      if (a.runtime) {
        const rt = document.createElement('span');
        rt.className = 'attempt-runtime';
        rt.textContent = a.runtime;
        header.appendChild(rt);
      }

      // Eval repo PR link
      if (a.eval_repo_pr) {
        if (evalRepo) {
          const link = document.createElement('a');
          link.className = 'attempt-eval-link';
          link.href = 'https://github.com/ai4curation/' + evalRepo + '/pull/' + a.eval_repo_pr;
          link.target = '_blank';
          link.rel = 'noopener';
          link.textContent = 'Eval PR #' + a.eval_repo_pr;
          header.appendChild(link);
        } else {
          const prSpan = document.createElement('span');
          prSpan.className = 'attempt-runtime';
          prSpan.textContent = 'Eval PR #' + a.eval_repo_pr;
          header.appendChild(prSpan);
        }
      }

      ['f1','precision','recall'].forEach(function(metric) {
        const v = a[metric];
        if (v === null || v === undefined) return;
        const pill = document.createElement('span');
        pill.className = 'score-pill ' + pillClass(v);
        pill.textContent = metric.toUpperCase() + ' ' + v.toFixed(2);
        header.appendChild(pill);
      });

      // Trace and workflow links
      if (a.trace_url) {
        var tl = document.createElement('a');
        tl.href = a.trace_url;
        tl.target = '_blank';
        tl.className = 'attempt-link';
        tl.textContent = 'trace';
        header.appendChild(tl);
      }
      var evalRepo = getEvalRepo(ontology);
      if (a.workflow_run && evalRepo) {
        var wl = document.createElement('a');
        wl.href = 'https://github.com/ai4curation/' + evalRepo + '/actions/runs/' + a.workflow_run;
        wl.target = '_blank';
        wl.className = 'attempt-link';
        wl.textContent = 'run';
        header.appendChild(wl);
      }

      const expander = document.createElement('span');
      expander.className = 'attempt-expander';
      expander.textContent = 'show';
      header.appendChild(expander);

      card.appendChild(header);

      const abody = document.createElement('div');
      abody.className = 'attempt-body';

      if (a.pr_comment) {
        var t2 = document.createElement('div');
        t2.className = 'attempt-section-title';
        t2.textContent = 'Agent PR Comment';
        abody.appendChild(t2);
        var pc = document.createElement('div');
        pc.className = 'narrative agent-comment';
        pc.innerHTML = renderMarkdown(a.pr_comment);
        abody.appendChild(pc);
      }

      if (a.issue_comment) {
        var t3 = document.createElement('div');
        t3.className = 'attempt-section-title';
        t3.textContent = 'Agent Issue Comment';
        abody.appendChild(t3);
        var ic = document.createElement('div');
        ic.className = 'narrative agent-comment';
        ic.innerHTML = renderMarkdown(a.issue_comment);
        abody.appendChild(ic);
      }

      if (a.diff) {
        const t = document.createElement('div');
        t.className = 'attempt-section-title';
        t.textContent = 'Agent Diff';
        abody.appendChild(t);
        const dv = document.createElement('div');
        dv.className = 'diff-view';
        dv.innerHTML = renderDiff(a.diff);
        abody.appendChild(dv);
      }

      if (a.reviews && a.reviews.length > 0) {
        renderReviews(a.reviews, abody);
      }

      card.appendChild(abody);

      expander.addEventListener('click', function() {
        const open = abody.classList.toggle('open');
        expander.textContent = open ? 'hide' : 'show';
      });

      body.appendChild(card);
    });
  }

  function badgeHtml(label, value, extra) {
    const cls = extra || ('badge-' + label);
    return '<span class="badge ' + cls + '">' + escHtml(value) + '</span>';
  }

  function selectCase(idx) {
    if (idx < 0 || idx >= allCases.length) return;
    activeIdx = idx;
    renderSidebar(document.getElementById('filter').value);

    const entry = allCases[idx];
    const c = entry.c;
    const m = c.metadata;
    const repo = m.repo || '';

    document.getElementById('detail-placeholder').style.display = 'none';
    document.getElementById('detail-content').style.display = 'block';

    document.getElementById('d-title').textContent = 'PR #' + c.pr_number + ' - ' + (m.issue_title || '');

    // GitHub links row
    const ghLinks = document.getElementById('d-gh-links');
    ghLinks.innerHTML = '';
    if (repo) {
      if (m.issue_number) {
        const issueLink = document.createElement('a');
        issueLink.href = 'https://github.com/' + repo + '/issues/' + m.issue_number;
        issueLink.target = '_blank';
        issueLink.rel = 'noopener';
        issueLink.textContent = 'Issue #' + m.issue_number;
        ghLinks.appendChild(issueLink);
      }
      const prLink = document.createElement('a');
      prLink.href = 'https://github.com/' + repo + '/pull/' + c.pr_number;
      prLink.target = '_blank';
      prLink.rel = 'noopener';
      prLink.textContent = 'PR #' + c.pr_number;
      ghLinks.appendChild(prLink);
    }

    const badges = document.getElementById('d-badges');
    badges.innerHTML = '';
    if (m.task_type) badges.innerHTML += badgeHtml('task_type', m.task_type, 'badge badge-task_type');
    if (m.difficulty) {
      const dCls = 'badge badge-difficulty-' + m.difficulty;
      badges.innerHTML += '<span class="badge ' + dCls + '">' + escHtml(m.difficulty) + '</span>';
    }
    if (m.scoping) badges.innerHTML += badgeHtml('scoping', m.scoping, 'badge badge-scoping');
    if (m.review_outcome) badges.innerHTML += badgeHtml('review_outcome', m.review_outcome, 'badge badge-review_outcome');
    if (m.pr_author) badges.innerHTML += badgeHtml('author', '@' + m.pr_author, 'badge badge-author');

    document.getElementById('d-narrative').innerHTML = renderMarkdown(c.narrative_md);

    // Human diff
    const hdView = document.getElementById('d-human-diff');
    // Reset collapsible state when switching cases
    document.getElementById('d-human-diff-toggle').classList.remove('open');
    document.getElementById('d-attempts-toggle').classList.remove('open');

    if (c.human_diff) {
      document.getElementById('d-human-diff-wrap').style.display = '';
      hdView.innerHTML = renderDiff(c.human_diff);
    } else {
      document.getElementById('d-human-diff-wrap').style.display = 'none';
    }

    // Agent attempts
    if (c.agent_attempts && c.agent_attempts.length > 0) {
      document.getElementById('d-attempts-wrap').style.display = '';
    } else {
      document.getElementById('d-attempts-wrap').style.display = 'none';
    }
    renderAttempts(c.agent_attempts, c.ontology);
  }

  // Collapsible headers for detail pane
  ['d-human-diff-toggle','d-attempts-toggle'].forEach(function(id) {
    const el = document.getElementById(id);
    el.addEventListener('click', function() {
      el.classList.toggle('open');
    });
  });

  // Filter
  document.getElementById('filter').addEventListener('input', function(e) {
    renderSidebar(e.target.value);
  });

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (document.activeElement && document.activeElement.tagName === 'INPUT') return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectCase(Math.min(activeIdx + 1, allCases.length - 1));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectCase(Math.max(activeIdx - 1, 0));
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      // Open first closed collapsible: Human Diff first, then Agent Attempts
      const humanToggle = document.getElementById('d-human-diff-toggle');
      const attemptsToggle = document.getElementById('d-attempts-toggle');
      if (humanToggle && humanToggle.style.display !== 'none' && !humanToggle.classList.contains('open')) {
        humanToggle.classList.add('open');
      } else if (attemptsToggle && attemptsToggle.style.display !== 'none' && !attemptsToggle.classList.contains('open')) {
        attemptsToggle.classList.add('open');
      }
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      // Close last open collapsible: Agent Attempts first, then Human Diff
      const humanToggle = document.getElementById('d-human-diff-toggle');
      const attemptsToggle = document.getElementById('d-attempts-toggle');
      if (attemptsToggle && attemptsToggle.classList.contains('open')) {
        attemptsToggle.classList.remove('open');
      } else if (humanToggle && humanToggle.classList.contains('open')) {
        humanToggle.classList.remove('open');
      }
    }
  });

  // Initial render
  renderSidebar('');
  if (allCases.length > 0) selectCase(0);
})();
</script>
</body>
</html>
"""


def generate_gallery(
    analysis_dir: Path,
    output: Path,
    *,
    max_diff_lines: int = 200,
) -> Path:
    """Generate a self-contained HTML gallery from an analysis directory.

    Args:
        analysis_dir: Path containing ``{ont}/cases/`` subdirectories.
        output: Path for the output HTML file.
        max_diff_lines: Maximum lines per diff to embed. 0 for unlimited.

    Returns:
        Path to the generated HTML file.

    >>> import tempfile
    >>> from pathlib import Path
    >>> with tempfile.TemporaryDirectory() as tmp:
    ...     case_dir = Path(tmp) / "ont" / "cases" / "pr1"
    ...     case_dir.mkdir(parents=True)
    ...     _ = (case_dir / "METADATA.md").write_text(
    ...         "---\\nrepo: r\\nissue_number: 1\\npr_number: 1\\n"
    ...         'issue_title: "T"\\nissue_created_at: "2026-01-01"\\n'
    ...         "pr_author: a\\nscoping: s\\ntask_type: t\\n"
    ...         "difficulty: simple\\nscope: s\\nreview_outcome: ro\\n"
    ...         "curated_by: c\\ncurated_at: \\"2026-01-01\\"\\nrationale: r\\n---\\nBody.\\n"
    ...     )
    ...     out = Path(tmp) / "gallery.html"
    ...     result = generate_gallery(Path(tmp), out)
    ...     result == out
    True
    """
    data = collect_gallery_data(analysis_dir, max_diff_lines=max_diff_lines)
    # ensure_ascii=True so all non-ASCII is \uXXXX-escaped (safe in JS source).
    json_blob = json.dumps(data, indent=None, ensure_ascii=True)
    # Escape </ sequences that would prematurely close the <script> tag.
    json_blob = json_blob.replace("</", r"<\/")
    # Escape backticks which are JS template literal delimiters.
    json_blob = json_blob.replace("`", r"\u0060")
    html = GALLERY_HTML_TEMPLATE.replace("__GALLERY_DATA__", json_blob)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html)
    return output
