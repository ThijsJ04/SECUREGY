import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from typing import Tuple


def compute_scores_to_base(results_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute scores comparing each variant to the base variant for each configuration.

    Args:
        results_df (pd.DataFrame): The DataFrame containing the results.

    Raises:
        ValueError: If no valid comparisons are found.

    Returns:
        pd.DataFrame: A DataFrame containing the aggregated scores.
    """

    aggregated_scores = []

    for config in results_df["config"].unique():
        config_data = results_df[results_df["config"] == config]

        # Find base variant data for this config
        base_data = config_data[config_data["variant_id"] == "base"]
        if base_data.empty:
            continue

        # Get unique variants (excluding base)
        variants = config_data[config_data["variant_id"] != "base"][
            "variant_id"
        ].unique()

        for variant in variants:
            variant_data = config_data[config_data["variant_id"] == variant]
            total_score = 0
            total_comparisons = 0

            for _, base_row in base_data.iterrows():
                metric = base_row["metric"]
                k_val = base_row["k_value"]
                base_value = base_row["value"]

                # Find corresponding variant row
                variant_row = variant_data[
                    (variant_data["metric"] == metric)
                    & (variant_data["k_value"] == k_val)
                ]

                if not variant_row.empty:
                    variant_value = variant_row["value"].iloc[0]

                    # Higher value is better
                    if variant_value > base_value:
                        total_score += 1
                    elif variant_value == base_value:
                        total_score += 0
                    else:
                        total_score += -1

                    total_comparisons += 1

            if total_comparisons > 0:
                aggregated_scores.append(
                    {"config": config, "variant_id": variant, "score": total_score}
                )

    if not aggregated_scores:
        raise ValueError("No valid to-base comparisons found")

    return pd.DataFrame(aggregated_scores)


def compute_scores_between_bases(results_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute scores comparing each base variant to every other base variant.

    Args:
        results_df (pd.DataFrame): The DataFrame containing the results.

    Raises:
        ValueError: If no base variants are found.
        ValueError: If no valid comparisons are found.

    Returns:
        pd.DataFrame: A DataFrame containing the aggregated scores.
    """

    aggregated_scores = []

    # Filter to get only base variants
    base_data = results_df[results_df["variant_id"] == "base"]
    if base_data.empty:
        raise ValueError("No base variants found")

    configs = base_data["config"].unique()

    for config1 in configs:
        for config2 in configs:
            if config1 == config2:
                # Same configuration gets score of 0
                aggregated_scores.append(
                    {"config1": config1, "config2": config2, "score": 0}
                )
                continue

            config1_data = base_data[base_data["config"] == config1]
            config2_data = base_data[base_data["config"] == config2]

            total_score = 0
            total_comparisons = 0

            for _, config1_row in config1_data.iterrows():
                metric = config1_row["metric"]
                k_val = config1_row["k_value"]
                config1_value = config1_row["value"]

                # Find corresponding config2 row
                config2_row = config2_data[
                    (config2_data["metric"] == metric)
                    & (config2_data["k_value"] == k_val)
                ]

                if not config2_row.empty:
                    config2_value = config2_row["value"].iloc[0]

                    # Higher value is better
                    if config1_value > config2_value:
                        total_score += 1
                    elif config1_value == config2_value:
                        total_score += 0
                    else:
                        total_score += -1

                    total_comparisons += 1

            if total_comparisons > 0:
                aggregated_scores.append(
                    {"config1": config1, "config2": config2, "score": total_score}
                )

    if not aggregated_scores:
        raise ValueError("No valid base-to-base comparisons found")

    return pd.DataFrame(aggregated_scores)


def create_heatmap_to_base(
    results_df: pd.DataFrame, figsize: Tuple[int, int] = (12, 8)
) -> plt.Figure:
    """
    Create a heatmap comparing each prompt variant's security performance against the base variant.

    Args:
        results_df (pd.DataFrame): The DataFrame containing the results.
        figsize (Tuple[int, int], optional): The size of the figure. Defaults to (12, 8).

    Returns:
        plt.Figure: The created heatmap figure.
    """

    results_df["config"] = (
        results_df["platform"]
        + " | "
        + results_df["model"]
        + " | "
        + results_df["temperature"]
    )

    scores_to_base = compute_scores_to_base(results_df)

    heatmap_data = scores_to_base.pivot(
        index="config", columns="variant_id", values="score"
    )
    heatmap_data = heatmap_data.fillna(0)

    plt.figure(figsize=figsize)

    ax = sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="RdYlGn",
        center=0,
        cbar_kws={"label": "Aggregated Score vs Base"},
        linewidths=0.0,
        square=False,
    )

    for i in range(len(heatmap_data.index)):
        ax.axhline(y=i, color="white", linewidth=5.0)

    plt.title(
        "Security Performance vs Base (All Metrics Aggregated)\n(Positive = Better, Negative = Worse)",
        fontsize=14,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Prompt Variant ID", fontweight="bold")
    plt.ylabel("Configuration (Platform | Model | Temperature)", fontweight="bold")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

    plt.tight_layout()
    return plt.gcf()


def create_heatmap_between_bases(
    results_df: pd.DataFrame, figsize: Tuple[int, int] = (14, 12)
) -> plt.Figure:
    """
    Create a heatmap comparing the security performance of different base variants against each other.

    Args:
        results_df (pd.DataFrame): The DataFrame containing the results.
        figsize (Tuple[int, int], optional): The size of the figure. Defaults to (14, 12).

    Returns:
        plt.Figure: The created heatmap figure.
    """

    results_df["config"] = (
        results_df["platform"]
        + " | "
        + results_df["model"]
        + " | "
        + results_df["temperature"]
    )

    scores_between_bases = compute_scores_between_bases(results_df)

    # Create config labels for both dimensions
    scores_between_bases["config1_label"] = scores_between_bases["config1"]
    scores_between_bases["config2_label"] = scores_between_bases["config2"]

    heatmap_data = scores_between_bases.pivot(
        index="config1", columns="config2", values="score"
    )
    heatmap_data = heatmap_data.fillna(0)

    plt.figure(figsize=figsize)

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="RdYlGn",
        center=0,
        cbar_kws={"label": "Score (Row vs Column)"},
        linewidths=0.5,
        square=True,
    )

    plt.title(
        "Base Variant Security Performance Comparison\n(Positive = Row Better than Column, Negative = Row Worse than Column)",
        fontsize=14,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Configuration (Platform | Model | Temperature)", fontweight="bold")
    plt.ylabel("Configuration (Platform | Model | Temperature)", fontweight="bold")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

    plt.tight_layout()
    return plt.gcf()
