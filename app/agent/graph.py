
from langgraph.graph import END, START, StateGraph

from app.agent.nodes.generate import generate_aiogram_bot_node
from app.agent.state import AgentState


graph_builder = StateGraph(AgentState)
graph_builder.add_node("generate_aiogram_bot", generate_aiogram_bot_node)
graph_builder.add_edge(START, "generate_aiogram_bot")
graph_builder.add_edge("generate_aiogram_bot", END)

graph = graph_builder.compile()
