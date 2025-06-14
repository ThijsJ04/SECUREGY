from collections import defaultdict
import pandas as pd
from scipy import stats
from typing import Optional

from result_parsing.energy_efficiency.energy_efficiency_figures import (
    create_heatmap_to_base,
    create_heatmap_between_bases,
)
from result_parsing.utils.transform_test_based_results_to_pd import (
    transform_test_based_results_to_pd,
)


def get_energy_data(
    df: pd.DataFrame, prompt_variant_id: Optional[str] = None
) -> pd.DataFrame:
    """
    Extract energy consumption data from the DataFrame.
    This function filters the DataFrame to return only the rows where the Key is 'energy_consumed_kwh'.

    Args:
        df (pd.DataFrame): DataFrame containing the results.
        prompt_variant_id (Optional[str], optional): Prompt variant ID to filter by. Defaults to None.

    Returns:
        pd.DataFrame: DataFrame containing the energy consumption data.
    """

    df_energy = df[df["Key"] == "energy_consumed_kwh"].copy()
    if prompt_variant_id is not None:
        df_energy = df_energy[df_energy["prompt_variant_id"] == prompt_variant_id]
    return df_energy


def compare_data_bundles(data_a: pd.DataFrame, data_b: pd.DataFrame) -> int:
    """
    Compare two data bundles using statistical tests to determine if one is significantly better or worse than the other.
    This function uses the Mann-Whitney U test to compare the energy consumption data of two different prompt variants.

    Args:
        data_a (pd.DataFrame): Energy consumption data for the first prompt variant.
        data_b (pd.DataFrame): Energy consumption data for the second prompt variant.

    Returns:
        int: Returns 1 if data_a is significantly better (lower energy) than data_b,
             -1 if data_a is significantly worse (higher energy) than data_b,
             and 0 if there is no significant difference.
    """

    if len(data_a) > 0 and len(data_b) > 0:
        # Both data bundles exist - perform statistical test

        # Test if data_a is significantly BETTER (lower energy) than data_b
        _, p_better = stats.mannwhitneyu(data_a, data_b, alternative="less")

        # Test if data_a is significantly WORSE (higher energy) than data_b
        _, p_worse = stats.mannwhitneyu(data_a, data_b, alternative="greater")

        if p_better < 0.05:
            return 1  # Significantly better
        elif p_worse < 0.05:
            return -1  # Significantly worse
        else:
            return 0  # No significant difference

    elif len(data_a) > 0 and len(data_b) == 0:
        # data_a exists, data_b doesn't
        return -1

    elif len(data_a) == 0 and len(data_b) > 0:
        # data_b exists, data_a doesn't
        return 1


def analyze_energy_efficiency_to_base(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze energy efficiency of different prompt variants compared to the base variant.
    This function compares the energy consumption of different prompt variants against the base variant
    per platform, model, and temperature combination.

    Args:
        df (pd.DataFrame): The input DataFrame containing energy consumption data.

    Returns:
        pd.DataFrame: A DataFrame containing the analysis results.
    """

    df_energy = get_energy_data(df)
    combinations = df_energy[["platform", "model", "temperature"]].drop_duplicates()
    results = []

    for _, combo in combinations.iterrows():
        platform, model, temp = combo["platform"], combo["model"], combo["temperature"]

        combo_data = df_energy[
            (df_energy["platform"] == platform)
            & (df_energy["model"] == model)
            & (df_energy["temperature"] == temp)
        ]

        variant_ids = combo_data["prompt_variant_id"].unique()
        variant_scores = defaultdict(int)
        run_indices = combo_data["run_index"].unique()

        for variant_id in variant_ids:
            if variant_id == "base":
                continue

            for run_idx in run_indices:
                base_data = combo_data[
                    (combo_data["prompt_variant_id"] == "base")
                    & (combo_data["run_index"] == run_idx)
                ]["Value"].values

                variant_data = combo_data[
                    (combo_data["prompt_variant_id"] == variant_id)
                    & (combo_data["run_index"] == run_idx)
                ]["Value"].values

                variant_scores[variant_id] += compare_data_bundles(
                    variant_data, base_data
                )

        for variant_id, score in variant_scores.items():
            results.append(
                {
                    "platform": platform,
                    "model": model,
                    "temperature": temp,
                    "prompt_variant_id": variant_id,
                    "score": score,
                }
            )

    return pd.DataFrame(results)


def analyze_energy_efficiency_between_bases(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze energy efficiency between different base variants.
    This function compares energy consumption data across different platform, model, and temperature combinations.

    Args:
        df (pd.DataFrame): The input DataFrame containing energy consumption data.

    Returns:
        pd.DataFrame: A DataFrame containing the comparison results between different base variants.
    """

    df_energy_base = get_energy_data(df, prompt_variant_id="base")
    combinations = df_energy_base[
        ["platform", "model", "temperature"]
    ].drop_duplicates()
    results = []

    for _, combo1 in combinations.iterrows():
        platform1, model1, temp1 = (
            combo1["platform"],
            combo1["model"],
            combo1["temperature"],
        )

        for _, combo2 in combinations.iterrows():
            platform2, model2, temp2 = (
                combo2["platform"],
                combo2["model"],
                combo2["temperature"],
            )

            if platform1 == platform2 and model1 == model2 and temp1 == temp2:
                score = 0
            else:
                combo1_data = df_energy_base[
                    (df_energy_base["platform"] == platform1)
                    & (df_energy_base["model"] == model1)
                    & (df_energy_base["temperature"] == temp1)
                ]

                combo2_data = df_energy_base[
                    (df_energy_base["platform"] == platform2)
                    & (df_energy_base["model"] == model2)
                    & (df_energy_base["temperature"] == temp2)
                ]

                run_indices1 = set(combo1_data["run_index"].unique())
                run_indices2 = set(combo2_data["run_index"].unique())
                common_runs = run_indices1.intersection(run_indices2)

                score = 0
                for run_idx in common_runs:
                    combo1_run_data = combo1_data[combo1_data["run_index"] == run_idx][
                        "Value"
                    ].values
                    combo2_run_data = combo2_data[combo2_data["run_index"] == run_idx][
                        "Value"
                    ].values

                    score += compare_data_bundles(combo1_run_data, combo2_run_data)

            results.append(
                {
                    "platform1": platform1,
                    "model1": model1,
                    "temperature1": temp1,
                    "platform2": platform2,
                    "model2": model2,
                    "temperature2": temp2,
                    "score": score,
                }
            )

    return pd.DataFrame(results)


def parse_energy_efficiency_results():
    """
    Parse energy efficiency results from CSV files in the evaluation/results directory.
    This function reads all CSV files, extracts relevant data, and generates heatmaps comparing energy efficiency.
    """

    results_df = transform_test_based_results_to_pd(
        section_filter="Emission_Metric",
        exclude_keys=["duration_seconds", "emissions_kgCO2eq"],
        select_columns=["Key", "Value", "Run_Number"],
    )
    results_df["Value"] = results_df["Value"].astype(float)

    results_to_base = analyze_energy_efficiency_to_base(results_df)
    heatmap_to_base = create_heatmap_to_base(results_to_base)
    heatmap_to_base.savefig(
        "result_parsing/results/energy_efficiency_heatmap_to_base.png"
    )

    results_between_bases = analyze_energy_efficiency_between_bases(results_df)
    heatmap_between_bases = create_heatmap_between_bases(results_between_bases)
    heatmap_between_bases.savefig(
        "result_parsing/results/energy_efficiency_heatmap_between_bases.png"
    )
