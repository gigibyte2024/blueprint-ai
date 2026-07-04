from langgraph.graph import StateGraph, END

from app.graph.state import BlueprintState
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.clarification_agent import ClarificationAgent
from app.agents.planning_agent import PlanningAgent

builder = StateGraph(BlueprintState)
planning = PlanningAgent()
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
        "planning": "planning"
    },
)

builder.add_edge(
    "clarification",
    END,
)

builder.add_node(
    "planning",
    planning.execute,
)
builder.add_edge(
    "planning",
    END,
)
workflow = builder.compile()