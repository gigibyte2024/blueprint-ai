import json

from app.graph.state import BlueprintState
from app.services.llm_service import generate_response
from app.utils.prompt_loader import load_prompt


def clarification_agent(state: BlueprintState) -> BlueprintState:

    prompt_template = load_prompt("clarification.txt")

    prompt = prompt_template.format(
        idea=state["idea"]
    )

    messages = [
        {
            "role": "system",
            "content": "You are a Senior Product Manager."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = generate_response(messages)

    data = json.loads(response)

    state["clarification_questions"] = data["questions"]

    return state