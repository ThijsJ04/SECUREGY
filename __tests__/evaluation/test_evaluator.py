import pytest
from csv import reader as csv_reader
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator
from unittest.mock import Mock, patch

from evaluation.evaluator import Evaluator


class TestEvaluator:
    @pytest.fixture
    def temp_dir(self) -> Generator[Path, None, None]:
        """Create a temporary directory for testing."""

        with TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)

    @pytest.fixture
    def mock_file_structure(self, temp_dir: Path) -> Path:
        """Create a mock file structure for testing."""

        # Create required directories
        evaluation_dir = temp_dir / "evaluation"
        evaluation_dir.mkdir()

        # Create test wrapper file
        test_wrapper = evaluation_dir / "test_wrapper.py"
        test_wrapper.write_text("# Mock test wrapper")

        # Create virtual environment directory
        venv_dir = evaluation_dir / ".venv"
        venv_dir.mkdir()

        # Create generation directory structure
        gen_dir = temp_dir / "generation" / "generated_code"
        gen_dir.mkdir(parents=True)

        # Create dataset directory structure
        dataset_dir = temp_dir / "dataset" / "unittests"
        dataset_dir.mkdir(parents=True)

        return temp_dir

    @patch("evaluation.evaluator.Path.cwd")
    def test_evaluator_init_success(
        self, mock_cwd: Mock, mock_file_structure: Path
    ) -> None:
        """Test successful initialization of Evaluator."""

        mock_cwd.return_value = mock_file_structure

        evaluator = Evaluator()

        assert evaluator._Evaluator__test_wrapper_file_path.exists()
        assert evaluator._Evaluator__experiment_dir.exists()
        assert evaluator._Evaluator__result_dir.exists()

    @patch("evaluation.evaluator.Path.cwd")
    def test_evaluator_init_missing_test_wrapper(
        self, mock_cwd: Mock, temp_dir: Path
    ) -> None:
        """Test initialization failure when test wrapper is missing."""

        mock_cwd.return_value = temp_dir

        with pytest.raises(FileNotFoundError, match="Test wrapper file not found"):
            Evaluator()

    @patch("evaluation.evaluator.Path.cwd")
    def test_evaluator_init_missing_venv(self, mock_cwd: Mock, temp_dir: Path) -> None:
        """Test initialization failure when virtual environment is missing."""

        mock_cwd.return_value = temp_dir

        # Create test wrapper but not venv
        evaluation_dir = temp_dir / "evaluation"
        evaluation_dir.mkdir()
        test_wrapper = evaluation_dir / "test_wrapper.py"
        test_wrapper.write_text("# Mock test wrapper")

        with pytest.raises(FileNotFoundError, match="Virtual environment not found"):
            Evaluator()

    @patch("evaluation.evaluator.Path.cwd")
    def test_create_test_groups(
        self, mock_cwd: Mock, mock_file_structure: Path
    ) -> None:
        """Test the creation of test groups."""

        mock_cwd.return_value = mock_file_structure

        # Create mock code files with proper structure
        code_dir = mock_file_structure / "generation" / "generated_code"
        platform_dir = code_dir / "platform1" / "model1" / "T0.5" / "variant1" / "R1"
        platform_dir.mkdir(parents=True)
        code_file = platform_dir / "prompt1.py"
        code_file.write_text("# Mock code")

        # Create corresponding test file
        test_dir = mock_file_structure / "dataset" / "unittests"
        test_file = test_dir / "test_prompt1.py"
        test_file.write_text("# Mock test")

        evaluator = Evaluator()
        test_groups = evaluator._Evaluator__test_groups

        assert len(test_groups) > 0
        assert str(test_file) in test_groups

    @patch("evaluation.evaluator.Path.cwd")
    def test_create_error_csv(self, mock_cwd: Mock, mock_file_structure: Path) -> None:
        """Test creation of error CSV file."""

        mock_cwd.return_value = mock_file_structure

        evaluator = Evaluator()
        error_file = mock_file_structure / "test_error.csv"
        error_message = "Test error message"

        evaluator._Evaluator__create_error_csv(error_file, error_message)

        assert error_file.exists()

        # Verify CSV content
        with open(error_file, "r", newline="") as f:
            reader = csv_reader(f)
            rows = list(reader)
            assert len(rows) == 2  # Header + error row
            assert rows[0] == ["Section", "Key", "Value", "Message", "Run_Number"]
            assert rows[1][3] == error_message

    @patch("evaluation.evaluator.Path.cwd")
    @patch("evaluation.evaluator.makedirs")
    @patch("evaluation.evaluator.copy2")
    def test_setup_thread_directory(
        self,
        mock_copy2: Mock,
        mock_makedirs: Mock,
        mock_cwd: Mock,
        mock_file_structure: Path,
    ) -> None:
        """Test setup of thread directory."""

        mock_cwd.return_value = mock_file_structure

        evaluator = Evaluator()
        thread_dir = mock_file_structure / "thread_test"
        test_file = mock_file_structure / "test.py"
        code_file = mock_file_structure / "code.py"

        # Create mock files
        test_file.write_text("# Test")
        code_file.write_text("# Code")

        evaluator._Evaluator__setup_thread_directory(thread_dir, test_file, code_file)

        # Verify directory creation and file copying
        mock_makedirs.assert_called()
        assert mock_copy2.call_count >= 3  # test_wrapper, test_file, code_file

    @patch("evaluation.evaluator.Path.cwd")
    @patch("evaluation.evaluator.which")
    def test_run_static_based_tests_no_codeql(
        self, mock_which: Mock, mock_cwd: Mock, mock_file_structure: Path
    ) -> None:
        """Test static-based tests failure when CodeQL is not available."""

        mock_cwd.return_value = mock_file_structure
        mock_which.return_value = None  # CodeQL not available

        evaluator = Evaluator()

        with pytest.raises(EnvironmentError, match="CodeQL CLI not found"):
            evaluator.run_static_based_tests()
