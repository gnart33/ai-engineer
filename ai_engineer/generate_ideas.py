import json
import os
import os.path as osp
import time
from typing import List, Dict, Union

import backoff
import requests

from ai_engineer.llm import (
    get_response_from_llm,
    extract_json_between_markers,
    create_client,
    AVAILABLE_LLMS,
)
from ai_engineer.prompt_templates import (
    SOLUTION_GENERATION_PROMPT,
    SOLUTION_REFLECTION_PROMPT,
    TECHNICAL_REVIEW_PROMPT,
    SYSTEM_MESSAGE,
)

S2_API_KEY = os.getenv("S2_API_KEY")


# GENERATE IDEAS
def generate_solutions(
    base_dir,
    client,
    model,
    skip_generation=False,
    max_solutions=20,
    num_iterations=5,
):
    if skip_generation:
        # Load existing ideas from file
        try:
            with open(osp.join(base_dir, "ideas.json"), "r") as f:
                ideas = json.load(f)
            print("Loaded existing ideas:")
            for idea in ideas:
                print(idea)
            return ideas
        except FileNotFoundError:
            print("No existing ideas found. Generating new ideas.")
        except json.JSONDecodeError:
            print("Error decoding existing ideas. Generating new ideas.")

    idea_str_archive = []
    with open(osp.join(base_dir, "seed_ideas.json"), "r") as f:
        seed_ideas = json.load(f)
    for seed_idea in seed_ideas:
        idea_str_archive.append(json.dumps(seed_idea))

    with open(osp.join(base_dir, "experiment.py"), "r") as f:
        code = f.read()

    with open(osp.join(base_dir, "prompt.json"), "r") as f:
        prompt = json.load(f)

    idea_system_prompt = prompt["system"]

    for _ in range(max_solutions):
        print()
        print(f"Generating solution {_ + 1}/{max_solutions}")
        try:
            prev_solutions_string = "\n\n".join(idea_str_archive)

            msg_history = []
            print(f"Iteration 1/{num_iterations}")
            text, msg_history = get_response_from_llm(
                SOLUTION_GENERATION_PROMPT.format(
                    task_description=prompt["task_description"],
                    code=code,
                    prev_solutions_string=prev_solutions_string,
                ),
                client=client,
                model=model,
                system_message=SYSTEM_MESSAGE,
                msg_history=msg_history,
            )
            ## PARSE OUTPUT
            json_output = extract_json_between_markers(text)
            assert json_output is not None, "Failed to extract JSON from LLM output"
            print(json_output)

            # Iteratively improve task.
            if num_iterations > 1:
                for j in range(num_iterations - 1):
                    print(f"Iteration {j + 2}/{num_iterations}")
                    text, msg_history = get_response_from_llm(
                        SOLUTION_REFLECTION_PROMPT.format(
                            current_round=j + 2, num_iterations=num_iterations
                        ),
                        client=client,
                        model=model,
                        system_message=SYSTEM_MESSAGE,
                        msg_history=msg_history,
                    )
                    ## PARSE OUTPUT
                    json_output = extract_json_between_markers(text)
                    assert (
                        json_output is not None
                    ), "Failed to extract JSON from LLM output"
                    print(json_output)

                    if "SOLUTION FINALIZED" in text:
                        print(
                            f"Solution generation converged after {j + 2} iterations."
                        )
                        break

            idea_str_archive.append(json.dumps(json_output))
        except Exception as e:
            print(f"Failed to generate solution: {e}")
            continue

    ## SAVE IDEAS
    ideas = []
    for idea_str in idea_str_archive:
        ideas.append(json.loads(idea_str))

    with open(osp.join(base_dir, "ideas.json"), "w") as f:
        json.dump(ideas, f, indent=4)

    return ideas


