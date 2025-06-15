import pytest
from json import dump
from os import unlink
from tempfile import NamedTemporaryFile

from dataset.prompt_loader import load_input_prompts


class TestLoadInputPrompts:
    def test_load_valid_prompts(self) -> None:
        """Test that valid JSON prompt data is loaded correctly."""

        valid_data = [
            {"id": "1", "prompt": "Test prompt 1"},
            {"id": "2", "prompt": "Test prompt 2"},
        ]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            dump(valid_data, f)
            temp_path = f.name

        try:
            result = load_input_prompts(temp_path)
            assert len(result) == 2
            assert result[0]["id"] == "1"
            assert result[0]["prompt"] == "Test prompt 1"
            assert result[1]["id"] == "2"
            assert result[1]["prompt"] == "Test prompt 2"
        finally:
            unlink(temp_path)

    def test_file_not_found(self):
        """Test that a SystemExit is raised when the file doesn't exist."""

        with pytest.raises(SystemExit) as excinfo:
            load_input_prompts("non_existent_file.json")
        assert excinfo.value.code == 1

    def test_invalid_json_format(self):
        """Test that a SystemExit is raised when the JSON format is invalid."""

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            f.write('{"invalid": json}')
            temp_path = f.name

        try:
            with pytest.raises(SystemExit) as excinfo:
                load_input_prompts(temp_path)
            assert excinfo.value.code == 1
        finally:
            unlink(temp_path)

    def test_missing_required_field(self) -> None:
        """Test that a SystemExit is raised when required fields are missing."""

        invalid_data = [{"prompt": "Test prompt without id"}]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            dump(invalid_data, f)
            temp_path = f.name

        try:
            with pytest.raises(SystemExit) as excinfo:
                load_input_prompts(temp_path)
            assert excinfo.value.code == 1
        finally:
            unlink(temp_path)

    def test_additional_properties_not_allowed(self):
        """Test that a SystemExit is raised when additional properties are present."""

        invalid_data = [{"id": "1", "prompt": "Test", "extra_field": "not allowed"}]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            dump(invalid_data, f)
            temp_path = f.name

        try:
            with pytest.raises(SystemExit) as excinfo:
                load_input_prompts(temp_path)
            assert excinfo.value.code == 1
        finally:
            unlink(temp_path)

    def test_wrong_data_type(self):
        """Test that a SystemExit is raised when field data types are incorrect."""

        invalid_data = [{"id": 123, "prompt": "Test prompt"}]

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            dump(invalid_data, f)
            temp_path = f.name

        try:
            with pytest.raises(SystemExit) as excinfo:
                load_input_prompts(temp_path)
            assert excinfo.value.code == 1
        finally:
            unlink(temp_path)

    def test_not_array_format(self):
        """Test that a SystemExit is raised when the JSON is not an array."""

        invalid_data = {"id": "1", "prompt": "Test"}

        with NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            dump(invalid_data, f)
            temp_path = f.name

        try:
            with pytest.raises(SystemExit) as excinfo:
                load_input_prompts(temp_path)
            assert excinfo.value.code == 1
        finally:
            unlink(temp_path)
