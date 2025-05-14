from argparse import ArgumentParser
from os import makedirs, path as os_path
from sys import path as sys_path
from typing import Any, Union

# Add the parent directory to sys.path. I don't want to create an entire
# package just for import simplicity.
sys_path.append(os_path.dirname(os_path.dirname(os_path.abspath(__file__))))

from backend_handlers import OllamaBackendHandler, get_backend_handler_by_name
from config_parser import Config, load_config
from dataset.dataset_handlers import (
    HumanEvalV2DatasetHandler,
    SALLMDatasetHandler,
    get_dataset_handler_by_name,
)


def generate(
    backend_handler: OllamaBackendHandler,
    config: Config,
    dataset_handler: Union[HumanEvalV2DatasetHandler, SALLMDatasetHandler],
) -> None:
    dataset = dataset_handler.load_dataset()
    for index, entry in enumerate(dataset):
        print(f"Generating code for entry {index + 1}/{len(dataset)}")
        for sample_index in range(config["sample_amount"]):
            generation_variables = dataset_handler.get_generation_variables_for_entry(
                config, entry, sample_index
            )

            if config["rci"] > 0:
                code = backend_handler.rci_request(
                    config["rci_variant"] if config["rci_variant"] else "security",
                    generation_variables["prompt"],
                )
            else:
                code = backend_handler.request(generation_variables["prompt"])

            if code is None:
                continue

            makedirs(
                os_path.dirname(generation_variables["output_file"]), exist_ok=True
            )
            with open(
                generation_variables["output_file"], "w", encoding="utf-8"
            ) as output_file_obj:
                output_file_obj.write(code)


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate code using a language model.")
    parser.add_argument(
        "-c", "--config", type=str, required=True, help="Path to the config file."
    )
    args = parser.parse_args()

    config = load_config(args.config)

    backend_handler = get_backend_handler_by_name(
        config,
        config["system_prompt_prefix"]
        + "You are an AI code developer. Always respond with a code block. Do not include any explanations or comments."
        + config["system_prompt_suffix"],
    )
    dataset_handler = get_dataset_handler_by_name(config["dataset"])

    generate(backend_handler, config, dataset_handler)
