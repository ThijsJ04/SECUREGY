from argparse import ArgumentParser
from os import makedirs, path as os_path
import sys

from dataset.prompt_loader import load_input_prompts
from experiment_configuration import experiment_configuration
from evaluation.evaluator import Evaluator
from generation.generator import Generator
from generation.post_processing import apply_post_processing
from result_parsing.energy_efficiency.energy_efficiency_parsing import (
    parse_energy_efficiency_results,
)
from result_parsing.security.security_parsing import parse_security_results

#####
## Specify which phases of the experiment to run
#####
CODE_GENERATION_PHASE = True
CODE_GENERATION_PHASE_APPLY_POST_PROCESSING = True
CODE_EVALUATION_PHASE = True
RESULT_PARSING_PHASE = True

if __name__ == "__main__":
    # Change STDOUT and STDERR to /logs
    makedirs("logs", exist_ok=True)
    sys.stderr = open(os_path.join("logs", "stderr.log"), "w")
    sys.stdout = open(os_path.join("logs", "stdout.log"), "w")

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
        print("Starting code generation phase...", file=sys.stdout)
        input_prompts = load_input_prompts(dataset_path=args.dataset)
        generator = Generator(experiment_configuration=experiment_configuration)
        generator.generate(prompts=input_prompts)
        if CODE_GENERATION_PHASE_APPLY_POST_PROCESSING:
            print("Applying post-processing to generated code...", file=sys.stdout)
            apply_post_processing(dataset_path=args.dataset)
        else:
            print("Skipping post-processing of generated code.", file=sys.stdout)
    else:
        print("Skipping code generation phase.", file=sys.stdout)

    if CODE_EVALUATION_PHASE:
        print("Starting code evaluation phase...", file=sys.stdout)
        evaluator = Evaluator()
        evaluator.run_all_test_based_tests()
        evaluator.run_static_based_tests()
    else:
        print("Skipping code evaluation phase.", file=sys.stdout)

    if RESULT_PARSING_PHASE:
        print("Starting result parsing phase...", file=sys.stdout)
        parse_energy_efficiency_results()
        parse_security_results(k_values=[1, 3, 5])
    else:
        print("Skipping result parsing phase.", file=sys.stdout)
