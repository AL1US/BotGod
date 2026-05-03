

from typing import Sequence

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage

from app.agent.utils import (
    HISTORY_CONTEXT_MESSAGES,
    SYSTEM_MESSAGE,
    SYSTEM_MESSAGE_ABOUT_TOKEN,
)


def build_graph_messages(
    prompt: str,
    previous_messages: Sequence[BaseMessage],
    previous_code: str,
    bot_token_provided: bool = False,
) -> list[BaseMessage]:
    messages: list[BaseMessage] = [SYSTEM_MESSAGE]

    if bot_token_provided:
        messages.append(SYSTEM_MESSAGE_ABOUT_TOKEN)

    if previous_code.strip():
        messages.append(
            SystemMessage(
                content=(
                    "Current main.py code. Use it as context and return the full updated file:\n\n"
                    f"{previous_code}"
                )
            )
        )

    messages.extend(previous_messages[-HISTORY_CONTEXT_MESSAGES:])
    messages.append(HumanMessage(content=prompt))
    return messages
