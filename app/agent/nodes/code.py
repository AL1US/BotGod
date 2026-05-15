from langchain_core.messages import SystemMessage

from app.agent.llms import llm
from app.agent.messages_for_model.about_agent import SYSTEM_PROMPT, REQUIREMENTS_PROMPT
from app.agent.state import AgentState
from app.agent.helpers.clean import clean_code_block

def generate_node(state: AgentState) -> AgentState:
    system_message = SystemMessage(content=SYSTEM_PROMPT)

    code = [
        system_message,
        *state["messages"], # * распаковка (элементы списка вставлются внутрь другого списка)
    ]

    code = llm.invoke(code)

    requirements = llm.invoke(code.content + REQUIREMENTS_PROMPT)
    
    return {
        "code": clean_code_block(code.content),
        "requirements": clean_code_block(requirements.content)
    }
