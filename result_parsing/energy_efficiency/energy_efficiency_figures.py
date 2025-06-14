import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from typing import Tuple


def create_heatmap_to_base(
    results_df: pd.DataFrame, figsize: Tuple[int, int] = (12, 8)
) -> None:
    viz_data = results_df.copy()

    viz_data["config"] = (
        viz_data["platform"]
        + " | "
        + viz_data["model"]
        + " | "
        + viz_data["temperature"].astype(str)
    )

    heatmap_data = viz_data.pivot(
        index="config", columns="prompt_variant_id", values="score"
    )
    heatmap_data = heatmap_data.fillna(0)

    plt.figure(figsize=figsize)

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="RdYlGn",
        center=0,
        cbar_kws={"label": "Score vs Base"},
        linewidths=0.5,
        square=False,
    )

    plt.title(
        "Energy Efficiency Performance vs Base\n(Positive = Better, Negative = Worse)",
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
) -> None:
    viz_data = results_df.copy()

    viz_data["config1"] = (
        viz_data["platform1"]
        + " | "
        + viz_data["model1"]
        + " | "
        + viz_data["temperature1"].astype(str)
    )

    viz_data["config2"] = (
        viz_data["platform2"]
        + " | "
        + viz_data["model2"]
        + " | "
        + viz_data["temperature2"].astype(str)
    )

    heatmap_data = viz_data.pivot(index="config1", columns="config2", values="score")
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
        "Base Variant Energy Efficiency Comparison\n(Positive = Row Better than Column, Negative = Row Worse than Column)",
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
