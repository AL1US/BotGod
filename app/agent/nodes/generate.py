

from langchain_core.messages import AIMessage

from app.agent.helpers.clean import clean_code_block
from app.agent.helpers.validate import validate_python_code
from app.agent.llms import llm
from app.agent.state import AgentState


def generate_aiogram_bot_node(state: AgentState) -> dict:
    try:
        response = llm.invoke(state["messages"])
        code = clean_code_block(response.content)
        validate_python_code(code)
    except Exception as error:
        code = state["code"]
        error_message = (
            "Could not generate aiogram bot code because the Mistral request failed: "
            f"{type(error).__name__}: {error}"
        )
        return {
            "messages": [AIMessage(content=error_message)],
            "code": code,
            "error": error_message,
        }

    return {
        "messages": [AIMessage(content=code)],
        "code": code,
        "error": "",
    }
