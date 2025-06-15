import pytest
from json import dump
from unittest.mock import patch

from generation.post_processing import (
    retrieve_contextual_code_from_prompts,
    prepend_contextual_code_to_generated_code_if_missing,
    apply_post_processing,
)


class TestRetrieveContextualCodeFromPrompts:
    def test_valid_json_file(self, tmp_path):
        """Test that contextual code is retrieved correctly from a valid JSON file."""

        test_data = [
            {
                "id": "test1",
                "prompt": "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/test')\ndef test():\n    pass",
            },
            {
                "id": "test2",
                "prompt": 'import os\nfrom pathlib import Path\n\ndef helper():\n    """\n    Helper function\n    """\n    pass',
            },
        ]

        json_file = tmp_path / "test_prompts.json"
        with open(json_file, "w") as f:
            dump(test_data, f)

        result = retrieve_contextual_code_from_prompts(str(json_file))

        assert "test1" in result
        assert "test2" in result
        assert "from flask import Flask" in result["test1"]
        assert "@app.route('/test')" not in result["test1"]
        assert "import os" in result["test2"]
        assert "def helper():" not in result["test2"]

    def test_nonexistent_file(self):
        """Test that a FileNotFoundError is raised for a nonexistent file."""

        with pytest.raises(FileNotFoundError, match="Prompts JSON file not found"):
            retrieve_contextual_code_from_prompts("/nonexistent/path.json")


class TestPrependContextualCodeToGeneratedCodeIfMissing:
    def test_prepend_to_empty_file(self, tmp_path):
        """Test that contextual code is prepended to an empty file."""

        code_file = tmp_path / "empty.py"
        code_file.write_text("")
        contextual_code = "from flask import Flask\napp = Flask(__name__)"

        prepend_contextual_code_to_generated_code_if_missing(code_file, contextual_code)

        content = code_file.read_text()
        assert content.startswith(contextual_code)

    def test_prepend_to_file_starting_with_function(self, tmp_path):
        """Test that contextual code is prepended to a file starting with a function."""

        code_file = tmp_path / "func_start.py"
        original_content = "def test_func():\n    return True"
        code_file.write_text(original_content)
        contextual_code = "import os\nfrom pathlib import Path"

        prepend_contextual_code_to_generated_code_if_missing(code_file, contextual_code)

        content = code_file.read_text()
        assert content.startswith(contextual_code)
        assert original_content in content

    def test_prepend_to_file_starting_with_app_route(self, tmp_path):
        """Test that contextual code is prepended to a file starting with an app route."""

        code_file = tmp_path / "route_start.py"
        original_content = "@app.route('/test')\ndef test():\n    return 'hello'"
        code_file.write_text(original_content)
        contextual_code = "from flask import Flask\napp = Flask(__name__)"

        prepend_contextual_code_to_generated_code_if_missing(code_file, contextual_code)

        content = code_file.read_text()
        assert content.startswith(contextual_code)
        assert original_content in content


class TestApplyPostProcessing:
    @patch("generation.post_processing.Path.cwd")
    def test_apply_post_processing_success(self, mock_cwd, tmp_path):
        """Test successful application of post-processing to generated code."""

        # Setup mock directory structure
        generated_code_dir = tmp_path / "generation" / "generated_code"
        generated_code_dir.mkdir(parents=True)

        # Create test files
        code_file1 = generated_code_dir / "test1.py"
        code_file1.write_text("def test():\n    pass")
        code_file2 = generated_code_dir / "test2.py"
        code_file2.write_text("@app.route('/api')\ndef api():\n    pass")

        # Setup prompts file
        prompts_data = [
            {
                "id": "test1",
                "prompt": 'import os\n\ndef test():\n    """\n    Test function\n    """\n    pass',
            },
            {
                "id": "test2",
                "prompt": "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/api')\ndef api():\n    pass",
            },
        ]
        prompts_file = tmp_path / "prompts.json"
        with open(prompts_file, "w") as f:
            dump(prompts_data, f)

        mock_cwd.return_value = tmp_path

        apply_post_processing(str(prompts_file))

        # Check that contextual code was prepended
        content1 = code_file1.read_text()
        content2 = code_file2.read_text()
        assert "import os" in content1
        assert "from flask import Flask" in content2

    @patch("generation.post_processing.Path.cwd")
    def test_apply_post_processing_no_files(self, mock_cwd, tmp_path):
        """Test error when no generated code files found."""

        generated_code_dir = tmp_path / "generation" / "generated_code"
        generated_code_dir.mkdir(parents=True)

        prompts_file = tmp_path / "prompts.json"
        with open(prompts_file, "w") as f:
            dump([], f)

        mock_cwd.return_value = tmp_path

        with pytest.raises(FileNotFoundError, match="No generated code files found"):
            apply_post_processing(str(prompts_file))

    @patch("generation.post_processing.Path.cwd")
    def test_apply_post_processing_missing_prompt_id(self, mock_cwd, tmp_path, capsys):
        """Test warning when prompt ID not found in contextual code."""

        generated_code_dir = tmp_path / "generation" / "generated_code"
        generated_code_dir.mkdir(parents=True)

        code_file = generated_code_dir / "missing_id.py"
        code_file.write_text("def test():\n    pass")

        prompts_data = [{"id": "different_id", "prompt": "import os"}]
        prompts_file = tmp_path / "prompts.json"
        with open(prompts_file, "w") as f:
            dump(prompts_data, f)

        mock_cwd.return_value = tmp_path

        apply_post_processing(str(prompts_file))

        captured = capsys.readouterr()
        assert (
            "Warning: No contextual code found for prompt ID missing_id" in captured.err
        )

    def test_apply_post_processing_invalid_dataset_path(self):
        """Test error when dataset path is invalid."""

        with pytest.raises(FileNotFoundError, match="Prompts JSON file not found"):
            apply_post_processing("/invalid/path.json")
