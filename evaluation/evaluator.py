from concurrent.futures import ThreadPoolExecutor
from csv import writer as csv_writer
from pathlib import Path
from os import chdir, makedirs
from shutil import copy2, copytree, rmtree, which
from subprocess import PIPE, Popen, TimeoutExpired, run as subprocess_run
import sys
from typing import Dict, List, TypedDict


class TestGroups(TypedDict):
    file_path: str
    platform: str
    model: str
    temperature: str
    prompt_variant_id: str
    sample_index: str
    input_prompt_id: str


class Evaluator:
    def __init__(self):
        """
        Initializes the Evaluator class.

        Raises:
            FileNotFoundError: If the test wrapper file or virtual environment is not found.
        """

        #####
        ## Test based tests variables
        #####
        self.__test_wrapper_file_path = Path.cwd() / "evaluation" / "test_wrapper.py"
        if not self.__test_wrapper_file_path.exists():
            raise FileNotFoundError(
                f"Test wrapper file not found at {self.__test_wrapper_file_path}"
            )

        if not (Path.cwd() / "evaluation" / ".venv").exists():
            raise FileNotFoundError(
                "Virtual environment not found at evaluation/.venv. "
                "Please run 'python -m venv .venv' in the evaluation directory. "
                "Also, make sure to install the required packages with 'pip install -r evaluation_requirements.txt'."
            )

        self.__experiment_dir = Path.cwd() / "evaluation" / "temp_evaluation_dump"
        makedirs(self.__experiment_dir, exist_ok=True)

        self.__result_dir = Path.cwd() / "evaluation" / "results"
        makedirs(self.__result_dir, exist_ok=True)

        self.__test_groups = self.__create_test_groups(
            Path.cwd() / "generation" / "generated_code",
            (Path.cwd() / "dataset" / "unittests").glob("**/*.py"),
        )

        #####
        ## Static based tests variables
        #####
        self.__codeql_db_path = Path.cwd() / "evaluation" / "CodeQL_DB"
        makedirs(self.__codeql_db_path, exist_ok=True)
        self.__codeql_results_path = Path.cwd() / "evaluation" / "CodeQL_results"
        makedirs(self.__codeql_results_path, exist_ok=True)
        self.__codeql_code_files_dir = "generation/generated_code"

    def __create_test_groups(
        self, code_files_dir: Path, unittests: List[Path]
    ) -> Dict[str, List[TestGroups]]:
        """
        Create test groups by mapping test files to their corresponding code files.

        Args:
            code_files_dir (Path): The directory containing code files.
            unittests (List[Path]): A list of unit test file paths.

        Returns:
            Dict[str, List[TestGroups]]: A mapping of test files to their corresponding code files and metadata.
        """

        # Map test files by removing 'test_' prefix
        test_file_map = {
            f.stem[5:]: str(f) for f in unittests if f.name.startswith("test_")
        }

        valid_prompt_ids = set(test_file_map.keys())
        test_groups = {}
        py_files = list(code_files_dir.rglob("*.py"))

        for file_path in py_files:
            try:
                parts = file_path.relative_to(code_files_dir).parts

                # Expected: platform/model/T{temp}/variant/R{sample}/{prompt_id}.py
                if len(parts) != 6:
                    continue

                platform, model, temp_str, variant, sample_str, filename = parts

                prompt_id = filename.split(".", 1)[0]
                if prompt_id not in valid_prompt_ids:
                    continue

                # Extract values by removing prefixes
                temperature = (
                    temp_str[1:]
                    if temp_str[0] == "T" and len(temp_str) > 1
                    else temp_str
                )
                sample_index = (
                    sample_str[1:]
                    if sample_str[0] == "R" and len(sample_str) > 1
                    else sample_str
                )

                test_file = test_file_map[prompt_id]

                if test_file not in test_groups:
                    test_groups[test_file] = []

                test_groups[test_file].append(
                    {
                        "file_path": str(file_path),
                        "platform": platform,
                        "model": model,
                        "temperature": temperature,
                        "prompt_variant_id": variant,
                        "sample_index": sample_index,
                        "input_prompt_id": prompt_id,
                    }
                )
            except Exception as e:
                print(f"Error processing file {file_path}: {e}", file=sys.stderr)
                continue

        return test_groups

    def __create_error_csv(self, output_file: Path, error_message: str) -> None:
        """
        Create an CSV file with error information if a test fails.

        Args:
            output_file (Path): The path to the output CSV file.
            error_message (str): The error message to include in the CSV.
        """

        try:
            makedirs(output_file.parent, exist_ok=True)
            with open(output_file, "w", newline="") as f:
                writer = csv_writer(f)
                writer.writerow(["Section", "Key", "Value", "Message", "Run_Number"])
                writer.writerow(
                    ["Error", "execution_error", "error", error_message, ""]
                )
        except Exception as e:
            print(f"Failed to create error CSV {output_file}: {e}", file=sys.stderr)

    def __setup_thread_directory(
        self, thread_dir: Path, test_file: Path, code_file: Path
    ) -> None:
        """
        Set up the thread directory for running tests.

        Args:
            thread_dir (Path): The directory for the thread.
            test_file (Path): The test file to run.
            code_file (Path): The code file to test.
        """

        # Create thread directory
        makedirs(thread_dir, exist_ok=True)

        # Copy test wrapper
        copy2(self.__test_wrapper_file_path, thread_dir / "test_wrapper.py")

        # Copy test file
        copy2(test_file, thread_dir / test_file.name)

        # Copy the code file to test
        copy2(code_file, thread_dir / code_file.name)

        # Copy required folders if they exist
        unittests_dir = Path.cwd() / "dataset" / "unittests"
        for folder_name in ["assets", "Database", "static", "templates"]:
            source_folder = unittests_dir / folder_name
            if source_folder.exists() and source_folder.is_dir():
                copytree(source_folder, thread_dir / folder_name, dirs_exist_ok=True)

    def __run_single_test_based_test(
        self, test_file: Path, code_file_data: list, thread_id: int
    ) -> None:
        """
        Run a single test based on the provided test file and code file data.
        This method sets up a thread-specific directory, runs the test using a subprocess,

        Args:
            test_file (Path): The test file to run.
            code_file_data (list): A list of code file data dictionaries.
            thread_id (int): The ID of the thread.
        """
        thread_dir = self.__experiment_dir / f"thread_{thread_id}"

        original_cwd = Path.cwd()
        chdir(original_cwd)

        try:
            for file_data in code_file_data:
                original_path = file_data["file_path"]
                try:
                    code_file = Path(file_data["file_path"])

                    # Clean up any existing thread directory first
                    if thread_dir.exists():
                        chdir(original_cwd)
                        rmtree(thread_dir, ignore_errors=True)

                    # Set up clean thread directory for this specific test
                    self.__setup_thread_directory(thread_dir, test_file, code_file)

                    chdir(thread_dir)

                    output_filename = (
                        f"result_{file_data['platform']}_{file_data['model']}_"
                        f"T{file_data['temperature']}_{file_data['prompt_variant_id']}_"
                        f"R{file_data['sample_index']}_{file_data['input_prompt_id']}.csv"
                    )
                    output_file = self.__result_dir / output_filename

                    try:
                        proc = Popen(
                            [
                                "../../.venv/scripts/python.exe",
                                "test_wrapper.py",
                                "--test-file",
                                test_file.name,
                                "--output-location",
                                str(output_file),
                            ],
                            cwd=thread_dir,
                            stdout=PIPE,
                            stderr=PIPE,
                            text=True,
                        )
                        proc.communicate(timeout=600)

                        # Check if CSV was actually created
                        if not output_file.exists():
                            self.__create_error_csv(
                                output_file,
                                f"Process failed with return code {proc.returncode}.",
                            )
                    except TimeoutExpired:
                        proc.kill()
                        proc.wait()

                        self.__create_error_csv(
                            output_file,
                            f"Process timeout after 600 seconds for {original_path}",
                        )
                except Exception as e:
                    self.__create_error_csv(
                        output_file, f"Error running test for {original_path}: {str(e)}"
                    )
                finally:
                    # Clean up the thread directory after each test
                    chdir(original_cwd)
                    rmtree(thread_dir, ignore_errors=True)
        except Exception as e:
            print(f"Critical error in thread {thread_id}: {e}", file=sys.stderr)

    def run_all_test_based_tests(self, max_workers: int = 10) -> None:
        """
        Run all test-based tests using multithreading.

        Args:
            max_workers (int, optional): The maximum number of worker threads to use. Defaults to 10.
        """

        # Clean up any existing thread directories before starting
        if self.__experiment_dir.exists():
            rmtree(self.__experiment_dir, ignore_errors=True)
            makedirs(self.__experiment_dir, exist_ok=True)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for i, (test_file_path, code_file_data) in enumerate(
                self.__test_groups.items()
            ):
                futures.append(
                    executor.submit(
                        self.__run_single_test_based_test,
                        Path(test_file_path),
                        code_file_data,
                        i,
                    )
                )

            # Wait for all futures to complete
            for future in futures:
                future.result()

        # Final cleanup of all thread directories
        if self.__experiment_dir.exists():
            rmtree(self.__experiment_dir, ignore_errors=True)

        print("All test-based tests completed!", file=sys.stdout)

    def run_static_based_tests(self):
        """
        Run static-based tests using CodeQL.
        This method creates a CodeQL database from the generated code files and analyzes it for security vulnerabilities.

        Raises:
            EnvironmentError: If CodeQL CLI is not found.
        """

        if which("codeql") is None:
            raise EnvironmentError(
                "CodeQL CLI not found. Please install CodeQL CLI and ensure it is in your PATH."
            )

        subprocess_run(
            [
                "codeql",
                "database",
                "create",
                self.__codeql_db_path,
                "--language=python",
                f"--source-root={self.__codeql_code_files_dir}",
                "--overwrite",
            ],
            check=True,
        )

        subprocess_run(
            [
                "codeql",
                "database",
                "analyze",
                self.__codeql_db_path,
                "--format=sarif-latest",
                "--output",
                f"{self.__codeql_results_path}/results.sarif",
                "python-security-extended",
            ],
            check=True,
        )
