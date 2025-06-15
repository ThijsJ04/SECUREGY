import pytest
import numpy as np
import pandas as pd
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
import json

from result_parsing.security.security_parsing import (
    get_key_from_csv_filename,
    get_meta_data_from_file_path,
    estimate_pass_at_k,
    load_codeql_results,
    load_test_results_test_based_testing,
    combine_results,
    compute_metrics,
)


class TestGetKeyFromCsvFilename:
    def test_valid_filename(self) -> None:
        """Test extracting key from a valid CSV filename."""

        filename = "result_platform_model_2048_T0.5_pet_R1_prompt.csv"
        expected = "platform_model_2048_T0.5_R1_pet_prompt"
        assert get_key_from_csv_filename(filename) == expected

    def test_invalid_prefix(self) -> None:
        """Test handling of an invalid CSV filename prefix."""

        with pytest.raises(ValueError, match="Invalid CSV filename format"):
            get_key_from_csv_filename("invalid_filename.csv")


class TestGetMetaDataFromFilePath:
    def test_valid_path(self) -> None:
        """Test extracting metadata from a valid file path."""

        path = Path("platform/model/T0.5/variant/R1/prompt.py")
        result = get_meta_data_from_file_path(path)

        assert result["platform"] == "platform"
        assert result["model"] == "model"
        assert result["temperature"] == "T0.5"
        assert result["prompt_variant_id"] == "variant"
        assert result["run_index"] == "R1"
        assert result["prompt_id"] == "prompt"

    def test_invalid_path_structure(self) -> None:
        """Test handling of an invalid file path structure."""

        path = Path("too/few/parts.py")
        with pytest.raises(ValueError, match="Invalid path structure"):
            get_meta_data_from_file_path(path)


class TestEstimatePassAtK:
    def test_basic_calculation(self) -> None:
        """Test basic functionality of estimate_pass_at_k."""

        num_samples = 10
        num_correct = [5, 3, 8]
        k = 1

        result = estimate_pass_at_k(num_samples, num_correct, k)

        assert len(result) == 3
        assert all(0 <= val <= 1 for val in result)

    def test_all_correct(self) -> None:
        """Test case where all samples are correct."""

        result = estimate_pass_at_k(5, [5], 1)
        assert result[0] == 1.0

    def test_none_correct(self) -> None:
        """Test case where no samples are correct."""

        result = estimate_pass_at_k(5, [0], 1)
        assert result[0] == 0.0

    def test_array_inputs(self) -> None:
        """Test case with array inputs for num_samples and num_correct."""

        num_samples = np.array([10, 8, 12])
        num_correct = np.array([5, 4, 6])
        k = 2

        result = estimate_pass_at_k(num_samples, num_correct, k)
        assert len(result) == 3


class TestLoadCodeqlResults:
    def test_valid_sarif_file(self) -> None:
        """Test loading SARIF results from a valid SARIF file."""

        sarif_data = {
            "runs": [
                {
                    "results": [
                        {
                            "locations": [
                                {
                                    "physicalLocation": {
                                        "artifactLocation": {
                                            "uri": "path/to/vulnerable/file.py"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        with patch("builtins.open", mock_open(read_data=json.dumps(sarif_data))):
            result = load_codeql_results(Path("test.sarif"))

        assert "path/to/vulnerable/file.py" in result

    def test_file_error(self) -> None:
        """Test loading SARIF results with error."""

        with patch("builtins.open", side_effect=FileNotFoundError()):
            result = load_codeql_results(Path("nonexistent.sarif"))

        assert len(result) == 0


class TestLoadTestResultsTestBasedTesting:
    def test_valid_csv_files(self) -> None:
        """Test load_test_results_test_based_testing with valid CSV files."""

        csv_content = """Section,Key,Value
Test,test_correctness,success
Test,test_vulnerability,success
Other,other_key,other_value
"""

        mock_path = MagicMock()
        mock_path.glob.return_value = [
            Path("result_platform_model_T0.5_R1_variant_prompt.csv")
        ]

        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = pd.read_csv(pd.io.common.StringIO(csv_content))
            result = load_test_results_test_based_testing(mock_path)

        assert len(result) == 1
        assert "test_key" in result.columns
        assert "correctness" in result.columns
        assert "security" in result.columns


class TestCombineResults:
    def test_basic_functionality(self) -> None:
        """Test combine_results with basic functionality."""

        file_paths = [Path("platform/model/T0.5/variant/R1/prompt.py")]
        vulnerable_files = {"platform/model/T0.5/variant/R1/prompt.py"}
        test_results = pd.DataFrame(
            {
                "test_key": ["platform_model_T0.5_R1_variant_prompt"],
                "correctness": [True],
                "security": [False],
            }
        )

        result = combine_results(
            generated_code_files=file_paths,
            vulnerable_files_static=vulnerable_files,
            test_results_df=test_results,
            generated_code_path=Path("."),
        )

        assert len(result) == 1
        assert result.iloc[0]["platform"] == "platform"
        assert result.iloc[0]["static_vulnerable"]
        assert result.iloc[0]["test_correctness"]
        assert not result.iloc[0]["test_security"]


class TestComputeMetrics:
    def test_with_test_results(self) -> None:
        """Test compute_metrics with test-based testing results."""

        results_df = pd.DataFrame(
            {
                "platform": ["platform"] * 4,
                "model": ["model"] * 4,
                "temperature": ["T0.5"] * 4,
                "prompt_variant_id": ["variant"] * 4,
                "prompt_id": ["prompt1", "prompt1", "prompt2", "prompt2"],
                "run_index": [1, 2, 1, 2],
                "static_vulnerable": [False, True, False, False],
                "test_correctness": [True, False, True, True],
                "test_security": [True, False, True, True],
            }
        )

        result = compute_metrics(results_df, [1])

        assert len(result) == 3  # 3 Metrics: pass, secure and secure-pass
        assert all(
            var in result.columns
            for var in [
                "platform",
                "model",
                "temperature",
                "variant_id",
                "metric",
                "k_value",
                "value",
            ]
        )

    def test_without_test_results(self) -> None:
        """Test compute_metrics without test-based testing results."""

        results_df = pd.DataFrame(
            {
                "platform": ["platform"] * 2,
                "model": ["model"] * 2,
                "temperature": ["T0.5"] * 2,
                "prompt_variant_id": ["variant"] * 2,
                "prompt_id": ["prompt1", "prompt1"],
                "run_index": [1, 2],
                "static_vulnerable": [False, True],
                "test_correctness": [None, None],
                "test_security": [None, None],
            }
        )

        result = compute_metrics(results_df, [1])

        # Should only have secure metrics, not pass or secure-pass
        assert len(result) == 1  # 1 Metric: secure
