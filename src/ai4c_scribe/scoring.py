"""Scoring module for evaluation runs.

Handles:
- Fetching and caching diffs (human and agent)
- Running metadiff comparisons
- Normalizing model/runtime names
- Producing structured score records

All results are cached per-run so re-scoring is instant.
"""

from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional
import json
import re
import subprocess

import yaml


# === Vocabularies ===

# Canonical model names. Raw values from PR titles or workflow inputs
# are normalized to these.
MODEL_CANONICAL = {
    # From PR title short forms
    "sonnet-4.5": "claude-sonnet-4.5",
    "haiku-4.5": "claude-haiku-4.5",
    "opus-4.7": "claude-opus-4.7",
    # From workflow inputs with provider prefix
    "openai/gpt-5.4": "gpt-5.4",
    "openai/gpt-5.5": "gpt-5.5",
    # Already canonical
    "gpt-5.4": "gpt-5.4",
    "gpt-5.5": "gpt-5.5",
    "claude-sonnet-4-5": "claude-sonnet-4.5",
    "claude-haiku-4-5": "claude-haiku-4.5",
    "claude-opus-4-7": "claude-opus-4.7",
    "codex-mini-latest": "codex-mini",
}

RUNTIME_VALUES = {"claude", "codex", "opencode", "pi"}

# Map runtime to how it appears in PR titles
RUNTIME_FROM_MODEL = {
    "sonnet-4.5": "claude",
    "haiku-4.5": "claude",
    "opus-4.7": "claude",
}


def normalize_model(raw: str) -> str:
    """Normalize a model string to canonical form.

    >>> normalize_model("openai/gpt-5.5")
    'gpt-5.5'
    >>> normalize_model("sonnet-4.5")
    'claude-sonnet-4.5'
    >>> normalize_model("gpt-5.4")
    'gpt-5.4'
    """
    return MODEL_CANONICAL.get(raw, raw)


def infer_runtime(model_raw: str) -> str:
    """Infer runtime from the raw model string in a PR title.

    >>> infer_runtime("sonnet-4.5")
    'claude'
    >>> infer_runtime("gpt-5.5")
    'codex'
    >>> infer_runtime("openai/gpt-5.5")
    'opencode'
    """
    if model_raw in RUNTIME_FROM_MODEL:
        return RUNTIME_FROM_MODEL[model_raw]
    if model_raw.startswith("openai/"):
        return "opencode"
    return "codex"


# === Data structures ===

@dataclass
class ScoreRecord:
    """One scored evaluation run."""
    ontology: str
    issue_number: int
    pr_number: int  # human PR
    case_type: str
    difficulty: str
    agent_config_tag: str
    model: str  # canonical
    runtime: str
    eval_repo_pr: int  # agent PR in eval repo
    f1: float
    precision: float
    recall: float
    jaccard: float

    def to_dict(self) -> dict:
        return asdict(self)


# === Caching ===

def _score_cache_path(ontology: str, eval_repo_pr: int, analysis_dir: Path) -> Path:
    """Path to cached score for a specific run."""
    return analysis_dir / ontology / "results" / "scores_cache" / f"pr{eval_repo_pr}.json"


def get_cached_score(ontology: str, eval_repo_pr: int,
                     analysis_dir: Path = Path("analysis")) -> Optional[ScoreRecord]:
    """Load a cached score record if available."""
    cache_path = _score_cache_path(ontology, eval_repo_pr, analysis_dir)
    if cache_path.exists():
        data = json.loads(cache_path.read_text())
        return ScoreRecord(**data)
    return None


def cache_score(record: ScoreRecord, analysis_dir: Path = Path("analysis")) -> None:
    """Cache a score record to disk."""
    cache_path = _score_cache_path(record.ontology, record.eval_repo_pr, analysis_dir)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(record.to_dict(), indent=2))


# === Case metadata ===

