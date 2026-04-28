"""Tests for runner configuration loading."""


import pytest
import yaml

from ai4c_scribe.runner import (
    get_config_path,
    load_runner_config,
)


def test_get_config_path(tmp_path):
    """Test config path generation."""
    path = get_config_path(tmp_path)
    assert path == tmp_path / ".ai4cscribe" / "runner.yaml"


def test_load_runner_config(tmp_path):
    """Test loading configuration from YAML."""
    config_dir = tmp_path / ".ai4cscribe"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "runner.yaml"

    config_data = {
        "experiment_id": "exp001",
        "system_prompt": "You are a helpful assistant.",
        "agent_timeout": 300,
    }

    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    config = load_runner_config(tmp_path)
    assert config.experiment_id == "exp001"
    assert config.system_prompt == "You are a helpful assistant."
    assert config.agent_timeout == 300


def test_load_runner_config_not_found(tmp_path):
    """Test loading config raises FileNotFoundError when missing."""
    with pytest.raises(FileNotFoundError, match="Config file not found"):
        load_runner_config(tmp_path)


def test_load_runner_config_custom_path(tmp_path):
    """Test loading config from custom path."""
    custom_config = tmp_path / "custom-config.yaml"

    config_data = {"experiment_id": "custom-exp"}

    with open(custom_config, "w") as f:
        yaml.dump(config_data, f)

    config = load_runner_config(tmp_path, config_path=custom_config)
    assert config.experiment_id == "custom-exp"
