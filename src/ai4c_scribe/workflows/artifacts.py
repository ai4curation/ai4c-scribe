"""Artifact download from completed workflow runs.

Downloads and tracks artifacts from GitHub Actions runs.
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

import duckdb

from ai4c_scribe.pr_mining import _parse_gh_json
from ai4c_scribe.workflows.db import insert_artifact
from ai4c_scribe.workflows.models import Artifact, ArtifactDownloadResult


def list_artifacts(repo: str, run_id: int) -> list[dict]:
    """List artifacts for a workflow run.

    Args:
        repo: Repository (owner/repo)
        run_id: GitHub run ID

    Returns:
        List of artifact metadata dicts with keys:
        - id: artifact ID
        - name: artifact name
        - size_in_bytes: size
        - expired: whether artifact has expired
    """
    cmd = [
        "gh",
        "api",
        f"repos/{repo}/actions/runs/{run_id}/artifacts",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = _parse_gh_json(result, cmd)

    return data.get("artifacts", [])


def download_artifact(
    repo: str,
    artifact_name: str,
    run_id: int,
    output_dir: Path,
) -> Path:
    """Download a single artifact by name.

    Uses `gh run download` which handles extraction automatically.
    Clears the output directory first to avoid "file exists" errors.

    Args:
        repo: Repository (owner/repo)
        artifact_name: Name of the artifact
        run_id: GitHub run ID
        output_dir: Directory to download to

    Returns:
        Path to the downloaded artifact directory
    """
    import shutil

    # Clear and recreate directory to avoid "file exists" errors
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gh",
        "run",
        "download",
        str(run_id),
        "--repo",
        repo,
        "--name",
        artifact_name,
        "--dir",
        str(output_dir),
    ]

    subprocess.run(cmd, check=True, capture_output=True, text=True)

    return output_dir


def download_run_artifacts(
    conn: duckdb.DuckDBPyConnection,
    repo: str,
    run_id: int,
    output_dir: Optional[Path] = None,
    verbose: bool = False,
) -> ArtifactDownloadResult:
    """Download all artifacts for a run.

    Args:
        conn: Database connection
        repo: Repository (owner/repo)
        run_id: GitHub run ID
        output_dir: Directory to download to (default: .ai4cscribe/artifacts/{run_id}/)
        verbose: If True, print progress

    Returns:
        ArtifactDownloadResult with download details
    """
    if output_dir is None:
        output_dir = Path(".ai4cscribe/artifacts") / str(run_id)

    artifacts_data = list_artifacts(repo, run_id)

    downloaded = []
    total_bytes = 0

    for artifact_data in artifacts_data:
        artifact_id = artifact_data["id"]
        name = artifact_data["name"]
        size_bytes = artifact_data.get("size_in_bytes", 0)
        expired = artifact_data.get("expired", False)

        if expired:
            if verbose:
                print(f"Skipping expired artifact: {name}")
            continue

        try:
            if verbose:
                print(f"Downloading artifact: {name} ({size_bytes} bytes)...")

            # Download to a subdirectory named after the artifact
            artifact_dir = output_dir / name
            download_artifact(repo, name, run_id, artifact_dir)

            artifact = Artifact(
                artifact_id=artifact_id,
                run_id=run_id,
                name=name,
                size_bytes=size_bytes,
                downloaded_at=datetime.now(),
                local_path=artifact_dir,
                expired=False,
            )

            insert_artifact(conn, artifact)
            downloaded.append(artifact)
            total_bytes += size_bytes

            if verbose:
                print(f"  -> Downloaded to {artifact_dir}")

        except Exception as e:
            if verbose:
                print(f"  -> Failed to download {name}: {e}")

    return ArtifactDownloadResult(
        run_id=run_id,
        artifacts_found=len(artifacts_data),
        artifacts_downloaded=len(downloaded),
        total_bytes=total_bytes,
        artifacts=downloaded,
    )


def get_artifact_content(artifact_path: Path, filename: Optional[str] = None) -> Optional[str]:
    """Read content from a downloaded artifact.

    Args:
        artifact_path: Path to artifact directory
        filename: Specific file to read (if None, reads first file found)

    Returns:
        File contents as string, or None if not found
    """
    if not artifact_path.exists():
        return None

    if filename:
        file_path = artifact_path / filename
        if file_path.exists():
            return file_path.read_text()
        return None

    # Find first file in the artifact directory
    for item in artifact_path.iterdir():
        if item.is_file():
            return item.read_text()

    return None