def load_case_metadata(ontology: str, analysis_dir: Path = Path("analysis")) -> dict:
    """Load all case metadata for an ontology.

    Returns dict mapping issue_number (str) -> {pr, task_type, difficulty}
    """
    cases = {}
    case_dir = analysis_dir / ontology / "cases"
    if not case_dir.exists():
        return cases
    for d in case_dir.iterdir():
        md = d / "METADATA.md"
        if not md.exists():
            continue
        text = md.read_text()
        issue = pr = task = diff = None
        for line in text.split("\n"):
            if line.startswith("issue_number:"):
                issue = line.split(":")[1].strip()
            elif line.startswith("pr_number:"):
                pr = line.split(":")[1].strip()
            elif line.startswith("task_type:"):
                task = line.split(":")[1].strip()
            elif line.startswith("difficulty:"):
                diff = line.split(":")[1].strip()
        if issue:
            cases[issue] = {"pr": pr, "task_type": task, "difficulty": diff}
    return cases


# === Diff fetching ===

def fetch_human_diff(ontology: str, pr_number: str, source_repo: str,
                     analysis_dir: Path = Path("analysis")) -> Optional[Path]:
    """Fetch and cache the human (ground truth) PR diff."""
    diff_path = analysis_dir / ontology / "results" / "diffs" / "human" / f"pr{pr_number}.diff"
    if diff_path.exists() and diff_path.stat().st_size > 0:
        return diff_path
    diff_path.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["gh", "pr", "diff", pr_number, "--repo", source_repo],
        capture_output=True, text=True,
    )
    if r.returncode == 0 and r.stdout:
        diff_path.write_text(r.stdout)
        return diff_path
    return None


def fetch_agent_diff(eval_repo: str, pr_number: int, ontology: str = "",
                     analysis_dir: Path = Path("analysis")) -> Optional[str]:
    """Fetch and cache an agent PR diff.

    Cached to analysis/{ont}/results/diffs/agent/ for permanence.
    """
    # Check cache first
    if ontology:
        cache_path = analysis_dir / ontology / "results" / "diffs" / "agent" / f"pr{pr_number}.diff"
        if cache_path.exists() and cache_path.stat().st_size > 0:
            return cache_path.read_text()

    r = subprocess.run(
        ["gh", "pr", "diff", str(pr_number), "--repo", f"ai4curation/{eval_repo}"],
        capture_output=True, text=True,
    )
    if r.returncode == 0 and r.stdout:
        # Cache it
        if ontology:
            cache_path = analysis_dir / ontology / "results" / "diffs" / "agent" / f"pr{pr_number}.diff"
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(r.stdout)
        return r.stdout
    return None


def fetch_trace(eval_repo: str, run_id: str, ontology: str,
                analysis_dir: Path = Path("analysis")) -> Optional[Path]:
    """Fetch and cache the trace directory from the eval repo.

    Downloads agent-trace.json, ISSUE_COMMENTS.md, PR_COMMENTS.md,
    and run-metadata.json from traces/{run_id}/ on master.

    Returns path to the local trace directory, or None if not found.
    """
    trace_dir = analysis_dir / ontology / "results" / "traces" / f"run{run_id}"
    if trace_dir.exists() and any(trace_dir.iterdir()):
        return trace_dir

    trace_dir.mkdir(parents=True, exist_ok=True)

    # Fetch file list from the eval repo's traces directory
    r = subprocess.run(
        ["gh", "api", f"repos/ai4curation/{eval_repo}/contents/traces/{run_id}",
         "--jq", ".[].name"],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not r.stdout.strip():
        return None

    files = r.stdout.strip().split("\n")
    for fname in files:
        file_r = subprocess.run(
            ["gh", "api",
             f"repos/ai4curation/{eval_repo}/contents/traces/{run_id}/{fname}",
             "--jq", ".content"],
            capture_output=True, text=True,
        )
        if file_r.returncode == 0 and file_r.stdout.strip():
            import base64
            content = base64.b64decode(file_r.stdout.strip()).decode("utf-8", errors="replace")
            (trace_dir / fname).write_text(content)

    return trace_dir if any(trace_dir.iterdir()) else None


# === Metadiff ===

def run_metadiff(human_diff_path: Path, agent_diff: str, config: str = "obo") -> Optional[dict]:
    """Run metadiff compare and return scores dict."""
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".diff", delete=False) as f:
        f.write(agent_diff)
        agent_path = f.name

    r = subprocess.run(
        ["uv", "run", "ai4c-scribe", "metadiff", "compare",
         str(human_diff_path), agent_path, "--config", config],
        capture_output=True, text=True,
    )
    Path(agent_path).unlink(missing_ok=True)

    scores = {}
    for line in r.stdout.split("\n"):
        if "F1 Score" in line:
            scores["f1"] = float(line.split()[-1])
        elif "Precision" in line:
            scores["precision"] = float(line.split()[-1])
        elif "Recall" in line:
            scores["recall"] = float(line.split()[-1])
        elif "Jaccard" in line:
            scores["jaccard"] = float(line.split()[-1])

    return scores if "f1" in scores else None


