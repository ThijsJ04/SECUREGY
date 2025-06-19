from itertools import repeat
from json import load as json_load
import numpy as np
from os import makedirs
from pathlib import Path
import pandas as pd
import sys
from typing import List, Set, TypedDict, Union

from result_parsing.security.security_figures import (
    create_heatmap_to_base,
    create_heatmap_between_bases,
)


def get_key_from_csv_filename(csv_filename: str) -> str:
    """
    Extracts a key from a CSV filename that follows the format:
    result_<platform>_<model>_T<temperature>_<prompt_variant_id>_R<run_index>_<prompt_id>.csv

    Args:
        csv_filename (str): The CSV filename to extract the key from.

    Raises:
        ValueError: If the CSV filename format is invalid.
        ValueError: If the temperature is not found.
        ValueError: If the run index is not found.

    Returns:
        str: The extracted key in the format:
        <platform>_<model>_<temperature>_<run_index>_<prompt_variant_id>_<prompt_id>
    """

    if not csv_filename.startswith("result_"):
        raise ValueError(f"Invalid CSV filename format: {csv_filename}")

    # Remove 'result_' prefix and '.csv' suffix
    parts = csv_filename[7:-4].split("_")

    if len(parts) < 6:
        raise ValueError(f"Invalid CSV filename format: {csv_filename}")

    platform = parts[0]

    # Find temperature and run indices
    temp_idx = run_idx = None
    for i, part in enumerate(parts[1:], 1):
        if temp_idx is None and part.startswith("T"):
            temp_idx = i
        elif temp_idx is not None and run_idx is None and part.startswith("R"):
            run_idx = i
            break

    if temp_idx is None:
        raise ValueError(
            f"Cannot find temperature in filename: {csv_filename}", file=sys.stderr
        )

    if run_idx is None:
        raise ValueError(
            f"Cannot find run index in filename: {csv_filename}", file=sys.stderr
        )

    # Extract components
    model = "_".join(parts[1:temp_idx])
    temperature = parts[temp_idx]
    prompt_variant_id = "_".join(parts[temp_idx + 1 : run_idx])
    run_index = parts[run_idx]
    prompt_id = "_".join(parts[run_idx + 1 :])

    return (
        f"{platform}_{model}_{temperature}_{run_index}_{prompt_variant_id}_{prompt_id}"
    )


class FileMetaData(TypedDict):
    platform: str
    model: str
    temperature: str
    prompt_variant_id: str
    run_index: str
    prompt_id: str


def get_meta_data_from_file_path(file_path: Path) -> FileMetaData:
    """
    Extracts metadata from a file path that follows the structure:
    <platform>/<model>/<temperature>/<prompt_variant_id>/<run_index>/<prompt_id>.py

    Args:
        file_path (Path): The file path to extract metadata from.

    Raises:
        ValueError: If the file path structure is invalid.

    Returns:
        FileMetaData: The extracted metadata.
    """

    parts = file_path.parts

    if len(parts) < 5:
        raise ValueError(f"Invalid path structure: {file_path}")

    return FileMetaData(
        platform=parts[0],
        model=parts[1],
        temperature=parts[2],
        prompt_variant_id=parts[3],
        run_index=parts[4],
        prompt_id=file_path.stem,
    )


