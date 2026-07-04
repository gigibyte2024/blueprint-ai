from typing import TypedDict, List, Dict, Any


class BlueprintState(TypedDict):
    """
    Shared state passed between all agents.
    """
    current_step: str
    is_clarification_complete: bool
    # User Input
    idea: str

    # Clarification Phase
    clarification_questions: List[str]
    clarification_answers: List[str]

    # Planning Phase
    prd: str
    user_stories: str
    feature_list: str

    # Technical Phase
    database_schema: str
    api_specification: str
    tech_stack: str

    # UI Phase
    ui_prompt: str

    # Planning
    roadmap: str

    # Final Output
    final_blueprint: Dict[str, Any]