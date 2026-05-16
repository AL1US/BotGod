from langchain_core.messages import SystemMessage

from app.agent.llms import llm
from app.agent.messages_for_model.about_agent import SYSTEM_PROMPT, REQUIREMENTS_PROMPT
from app.agent.state import AgentState
from app.agent.helpers.clean import clean_code_block

def start_project(state: AgentState) -> AgentState:

    # path to project
    
    # вызов tool
    
    # отправка статуса - False/True
    
    return {
        "code": clean_code_block(code.content),
        "requirements": clean_code_block(requirements.content)
    }
