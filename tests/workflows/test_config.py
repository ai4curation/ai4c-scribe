"""Tests for config loading."""

import pytest
import tempfile
from pathlib import Path

from ai4c_scribe.workflows.config import (
    load_config,
    compute_config_hash,
    validate_config,
    config_to_yaml,
)
from ai4c_scribe.workflows.models import (
    WorkflowConfig,
    WorkflowLimits,
)


@pytest.fixture
def temp_config_file():
    """Create a temporary config file."""
    content = """\
workflow: eval-agent-on-issue.yml
repo: owner/repo
description: Test config

inputs:
  issue_repo: monarch-initiative/mondo
  model:
    - claude-sonnet-4-5-20250929
    - claude-opus-4-5-20251101
  iter_num: 1

limits:
  max_concurrent: 3
  batch_size: 5
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False
    ) as f:
        f.write(content)
        f.flush()  # Ensure content is written to disk
        tmp_path = Path(f.name)
    yield tmp_path
    # Cleanup
    tmp_path.unlink(missing_ok=True)


@pytest.fixture
def temp_config_with_input_sets():
    """Create a config file with input_sets."""
    content = """\
workflow: eval.yml
repo: org/repo

inputs:
  model: sonnet

input_sets:
  - issue_number: "100"
    pr_number: "101"
  - issue_number: "200"
    pr_number: "201"
  - issue_number: "300"
    pr_number: "301"
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False
    ) as f:
        f.write(content)
        f.flush()  # Ensure content is written to disk
        tmp_path = Path(f.name)
    yield tmp_path
    tmp_path.unlink(missing_ok=True)


class TestLoadConfig:
    """Tests for config loading."""

    def test_load_basic_config(self, temp_config_file):
        """Test loading a basic config file."""
        config = load_config(temp_config_file)

        assert config.workflow == "eval-agent-on-issue.yml"
        assert config.repo == "owner/repo"
        assert config.description == "Test config"
        assert config.inputs["issue_repo"] == "monarch-initiative/mondo"
        assert config.inputs["model"] == [
            "claude-sonnet-4-5-20250929",
            "claude-opus-4-5-20251101",
        ]
        assert config.inputs["iter_num"] == 1

    def test_load_config_limits(self, temp_config_file):
        """Test that limits are loaded correctly."""
        config = load_config(temp_config_file)

        assert config.limits.max_concurrent == 3
        assert config.limits.batch_size == 5

    def test_load_config_with_input_sets(self, temp_config_with_input_sets):
        """Test loading config with input_sets."""
        config = load_config(temp_config_with_input_sets)

        assert len(config.input_sets) == 3
        assert config.input_sets[0] == {"issue_number": "100", "pr_number": "101"}
        assert config.input_sets[1] == {"issue_number": "200", "pr_number": "201"}
        assert config.input_sets[2] == {"issue_number": "300", "pr_number": "301"}

    def test_load_config_file_not_found(self):
        """Test that FileNotFoundError is raised for missing file."""
        with pytest.raises(FileNotFoundError):
            load_config(Path("/nonexistent/config.yaml"))

    def test_load_minimal_config(self):
        """Test loading a minimal config."""
        content = """
workflow: test.yml
repo: o/r
"""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False
        ) as f:
            f.write(content)
            path = Path(f.name)

        try:
            config = load_config(path)
            assert config.workflow == "test.yml"
            assert config.repo == "o/r"
            assert config.inputs == {}
            assert config.limits.max_concurrent == 5  # default
        finally:
            path.unlink(missing_ok=True)


class TestComputeConfigHash:
    """Tests for config hash computation."""

    def test_hash_is_deterministic(self, temp_config_file):
        """Test that hash is deterministic."""
        hash1 = compute_config_hash(temp_config_file)
        hash2 = compute_config_hash(temp_config_file)
        assert hash1 == hash2

    def test_hash_length(self, temp_config_file):
        """Test that hash is 16 characters."""
        h = compute_config_hash(temp_config_file)
        assert len(h) == 16

    def test_different_files_different_hash(self):
        """Test that different files produce different hashes."""
        content1 = "workflow: a.yml\nrepo: o/r\n"
        content2 = "workflow: b.yml\nrepo: o/r\n"

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f1:
            f1.write(content1)
            path1 = Path(f1.name)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f2:
            f2.write(content2)
            path2 = Path(f2.name)

        try:
            hash1 = compute_config_hash(path1)
            hash2 = compute_config_hash(path2)
            assert hash1 != hash2
        finally:
            path1.unlink(missing_ok=True)
            path2.unlink(missing_ok=True)


class TestValidateConfig:
    """Tests for config validation."""

    def test_valid_config(self):
        """Test validation of a valid config."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
        )
        warnings = validate_config(config)
        assert len(warnings) == 0

    def test_high_concurrent_warning(self):
        """Test warning for high max_concurrent."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            limits=WorkflowLimits(max_concurrent=25),
        )
        warnings = validate_config(config)
        assert any("rate limiting" in w for w in warnings)

    def test_high_batch_size_warning(self):
        """Test warning for high batch_size."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            limits=WorkflowLimits(batch_size=100),
        )
        warnings = validate_config(config)
        assert any("batch_size" in w for w in warnings)

    def test_input_sets_inconsistent_keys(self):
        """Test warning for input_sets with inconsistent keys."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            input_sets=[
                {"a": 1, "b": 2},
                {"a": 3, "c": 4},  # Different keys
            ],
        )
        warnings = validate_config(config)
        assert any("different keys" in w for w in warnings)

    def test_input_sets_consistent_keys(self):
        """Test no warning when input_sets have consistent keys."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            input_sets=[
                {"a": 1, "b": 2},
                {"a": 3, "b": 4},
            ],
        )
        warnings = validate_config(config)
        assert not any("different keys" in w for w in warnings)


class TestConfigToYaml:
    """Tests for YAML serialization."""

    def test_basic_config_to_yaml(self):
        """Test serializing a basic config."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            inputs={"model": "sonnet"},
        )
        yaml_str = config_to_yaml(config)

        assert "workflow: test.yml" in yaml_str
        assert "repo: owner/repo" in yaml_str
        assert "model: sonnet" in yaml_str

    def test_config_with_description(self):
        """Test serializing config with description."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            description="My test config",
        )
        yaml_str = config_to_yaml(config)

        assert "description: My test config" in yaml_str

    def test_config_with_tags(self):
        """Test serializing config with tags."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            tags=["eval", "test"],
        )
        yaml_str = config_to_yaml(config)

        assert "tags:" in yaml_str

    def test_config_with_list_inputs(self):
        """Test serializing config with list inputs."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="owner/repo",
            inputs={"model": ["a", "b"]},
        )
        yaml_str = config_to_yaml(config)

        assert "model:" in yaml_str
        # List should be present
        assert "- a" in yaml_str or "['a'" in yaml_str or "[a," in yaml_str

    def test_roundtrip(self, temp_config_file):
        """Test that we can load and serialize back."""
        config = load_config(temp_config_file)
        yaml_str = config_to_yaml(config)

        # Should contain key elements
        assert "workflow:" in yaml_str
        assert "repo:" in yaml_str
