import pytest
from generation.backend_handlers import (
    get_backend_handler_by_name,
    OllamaBackendHandler,
)

# __tests__/generation/test_backend_handlers.py


def test_get_backend_handler_by_name_valid_platform():
    # Arrange
    config = {
        "platform": "Ollama",
        "model": "test-model",
        "rci": 0,
        "system_prompt": "test-prompt",
        "temperature": 0.7,
    }

    # Act
    handler = get_backend_handler_by_name(config, "test-system-prompt")

    # Assert
    assert isinstance(handler, OllamaBackendHandler)
    assert handler.model == "test-model"
    assert handler.system_prompt == "test-system-prompt"
    assert handler.temperature == 0.7


def test_get_backend_handler_by_name_invalid_platform():
    # Arrange
    config = {
        "platform": "UnsupportedPlatform",
        "model": "test-model",
        "rci": 0,
        "system_prompt": "test-prompt",
        "temperature": 0.7,
    }

    # Act & Assert
    with pytest.raises(SystemExit) as excinfo:
        get_backend_handler_by_name(config, "test-system-prompt")
    assert excinfo.value.code == 1
