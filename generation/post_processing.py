from json import load as json_load
from pathlib import Path
import sys
from typing import Dict


def retrieve_contextual_code_from_prompts(dataset_path: str) -> Dict[str, str]:
    """
    Retrieves the contextual code from the prompts.

    Args:
        dataset_path (str): The path to the dataset containing prompts in JSON format.

    Returns:
        Dict[str, str]: A dictionary mapping prompt IDs to their corresponding
        contextual code. The contextual code is defined as the part of the prompt
        that provides context for the code generation task.
    """

    def extract_contextual_code(prompt: str) -> str:
        """
        Extracts the contextual code from a prompt. The function considers
        the contextual code to end when it encounters one of the following:
        1. A line that starts with '@app.route(', indicating the start of a route definition.
        2. A function definition that has a docstring.

        Args:
            prompt (str): The input prompt from which to extract contextual code.

        Returns:
            str: The extracted contextual code.
        """

        lines = prompt.split("\n")
        prompt_lines = []

        for i, line in enumerate(lines):
            # Check if this line starts an app route
            if line.strip().startswith("@app.route("):
                break

            # Check if this line starts a function definition with a docstring.
            if line.strip().startswith("def "):
                # Look ahead to see if the next non-empty line is a docstring.
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if not next_line:
                        continue
                    if next_line.startswith('"""') or next_line.startswith("'''"):
                        # This function has a docstring, so stop here.
                        return "\n".join(prompt_lines)
                    else:
                        # This function doesn't have a docstring, include it in the context.
                        break

            prompt_lines.append(line)

        return "\n".join(prompt_lines)

    prompts_json_path = Path(dataset_path)
    if not prompts_json_path.exists():
        raise FileNotFoundError(f"Prompts JSON file not found at {prompts_json_path}")

    with open(prompts_json_path, "r", encoding="utf-8") as f:
        prompts_data = json_load(f)

    contextual_code = {}
    for prompt_entry in prompts_data:
        contextual_code[prompt_entry["id"]] = extract_contextual_code(
            prompt_entry["prompt"]
        )

    return contextual_code


def prepend_contextual_code_to_generated_code_if_missing(
    code_file_path: Path, contextual_code: str
) -> None:
    """
    Prepends the contextual code to the generated code file if it is missing.

    Args:
        code_file_path (Path): The path to the generated code file.
        contextual_code (str): The contextual code to prepend.
    """

    def check_if_contextual_code_is_missing(code_content: str) -> bool:
        """
        Checks if the contextual code is missing from the generated code file.
        This function considers the contextual code to be missing if:
        1. The code file is empty.
        2. The first line of the code file starts with a function definition or an app route.
        3. There are no imports at the beginning of the code file, and it starts with a function definition or an app route.

        Args:
            code_content (str): The content of the generated code file.

        Returns:
            bool: True if the contextual code is missing, False otherwise.
        """

        lines = [line.strip() for line in code_content.split("\n") if line.strip()]

        if not lines:
            # If the code file is empty, the contextual code is considered missing
            return True

        # Check if the code starts directly with a function definition or app route
        first_line = lines[0]

        # If it starts with @app.route or def, the contextual code is likely missing
        if first_line.startswith("@app.route(") or first_line.startswith("def "):
            return True

        # Check if there are no imports at the beginning
        has_imports = any(
            line.startswith("import ") or line.startswith("from ") for line in lines[:5]
        )  # Check first 5 lines

        # If no imports and starts with function/route, contextual code is missing
        if not has_imports and (
            any(
                line.startswith("@app.route(") or line.startswith("def ")
                for line in lines[:3]
            )
        ):
            return True

        return False

    try:
        with open(code_file_path, "r", encoding="utf-8") as file:
            code_content = file.read()

        if check_if_contextual_code_is_missing(code_content):
            with open(code_file_path, "w", encoding="utf-8") as file:
                file.write(contextual_code + "\n" + code_content)
    except Exception as e:
        print(f"Error reading file {code_file_path}: {e}", file=sys.stderr)
        return


def apply_post_processing(dataset_path: str) -> None:
    """
    Applies post-processing to the generated code files by conditionally prepending
    the contextual code extracted from the prompts.

    Args:
        dataset_path (str): The path to the dataset containing prompts in JSON format.

    Raises:
        FileNotFoundError: If no generated code files are found.
    """

    contextual_code = retrieve_contextual_code_from_prompts(dataset_path)

    code_files = list((Path.cwd() / "generation" / "generated_code").rglob("*.py"))
    if len(code_files) == 0:
        raise FileNotFoundError("No generated code files found.")

    for code_file in code_files:
        prompt_id = code_file.stem
        if not prompt_id or prompt_id not in contextual_code:
            print(
                f"Warning: No contextual code found for prompt ID {prompt_id}. Skipping post-processing.",
                file=sys.stderr,
            )
            continue

        prepend_contextual_code_to_generated_code_if_missing(
            code_file, contextual_code[prompt_id]
        )
