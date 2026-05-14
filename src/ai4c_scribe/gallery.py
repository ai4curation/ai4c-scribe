"""Generate a static HTML gallery browser for evaluation case studies.

Walks an analysis directory tree containing case study METADATA.md files,
human/agent diffs, scores TSV, and review files. Produces a single
self-contained HTML file for browsing cases in a sidebar + detail layout.
"""

import csv
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


def collect_gallery_data(analysis_dir: Path) -> dict:
    """Walk the analysis directory and assemble gallery data.

    Args:
        analysis_dir: Path containing ``{ont}/cases/`` and optionally
            ``{ont}/results/`` subdirectories.

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
            human_diff = human_diff_path.read_text() if human_diff_path.exists() else None

            # Agent attempts — joined via scores.tsv
            agent_attempts = []
            for score_row in scores_by_pr.get(pr_number, []):
                eval_pr = int(score_row["eval_repo_pr"])

                # Agent diff
                agent_diff_path = results_dir / "diffs" / "agent" / f"pr{eval_pr}.diff"
                agent_diff = agent_diff_path.read_text() if agent_diff_path.exists() else None

                # Review file(s) — match pr{eval_pr}-*.md
                review_md = None
                reviews_dir = results_dir / "reviews"
                if reviews_dir.exists():
                    for review_path in reviews_dir.glob(f"pr{eval_pr}-*.md"):
                        review_md = review_path.read_text()
                        break  # take first match

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
                    "review_md": review_md,
                })

            # Serialize dates to strings for JSON
            metadata = dict(frontmatter)
            for key in ("issue_created_at", "pr_merged_at", "curated_at",
                        "issue_closed_at"):
                if key in metadata and hasattr(metadata[key], "isoformat"):
                    metadata[key] = metadata[key].isoformat()

            cases.append({
                "pr_number": pr_number,
                "ontology": ont_name,
                "metadata": metadata,
                "narrative_md": body,
                "human_diff": human_diff,
                "agent_attempts": agent_attempts,
            })

        ontologies[ont_name] = {"cases": cases}

    return {"ontologies": ontologies}
