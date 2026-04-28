"""YAML configuration loading for workflows.

Loads and validates workflow configurations from YAML files.

Example YAML config:
    workflow: eval-agent-on-issue.yml
    repo: owner/repo
    description: "Evaluate agents on issues"

    inputs:
      issue_repo: monarch-initiative/mondo
      model: [claude-sonnet-4-5-20250929, claude-opus-4-5-20251101]
      agent_config_tag: v1.0.0

    # Each dict is one complete combination (zipped, not cross-product)
    input_sets:
      - issue_number: "7712"
        pr_number: "7800"
      - issue_number: "8116"
        pr_number: "8200"

    limits:
      max_concurrent: 5
      batch_size: 10
"""

import hashlib
from pathlib import Path

import yaml

from ai4c_scribe.workflows.models import (
    WorkflowConfig,
    WorkflowLimits,
)


def load_config(config_path: Path) -> WorkflowConfig:
    """Load workflow configuration from YAML file.

    Args:
        config_path: Path to YAML config file

    Returns:
        Validated WorkflowConfig

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValidationError: If config is invalid

    Example:
        >>> from pathlib import Path
        >>> # Would load from actual file:
        >>> # config = load_config(Path("workflows/eval.yaml"))
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        data = yaml.safe_load(f)

    if data is None:
        data = {}

    # Handle limits
    limits = WorkflowLimits()
    if "limits" in data:
        limits = WorkflowLimits(**data.pop("limits"))

    # input_sets is already in the right format (list of dicts)
    # just pass it through

    return WorkflowConfig(
        limits=limits,
        **data,
    )


def compute_config_hash(config_path: Path) -> str:
    """Compute hash of config file contents.

    Args:
        config_path: Path to config file

    Returns:
        SHA256 hash (first 16 chars)

    Example:
        >>> from pathlib import Path
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        ...     _ = f.write("workflow: test.yml\\nrepo: o/r\\n")
        ...     tmp_path = Path(f.name)
        >>> h = compute_config_hash(tmp_path)
        >>> len(h)
        16
        >>> tmp_path.unlink()
    """
    with open(config_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def validate_config(config: WorkflowConfig) -> list[str]:
    """Validate configuration for common issues.

    Args:
        config: Config to validate

    Returns:
        List of warning messages (empty if valid)

    Example:
        >>> config = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="owner/repo",
        ... )
        >>> warnings = validate_config(config)
        >>> len(warnings)
        0

        >>> config_high_concurrent = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="owner/repo",
        ...     limits=WorkflowLimits(max_concurrent=25),
        ... )
        >>> warnings = validate_config(config_high_concurrent)
        >>> any("rate limiting" in w for w in warnings)
        True
    """
    warnings = []

    if not config.workflow:
        warnings.append("workflow is required")

    if not config.repo:
        warnings.append("repo is required")

    # Validate input_sets have consistent keys
    if config.input_sets and len(config.input_sets) > 1:
        first_keys = set(config.input_sets[0].keys())
        for i, input_set in enumerate(config.input_sets[1:], start=2):
            current_keys = set(input_set.keys())
            if current_keys != first_keys:
                warnings.append(
                    f"input_sets[{i}] has different keys than first set: "
                    f"expected {first_keys}, got {current_keys}"
                )

    # Check limits are reasonable
    if config.limits.max_concurrent > 20:
        warnings.append(
            f"max_concurrent={config.limits.max_concurrent} may cause rate limiting"
        )

    if config.limits.batch_size > 50:
        warnings.append(
            f"batch_size={config.limits.batch_size} is very large, consider reducing"
        )

    return warnings


def config_to_yaml(config: WorkflowConfig) -> str:
    """Convert a WorkflowConfig back to YAML string.

    Useful for generating config templates or debugging.

    Args:
        config: Configuration to serialize

    Returns:
        YAML string representation

    Example:
        >>> config = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="owner/repo",
        ...     inputs={"model": "sonnet"},
        ... )
        >>> yaml_str = config_to_yaml(config)
        >>> "workflow: test.yml" in yaml_str
        True
    """
    from typing import Any

    data: dict[str, Any] = {
        "workflow": config.workflow,
        "repo": config.repo,
    }

    if config.description:
        data["description"] = config.description

    if config.tags:
        data["tags"] = config.tags

    if config.inputs:
        data["inputs"] = config.inputs

    if config.input_sets:
        data["input_sets"] = config.input_sets

    # Only include limits if non-default
    default_limits = WorkflowLimits()
    if config.limits != default_limits:
        data["limits"] = {
            "max_concurrent": config.limits.max_concurrent,
            "batch_size": config.limits.batch_size,
            "poll_interval_seconds": config.limits.poll_interval_seconds,
        }

    return yaml.dump(data, default_flow_style=False, sort_keys=False)
