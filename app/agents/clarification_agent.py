from app.graph.state import BlueprintState
from app.services.llm_service import generate_response
from app.utils.prompt_loader import load_prompt


def clarification_agent(state: BlueprintState) -> BlueprintState:
    """
    Reads the user's idea and generates clarification questions.
    """

    prompt_template = load_prompt("clarification.txt")

    prompt = prompt_template.format(
        idea=state["idea"]
    )

    response = generate_response(prompt)

    questions = [
        line.strip()
        for line in response.split("\n")
        if line.strip()
    ]

    state["clarification_questions"] = questions

    return state