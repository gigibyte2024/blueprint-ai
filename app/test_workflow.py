from app.graph.workflow import workflow

state = {
    "current_step": "",

    "is_clarification_complete": False,
    "idea": "Blueprint AI converts startup ideas into complete product blueprints.",

    "clarification_questions": [],
    "clarification_answers": [],

    "prd": "",
    "user_stories": "",
    "feature_list": "",

    "database_schema": "",
    "api_specification": "",
    "tech_stack": "",

    "ui_prompt": "",
    "roadmap": "",

    "final_blueprint": {}
}

result = workflow.invoke(state)

print("\nQuestions:\n")

for q in result["clarification_questions"]:
    print("-", q)