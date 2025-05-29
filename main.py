from argparse import ArgumentParser
from os import makedirs, path as os_path
import sys

from dataset.prompt_loader import load_input_prompts
from experiment_configuration import experiment_configuration
from generation.generator import Generator


if __name__ == "__main__":
    # Change STDOUT and STDERR to /logs
    makedirs("logs", exist_ok=True)
    sys.stdout = open(os_path.join("logs", "stdout.log"), "w")
    sys.stderr = open(os_path.join("logs", "stderr.log"), "w")

    parser = ArgumentParser(
        description="Generate code using a language model and evaluate it on security and energy efficiency."
    )
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        help="Relative path to the dataset file.",
        default="dataset/prompts/SALLM_subset.json",
    )

    args = parser.parse_args()
    input_prompts = load_input_prompts(dataset_path=args.dataset)
    generator = Generator(experiment_configuration=experiment_configuration)
    generator.generate(prompts=input_prompts)
