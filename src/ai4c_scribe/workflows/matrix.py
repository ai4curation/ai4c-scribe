"""Matrix expansion for workflow inputs.

Expands list-valued inputs into individual job combinations.
Supports:
- Cross-product expansion (default for list inputs)
- Input sets for related inputs that should be zipped together
- Deduplication against existing runs

Example:
    >>> from ai4c_scribe.workflows.models import WorkflowConfig
    >>> config = WorkflowConfig(
    ...     workflow="test.yml",
    ...     repo="o/r",
    ...     inputs={"model": ["a", "b"], "iter": 1},
    ... )
    >>> jobs = expand_matrix(config, "abc123")
    >>> len(jobs)
    2
"""

import itertools
import uuid

from ai4c_scribe.workflows.db import compute_params_hash
from ai4c_scribe.workflows.models import (
    InputValue,
    MatrixJob,
    WorkflowConfig,
)


def expand_matrix(config: WorkflowConfig, config_hash: str) -> list[MatrixJob]:
    """Expand config into individual matrix jobs.

    Handles:
    - Scalar inputs (pass through)
    - List inputs (cross-product expansion)
    - Input sets (zipped combinations, each dict is one row)

    Args:
        config: Workflow configuration
        config_hash: Hash of the config file

    Returns:
        List of MatrixJob objects, one per combination

    Example:
        >>> config = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": ["a", "b"], "iter": 1},
        ... )
        >>> jobs = expand_matrix(config, "abc123")
        >>> len(jobs)
        2
        >>> jobs[0].inputs["iter"]
        1

        >>> # With only scalars
        >>> config2 = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": "sonnet", "iter": 1},
        ... )
        >>> jobs2 = expand_matrix(config2, "def456")
        >>> len(jobs2)
        1

        >>> # With input_sets
        >>> config3 = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": ["a", "b"]},
        ...     input_sets=[
        ...         {"issue": "10", "pr": "11"},
        ...         {"issue": "20", "pr": "21"},
        ...     ],
        ... )
        >>> jobs3 = expand_matrix(config3, "xyz789")
        >>> len(jobs3)  # 2 models x 2 input_sets = 4
        4
    """
    # Separate scalar and matrix inputs
    scalar_inputs: dict[str, InputValue] = {}
    matrix_inputs: dict[str, list[InputValue]] = {}

    for name, value in config.inputs.items():
        if isinstance(value, list):
            matrix_inputs[name] = value
        else:
            scalar_inputs[name] = value

    # Generate cross-product for matrix inputs
    if matrix_inputs:
        keys = list(matrix_inputs.keys())
        value_lists = [matrix_inputs[k] for k in keys]
        cross_product = list(itertools.product(*value_lists))
    else:
        keys = []
        cross_product = [()]  # Single empty combination

    # Combine everything
    jobs = []

    # If we have input_sets, combine them with cross-product
    if config.input_sets:
        for input_set in config.input_sets:
            for cross_combo in cross_product:
                inputs: dict[str, InputValue] = dict(scalar_inputs)
                inputs.update(input_set)
                inputs.update(dict(zip(keys, cross_combo)))

                job = _create_job(config, config_hash, inputs)
                jobs.append(job)
    else:
        for cross_combo in cross_product:
            inputs = dict(scalar_inputs)
            inputs.update(dict(zip(keys, cross_combo)))

            job = _create_job(config, config_hash, inputs)
            jobs.append(job)

    return jobs


def _create_job(
    config: WorkflowConfig,
    config_hash: str,
    inputs: dict[str, InputValue],
) -> MatrixJob:
    """Create a MatrixJob from inputs.

    Args:
        config: Source workflow config
        config_hash: Hash of the config file
        inputs: Concrete input values

    Returns:
        New MatrixJob instance
    """
    return MatrixJob(
        job_id=str(uuid.uuid4()),
        config_hash=config_hash,
        params_hash=compute_params_hash(inputs),
        workflow=config.workflow,
        repo=config.repo,
        inputs=inputs,
    )


def filter_existing(
    jobs: list[MatrixJob],
    existing_hashes: set[str],
) -> tuple[list[MatrixJob], int]:
    """Filter out jobs that already exist.

    Args:
        jobs: List of jobs to filter
        existing_hashes: Set of params_hash values that already exist

    Returns:
        Tuple of (filtered_jobs, skipped_count)

    Example:
        >>> from ai4c_scribe.workflows.models import MatrixJob
        >>> job1 = MatrixJob(
        ...     job_id="1",
        ...     config_hash="c",
        ...     params_hash="existing_hash",
        ...     workflow="w",
        ...     repo="r",
        ...     inputs={},
        ... )
        >>> job2 = MatrixJob(
        ...     job_id="2",
        ...     config_hash="c",
        ...     params_hash="new_hash",
        ...     workflow="w",
        ...     repo="r",
        ...     inputs={},
        ... )
        >>> filtered, skipped = filter_existing([job1, job2], {"existing_hash"})
        >>> len(filtered)
        1
        >>> skipped
        1
        >>> filtered[0].params_hash
        'new_hash'
    """
    new_jobs = []
    skipped = 0

    for job in jobs:
        if job.params_hash in existing_hashes:
            skipped += 1
        else:
            new_jobs.append(job)

    return new_jobs, skipped


def count_matrix_size(config: WorkflowConfig) -> int:
    """Count the total number of jobs that would be created.

    Useful for showing dry-run information without actually expanding.

    Args:
        config: Workflow configuration

    Returns:
        Number of jobs that would be created

    Example:
        >>> config = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": ["a", "b"], "iter": [1, 2, 3]},
        ... )
        >>> count_matrix_size(config)
        6

        >>> # With input_sets
        >>> config2 = WorkflowConfig(
        ...     workflow="test.yml",
        ...     repo="o/r",
        ...     inputs={"model": ["a", "b"]},
        ...     input_sets=[{"x": 1}, {"x": 2}, {"x": 3}],
        ... )
        >>> count_matrix_size(config2)
        6
    """
    # Count matrix dimensions from list inputs
    matrix_size = 1

    for value in config.inputs.values():
        if isinstance(value, list):
            matrix_size *= len(value)

    # Multiply by input_sets size (if any)
    if config.input_sets:
        matrix_size *= len(config.input_sets)

    return matrix_size
