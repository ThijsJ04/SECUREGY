import numpy as np
import pandas as pd

from result_parsing.energy_efficiency.energy_efficiency_parsing import (
    get_energy_data,
    compare_data_bundles,
    analyze_energy_efficiency_to_base,
    analyze_energy_efficiency_between_bases,
)


class TestEnergyEfficiencyParsing:
    def test_get_energy_data(self):
        """Test that get_energy_data correctly filters for energy consumption data."""

        df = pd.DataFrame(
            {
                "Key": ["energy_consumed_kwh", "other_metric", "energy_consumed_kwh"],
                "prompt_variant_id": ["base", "base", "variant1"],
                "Value": [1.5, 2.0, 1.8],
            }
        )

        result = get_energy_data(df)

        assert len(result) == 2
        assert all(result["Key"] == "energy_consumed_kwh")

    def test_compare_data_bundles_better(self):
        """Test that compare_data_bundles returns correct comparison result when data_a is better."""

        data_a = np.random.rand(100)
        data_b = np.random.rand(100) * 10  # Simulate data_b being significantly worse

        result = compare_data_bundles(data_a, data_b)

        assert result == 1  # data_a should be significantly better

    def test_compare_data_bundles_worse(self):
        """Test that compare_data_bundles returns correct comparison result when data_a is worse."""

        data_a = np.random.rand(100) * 10
        data_b = np.random.rand(100)
        result = compare_data_bundles(data_a, data_b)

        assert result == -1  # data_a should be significantly worse

    def test_analyze_energy_efficiency_to_base(self):
        """Test that analyze_energy_efficiency_to_base produces comparison results."""

        df = pd.DataFrame(
            {
                "Key": ["energy_consumed_kwh"] * 100,
                "platform": ["platform1"] * 100,
                "model": ["model1"] * 100,
                "temperature": [0.5] * 100,
                "prompt_variant_id": ["base"] * 50 + ["variant1"] * 50,
                "run_index": [1] * 100,
                "Value": [20.0] * 50 + [1.0] * 50,  # variant1 is better
            }
        )

        result = analyze_energy_efficiency_to_base(df)

        assert len(result) == 1
        assert result.iloc[0]["prompt_variant_id"] == "variant1"
        assert result.iloc[0]["score"] == 1  # Should be positive (better than base)

    def test_analyze_energy_efficiency_between_bases(self):
        """Test that analyze_energy_efficiency_between_bases compares different base configurations."""

        df = pd.DataFrame(
            {
                "Key": ["energy_consumed_kwh"] * 100,
                "platform": ["platform1"] * 50 + ["platform2"] * 50,
                "model": ["model1"] * 100,
                "temperature": [0.5] * 100,
                "prompt_variant_id": ["base"] * 100,
                "run_index": [1] * 100,
                "Value": [20.0] * 50 + [1.0] * 50,  # platform2 is better
            }
        )

        result = analyze_energy_efficiency_between_bases(df)
        assert len(result) == 4  # 2x2 combinations
        assert list(result["score"]) == [0, -1, 1, 0]
