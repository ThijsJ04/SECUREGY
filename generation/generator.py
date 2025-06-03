from os import makedirs
from pathlib import Path
from typing import List

from dataset.prompt_loader import InputPrompt
from experiment_configuration import ExperimentConfig, PromptEngineeringTechniqueConfig
from generation.backend_handlers import get_backend_handler_by_name


class Generator:
    def __init__(self, experiment_configuration: ExperimentConfig):
        self.__experiment_configuration = experiment_configuration
        self.__output_dir = Path.cwd() / "generation" / "generated_code"
        makedirs(self.__output_dir, exist_ok=True)

    def __apply_PET_to_system_prompt(
        self, system_prompt: str, pet: PromptEngineeringTechniqueConfig
    ) -> str:
        """
        Apply a prompt engineering technique to the system prompt.

        Args:
            system_prompt (str): The original system prompt.
            pet (PromptEngineeringTechniqueConfig): The prompt engineering technique to apply.

        Returns:
            str: The modified system prompt.
        """
        if pet.get("prefix"):
            system_prompt = f"{pet['prefix']}{system_prompt}"
        if pet.get("suffix"):
            system_prompt = f"{system_prompt}{pet['suffix']}"
        return system_prompt

    def __compute_generation_statistics(self, number_of_prompts: int) -> int:
        """
        Compute and print the generation statistics based on the experiment configuration.

        Args:
            number_of_prompts (int): The number of prompts to consider for the statistics.

        Returns:
            int: The total number of programs that will be generated.
        """

        total_programs = 0
        max_time = 0
        for generation in self.__experiment_configuration["generations"]:
            num_temperatures = len(generation["temperatures"])
            num_variants = len(generation["prompt_variants"])
            num_samples = generation["sample_amount"]
            timeout = generation["timeout"]

            programs = num_temperatures * num_variants * number_of_prompts * num_samples

            total_programs += programs
            max_time += (
                programs * timeout
            )  # For max time, assume all are run sequentially

        print("\n" + "=" * 60)
        print("Generation Statistics")
        print("=" * 60)

        print(f"    Total Programs Required    : {total_programs:,}")
        print(f"    Maximum Generation Time   : {max_time / 60:.2f} minutes")

        return total_programs

    def generate(self, prompts: List[InputPrompt]) -> None:
        """
        Generate code using the specified prompts and configurations.

        Args:
            prompts (List[InputPrompt]): The input prompts to use for code generation.
        """
        total_programs = self.__compute_generation_statistics(len(prompts))
        current_program = 0

        default_system_prompt = self.__experiment_configuration["system_prompt"]
        rci_follow_up_system_prompt = self.__experiment_configuration[
            "rci_follow_up_system_prompt"
        ]
        for generation in self.__experiment_configuration["generations"]:
            for temperature in generation["temperatures"]:
                backend_handler = get_backend_handler_by_name(
                    platform=generation["platform"],
                    model=generation["model"],
                    system_prompt=default_system_prompt,
                    rci_follow_up_system_prompt=rci_follow_up_system_prompt,
                    temperature=temperature,
                    timeout=generation["timeout"],
                )

                for prompt_variant in generation["prompt_variants"]:
                    modified_system_prompt = self.__apply_PET_to_system_prompt(
                        default_system_prompt, prompt_variant
                    )
                    backend_handler.change_system_prompt(modified_system_prompt)

                    for input_prompt in prompts:
                        if "COT" in prompt_variant and prompt_variant["COT"]:
                            input_prompt["prompt"] = (
                                f"Q: {input_prompt['prompt']}\n\n"
                                "A: Let's think step by step."
                            )

                        for sample_index in range(generation["sample_amount"]):
                            current_program += 1
                            print(
                                f"Generating program [{current_program}/{total_programs}]"
                            )

                            if "RCI" in prompt_variant and prompt_variant["RCI"]:
                                code = backend_handler.rci_request(
                                    prompt_variant["RCI"]["total_iterations"],
                                    prompt_variant["RCI"]["variant"],
                                    input_prompt["prompt"],
                                )
                            else:
                                code = backend_handler.request(input_prompt["prompt"])

                            output_path = (
                                self.__output_dir
                                / f"{generation['platform']}"
                                / f"{generation['model'].split(':')[0]}"
                                / f"T{temperature}"
                                / f"{prompt_variant['id']}"
                                / f"R{sample_index}"
                                / f"{input_prompt['id']}.py"
                            )
                            makedirs(output_path.parent, exist_ok=True)
                            with open(
                                output_path, "w", encoding="utf-8"
                            ) as output_file_obj:
                                output_file_obj.write(code if code else "")
