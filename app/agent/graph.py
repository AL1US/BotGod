from langgraph.graph import END, START, StateGraph

# from app.agent.nodes.generate import generate_aiogram_bot_node
from app.agent.state import AgentState

from app.agent.nodes.code import generate_node
from app.agent.nodes.data import save_node

graph = StateGraph(AgentState)
graph.add_node("generate", generate_node)
graph.add_node("save", save_node)
graph.add_edge(START, "generate")
graph.add_edge("generate", "save")
graph.add_edge("save", END)

agent = graph.compile()