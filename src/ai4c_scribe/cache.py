"""Explicit file-based caching for GitHub API responses.

Uses a structured directory layout:
.ai4cscribe/cache/{org}/{repo}/pr/{pr_number}/{endpoint}.json

This provides transparent caching with easy inspection and management.
"""

import json
from pathlib import Path
from typing import Any, Callable, Optional, TypeVar
from functools import wraps

T = TypeVar('T')

# Default cache directory
CACHE_DIR = Path(".ai4cscribe/cache")


def get_cache_dir() -> Path:
    """Get the cache directory, creating it if needed."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR


def get_pr_cache_path(repo: str, pr_number: int, endpoint: str) -> Path:
    """Get the cache file path for a PR-related endpoint.

    Args:
        repo: Repository in owner/name format (e.g., "monarch-initiative/mondo")
        pr_number: PR number
        endpoint: Endpoint name (e.g., "pr_data", "reviews", "commits")

    Returns:
        Path to cache file

    Example:
        >>> get_pr_cache_path("monarch-initiative/mondo", 8116, "pr_data")
        Path('.ai4cscribe/cache/monarch-initiative/mondo/pr/8116/pr_data.json')
    """
    cache_dir = get_cache_dir()
    pr_dir = cache_dir / repo / "pr" / str(pr_number)
    pr_dir.mkdir(parents=True, exist_ok=True)
    return pr_dir / f"{endpoint}.json"


def get_issue_cache_path(repo: str, issue_number: int, endpoint: str) -> Path:
    """Get the cache file path for an issue-related endpoint.

    Args:
        repo: Repository in owner/name format
        issue_number: Issue number
        endpoint: Endpoint name (e.g., "issue_data", "comments")

    Returns:
        Path to cache file
    """
    cache_dir = get_cache_dir()
    issue_dir = cache_dir / repo / "issue" / str(issue_number)
    issue_dir.mkdir(parents=True, exist_ok=True)
    return issue_dir / f"{endpoint}.json"


def get_commit_cache_path(repo: str, commit_sha: str) -> Path:
    """Get the cache file path for a commit.

    Args:
        repo: Repository in owner/name format
        commit_sha: Commit SHA

    Returns:
        Path to cache file
    """
    cache_dir = get_cache_dir()
    commit_dir = cache_dir / repo / "commit"
    commit_dir.mkdir(parents=True, exist_ok=True)
    return commit_dir / f"{commit_sha}.json"


def read_cache(cache_path: Path) -> Optional[Any]:
    """Read data from cache file.

    Args:
        cache_path: Path to cache file

    Returns:
        Cached data if exists, None otherwise
    """
    if cache_path.exists():
        with open(cache_path) as f:
            return json.load(f)
    return None


def write_cache(cache_path: Path, data: Any) -> None:
    """Write data to cache file.

    Args:
        cache_path: Path to cache file
        data: Data to cache (must be JSON-serializable or Pydantic model)
    """
    from pydantic import BaseModel

    cache_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert Pydantic models to dicts before caching
    def serialize(obj: Any) -> Any:
        if isinstance(obj, BaseModel):
            return obj.model_dump(mode='python')
        elif isinstance(obj, list):
            return [serialize(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: serialize(v) for k, v in obj.items()}
        else:
            return obj

    serialized_data = serialize(data)

    with open(cache_path, 'w') as f:
        json.dump(serialized_data, f, indent=2, default=str)


def clear_cache(repo: Optional[str] = None) -> None:
    """Clear the cache.

    Args:
        repo: If provided, only clear cache for this repo. Otherwise clear all.
    """
    cache_dir = get_cache_dir()

    if repo:
        repo_dir = cache_dir / repo
        if repo_dir.exists():
            import shutil
            shutil.rmtree(repo_dir)
    else:
        if cache_dir.exists():
            import shutil
            shutil.rmtree(cache_dir)


class CacheStats:
    """Cache statistics.

    Attributes:
        num_files: Number of cache files
        total_bytes: Total size in bytes
        total_mb: Total size in megabytes
        avg_file_size_kb: Average file size in kilobytes
    """

    def __init__(self, num_files: int, total_bytes: int):
        self.num_files = num_files
        self.total_bytes = total_bytes
        self.total_mb = total_bytes / (1024 * 1024)
        self.avg_file_size_kb = (
            (total_bytes / num_files) / 1024 if num_files > 0 else 0
        )

    def __repr__(self) -> str:
        return (
            f"CacheStats(files={self.num_files}, "
            f"size={self.total_mb:.2f}MB, "
            f"avg={self.avg_file_size_kb:.2f}KB)"
        )


def get_cache_stats(repo: Optional[str] = None) -> CacheStats:
    """Get cache statistics.

    Args:
        repo: If provided, only count this repo's cache. Otherwise count all.

    Returns:
        CacheStats object with statistics

    Example:
        >>> stats = get_cache_stats()
        >>> print(f"{stats.num_files} files, {stats.total_mb:.2f} MB")
        42 files, 1.23 MB

        >>> stats = get_cache_stats("monarch-initiative/mondo")
        >>> stats.num_files
        20
    """
    cache_dir = get_cache_dir()

    if repo:
        search_dir = cache_dir / repo
    else:
        search_dir = cache_dir

    if not search_dir.exists():
        return CacheStats(0, 0)

    num_files = 0
    total_bytes = 0

    for cache_file in search_dir.rglob("*.json"):
        num_files += 1
        total_bytes += cache_file.stat().st_size

    return CacheStats(num_files, total_bytes)


def cache_size(repo: Optional[str] = None) -> tuple[int, int]:
    """Get cache statistics (legacy function, use get_cache_stats instead).

    Args:
        repo: If provided, only count this repo's cache

    Returns:
        Tuple of (num_files, total_bytes)
    """
    stats = get_cache_stats(repo)
    return (stats.num_files, stats.total_bytes)


def cached_pr_endpoint(endpoint_name: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator for caching PR-related API calls.

    Args:
        endpoint_name: Name of the endpoint for cache filename

    Example:
        @cached_pr_endpoint("pr_data")
        def get_pr_data(repo: str, pr_number: int) -> dict:
            # Expensive API call
            pass
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(repo: str, pr_number: int, *args: Any, **kwargs: Any) -> T:
            cache_path = get_pr_cache_path(repo, pr_number, endpoint_name)

            # Try to read from cache
            cached = read_cache(cache_path)
            if cached is not None:
                return cached  # type: ignore

            # Call function and cache result
            result = func(repo, pr_number, *args, **kwargs)
            write_cache(cache_path, result)
            return result

        return wrapper
    return decorator


def cached_issue_endpoint(endpoint_name: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator for caching issue-related API calls.

    Args:
        endpoint_name: Name of the endpoint for cache filename

    Example:
        @cached_issue_endpoint("issue_data")
        def get_issue_data(repo: str, issue_number: int) -> dict:
            # Expensive API call
            pass
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(repo: str, issue_number: int, *args: Any, **kwargs: Any) -> T:
            cache_path = get_issue_cache_path(repo, issue_number, endpoint_name)

            # Try to read from cache
            cached = read_cache(cache_path)
            if cached is not None:
                return cached  # type: ignore

            # Call function and cache result
            result = func(repo, issue_number, *args, **kwargs)
            write_cache(cache_path, result)
            return result

        return wrapper
    return decorator


def cached_commit() -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator for caching commit-related API calls.

    Example:
        @cached_commit()
        def get_commit_diff(repo: str, commit_sha: str) -> Optional[str]:
            # Expensive API call
            pass
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(repo: str, commit_sha: str, *args: Any, **kwargs: Any) -> T:
            cache_path = get_commit_cache_path(repo, commit_sha)

            # Try to read from cache
            cached = read_cache(cache_path)
            if cached is not None:
                return cached  # type: ignore

            # Call function and cache result
            result = func(repo, commit_sha, *args, **kwargs)
            write_cache(cache_path, result)
            return result

        return wrapper
    return decorator
