from langchain_core.messages import HumanMessage

from app.agent.graph import agent


def build_project(prompt: str):
    return agent.invoke({
        "messages": [HumanMessage(content=prompt)]
    })

if __name__ == "__main__":
    result = build_project("Создай эхо бота")
    print(result)