# GENERATE IDEAS OPEN-ENDED
def generate_next_solution(
    base_dir,
    client,
    model,
    prev_idea_archive=[],
    num_iterations=5,
    max_attempts=10,
):
    idea_archive = prev_idea_archive
    original_archive_size = len(idea_archive)

    print(f"Generating solution {original_archive_size + 1}")

    if len(prev_idea_archive) == 0:
        print(f"First iteration, taking seed ideas")
        # seed the archive on the first run with pre-existing ideas
        with open(osp.join(base_dir, "seed_ideas.json"), "r") as f:
            seed_ideas = json.load(f)
        for seed_idea in seed_ideas[:1]:
            idea_archive.append(seed_idea)
    else:
        with open(osp.join(base_dir, "experiment.py"), "r") as f:
            code = f.read()
        with open(osp.join(base_dir, "prompt.json"), "r") as f:
            prompt = json.load(f)
        idea_system_prompt = prompt["system"]

        for _ in range(max_attempts):
            try:
                idea_strings = []
                for idea in idea_archive:
                    idea_strings.append(json.dumps(idea))
                prev_solutions_string = "\n\n".join(idea_strings)

                msg_history = []
                print(f"Iteration 1/{num_iterations}")
                text, msg_history = get_response_from_llm(
                    SOLUTION_GENERATION_PROMPT.format(
                        task_description=prompt["task_description"],
                        code=code,
                        prev_solutions_string=prev_solutions_string,
                    )
                    + """
Completed solutions have an additional "Score" field which indicates the assessment by an expert ML reviewer.
This is on a standard 1-10 ML conference scale.
Scores of 0 indicate the solution failed either during experimentation, writeup or reviewing.
""",
                    client=client,
                    model=model,
                    system_message=SYSTEM_MESSAGE,
                    msg_history=msg_history,
                )
                ## PARSE OUTPUT
                json_output = extract_json_between_markers(text)
                assert json_output is not None, "Failed to extract JSON from LLM output"
                print(json_output)

                # Iteratively improve task.
                if num_iterations > 1:
                    for j in range(num_iterations - 1):
                        print(f"Iteration {j + 2}/{num_iterations}")
                        text, msg_history = get_response_from_llm(
                            SOLUTION_REFLECTION_PROMPT.format(
                                current_round=j + 2, num_iterations=num_iterations
                            ),
                            client=client,
                            model=model,
                            system_message=SYSTEM_MESSAGE,
                            msg_history=msg_history,
                        )
                        ## PARSE OUTPUT
                        json_output = extract_json_between_markers(text)
                        assert (
                            json_output is not None
                        ), "Failed to extract JSON from LLM output"
                        print(json_output)

                        if "SOLUTION FINALIZED" in text:
                            print(
                                f"Solution generation converged after {j + 2} iterations."
                            )
                            break

                idea_archive.append(json_output)
                break
            except Exception as e:
                print(f"Failed to generate solution: {e}")
                continue

    ## SAVE IDEAS
    with open(osp.join(base_dir, "ideas.json"), "w") as f:
        json.dump(idea_archive, f, indent=4)

    return idea_archive


def on_backoff(details):
    print(
        f"Backing off {details['wait']:0.1f} seconds after {details['tries']} tries "
        f"calling function {details['target'].__name__} at {time.strftime('%X')}"
    )


@backoff.on_exception(
    backoff.expo, requests.exceptions.HTTPError, on_backoff=on_backoff
)
def search_for_papers(query, result_limit=10) -> Union[None, List[Dict]]:
    if not query:
        return None
    rsp = requests.get(
        "https://api.semanticscholar.org/graph/v1/paper/search",
        headers={"X-API-KEY": S2_API_KEY},
        params={
            "query": query,
            "limit": result_limit,
            "fields": "title,authors,venue,year,abstract,citationStyles,citationCount",
        },
    )
    print(f"Response Status Code: {rsp.status_code}")
    print(
        f"Response Content: {rsp.text[:500]}"
    )  # Print the first 500 characters of the response content
    rsp.raise_for_status()
    results = rsp.json()
    total = results["total"]
    time.sleep(1.0)
    if not total:
        return None

    papers = results["data"]
    return papers


