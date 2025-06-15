import pytest
import pandas as pd

import matplotlib.pyplot as plt
from result_parsing.security.security_figures import (
    compute_scores_to_base,
    compute_scores_between_bases,
    create_heatmap_to_base,
    create_heatmap_between_bases,
)


class TestComputeScores:
    def test_compute_scores_to_base_correct(self):
        """Test that variants are correctly scored against base with mixed performance metrics."""

        data = [
            {
                "config": "config1",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
            {
                "config": "config1",
                "variant_id": "base",
                "metric": "secure@1",
                "k_value": 1,
                "value": 0.3,
            },
            {
                "config": "config1",
                "variant_id": "variant1",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.7,
            },
            {
                "config": "config1",
                "variant_id": "variant1",
                "metric": "secure@1",
                "k_value": 1,
                "value": 0.2,
            },
            {
                "config": "config1",
                "variant_id": "variant2",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.4,
            },
            {
                "config": "config1",
                "variant_id": "variant2",
                "metric": "secure@1",
                "k_value": 1,
                "value": 0.6,
            },
        ]
        df = pd.DataFrame(data)

        result = compute_scores_to_base(df)

        assert len(result) == 2
        assert "variant1" in result["variant_id"].values
        assert "variant2" in result["variant_id"].values

        # variant1: pass@1 better (+1), secure@1 worse (-1) = total 0
        variant1_score = result[result["variant_id"] == "variant1"]["score"].iloc[0]
        assert variant1_score == 0

        # variant2: pass@1 worse (-1), secure@1 better (+1) = total 0
        variant2_score = result[result["variant_id"] == "variant2"]["score"].iloc[0]
        assert variant2_score == 0

    def test_compute_scores_to_base_error(self):
        """Test that ValueError is raised when no base variants exist in the data."""

        data = [
            {
                "config": "config1",
                "variant_id": "variant1",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
        ]
        df = pd.DataFrame(data)

        with pytest.raises(ValueError, match="No valid to-base comparisons found"):
            compute_scores_to_base(df)

    def test_compute_scores_between_bases_correct(self):
        """Test that base configurations are correctly scored against each other in a comparison matrix."""

        data = [
            {
                "config": "config1",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.8,
            },
            {
                "config": "config1",
                "variant_id": "base",
                "metric": "secure@1",
                "k_value": 1,
                "value": 0.6,
            },
            {
                "config": "config2",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
            {
                "config": "config2",
                "variant_id": "base",
                "metric": "secure@1",
                "k_value": 1,
                "value": 0.7,
            },
        ]
        df = pd.DataFrame(data)

        result = compute_scores_between_bases(df)

        assert len(result) == 4  # 2x2 comparison matrix

        # Same config comparisons should have score 0
        same_config_scores = result[result["config1"] == result["config2"]]["score"]
        assert all(score == 0 for score in same_config_scores)

        # config1 vs config2: pass@1 better (+1), secure@1 worse (-1) = total 0
        config1_vs_config2 = result[
            (result["config1"] == "config1") & (result["config2"] == "config2")
        ]["score"].iloc[0]
        assert config1_vs_config2 == 0

    def test_compute_scores_between_bases_error(self):
        """Test that ValueError is raised when no base variants exist for comparison."""

        data = [
            {
                "config": "config1",
                "variant_id": "variant1",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
        ]
        df = pd.DataFrame(data)

        with pytest.raises(ValueError, match="No base variants found"):
            compute_scores_between_bases(df)


class TestCreateSecurityHeatmaps:
    def test_create_heatmap_to_base(self):
        """Test that a valid matplotlib figure is created for variant-to-base comparisons."""

        data = [
            {
                "platform": "platform1",
                "model": "model1",
                "temperature": "0.5",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
            {
                "platform": "platform1",
                "model": "model1",
                "temperature": "0.5",
                "variant_id": "variant1",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.7,
            },
        ]

        df = pd.DataFrame(data)
        fig = create_heatmap_to_base(df)

        assert isinstance(fig, plt.Figure)
        assert fig.get_axes()
        plt.close(fig)

    def test_create_heatmap_between_bases(self):
        """Test that a valid matplotlib figure is created for base-to-base comparisons."""

        data = [
            {
                "platform": "platform1",
                "model": "model1",
                "temperature": "0.5",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.5,
            },
            {
                "platform": "platform2",
                "model": "model2",
                "temperature": "0.7",
                "variant_id": "base",
                "metric": "pass@1",
                "k_value": 1,
                "value": 0.6,
            },
        ]

        df = pd.DataFrame(data)
        fig = create_heatmap_between_bases(df)

        assert isinstance(fig, plt.Figure)
        assert fig.get_axes()
        plt.close(fig)
