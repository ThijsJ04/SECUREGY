import pandas as pd
from unittest.mock import patch
from result_parsing._extras.get_error_rates import (
    clean_error_message,
    get_error_rates,
)


class TestGetErrorRates:
    def test_clean_error_message(self) -> None:
        """Test cleaning of error messages."""

        test_cases = [
            ("Error running test for variant", "Error running test"),
            ("Process timeout after 30 seconds", "Process timeout"),
            ("Process failed with return code 1", "Process failed"),
            ("Unknown error occurred", "Unknown error occurred"),
        ]

        for input_msg, expected in test_cases:
            assert clean_error_message(input_msg) == expected

    def test_get_error_rates(self, tmp_path):
        """Test that get_error_rates creates correct error data and output CSV."""

        mock_df = pd.DataFrame(
            {
                "Section": ["Error"] * 5,
                "Key": ["execution_error"] * 5,
                "Value": ["error"] * 5,
                "Message": [
                    "Process timeout after 600 seconds for C:\\Users...",
                    "Process timeout after 600 seconds for C:\\Users...",
                    "Process failed with return code 1.",
                    "Process failed with return code 1.",
                    "Process failed with return code 1.",
                ],
                "Run_Number": [None] * 5,
                "platform": ["Ollama"] * 5,
                "model": ["deepseek-r1_16384"] * 5,
                "temperature": [0.5] * 5,
                "prompt_variant_id": ["base"] * 5,
                "run_index": [2.0, 3.0, 2.0, 6.0, 3.0],
                "prompt_id": [
                    "Tainted_Author_A_cwe094_0",
                    "Tainted_Author_A_cwe089_0",
                    "Tainted_Author_A_cwe089_0",
                    "Matching_Author_A_cwe502_0",
                    "Assertion_Author_A_cwe079_0",
                ],
            }
        )

        output_path = tmp_path / "error_summary.csv"
        with patch(
            "result_parsing._extras.get_error_rates.transform_test_based_results_to_pd",
            return_value=mock_df,
        ):
            get_error_rates(str(output_path))

        df = pd.read_csv(output_path)
        # Should have one row of data (plus header)
        assert df.shape[0] == 1
        assert "Total Errors (max 100)" in df.columns
        assert df["Total Errors (max 100)"].iloc[0] == 5
