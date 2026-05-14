from langgraph.graph import END, START, StateGraph

# from app.agent.nodes.generate import generate_aiogram_bot_node
from app.agent.state import AgentState


graph_builder = StateGraph(AgentState)

app = graph_builder.compile()