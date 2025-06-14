import matplotlib.pyplot as plt
from typing import List, Tuple


def compute_pareto_front(
    energy_efficiency_results: List[float], security_results: List[float]
) -> List[Tuple[float, float]]:
    pareto_front = []

    for i in range(len(energy_efficiency_results)):
        is_pareto = True
        for j in range(len(energy_efficiency_results)):
            if i != j:
                if (
                    energy_efficiency_results[j] >= energy_efficiency_results[i]
                    and security_results[j] >= security_results[i]
                ):
                    is_pareto = False
                    break
        if is_pareto:
            pareto_front.append((energy_efficiency_results[i], security_results[i]))

    return pareto_front


if __name__ == "__main__":
    variants = [
        "cot",
        "cot_secure_rci_1",
        "energy_efficient_rci_1",
        "energy_efficient_suffix",
        "for_loops_suffix",
        "library_functions_suffix",
        "persona_energy_efficient_prefix",
        "persona_secure_prefix",
        "secure_rci_1",
        "secure_suffix",
    ]

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    fig.suptitle(
        "Security-Energy Efficiency Pareto Front Analysis",
        fontsize=18,
        fontweight="bold",
    )

    energy_efficiency_results = [6, 4, 18, 11, 25, 18, 11, 20, 9, 1]
    security_results = [7, -6, 9, -21, 3, -25, -29, -24, -5, -4]

    ax.scatter(
        energy_efficiency_results,
        security_results,
        alpha=0.7,
        s=100,
        c="lightblue",
        edgecolors="black",
        linewidth=1,
    )

    pareto_front = compute_pareto_front(energy_efficiency_results, security_results)
    sorted_pareto_front = sorted(pareto_front, key=lambda p: p[0])
    pareto_x, pareto_y = zip(*sorted_pareto_front)

    ax.plot(
        pareto_x,
        pareto_y,
        marker="o",
        color="red",
        linewidth=2,
        label="Pareto Front",
    )

    # Add labels for each point
    for i, (x, y) in enumerate(zip(energy_efficiency_results, security_results)):
        ax.annotate(
            variants[i],
            (x, y),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
            ha="left",
            va="bottom",
        )

    ax.set_xlabel("Energy Efficiency (scoring units)", fontsize=12)
    ax.set_ylabel("Security (scoring units)", fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()
