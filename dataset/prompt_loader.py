from json import JSONDecodeError, loads as json_loads
from jsonschema import validate as json_validate, ValidationError
import sys
from typing import List, TypedDict

input_prompt_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "prompt": {"type": "string"},
        },
        "required": [
            "id",
            "prompt",
        ],
        "additionalProperties": False,
    },
}


class InputPrompt(TypedDict):
    id: str
    prompt: str


def load_input_prompts(dataset_path: str) -> List[InputPrompt]:
    """
    Load the input prompts from a JSON file.

    Args:
        dataset_path (str): Path to the dataset file.

    Returns:
        List[InputPrompt]: List of parsed input prompts.
    """

    try:
        with open(dataset_path, "r") as file:
            dataset_maybe = json_loads(file.read())

        json_validate(instance=dataset_maybe, schema=input_prompt_schema)
        return [InputPrompt(**item) for item in dataset_maybe]
    except FileNotFoundError:
        print(f"Error: The file {dataset_path} was not found.", file=sys.stderr)
        exit(1)
    except JSONDecodeError as e:
        print(f"Invalid JSON format in config file: {e}", file=sys.stderr)
        exit(1)
    except ValidationError as e:
        print(f"Config file does not match schema: {e}", file=sys.stderr)
        exit(1)
