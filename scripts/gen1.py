import anthropic
import os
from pathlib import Path

from ai_engineer.generate_ideas import generate_solutions, check_solution_feasibility


def main():
    MAX_NUM_GENERATIONS = 32
    NUM_REFLECTIONS = 5
    model = "anthropic/claude-3-5-sonnet-20240620"

    # Create client
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )
    model = ("claude-3-5-sonnet-20241022",)

    base_path = Path("templates/hack1")
    results_path = Path("results/hack1")
    ideas = generate_solutions(
        base_path,
        client=client,
        model=model,
        skip_generation=False,
        max_solutions=MAX_NUM_GENERATIONS,
        num_iterations=NUM_REFLECTIONS,
    )

    # ideas = check_solution_feasibility(
    #     ideas,
    #     base_dir=base_dir,
    #     client=client,
    #     model=client_model,
    # )


if __name__ == "__main__":
    main()
