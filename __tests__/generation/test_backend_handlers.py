import pytest
from io import StringIO
from ollama import ResponseError
from unittest.mock import Mock, patch

from generation.backend_handlers import (
    OllamaBackendHandler,
    get_backend_handler_by_name,
)


class TestBackendHandler:
    def test_change_system_prompt(self) -> None:
        """Test that the system prompt can be changed successfully."""

        handler = OllamaBackendHandler(
            model="test_model",
            system_prompt="initial_prompt",
            rci_follow_up_system_prompt="test_rci",
            temperature=0.5,
        )

        handler.change_system_prompt("new_prompt")
        assert handler._BackendHandler__system_prompt == "new_prompt"


class TestOllamaBackendHandler:
    def test_extract_code_block_content_with_code_block(self) -> None:
        """Test that code block content is extracted correctly when code blocks are present."""

        handler = OllamaBackendHandler(
            model="test",
            system_prompt="test",
            rci_follow_up_system_prompt="test",
            temperature=0.5,
        )

        input_string = "```python\nprint('hello')\n```"
        result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
        assert result == "print('hello')"

    def test_extract_code_block_content_with_language_specification(self) -> None:
        """Test that code block content is extracted correctly with language specification."""

        handler = OllamaBackendHandler(
            model="test",
            system_prompt="test",
            rci_follow_up_system_prompt="test",
            temperature=0.5,
        )

        input_string = "```javascript\nconsole.log('hello');\n```"
        result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
        assert result == "console.log('hello');"

    def test_extract_code_block_content_no_code_block(self) -> None:
        """Test that input string is returned unchanged when no code block is present."""

        handler = OllamaBackendHandler(
            model="test",
            system_prompt="test",
            rci_follow_up_system_prompt="test",
            temperature=0.5,
        )

        input_string = "just some text"
        result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
        assert result == "just some text"

    def test_extract_code_block_content_with_think_tags(self) -> None:
        """Test that think tags are removed from extracted code block content."""

        handler = OllamaBackendHandler(
            model="test",
            system_prompt="test",
            rci_follow_up_system_prompt="test",
            temperature=0.5,
        )

        input_string = "```python\n<think>thinking</think>\nprint('hello')\n```"
        result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
        assert result == "print('hello')"

    @patch("generation.backend_handlers.Client")
    def test_chat_success(self, mock_client_class: Mock) -> None:
        """Test that chat method returns extracted code when successful."""

        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock()
        mock_response.message.content = "```python\ntest_code\n```"
        mock_client.chat.return_value = mock_response

        handler = OllamaBackendHandler(
            model="test_model",
            system_prompt="test_system",
            rci_follow_up_system_prompt="test_rci",
            temperature=0.5,
            timeout=30,
        )

        result = handler._OllamaBackendHandler__chat("system", "user", extract=True)
        assert result == "test_code"

    @patch("generation.backend_handlers.Client")
    @patch("sys.stderr", new_callable=StringIO)
    def test_chat_response_error(
        self, mock_stderr: StringIO, mock_client_class: Mock
    ) -> None:
        """Test that chat method returns None and logs error when ResponseError occurs."""

        mock_client = Mock()
        mock_client_class.return_value = mock_client
        mock_client.chat.side_effect = ResponseError("Connection failed")

        handler = OllamaBackendHandler(
            model="test_model",
            system_prompt="test_system",
            rci_follow_up_system_prompt="test_rci",
            temperature=0.5,
        )

        result = handler._OllamaBackendHandler__chat("system", "user")
        assert result is None
        assert "Failed to get response from model" in mock_stderr.getvalue()

    @patch("generation.backend_handlers.Client")
    def test_chat_extraction_failure(self, mock_client_class: Mock) -> None:
        """Test that chat method returns None when code block extraction fails."""

        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock()
        mock_response.message.content = "no code block here"
        mock_client.chat.return_value = mock_response

        handler = OllamaBackendHandler(
            model="test_model",
            system_prompt="test_system",
            rci_follow_up_system_prompt="test_rci",
            temperature=0.5,
        )

        handler._OllamaBackendHandler__extract_code_block_content = Mock(
            return_value=None
        )

        result = handler._OllamaBackendHandler__chat("system", "user")
        assert result is None


class TestGetBackendHandlerByName:
    def test_get_ollama_handler(self) -> None:
        """Test that Ollama backend handler is returned for Ollama platform."""

        handler = get_backend_handler_by_name(
            platform="Ollama",
            model="test_model",
            system_prompt="test_system",
            rci_follow_up_system_prompt="test_rci",
            temperature=0.5,
            timeout=30,
        )

        assert isinstance(handler, OllamaBackendHandler)
        assert handler._BackendHandler__model == "test_model"

    @patch("sys.stderr", new_callable=StringIO)
    def test_get_unsupported_handler(self, mock_stderr):
        """Test that SystemExit is raised for unsupported backend platforms."""

        with pytest.raises(SystemExit) as exc_info:
            get_backend_handler_by_name(
                platform="UnsupportedPlatform",
                model="test_model",
                system_prompt="test_system",
                rci_follow_up_system_prompt="test_rci",
                temperature=0.5,
                timeout=30,
            )

        assert exc_info.value.code == 1
        assert "Backend UnsupportedPlatform not supported" in mock_stderr.getvalue()
