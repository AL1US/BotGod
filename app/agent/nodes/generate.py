from langchain_core.messages import AIMessage, BaseMessage

from app.agent.llms import llm
from app.agent.state import AgentState
# IMPORT INSTRUCTIONS FOR MODEL

def generate_node(state: AgentState) -> AgentState:
    
    instructions_for_mode = BaseMessage(content=IMPORT_SOME_HERE)
    
    message = llm.invoke()