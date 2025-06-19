from result_parsing.utils.transform_test_based_results_to_pd import (
    transform_test_based_results_to_pd,
)


def clean_error_message(message: str) -> str:
    """
    Extract core error type from detailed error messages.

    Args:
        message (str): Detailed error message.

    Returns:
        str: Extracted core error type.
    """

    if message.startswith("Error running test for"):
        return "Error running test"
    elif message.startswith("Process timeout after"):
        return "Process timeout"
    elif message.startswith("Process failed with return code"):
        return "Process failed"
    else:
        return message


def get_error_rates(
    output_path: str = "result_parsing/results/error_summary.csv",
) -> None:
    """
    Calculate error rates from test-based results and save a summary CSV.
    """

    results_df = transform_test_based_results_to_pd(section_filter="Error")
    print(results_df.head())
    results_df["Message"] = results_df["Message"].apply(clean_error_message)
    print(results_df.head())

    error_summary = results_df.pivot_table(
        values="Key",
        index=["platform", "model", "temperature", "prompt_variant_id"],
        columns="Message",
        aggfunc="count",
        fill_value=0,
    )

    error_summary["Total Errors (max 100)"] = error_summary.sum(axis=1)
    error_summary.to_csv(output_path)