# === PR title parsing ===

def parse_pr_title(title: str) -> Optional[dict]:
    """Parse a DO NOT MERGE eval PR title into components.

    >>> parse_pr_title("[DO NOT MERGE] eval #31961 i:1: some title (gpt-5.5, .)")
    {'issue_number': '31961', 'model_raw': 'gpt-5.5'}
    >>> parse_pr_title("[DO NOT MERGE] eval #3454 i:1: some (parens) title (openai/gpt-5.5, .)")
    {'issue_number': '3454', 'model_raw': 'openai/gpt-5.5'}
    >>> parse_pr_title("not a valid title")
    """
    if "DO NOT MERGE" not in title:
        return None
    m_issue = re.search(r"eval #(\d+)", title)
    if not m_issue:
        return None
    # Model is always in the LAST parenthesized group: "(model, .)"
    m_model = re.search(r"\(([^()]+),\s*\.\)\s*$", title)
    if not m_model:
        return None
    return {
        "issue_number": m_issue.group(1),
        "model_raw": m_model.group(1).strip(),
    }


# === Main scoring function ===

def score_eval_repo(
    ontology: str,
    eval_repo: str,
    source_repo: str,
    metadiff_config: str = "obo",
    config_tag: str = "v9",
    analysis_dir: Path = Path("analysis"),
    use_cache: bool = True,
) -> list[ScoreRecord]:
    """Score all eval PRs in a repo, with caching.

    Args:
        ontology: Ontology name
        eval_repo: Eval repo name (without org prefix)
        source_repo: Source ontology repo (org/name)
        metadiff_config: Metadiff normalizer config
        config_tag: Agent config tag
        analysis_dir: Root analysis directory
        use_cache: Whether to use cached scores

    Returns:
        List of ScoreRecord objects
    """
    # Load case metadata
    cases = load_case_metadata(ontology, analysis_dir)
    if not cases:
        return []

    # Get all PRs from the eval repo
    r = subprocess.run(
        ["gh", "pr", "list", "--repo", f"ai4curation/{eval_repo}",
         "--limit", "500", "--state", "all",
         "--json", "number,title,additions,deletions"],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not r.stdout.strip():
        return []

    prs = json.loads(r.stdout)
    records = []

    for pr in prs:
        title = pr.get("title", "")
        additions = pr.get("additions", 0)
        deletions = pr.get("deletions", 0)

        # Skip PRs with no changes
        if additions == 0 and deletions == 0:
            continue

        # Parse title
        parsed = parse_pr_title(title)
        if not parsed:
            continue

        issue = parsed["issue_number"]
        model_raw = parsed["model_raw"]
        pr_num = pr["number"]

        # Check cache
        if use_cache:
            cached = get_cached_score(ontology, pr_num, analysis_dir)
            if cached:
                records.append(cached)
                continue

        # Look up case metadata
        if issue not in cases:
            continue
        case = cases[issue]
        human_pr = case["pr"]

        # Fetch human diff
        human_path = fetch_human_diff(ontology, human_pr, source_repo, analysis_dir)
        if not human_path:
            continue

        # Fetch agent diff
        agent_diff = fetch_agent_diff(eval_repo, pr_num, ontology, analysis_dir)
        if not agent_diff:
            continue

        # Run metadiff
        scores = run_metadiff(human_path, agent_diff, metadiff_config)
        if not scores:
            continue

        # Build record
        record = ScoreRecord(
            ontology=ontology,
            issue_number=int(issue),
            pr_number=int(human_pr),
            case_type=case["task_type"],
            difficulty=case["difficulty"],
            agent_config_tag=config_tag,
            model=normalize_model(model_raw),
            runtime=infer_runtime(model_raw),
            eval_repo_pr=pr_num,
            f1=scores["f1"],
            precision=scores["precision"],
            recall=scores["recall"],
            jaccard=scores["jaccard"],
        )
        records.append(record)
        cache_score(record, analysis_dir)

    return records


# === Config ===

# Evaluation repos configuration
EVAL_REPOS = {
    "go-ontology": {
        "eval_repo": "eval-ont-agent-go",
        "source_repo": "geneontology/go-ontology",
        "metadiff_config": "obo",
        "config_tag": "v9",
    },
    "cell-ontology": {
        "eval_repo": "eval-ont-agent-cl",
        "source_repo": "obophenotype/cell-ontology",
        "metadiff_config": "generic",
        "config_tag": "v3",
    },
    "uberon": {
        "eval_repo": "eval-ont-agent-uberon",
        "source_repo": "obophenotype/uberon",
        "metadiff_config": "obo",
        "config_tag": "v3",
    },
    "mondo": {
        "eval_repo": "eval-ont-agent-mondo",
        "source_repo": "monarch-initiative/mondo",
        "metadiff_config": "obo",
        "config_tag": "v3",
    },
}


def load_cached_scores(ontology: str, analysis_dir: Path = Path("analysis")) -> list[ScoreRecord]:
    """Load all cached score records for an ontology from disk."""
    cache_dir = analysis_dir / ontology / "results" / "scores_cache"
    records = []
    if cache_dir.exists():
        for f in cache_dir.glob("*.json"):
            data = json.loads(f.read_text())
            records.append(ScoreRecord(**data))
    return records


def score_all(analysis_dir: Path = Path("analysis"), use_cache: bool = True) -> list[ScoreRecord]:
    """Score all evaluation repos.

    Combines freshly-scored runs (from API) with any previously-cached
    scores that the API didn't return (handles flaky API responses).

    Returns combined list of ScoreRecords across all ontologies.
    """
    all_records = []
    for ontology, cfg in EVAL_REPOS.items():
        # Score what the API returns (uses cache for known PRs)
        fresh = score_eval_repo(
            ontology=ontology,
            analysis_dir=analysis_dir,
            use_cache=use_cache,
            **cfg,
        )
        fresh_prs = {r.eval_repo_pr for r in fresh}

        # Also load any cached scores the API didn't return
        cached = load_cached_scores(ontology, analysis_dir)
        for r in cached:
            if r.eval_repo_pr not in fresh_prs:
                fresh.append(r)

        all_records.extend(fresh)
    return all_records


def load_agents_config(ontology: str, analysis_dir: Path = Path("analysis")) -> dict:
    """Load agents.yaml for an ontology.

    Returns dict mapping handle -> agent config dict.

    >>> agents = load_agents_config("go-ontology", Path("analysis"))
    >>> "codex_g55_v9" in agents  # doctest: +SKIP
    True
    """
    agents_path = analysis_dir / ontology / "agents.yaml"
    if not agents_path.exists():
        return {}
    data = yaml.safe_load(agents_path.read_text())
    return data.get("agents", {})


def resolve_agent_handle(record: ScoreRecord, analysis_dir: Path = Path("analysis")) -> str:
    """Resolve a ScoreRecord to its agent handle from agents.yaml.

    Matches on (runtime, model, config_tag). Returns handle or
    a generated fallback like 'codex/gpt-5.5/v9'.
    """
    agents = load_agents_config(record.ontology, analysis_dir)
    for handle, cfg in agents.items():
        if (cfg.get("runtime") == record.runtime and
            cfg.get("model") == record.model and
            cfg.get("config_tag") == record.agent_config_tag):
            return handle
    # Fallback: generate from components
    return f"{record.runtime}/{record.model}/{record.agent_config_tag}"


def records_to_dataframe(records: list[ScoreRecord], analysis_dir: Path = Path("analysis")):
    """Convert ScoreRecords to a pandas DataFrame with agent handles."""
    import pandas as pd
    if not records:
        return pd.DataFrame(columns=[
            "ontology", "issue_number", "pr_number", "case_type", "difficulty",
            "agent_config_tag", "model", "runtime", "eval_repo_pr",
            "f1", "precision", "recall", "jaccard", "case", "agent",
        ])
    df = pd.DataFrame([r.to_dict() for r in records])
    df["case"] = df["ontology"].str[:3] + "#" + df["issue_number"].astype(str)
    df["agent"] = [resolve_agent_handle(r, analysis_dir) for r in records]
    return df
