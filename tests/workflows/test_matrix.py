"""Tests for matrix expansion."""

import pytest

from ai4c_scribe.workflows.matrix import (
    expand_matrix,
    filter_existing,
    count_matrix_size,
)
from ai4c_scribe.workflows.models import (
    WorkflowConfig,
    MatrixJob,
)


class TestExpandMatrix:
    """Tests for matrix expansion."""

    def test_scalar_inputs_only(self):
        """Test expansion with only scalar inputs (no matrix)."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": "sonnet", "iter": 1},
        )
        jobs = expand_matrix(config, "abc123")

        assert len(jobs) == 1
        assert jobs[0].inputs == {"model": "sonnet", "iter": 1}

    def test_single_list_input(self):
        """Test expansion with one list input."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["sonnet", "opus"], "iter": 1},
        )
        jobs = expand_matrix(config, "abc123")

        assert len(jobs) == 2
        models = {j.inputs["model"] for j in jobs}
        assert models == {"sonnet", "opus"}
        # All should have iter=1
        assert all(j.inputs["iter"] == 1 for j in jobs)

    def test_cross_product(self):
        """Test cross-product expansion with multiple lists."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["a", "b"], "iter": [1, 2]},
        )
        jobs = expand_matrix(config, "abc123")

        assert len(jobs) == 4  # 2 x 2
        combinations = {(j.inputs["model"], j.inputs["iter"]) for j in jobs}
        assert combinations == {("a", 1), ("a", 2), ("b", 1), ("b", 2)}

    def test_three_way_cross_product(self):
        """Test cross-product with three list inputs."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={
                "model": ["a", "b"],
                "config": ["x", "y"],
                "iter": [1, 2],
            },
        )
        jobs = expand_matrix(config, "abc123")

        assert len(jobs) == 8  # 2 x 2 x 2

    def test_input_sets(self):
        """Test input_sets (zipped) expansion."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": "sonnet"},
            input_sets=[
                {"issue_number": 100, "pr_number": 101},
                {"issue_number": 200, "pr_number": 201},
                {"issue_number": 300, "pr_number": 301},
            ],
        )
        jobs = expand_matrix(config, "abc123")

        # Should be 3 jobs (from input_sets), not 9 (cross-product)
        assert len(jobs) == 3

        # Check the pairing is preserved
        issue_pr_pairs = {(j.inputs["issue_number"], j.inputs["pr_number"]) for j in jobs}
        assert issue_pr_pairs == {(100, 101), (200, 201), (300, 301)}

        # All should have model=sonnet
        assert all(j.inputs["model"] == "sonnet" for j in jobs)

    def test_input_sets_with_matrix(self):
        """Test input_sets combined with matrix expansion."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["sonnet", "opus"]},
            input_sets=[
                {"issue": 1, "pr": 10},
                {"issue": 2, "pr": 20},
            ],
        )
        jobs = expand_matrix(config, "abc123")

        # 2 models x 2 input_sets = 4 jobs
        assert len(jobs) == 4

        # Check all combinations exist
        combos = {(j.inputs["model"], j.inputs["issue"], j.inputs["pr"]) for j in jobs}
        expected = {
            ("sonnet", 1, 10),
            ("sonnet", 2, 20),
            ("opus", 1, 10),
            ("opus", 2, 20),
        }
        assert combos == expected

    def test_empty_inputs(self):
        """Test expansion with no inputs."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        jobs = expand_matrix(config, "abc123")

        assert len(jobs) == 1
        assert jobs[0].inputs == {}

    def test_job_metadata(self):
        """Test that expanded jobs have correct metadata."""
        config = WorkflowConfig(
            workflow="my-workflow.yml",
            repo="owner/repo",
            inputs={"model": ["a", "b"]},
        )
        jobs = expand_matrix(config, "config_hash_123")

        for job in jobs:
            assert job.workflow == "my-workflow.yml"
            assert job.repo == "owner/repo"
            assert job.config_hash == "config_hash_123"
            assert len(job.job_id) > 0  # UUID
            assert len(job.params_hash) == 16

    def test_unique_params_hash(self):
        """Test that different parameter combinations get unique hashes."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["a", "b", "c"]},
        )
        jobs = expand_matrix(config, "abc123")

        hashes = {j.params_hash for j in jobs}
        assert len(hashes) == 3  # All unique


class TestFilterExisting:
    """Tests for deduplication filtering."""

    def test_filter_none_existing(self):
        """Test when no jobs already exist."""
        jobs = [
            MatrixJob(
                job_id="1",
                config_hash="c",
                params_hash="hash_a",
                workflow="w",
                repo="r",
                inputs={},
            ),
            MatrixJob(
                job_id="2",
                config_hash="c",
                params_hash="hash_b",
                workflow="w",
                repo="r",
                inputs={},
            ),
        ]
        filtered, skipped = filter_existing(jobs, set())

        assert len(filtered) == 2
        assert skipped == 0

    def test_filter_some_existing(self):
        """Test filtering out some existing jobs."""
        jobs = [
            MatrixJob(
                job_id="1",
                config_hash="c",
                params_hash="existing_hash",
                workflow="w",
                repo="r",
                inputs={},
            ),
            MatrixJob(
                job_id="2",
                config_hash="c",
                params_hash="new_hash",
                workflow="w",
                repo="r",
                inputs={},
            ),
        ]
        filtered, skipped = filter_existing(jobs, {"existing_hash"})

        assert len(filtered) == 1
        assert filtered[0].params_hash == "new_hash"
        assert skipped == 1

    def test_filter_all_existing(self):
        """Test when all jobs already exist."""
        jobs = [
            MatrixJob(
                job_id="1",
                config_hash="c",
                params_hash="hash_a",
                workflow="w",
                repo="r",
                inputs={},
            ),
            MatrixJob(
                job_id="2",
                config_hash="c",
                params_hash="hash_b",
                workflow="w",
                repo="r",
                inputs={},
            ),
        ]
        filtered, skipped = filter_existing(jobs, {"hash_a", "hash_b"})

        assert len(filtered) == 0
        assert skipped == 2

    def test_filter_empty_jobs(self):
        """Test filtering empty job list."""
        filtered, skipped = filter_existing([], {"some_hash"})

        assert len(filtered) == 0
        assert skipped == 0


class TestCountMatrixSize:
    """Tests for matrix size counting."""

    def test_scalar_only(self):
        """Test count with only scalar inputs."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": "sonnet", "iter": 1},
        )
        assert count_matrix_size(config) == 1

    def test_single_list(self):
        """Test count with one list."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["a", "b", "c"]},
        )
        assert count_matrix_size(config) == 3

    def test_cross_product(self):
        """Test count for cross-product."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["a", "b"], "iter": [1, 2, 3]},
        )
        assert count_matrix_size(config) == 6  # 2 x 3

    def test_with_input_sets(self):
        """Test count with input_sets."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={"model": ["a", "b"]},
            input_sets=[
                {"issue": 1, "pr": 10},
                {"issue": 2, "pr": 20},
                {"issue": 3, "pr": 30},
            ],
        )
        # 2 models x 3 input_sets = 6
        assert count_matrix_size(config) == 6

    def test_empty_inputs(self):
        """Test count with no inputs."""
        config = WorkflowConfig(
            workflow="test.yml",
            repo="o/r",
            inputs={},
        )
        assert count_matrix_size(config) == 1
