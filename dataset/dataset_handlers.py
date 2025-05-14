from generation.config_parser import Config
from json import loads as json_loads
from os import path
from sys import exit, stderr
from typing import Dict, Generic, List, Type, TypeVar, TypedDict, Union

T = TypeVar("T")


class DatasetHandler(Generic[T]):
    def __init__(self, dataset_path: str, dataset_structure: Type[T]):
        self.dataset_path = dataset_path
        self.dataset_structure = dataset_structure

    def load_dataset(self) -> List[T]:
        """
        Load the dataset from the specified path and return it as a list of
        dictionaries.

        Returns:
            List[T]: A list of dictionaries representing the dataset.
        """
        with open(self.dataset_path, "r", encoding="utf-8") as file:
            return self.dataset_structure(**json_loads(file.read()))


class GenerationVariables(TypedDict):
    task_id: str
    prompt: str
    output_file: str


class SALLM(TypedDict):
    id: str
    technique: str
    source: str
    prompt: str
    insecure_code: str


class SALLMDatasetHandler(DatasetHandler[SALLM]):
    def get_generation_variables_for_entry(
        self, config: Config, entry: SALLM, sample_index: int
    ) -> GenerationVariables:
        """
        Decodes the prompt entry for the SALLM dataset.
        """

        prompt_id = ("_").join(entry["id"].split("_")[2:])
        prompt = entry["prompt"]
        output_file = path.normpath(
            path.join(
                config["output_dir"],
                f"{config['model_id']}_{config['temperature']}_{entry['technique']}_R{sample_index}",
                f"{prompt_id}",
            )
        )

        return GenerationVariables(
            task_id=prompt_id,
            prompt=prompt,
            output_file=output_file,
        )


class HumanEvalV2(TypedDict):
    task_id: str
    prompt: str
    entry_point: str
    canonical_solution: str
    test: str


class HumanEvalV2DatasetHandler(DatasetHandler[HumanEvalV2]):
    def get_generation_variables_for_entry(
        self, config: Config, entry: HumanEvalV2, sample_index: int
    ) -> GenerationVariables:
        """
        Decodes the prompt entry for the HumanEvalV2 dataset.
        """

        prompt_id = entry["task_id"].split("/")[1]
        prompt = entry["prompt"]
        output_file = path.normpath(
            path.join(
                config["output_dir"],
                f"{config['model_id']}_{config['temperature']}_{prompt_id}",
                f"R{sample_index}.py",
            )
        )

        return GenerationVariables(
            task_id=prompt_id,
            prompt=prompt,
            output_file=output_file,
        )


dataset_locations: Dict[str, str] = {
    "human_eval_v2": "dataset/dataset_dump/human-eval-v2.json",
    "sallm": "dataset/dataset_dump/SALLM.json",
}


def get_dataset_handler_by_name(
    dataset_name: "HumanEvalV2 | SALLM",
) -> Union[DatasetHandler[HumanEvalV2], DatasetHandler[SALLM]]:
    """
    Get the dataset handler by name.

    Args:
        dataset_name (HumanEvalV2 | SALLM): The name of the dataset to load.

    Returns:
        Union[DatasetHandler[HumanEvalV2], DatasetHandler[SALLM]]: The dataset handler for the specified dataset.
    """
    if dataset_name == "HumanEvalV2":
        return HumanEvalV2DatasetHandler(
            dataset_path=dataset_locations["human_eval_v2"],
            dataset_structure=HumanEvalV2,
        )
    elif dataset_name == "SALLM":
        return SALLMDatasetHandler(
            dataset_path=dataset_locations["sallm"],
            dataset_structure=SALLM,
        )
    else:
        print(f"Dataset {dataset_name} not supported.", file=stderr)
        exit(1)
