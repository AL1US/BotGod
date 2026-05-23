from app.agent.state import AgentState
from app.agent.helpers.data import (
    save_messages_history, 
    save_project_data,
    load_code,
    load_messages_history
)
from app.utils.path import (
    path_to_history,
    path_to_project
)


def save_node(state: AgentState) -> dict:
    save_messages_history(path_to_history, state["messages"])
    save_project_data(path_to_project, state["code"], state["requirements"], state["dockerfile"])

    return {
        "is_saved": True,
        "project_path": path_to_project
    }