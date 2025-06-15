import pandas as pd
import matplotlib.pyplot as plt

from result_parsing.energy_efficiency.energy_efficiency_figures import (
    create_heatmap_to_base,
    create_heatmap_between_bases,
)


class TestCreateEnergyEfficiencyHeatMaps:
    def test_create_heatmap_to_base(self):
        """Test that a valid matplotlib figure is created for variant-to-base comparisons."""

        fig = create_heatmap_to_base(
            pd.DataFrame(
                {
                    "platform": ["platform"],
                    "model": ["model"],
                    "temperature": [0.0],
                    "prompt_variant_id": ["base"],
                    "score": [-3],
                }
            )
        )

        assert isinstance(fig, plt.Figure)
        assert fig.get_axes()

    def test_create_heatmap_between_bases(self):
        """Test that a valid matplotlib figure is created for base-to-base comparisons."""

        fig = create_heatmap_between_bases(
            pd.DataFrame(
                {
                    "platform1": ["platform1"],
                    "model1": ["model1"],
                    "temperature1": [0.0],
                    "platform2": ["platform2"],
                    "model2": ["model2"],
                    "temperature2": [0.0],
                    "score": [-3],
                }
            )
        )

        assert isinstance(fig, plt.Figure)
        assert fig.get_axes()
