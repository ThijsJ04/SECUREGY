from abc import ABC, abstractmethod
from ollama import ResponseError, ChatResponse, Client
from re import DOTALL, search, sub
import sys
from textwrap import dedent
from typing import Literal, Union


class BackendHandler(ABC):
    def __init__(
        self,
        model: str,
        system_prompt: str,
        rci_follow_up_system_prompt: str,
        temperature: float,
        timeout: int = 60,
    ):
        self.__model = model
        self.__system_prompt = system_prompt
        self.__rci_follow_up_system_prompt = rci_follow_up_system_prompt
        self.__temperature = temperature
        self.__timeout = timeout

    def change_system_prompt(self, system_prompt: str) -> None:
        """
        Change the system prompt for the backend handler.

        Args:
            system_prompt (str): The new system prompt to set.
        """
        self.__system_prompt = system_prompt

    @abstractmethod
    def request(self, user_prompt: str) -> Union[str, None]:
        pass

    @abstractmethod
    def rci_request(
        self,
        amount_of_iterations: int,
        improve: Literal["security", "energy-efficiency"],
        user_prompt: str,
    ) -> Union[str, None]:
        pass


class OllamaBackendHandler(BackendHandler):
    def __extract_code_block_content(self, input_string: str) -> str:
        """
        Extract the content of the first code block from the input string and remove <think> tags if present.

        Args:
            input_string (str): The input string containing the code block.

        Returns:
            str: The content of the first code block, or just the input string if no code block is found.
        """
        pattern = r"```(?:\w+)?\n(.*?)```"

        match = search(pattern, input_string, DOTALL)

        if match:
            content = match.group(1)
        elif input_string.startswith("```"):
            content = input_string.split("```", 2)[1]
        else:
            content = input_string

        # Remove <think> tags and their content
        content = sub(r"<think>.*?</think>", "", content, flags=DOTALL)
        return content.strip("\n")

    def __chat(
        self, system_prompt: str, user_prompt: str, extract: bool = True
    ) -> Union[str, None]:
        """
        Send a prompt to the language model and return the generated code.

        Args:
            prompt (str): The user prompt to send to the language model.
            extract (bool): Whether to extract a code block from the response.
        Returns:
            Union[str, None]: The generated code or None if extraction fails.
        """
        try:
            client = Client(timeout=self._BackendHandler__timeout)
            response: ChatResponse = client.chat(
                model=self._BackendHandler__model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                options={
                    "temperature": self._BackendHandler__temperature,
                },
            )

            llm_output = response.message.content
            output = (
                self.__extract_code_block_content(llm_output) if extract else llm_output
            )

            if output is None:
                print("Failed to extract code block from LLM output", file=sys.stderr)
                print(f"LLM output: {llm_output}", file=sys.stderr)
            else:
                return dedent(output) if extract else output
        except ResponseError as e:
            print(f"Failed to get response from model: {e}", file=sys.stderr)

    def request(self, user_prompt: str) -> Union[str, None]:
        """
        Send a request to the language model.

        Args:
            user_prompt (str): The user prompt to send to the language model.

        Returns:
            Union[str, None]: The generated code or None if extraction fails.
        """
        return self.__chat(self._BackendHandler__system_prompt, user_prompt)

    def rci_request(
        self,
        amount_of_iterations: int,
        improve: Literal["security", "energy-efficiency"],
        user_prompt: str,
    ) -> Union[str, None]:
        """
        Send a request to the language model for RCI (Recursive Criticism and Improvement).

        Args:
            improve (str): The type of improvement to request.
            user_prompt (str): The user prompt to send to the language model.

        Returns:
            Union[str, None]: The generated code or None if extraction fails.
        """
        code = self.request(user_prompt)

        for _ in range(0, amount_of_iterations, 1):
            if code is None:
                print("Failed to get code needed for RCI from model.", file=sys.stderr)
                return None

            critique = self.__chat(
                system_prompt=None,
                user_prompt=f"Review the following answer and find {'security' if improve == 'security' else 'energy efficiency'} problems with it: \n```\n{code}\n```",
                extract=False,
            )

            modified_user_prompt = (
                f"Based on the critique: \n"
                f"{critique}\n"
                f"improve the following answer: \n"
                f"```\n{code}\n```"
            )

            code = self.__chat(
                system_prompt=self._BackendHandler__rci_follow_up_system_prompt,
                user_prompt=modified_user_prompt,
            )


def get_backend_handler_by_name(
    platform: str,
    model: str,
    system_prompt: str,
    rci_follow_up_system_prompt: str,
    temperature: float,
    timeout: int,
) -> BackendHandler:
    """
    Get the backend handler by name.

    Args:
        config (Config): A generation configuration object.
        dataset_name (str): The name of the dataset to load.

    Returns:
        BackendHandler: The backend handler for the specified dataset.
    """
    if platform == "Ollama":
        return OllamaBackendHandler(
            model=model,
            system_prompt=system_prompt,
            rci_follow_up_system_prompt=rci_follow_up_system_prompt,
            temperature=temperature,
            timeout=timeout,
        )
    else:
        print(f"Backend {platform} not supported.", file=sys.stderr)
        exit(1)