def estimate_pass_at_k(
    num_samples: Union[int, List[int], np.ndarray],
    num_correct: Union[List[int], np.ndarray],
    k: int,
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.

    Acknowledgment:
    Retrieved from the repository [SALLM: Security Assessment of Generated Code](https://github.com/s2e-lab/SALLM/tree/main),
    commit 2d87b63 from file `Evaluation/pass_at_k_tests.py` on 10-06-2025.
    """

    def estimator(n: int, c: int, k: int) -> float:
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array(
        [estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)]
    )


def load_codeql_results(codeql_result_path: Path) -> Set[str]:
    """
    Load CodeQL results from a SARIF file and extract vulnerable file paths.

    Args:
        codeql_result_path (Path): The path to the CodeQL SARIF file.

    Returns:
        Set[str]: A set of vulnerable file paths.
    """

    vulnerable_files = set()

    try:
        with open(codeql_result_path, "r") as file:
            sarif_data = json_load(file)

            # Extract file paths from SARIF results
            for run in sarif_data.get("runs", []):
                for result in run.get("results", []):
                    for location in result.get("locations", []):
                        physical_location = location.get("physicalLocation", {})
                        artifact_location = physical_location.get(
                            "artifactLocation", {}
                        )
                        uri = artifact_location.get("uri", "")
                        if uri:
                            normalized_path = str(Path(uri)).replace("\\", "/")
                            vulnerable_files.add(normalized_path)
    except Exception as e:
        print(f"Error loading CodeQL results: {e}", file=sys.stderr)

    return vulnerable_files


def load_test_results_test_based_testing(
    test_based_testing_result_path: Path,
) -> pd.DataFrame:
    """
    Load test results from CSV files in the specified directory.
    This function reads all CSV files in the directory, extracts test results,
    and returns them as a DataFrame. The DataFrame is empty if no valid test results are found.

    Args:
        test_based_testing_result_path (Path): The path to the test-based testing results directory.

    Returns:
        pd.DataFrame: A DataFrame containing the test results.
    """

    test_results = []
    csv_files = list(test_based_testing_result_path.glob("*.csv"))

    for csv_file in csv_files:
        try:
            key = get_key_from_csv_filename(csv_file.name)

            df = pd.read_csv(csv_file, usecols=["Section", "Key", "Value"])
            test_rows = df[df["Section"] == "Test"]

            # Filter for relevant test types
            correctness_rows = test_rows[
                test_rows["Key"].str.contains("test_correctness", na=False)
            ]
            security_rows = test_rows[
                test_rows["Key"].str.contains("test_vulnerability", na=False)
            ]

            correctness_passed = False
            security_passed = False

            if not correctness_rows.empty:
                correctness_passed = (correctness_rows["Value"] != "failure").any()

            if not security_rows.empty:
                security_passed = (security_rows["Value"] != "failure").any()

            test_results.append(
                {
                    "test_key": key,
                    "correctness": correctness_passed,
                    "security": security_passed,
                }
            )

        except Exception as e:
            print(f"Error processing {csv_file}: {e}", file=sys.stderr)

    return (
        pd.DataFrame(test_results)
        if test_results
        else pd.DataFrame(columns=["test_key", "correctness", "security"])
    )


def combine_results(
    generated_code_files: List[Path],
    vulnerable_files_static: Set[str],
    test_results_df: pd.DataFrame,
    generated_code_path: Path,
) -> pd.DataFrame:
    """
    Create a DataFrame containing results from generated code files, static vulnerability analysis,
    and test-based testing results.

    Args:
        generated_code_files (List[Path]): List of paths to generated code files.
        vulnerable_files_static (Set[str]): Set of paths to statically identified vulnerable files.
        test_results_df (pd.DataFrame): DataFrame containing test results.
        generated_code_path (Path): Path to the directory containing generated code files.

    Returns:
        pd.DataFrame: A DataFrame containing the results.
    """

    results_data = []

    for file_path in generated_code_files:
        relative_file_path = file_path.relative_to(generated_code_path)
        file_meta_data = get_meta_data_from_file_path(relative_file_path)

        is_static_vulnerable = (
            str(relative_file_path).replace("\\", "/") in vulnerable_files_static
        )

        test_key = (
            f"{file_meta_data['platform']}_"
            f"{file_meta_data['model']}_"
            f"{file_meta_data['temperature']}_"
            f"{file_meta_data['run_index']}_"
            f"{file_meta_data['prompt_variant_id']}_"
            f"{file_meta_data['prompt_id']}"
        )

        # Get test results if available
        test_result = test_results_df[test_results_df["test_key"] == test_key]
        test_correctness = (
            test_result["correctness"].iloc[0] if not test_result.empty else None
        )
        test_security = (
            test_result["security"].iloc[0] if not test_result.empty else None
        )

        results_data.append(
            {
                "platform": file_meta_data["platform"],
                "model": file_meta_data["model"],
                "temperature": file_meta_data["temperature"],
                "prompt_variant_id": file_meta_data["prompt_variant_id"],
                "prompt_id": file_meta_data["prompt_id"],
                "run_index": int(file_meta_data["run_index"].replace("R", "")),
                "file_path": str(relative_file_path),
                "static_vulnerable": is_static_vulnerable,
                "test_correctness": test_correctness,
                "test_security": test_security,
                "model_key": f"{file_meta_data['platform']}_{file_meta_data['model']}_{file_meta_data['temperature']}",
            }
        )

    return pd.DataFrame(results_data)


def compute_metrics(
    results_df: pd.DataFrame,
    k_values: List[int],
) -> pd.DataFrame:
    """
    Compute security metrics from the results data.
    This function calculates the following metrics for each configuration:
    - pass@k: Probability of at least one correct sample
    - secure@k: Probability of at least one secure sample (not vulnerable)
    - secure-pass@k: Probability of at least one sample that is both correct and secure

    Note:
    - If test-based results are available, they will be used for correctness and security.
    - If test-based results are not available, static analysis results will be used for security
        and correctness metrics will not be computed, since they are not available from static analysis.

    Args:
        results_data (Dict[str, List[ResultDataItem]]): The results data to compute metrics from.
        k_values (List[int]): The list of k values to compute metrics for.

    Returns:
        Dict[str, Dict[str, Dict[str, float]]]: A dictionary containing computed metrics for each configuration.
    """

    metrics_data = []

    # Check if we have test-based results
    has_test_results = results_df["test_correctness"].notna().any()

    # Group by configuration
    config_groups = results_df.groupby(
        ["platform", "model", "temperature", "prompt_variant_id"]
    )

    for (
        platform,
        model,
        temperature,
        prompt_variant_id,
    ), config_group in config_groups:
        # Group by prompt_id within configuration
        prompt_groups = config_group.groupby("prompt_id")

        total_samples = []
        correct_samples = []
        secure_samples = []
        secure_pass_samples = []

        for prompt_id, prompt_group in prompt_groups:
            if has_test_results:
                # Use test-based results
                passed = prompt_group["test_correctness"].tolist()
                secure = prompt_group["test_security"].tolist()
                secure_and_correct = [
                    corr and sec
                    for corr, sec in zip(
                        prompt_group["test_correctness"], prompt_group["test_security"]
                    )
                ]
            else:
                # Fall back to static analysis results
                passed = []  # Cannot compute correctness from static analysis
                secure = (
                    ~prompt_group["static_vulnerable"]
                ).tolist()  # Invert vulnerability
                secure_and_correct = []  # Cannot compute without correctness

            total_samples.append(len(secure) if not has_test_results else len(passed))
            correct_samples.append(sum(passed) if passed else 0)
            secure_samples.append(sum(secure))
            secure_pass_samples.append(
                sum(secure_and_correct) if secure_and_correct else 0
            )

        # Skip if no valid samples
        if not total_samples:
            continue

        total_samples = np.array(total_samples)
        correct_samples = np.array(correct_samples)
        secure_samples = np.array(secure_samples)
        secure_pass_samples = np.array(secure_pass_samples)

        # Calculate metrics for each k value
        for k in k_values:
            if (total_samples >= k).all():
                # pass@k: probability of at least one correct sample
                if has_test_results:
                    pass_at_k_value = (
                        estimate_pass_at_k(total_samples, correct_samples, k).mean()
                    ) * 100
                    metrics_data.append(
                        {
                            "platform": platform,
                            "model": model,
                            "temperature": temperature,
                            "variant_id": prompt_variant_id,
                            "metric": "pass",
                            "k_value": str(k),
                            "value": pass_at_k_value,
                        }
                    )

                # secure@k: probability of at least one secure sample
                secure_at_k_value = (
                    estimate_pass_at_k(total_samples, secure_samples, k).mean()
                ) * 100
                metrics_data.append(
                    {
                        "platform": platform,
                        "model": model,
                        "temperature": temperature,
                        "variant_id": prompt_variant_id,
                        "metric": "secure",
                        "k_value": str(k),
                        "value": secure_at_k_value,
                    }
                )

                # secure-pass@k: probability of at least one sample that is both correct and secure
                if has_test_results:
                    secure_pass_at_k_value = (
                        estimate_pass_at_k(total_samples, secure_pass_samples, k).mean()
                    ) * 100
                    metrics_data.append(
                        {
                            "platform": platform,
                            "model": model,
                            "temperature": temperature,
                            "variant_id": prompt_variant_id,
                            "metric": "secure-pass",
                            "k_value": str(k),
                            "value": secure_pass_at_k_value,
                        }
                    )

    return pd.DataFrame(metrics_data)


def parse_security_results(k_values: List[int]) -> pd.DataFrame:
    """
    Parse security results and return metrics as a DataFrame.

    Returns:
        pd.DataFrame: DataFrame with columns: model_key, variant_id, metric, k_value, value
    """

    generated_code_files = list(
        (Path.cwd() / "generation" / "generated_code").rglob("*.py")
    )
    if len(generated_code_files) == 0:
        raise FileNotFoundError(
            "No generated code files found in 'generation/generated_code' directory."
        )

    codeql_result_path = Path.cwd() / "evaluation" / "CodeQL_results" / "results.sarif"
    if not codeql_result_path.exists():
        raise FileNotFoundError(
            f"CodeQL results file not found at {codeql_result_path}. "
            "Please ensure CodeQL analysis has been run."
        )

    test_based_testing_result_path = Path.cwd() / "evaluation" / "results"
    if not test_based_testing_result_path.exists():
        raise FileNotFoundError(
            f"Test-based testing results directory not found at {test_based_testing_result_path}. "
            "Please ensure test-based testing has been run."
        )

    vulnerable_files_static = load_codeql_results(codeql_result_path)
    test_results_df = load_test_results_test_based_testing(
        test_based_testing_result_path
    )
    generated_code_path = Path.cwd() / "generation" / "generated_code"

    results_df = combine_results(
        generated_code_files,
        vulnerable_files_static,
        test_results_df,
        generated_code_path,
    )

    computed_metrics = compute_metrics(results_df, k_values)

    makedirs("result_parsing/results", exist_ok=True)

    heatmap_to_base = create_heatmap_to_base(computed_metrics)
    heatmap_to_base.savefig("result_parsing/results/security_heatmap_to_base.png")

    heatmap_between_bases = create_heatmap_between_bases(computed_metrics)
    heatmap_between_bases.savefig(
        "result_parsing/results/security_heatmap_between_bases.png"
    )
