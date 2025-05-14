from generation.backend_handlers import OllamaBackendHandler


def test_extract_code_block_content_valid_code_block():
    handler = OllamaBackendHandler("test-model", 0, "system-prompt", 0.7)
    input_string = "Some text before\n```\nprint('Hello, world!')\n```\nSome text after"
    result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
    assert result == "print('Hello, world!')"


def test_extract_code_block_content_no_code_block():
    handler = OllamaBackendHandler("test-model", 0, "system-prompt", 0.7)
    input_string = "This is a string without any code block."
    result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
    assert result == input_string


def test_extract_code_block_content_with_think_tags():
    handler = OllamaBackendHandler("test-model", 0, "system-prompt", 0.7)
    input_string = (
        "```python\n<think>Some internal thought</think>\nprint('Hello')\n```"
    )
    result = handler._OllamaBackendHandler__extract_code_block_content(input_string)
    assert result == "print('Hello')"