# Update the novelty check to focus on technical feasibility
def check_solution_feasibility(
    ideas,
    base_dir,
    client,
    model,
    max_num_iterations=10,
):
    with open(osp.join(base_dir, "experiment.py"), "r") as f:
        code = f.read()
    with open(osp.join(base_dir, "prompt.json"), "r") as f:
        prompt = json.load(f)
        task_description = prompt["task_description"]

    for idx, idea in enumerate(ideas):
        if "feasible" in idea:
            print(f"Skipping solution {idx}, already checked.")
            continue

        print(f"\nChecking feasibility of solution {idx}: {idea['Name']}")

        feasible = False
        msg_history = []
        papers_str = ""

        for j in range(max_num_iterations):
            try:
                text, msg_history = get_response_from_llm(
                    TECHNICAL_REVIEW_PROMPT.format(
                        current_round=j + 1,
                        num_iterations=max_num_iterations,
                        idea=idea,
                        last_query_results=papers_str,
                    ),
                    client=client,
                    model=model,
                    system_message=SYSTEM_MESSAGE,
                    msg_history=msg_history,
                )
                if "decision made: feasible" in text.lower():
                    print("Decision made: feasible after round", j)
                    feasible = True
                    break
                if "decision made: not feasible" in text.lower():
                    print("Decision made: not feasible after round", j)
                    break

                ## PARSE OUTPUT
                json_output = extract_json_between_markers(text)
                assert json_output is not None, "Failed to extract JSON from LLM output"

                ## SEARCH FOR PAPERS
                query = json_output["Query"]
                papers = search_for_papers(query, result_limit=10)
                if papers is None:
                    papers_str = "No papers found."

                paper_strings = []
                for i, paper in enumerate(papers):
                    paper_strings.append(
                        """{i}: {title}. {authors}. {venue}, {year}.\nNumber of citations: {cites}\nAbstract: {abstract}""".format(
                            i=i,
                            title=paper["title"],
                            authors=paper["authors"],
                            venue=paper["venue"],
                            year=paper["year"],
                            cites=paper["citationCount"],
                            abstract=paper["abstract"],
                        )
                    )
                papers_str = "\n\n".join(paper_strings)

            except Exception as e:
                print(f"Error: {e}")
                continue

        idea["feasible"] = feasible

    # Save results to JSON file
    results_file = osp.join(base_dir, "ideas.json")
    with open(results_file, "w") as f:
        json.dump(ideas, f, indent=4)

    return ideas


if __name__ == "__main__":
    MAX_NUM_GENERATIONS = 32
    NUM_REFLECTIONS = 5
    import argparse

    parser = argparse.ArgumentParser(description="Generate AI scientist ideas")
    # add type of experiment (nanoGPT, Boston, etc.)
    parser.add_argument(
        "--experiment",
        type=str,
        default="nanoGPT",
        help="Experiment to run AI Scientist on.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-2024-05-13",
        choices=AVAILABLE_LLMS,
        help="Model to use for AI Scientist.",
    )
    parser.add_argument(
        "--skip-idea-generation",
        action="store_true",
        help="Skip idea generation and use existing ideas.",
    )
    parser.add_argument(
        "--check-feasibility",
        action="store_true",
        help="Check feasibility of ideas.",
    )
    args = parser.parse_args()

    # Create client
    client, client_model = create_client(args.model)

    base_dir = osp.join("templates", args.experiment)
    results_dir = osp.join("results", args.experiment)
    ideas = generate_solutions(
        base_dir,
        client=client,
        model=client_model,
        skip_generation=args.skip_idea_generation,
        max_solutions=MAX_NUM_GENERATIONS,
        num_iterations=NUM_REFLECTIONS,
    )
    if args.check_feasibility:
        ideas = check_solution_feasibility(
            ideas,
            base_dir=base_dir,
            client=client,
            model=client_model,
        )
