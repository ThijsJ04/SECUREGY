from json import loads as json_loads, JSONDecodeError
from jsonschema import validate as json_validate, ValidationError
from sys import exit, stderr
from typing import TypedDict


config_schema = {
    "type": "object",
    "properties": {
        "dataset": {"type": "string"},
        "platform": {"type": "string"},
        "model": {"type": "string"},
        "model_id": {"type": "string"},
        "sample_amount": {"type": "integer"},
        "system_prompt_prefix": {"type": "string"},
        "system_prompt_suffix": {"type": "string"},
        "temperature": {"type": "number"},
        "rci": {"type": "integer"},
        "rci_variant": {"type": "string"},
        "cot": {"type": "boolean"},
        "output_dir": {"type": "string"},
    },
    "required": [
        "dataset",
        "platform",
        "model",
        "model_id",
        "sample_amount",
        "temperature",
        "rci",
        "cot",
        "output_dir",
    ],
    "additionalProperties": False,
}


class Config(TypedDict):
    # dataset is the decoder that will be used to retrieve the dataset
    # information. Currently, the only supported decoders are SALLM and
    # HumanEvalV2.
    dataset: str
    # platform is the environment that provides the model.
    # Currently, the only supported platform is Ollama.
    platform: str
    # model is the model identifier that is recognized by the platform.
    model: str
    # model_id is used in local file naming to differentiate between models.
    model_id: str
    # sample_amount is the number of samples to generate for each prompt.
    sample_amount: int
    # system_prompt_prefix will be prepended to the system prompt before
    # generation.
    system_prompt_prefix: str
    # system_prompt_suffix will be appended to the system prompt before
    # generation.
    system_prompt_suffix: str
    # temperature is the sampling temperature. The higher the temperature, the
    # more random the model will be.
    temperature: float
    # When rci is set to any value higher than 0, the PET Recursive Criticism
    # and Improvement (RCI) will be used. The amount of RCI iterations is set
    # by the rci parameter.
    rci: int
    # rci_variant is the variant of RCI to use. Currently, the only supported
    # variants are "security" and "energy-efficiency".
    rci_variant: str
    # When cot is set to true, the PET one-shot Chain of Thought (CoT) will be
    # used.
    cot: bool
    # output_dir is the directory where the generated code will be saved.
    output_dir: str


def load_config(config_path: str) -> Config:
    """
    Load the configuration from a JSON file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        Config: Parsed configuration.
    """

    try:
        with open(config_path, "r") as file:
            config_maybe = json_loads(file.read())

        json_validate(instance=config_maybe, schema=config_schema)
        return Config(**config_maybe)
    except FileNotFoundError:
        print(f"Error: The file {config_path} was not found.", file=stderr)
        exit(1)
    except JSONDecodeError as e:
        print(f"Invalid JSON format in config file: {e}", file=stderr)
        exit(1)
    except ValidationError as e:
        print(f"Config file does not match schema: {e}", file=stderr)
        exit(1)
