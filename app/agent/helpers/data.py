import json
from pathlib import Path
from typing import Sequence

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    messages_from_dict,
    messages_to_dict,
)

from app.agent.helpers.clean import clean_code_block
from app.agent.utils import DEFAULT_HISTORY_PATH


def load_agent_data(file_path: Path = DEFAULT_HISTORY_PATH) -> dict:
    if not file_path.exists():
        return {
            "messages": [],
            "code": "",
            "error": "",
        }

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_agent_data(
    messages: Sequence[BaseMessage],
    code: str,
    error: str = "",
    file_path: Path = DEFAULT_HISTORY_PATH,
) -> None:
    clean_code = clean_code_block(code)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            {
                "messages": messages_to_dict(messages),
                "code": clean_code,
                "error": error,
            },
            file,
            ensure_ascii=False,
            indent=2,
        )


def load_messages(data: dict) -> list[BaseMessage]:
    raw_messages = data.get("messages", [])
    if not raw_messages:
        return []

    messages = messages_from_dict(raw_messages)
    clean_messages: list[BaseMessage] = []
    for message in messages:
        if not isinstance(message, AIMessage) or not isinstance(message.content, str):
            clean_messages.append(message)
            continue

        if message.content.startswith("Could not generate aiogram bot code"):
            continue

        clean_messages.append(AIMessage(content=clean_code_block(message.content)))

    return clean_messages
