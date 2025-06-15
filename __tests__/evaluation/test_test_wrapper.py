import pytest
from os import path, unlink
from tempfile import NamedTemporaryFile
from unittest.mock import Mock, patch

from evaluation.test_wrapper import CSVTestResult, run_emission_test, run


class TestTestWrapper:
    @pytest.fixture
    def mock_test(self) -> Mock:
        """Create a mock test object for testing."""

        mock_test = Mock()
        mock_test.id.return_value = "test_example"
        return mock_test

    def test_csv_test_result_add_success(self, mock_test: Mock) -> None:
        """Test adding successful test result."""

        result = CSVTestResult(None, None, 0)
        result.addSuccess(mock_test)

        assert len(result.results) == 1
        assert result.results[0] == ("test_example", "success", "")

    def test_csv_test_result_add_error(self, mock_test: Mock) -> None:
        """Test adding error test result."""

        result = CSVTestResult(None, None, 0)
        error = (Exception, Exception("Test error"), None)

        result.addError(mock_test, error)

        assert len(result.results) == 1
        assert result.results[0] == ("test_example", "error", "Test error")

    def test_csv_test_result_add_failure(self, mock_test: Mock) -> None:
        """Test adding failure test result."""

        result = CSVTestResult(None, None, 0)
        error = (AssertionError, AssertionError("Test failed"), None)

        result.addFailure(mock_test, error)

        assert len(result.results) == 1
        assert result.results[0] == ("test_example", "failure", "Test failed")

    def test_save_to_csv(self) -> None:
        """Test saving results to CSV."""

        result = CSVTestResult(None, None, 0)
        result.results = [("test_1", "success", "")]
        emissions_data = [
            {
                "emissions_kgCO2eq": 0.001,
                "duration_seconds": 1.0,
                "energy_consumed_kwh": 0.0001,
            },
            {
                "emissions_kgCO2eq": 0.002,
                "duration_seconds": 1.1,
                "energy_consumed_kwh": 0.0002,
            },
        ]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
            filename = f.name

        try:
            result.save_to_csv(filename, emissions_data)

            with open(filename, "r") as f:
                content = f.read()
                lines = content.strip().split("\n")

            assert (
                len(lines) == 8
            )  # header + 1 test + 6 emission metrics (3 metrics × 2 runs)
            assert "Emission_Metric,emissions_kgCO2eq,0.001,,1" in content
            assert "Emission_Metric,duration_seconds,1.0,,1" in content
        finally:
            unlink(filename)

    @patch("evaluation.test_wrapper.EmissionsTracker")
    @patch("evaluation.test_wrapper.defaultTestLoader")
    @patch("evaluation.test_wrapper.TextTestRunner")
    def test_run_emission_test_success(
        self, mock_runner: Mock, mock_loader: Mock, mock_tracker_class: Mock
    ) -> None:
        """Test successful emission test run."""

        # Mock tracker instance
        mock_tracker = Mock()
        mock_tracker_class.return_value = mock_tracker

        # Mock emissions data
        mock_final_data = Mock()
        mock_final_data.emissions = 0.001
        mock_final_data.duration = 1.0
        mock_final_data.energy_consumed = 0.0001
        mock_tracker.final_emissions_data = mock_final_data

        # Mock test loading and running
        mock_suite = Mock()
        mock_loader.loadTestsFromName.return_value = mock_suite
        mock_runner_instance = Mock()
        mock_runner.return_value = mock_runner_instance

        with patch("evaluation.test_wrapper.time") as mock_time:
            # Mock time to control the 1-second loop
            # First call returns 0, second 0.5, third 1.5
            mock_time.side_effect = [0, 0.5, 1.5]

            # Only run 1 iteration for testing
            with patch("builtins.range", return_value=[0]):
                result = run_emission_test("test_module")

        assert result is not None
        assert len(result) == 1
        assert result[0]["emissions_kgCO2eq"] == 0.001
        assert result[0]["duration_seconds"] == 1.0
        assert result[0]["energy_consumed_kwh"] == 0.0001

    @patch("evaluation.test_wrapper.EmissionsTracker")
    def test_run_emission_test__error(self, mock_tracker_class: Mock) -> None:
        """Test emission test with error."""

        mock_tracker_class.side_effect = Exception("Tracker error")

        with patch("builtins.range", return_value=[0]):
            result = run_emission_test("test_module")

        assert result is not None
        assert len(result) == 1
        assert result[0]["emissions_kgCO2eq"] == 0.0
        assert result[0]["duration_seconds"] == 0.0
        assert result[0]["energy_consumed_kwh"] == 0.0

    @patch("evaluation.test_wrapper.defaultTestLoader")
    @patch("evaluation.test_wrapper.TextTestRunner")
    @patch("evaluation.test_wrapper.run_emission_test")
    def test_run_with_valid_test_file(
        self, mock_emission_test: Mock, mock_runner: Mock, mock_loader: Mock
    ) -> None:
        """Test run function with valid test file."""

        # Mock test suite
        mock_suite = Mock()
        mock_suite.countTestCases.return_value = 2
        mock_loader.loadTestsFromName.return_value = mock_suite

        # Mock test runner
        mock_result = CSVTestResult(None, None, 0)
        mock_runner_instance = Mock()
        mock_runner_instance.run.return_value = mock_result
        mock_runner.return_value = mock_runner_instance

        # Mock emissions data
        mock_emission_test.return_value = [{"emissions_kgCO2eq": 0.001}]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
            output_file = f.name

        try:
            run("test_module.py", output_file)

            # Verify the output file was created
            assert path.exists(output_file)
            mock_loader.loadTestsFromName.assert_called_with("test_module")
        finally:
            if path.exists(output_file):
                unlink(output_file)

    @patch("evaluation.test_wrapper.defaultTestLoader")
    def test_run_with_no_tests(self, mock_loader: Mock) -> None:
        """Test run function with no tests found."""

        # Mock empty test suite
        mock_suite = Mock()
        mock_suite.countTestCases.return_value = 0
        mock_loader.loadTestsFromName.return_value = mock_suite

        with NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
            output_file = f.name

        try:
            run("empty_test_module", output_file)

            # Verify the output file was created with "No tests available" message
            assert path.exists(output_file)
            with open(output_file, "r") as f:
                content = f.read()
                assert "No tests available" in content
        finally:
            if path.exists(output_file):
                unlink(output_file)

    @patch("evaluation.test_wrapper.defaultTestLoader")
    def test_run_with_exception(self, mock_loader: Mock) -> None:
        """Test run function when an exception."""

        mock_loader.loadTestsFromName.side_effect = Exception("Test loading error")

        with NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
            output_file = f.name

        try:
            run("invalid_test_module", output_file)

            # Verify the output file was created with error message
            assert path.exists(output_file)
            with open(output_file, "r") as f:
                content = f.read()
                assert "Error" in content
        finally:
            if path.exists(output_file):
                unlink(output_file)
