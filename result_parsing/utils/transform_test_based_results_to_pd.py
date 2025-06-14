import pandas as pd
from pathlib import Path
import sys
from typing import TypedDict, Optional, List


class FilenameResult(TypedDict):
    platform: str
    model: str
    temperature: float
    prompt_variant_id: str
    run_index: int
    prompt_id: str


def parse_result_filename(filename: str) -> Optional[FilenameResult]:
    """
    Parse the filename to extract metadata about the energy efficiency results.

    Args:
        filename (str): The name of the result file.

    Returns:
        Optional[FilenameResult]: A dictionary containing the parsed metadata or None if parsing fails.
    """

    # Remove .csv extension and 'result_' prefix
    name = filename.replace(".csv", "").replace("result_", "", 1)

    # Split by underscores, but be careful with model names that might contain underscores
    parts = name.split("_")

    if len(parts) < 6:
        return None

    try:
        platform = parts[0]

        # Find temperature part (starts with 'T')
        temp_idx = next(i for i, part in enumerate(parts) if part.startswith("T"))

        # Model is everything between platform and temperature
        model = "_".join(parts[1:temp_idx])
        temperature = float(parts[temp_idx][1:])  # Remove 'T' prefix

        # Find run index part (starts with 'R')
        run_idx = next(i for i, part in enumerate(parts) if part.startswith("R"))
        run_index = int(parts[run_idx][1:])  # Remove 'R' prefix

        # Prompt variant is between temperature and run index
        prompt_variant_id = "_".join(parts[temp_idx + 1 : run_idx])

        # Prompt ID is everything after run index
        prompt_id = "_".join(parts[run_idx + 1 :])

        return dict(
            platform=platform,
            model=model,
            temperature=temperature,
            prompt_variant_id=prompt_variant_id,
            run_index=run_index,
            prompt_id=prompt_id,
        )
    except (ValueError, IndexError, StopIteration):
        return None


def transform_test_based_results_to_pd(
    section_filter: str,
    exclude_keys: List[str] = None,
    select_columns: List[str] = None,
) -> pd.DataFrame:
    """
    Transform test-based results from CSV files into a pandas DataFrame.

    Args:
        section_filter (str): The section of the results to filter by.
        exclude_keys (List[str], optional): Keys to exclude from the results. Defaults to None.
        select_columns (List[str], optional): Columns to select from the results. Defaults to None.

    Returns:
        pd.DataFrame: DataFrame containing the transformed results.
    """

    all_dataframes = []
    csv_files = list((Path.cwd() / "evaluation" / "results").glob("*.csv"))
    for csv_file in csv_files:
        metadata = parse_result_filename(csv_file.name)
        corresponding_csv = pd.read_csv(csv_file)

        filter_condition = corresponding_csv["Section"] == section_filter
        if exclude_keys:
            for key in exclude_keys:
                filter_condition = filter_condition & (corresponding_csv["Key"] != key)

        filtered_csv = corresponding_csv[filter_condition]
        if select_columns:
            filtered_csv = filtered_csv[select_columns]
        filtered_csv = filtered_csv.reset_index(drop=True)

        metadata_df = pd.DataFrame([metadata] * len(filtered_csv))
        filtered_csv = pd.concat([metadata_df, filtered_csv], axis=1)
        all_dataframes.append(filtered_csv)

    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
    else:
        print("No valid CSV files found to process", file=sys.stderr)
        sys.exit(1)

    return combined_df
