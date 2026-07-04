from langgraph.graph import StateGraph, END

from app.graph.state import BlueprintState
from app.agents.clarification_agent import ClarificationAgent

clarification_agent = ClarificationAgent()

builder = StateGraph(BlueprintState)

builder.add_node(
    "clarification",
    clarification_agent.execute,
)

builder.set_entry_point("clarification")

builder.add_edge(
    "clarification",
    END,
)

workflow = builder.compile()