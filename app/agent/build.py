
from langchain_core.messages import BaseMessage, HumanMessage

from app.agent.graph import graph
from app.agent.helpers.clean import clean_code_block
from app.agent.helpers.data import load_agent_data, load_messages, save_agent_data
from app.agent.helpers.messages import build_graph_messages
from app.agent.state import AgentState



def run_agent(prompt: str, bot_token: str = "") -> AgentState:
    data = load_agent_data()
    previous_messages = load_messages(data)
    previous_code = clean_code_block(data.get("code", ""))

    graph_state = graph.invoke(
        {
            "messages": build_graph_messages(
                prompt,
                previous_messages,
                previous_code,
                bot_token_provided=bool(bot_token.strip()),
            ),
            "code": previous_code,
            "error": "",
        }
    )

    new_messages: list[BaseMessage] = [
        *previous_messages,
        HumanMessage(content=prompt),
        graph_state["messages"][-1],
    ]
    save_agent_data(
        messages=new_messages,
        code=graph_state["code"],
        error=graph_state.get("error", ""),
    )

    return {
        "messages": new_messages,
        "code": graph_state["code"],
        "error": graph_state.get("error", ""),
    }
