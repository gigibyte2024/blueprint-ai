from langgraph.graph import StateGraph, END

from app.graph.state import BlueprintState
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.clarification_agent import ClarificationAgent

builder = StateGraph(BlueprintState)

orchestrator = OrchestratorAgent()
clarification = ClarificationAgent()

builder.add_node("orchestrator", orchestrator.execute)
builder.add_node("clarification", clarification.execute)

builder.set_entry_point("orchestrator")


def route(state: BlueprintState):

    return state["current_step"]


builder.add_conditional_edges(
    "orchestrator",
    route,
    {
        "clarification": "clarification",
        "planning": END
    },
)

builder.add_edge(
    "clarification",
    END,
)

workflow = builder.compile()