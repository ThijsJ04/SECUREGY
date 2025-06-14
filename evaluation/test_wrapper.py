from argparse import ArgumentParser
from codecarbon import EmissionsTracker
from csv import writer as csv_writer
from tempfile import TemporaryDirectory
from time import time
from typing import Dict, Union, List
from unittest import TextTestResult, TextTestRunner, defaultTestLoader


class CSVTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append((test.id(), "success", ""))

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append((test.id(), "error", str(err[1])))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append((test.id(), "failure", str(err[1])))

    def save_to_csv(
        self, filename, all_emissions_data: Union[List[Dict[str, float]], None] = None
    ):
        with open(filename, "w", newline="") as f:
            writer = csv_writer(f)

            writer.writerow(["Section", "Key", "Value", "Message", "Run_Number"])

            for test_id, result, message in self.results:
                writer.writerow(["Test", test_id, result, message, ""])

            if all_emissions_data:
                for run_number, emissions_data in enumerate(all_emissions_data, 1):
                    for metric_name, metric_value in emissions_data.items():
                        writer.writerow(
                            [
                                "Emission_Metric",
                                metric_name,
                                metric_value,
                                "",
                                run_number,
                            ]
                        )


def run_emission_test(test_file: str) -> List[Dict[str, float]]:
    """
    Run the emission test for the given test suite.
    This function tracks 50 runs of the test suite, each for 1 second,
    and collects all individual emissions data.

    Args:
        test_file (str): The test file to run

    Returns:
        List[Dict[str, float]]: A list containing all individual emissions data from each run
    """

    all_emissions_data = []

    # Create a temporary directory for emissions files to avoid conflicts
    with TemporaryDirectory() as temp_emissions_dir:
        for i in range(50):
            try:
                tracker = EmissionsTracker(
                    output_dir=temp_emissions_dir, output_file=f"emissions_run_{i}.csv"
                )

                tracker.start()
                start_time = time()
                while time() - start_time < 1:  # Run for 1 second
                    test_suite = defaultTestLoader.loadTestsFromName(test_file)
                    runner = TextTestRunner(resultclass=CSVTestResult)
                    runner.run(test_suite)
                tracker.stop()

                try:
                    emissions: float = tracker.final_emissions_data.emissions
                    duration: float = tracker.final_emissions_data.duration
                    energy_consumed: float = (
                        tracker.final_emissions_data.energy_consumed
                    )

                    # Store individual run data
                    run_data = {
                        "emissions_kgCO2eq": emissions,
                        "duration_seconds": duration,
                        "energy_consumed_kwh": energy_consumed,
                    }
                    all_emissions_data.append(run_data)

                except Exception as e:
                    print(f"Error processing emissions data for run {i}: {e}")
                    # Store empty data for failed runs to maintain run numbering
                    run_data = {
                        "emissions_kgCO2eq": 0.0,
                        "duration_seconds": 0.0,
                        "energy_consumed_kwh": 0.0,
                    }
                    all_emissions_data.append(run_data)

            except Exception as e:
                print(f"Error in emissions tracking for run {i}: {e}")
                # Store empty data for failed runs to maintain run numbering
                run_data = {
                    "emissions_kgCO2eq": 0.0,
                    "duration_seconds": 0.0,
                    "energy_consumed_kwh": 0.0,
                }
                all_emissions_data.append(run_data)
                continue

    return all_emissions_data if all_emissions_data else None


def run(test_file: str, output_location: str) -> None:
    """
    Run the test suite and collect emissions data.

    Args:
        test_file (str): The path to the test file to run.
        output_location (str): The relative path to the output CSV file where results will be saved.
    """

    # Remove .py extension if present
    if test_file.endswith(".py"):
        test_file = test_file[:-3]

    try:
        test_suite = defaultTestLoader.loadTestsFromName(test_file)
        if not test_suite.countTestCases():
            result = CSVTestResult(None, None, 0)
            result.results.append(("No tests available", "info", ""))
            result.save_to_csv(output_location, None)
            return result, None

        runner = TextTestRunner(resultclass=CSVTestResult)
        correctness_result = runner.run(test_suite)
        all_emission_results = run_emission_test(test_file)
        correctness_result.save_to_csv(output_location, all_emission_results)
    except Exception as e:
        correctness_result = CSVTestResult(None, None, 0)
        correctness_result.results.append(("Error", "error", str(e)))
        correctness_result.save_to_csv(output_location, None)


if __name__ == "__main__":
    parser = ArgumentParser(description="Run unit tests and collect emissions data.")

    parser.add_argument(
        "--test-file",
        type=str,
        required=True,
        help="Path to the test file to run. Must be a Python file with 'test_' prefix.",
    )

    parser.add_argument(
        "--output-location",
        type=str,
        required=True,
        help="Relative path to the output CSV file where results will be saved.",
    )

    args = parser.parse_args()
    run(args.test_file, args.output_location)
