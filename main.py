from argparse import ArgumentParser
from os import makedirs, path as os_path
import sys

from dataset.prompt_loader import load_input_prompts
from experiment_configuration import experiment_configuration
from evaluation.evaluator import Evaluator
from generation.generator import Generator


# Specify which phases of the experiment to run
CODE_GENERATION_PHASE = True
CODE_UNIT_TESTING_PHASE = False
CODE_SECURITY_EVALUATION_PHASE = False


if __name__ == "__main__":
    # Change STDOUT and STDERR to /logs
    makedirs("logs", exist_ok=True)
    sys.stderr = open(os_path.join("logs", "stderr.log"), "w")
    # sys.stdout = open(os_path.join("logs", "stdout.log"), "w")  # Uncomment if you want to redirect stdout as well

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

    if CODE_GENERATION_PHASE:
        print("Starting code generation phase...")
        input_prompts = load_input_prompts(dataset_path=args.dataset)
        generator = Generator(experiment_configuration=experiment_configuration)
        generator.generate(prompts=input_prompts)

    # if CODE_UNIT_TESTING_PHASE:
    #     print("Starting code unit testing phase...")
    #     evaluator = Evaluator()
    #     evaluator.evaluate()
