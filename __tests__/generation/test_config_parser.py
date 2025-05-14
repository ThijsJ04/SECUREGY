import pytest
from json import dumps
from generation.config_parser import load_config, Config


def test_load_config_valid_file(tmp_path: str) -> None:
    # Arrange
    valid_config = {
        "dataset": "SALLM",
        "platform": "Ollama",
        "model": "test-model",
        "model_id": "test-model-id",
        "sample_amount": 10,
        "temperature": 0.7,
        "rci": 2,
        "cot": True,
        "output_dir": "output",
    }
    config_path = tmp_path / "valid_config.json"
    config_path.write_text(dumps(valid_config))

    # Act
    config = load_config(str(config_path))

    # Assert
    assert config == Config(**valid_config)


def test_load_config_file_not_found():
    # Arrange
    invalid_path = "non_existent_config.json"

    # Act & Assert
    with pytest.raises(SystemExit) as excinfo:
        load_config(invalid_path)
    assert excinfo.value.code == 1


def test_load_config_invalid_json_format(tmp_path):
    # Arrange
    invalid_json = "{invalid: json}"
    config_path = tmp_path / "invalid_config.json"
    config_path.write_text(invalid_json)

    # Act & Assert
    with pytest.raises(SystemExit) as excinfo:
        load_config(str(config_path))
    assert excinfo.value.code == 1


def test_load_config_invalid_schema(tmp_path):
    # Arrange
    invalid_config = {
        "dataset": "SALLM",
        "platform": "Ollama",
        "model": "test-model",
        "model_id": "test-model-id",
        "sample_amount": 10,
        "temperature": 0.7,
        "rci": 2,
        # Missing required "cot" field
    }
    config_path = tmp_path / "invalid_schema_config.json"
    config_path.write_text(dumps(invalid_config))

    # Act & Assert
    with pytest.raises(SystemExit) as excinfo:
        load_config(str(config_path))
    assert excinfo.value.code == 1


def test_load_config_additional_properties(tmp_path):
    # Arrange
    invalid_config = {
        "dataset": "SALLM",
        "platform": "Ollama",
        "model": "test-model",
        "model_id": "test-model-id",
        "sample_amount": 10,
        "system_prompt": "Generate code for the following prompt:",
        "temperature": 0.7,
        "rci": 2,
        "cot": True,
        "extra_property": "not_allowed",
    }
    config_path = tmp_path / "additional_properties_config.json"
    config_path.write_text(dumps(invalid_config))

    # Act & Assert
    with pytest.raises(SystemExit) as excinfo:
        load_config(str(config_path))
    assert excinfo.value.code == 1
