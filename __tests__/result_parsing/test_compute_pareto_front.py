from result_parsing._extras.compute_pareto_front import compute_pareto_front


class TestParetoFront:
    def test_compute_pareto_front_multiple_points(self) -> None:
        """Test with multiple Pareto optimal points."""

        energy_efficiency = [1, 3, 2, 4]
        security = [4, 2, 1, 3]

        result = compute_pareto_front(energy_efficiency, security)

        expected = [(1, 4), (4, 3)]
        assert sorted(result) == sorted(expected)

    def test_compute_pareto_front_all_dominated(self) -> None:
        """Test where one point dominates all others."""

        energy_efficiency = [1, 2, 3, 4]
        security = [1, 2, 3, 4]

        result = compute_pareto_front(energy_efficiency, security)

        # Only the point (4, 4) should be on the Pareto front
        assert result == [(4, 4)]

    def test_compute_pareto_front_empty_lists(self) -> None:
        """Test with empty input lists."""

        energy_efficiency = []
        security = []

        result = compute_pareto_front(energy_efficiency, security)

        assert result == []
