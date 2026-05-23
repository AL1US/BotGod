from langchain_core.messages import SystemMessage

from app.agent.llms import llm
from app.agent.messages_for_model.about_agent import SYSTEM_PROMPT, REQUIREMENTS_PROMPT
from app.agent.state import AgentState
from app.agent.helpers.docker import run_dockerfile
from app.utils.path import path_to_project


def start_node(state: AgentState) -> AgentState:
    
    # По хорошему сюда еще запихнуть проверку того успешно запустился ли он        
    status = run_dockerfile(path_to_project)
    
    return {
        "launched": status
    }