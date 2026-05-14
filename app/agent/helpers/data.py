from app.utils.path import path_to_history, path_to_project
from typing import Sequence
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    messages_from_dict,
    messages_to_dict,
)
from pathlib import Path

import json

def check_exitst(file_path: Path) -> bool:
    if not file_path.exists():
        return False
    return True

def save_messages_history(path_to, messages: Sequence[BaseMessage]):
    
    with open(path_to, "w", encoding="utf-8") as file:
        json.dump(
            {
                "messages": messages_to_dict(messages)
            },
            file,
            ensure_ascii=False, # поддержка русского языка и других символов
            indent=2, # красивое формативрование
        )

def save_code():
    pass

def load_messages_history() -> dict:
    pass

    
    
def load_code()
    pass