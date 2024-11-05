"""
Prompt templates for engineering solution generation and evaluation.
"""

# Initial prompt for generating engineering solutions
SOLUTION_GENERATION_PROMPT = """{task_description}
<code>
{code}
</code>

Previously proposed solutions:
'''
{prev_solutions_string}
'''

Propose a practical engineering solution for the problem described above.
Consider implementation feasibility, maintainability, and scalability.

Respond in the following format:

ANALYSIS:
<ANALYSIS>

SOLUTION JSON:
```json
<JSON>
```

In <ANALYSIS>, discuss:
- Problem breakdown
- Technical constraints
- Implementation approach
- Trade-offs considered

The JSON should contain:
- "Name": Short descriptor (lowercase, underscores allowed)
- "Title": Descriptive title
- "Implementation": Technical details, architecture, and implementation steps
- "Complexity": Rating 1-10 (implementation difficulty)
- "Maintainability": Rating 1-10
- "Scalability": Rating 1-10
"""

# Prompt for iterative solution refinement
SOLUTION_REFLECTION_PROMPT = """Round {current_round}/{num_reflections}.
Review your proposed solution considering:
- Code quality and best practices
- Performance implications
- Edge cases and error handling
- Integration requirements

Respond in the same format:
ANALYSIS:
<ANALYSIS>

SOLUTION JSON:
```json
<JSON>
```

Include "SOLUTION FINALIZED" at the end of analysis if no further improvements needed."""

# Technical feasibility review prompt
TECHNICAL_REVIEW_PROMPT = """You are a senior software engineer reviewing a proposed solution.
Evaluate the technical feasibility, considering:
- System requirements
- Performance implications
- Security considerations
- Maintenance overhead

{task_description}
<code>
{code}
</code>

Previous solution:
{solution_json}

Evaluate the solution and respond in the following format:

ANALYSIS:
<ANALYSIS>

FEASIBILITY:
<FEASIBLE/NOT_FEASIBLE>

CONCERNS:
- <List key technical concerns>

RECOMMENDATIONS:
- <List suggested improvements>
"""

# System message for the LLM
SYSTEM_MESSAGE = """You are an experienced software engineer tasked with generating and evaluating practical engineering solutions.
Focus on:
1. Technical feasibility
2. Implementation complexity
3. Maintainability
4. Scalability
5. Best practices and patterns

Provide detailed, actionable solutions that can be implemented by a development team."""
