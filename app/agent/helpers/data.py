from typing import Sequence

from langchain_core.messages import (
    BaseMessage,
    messages_from_dict,
    messages_to_dict,
)

from app.utils.data import DOCKERFILE_CONTENT, REQUIREMENTS_CONTENT
from app.utils.path import (
    path_to_project_dockerfile,
    path_to_project_env,
    path_to_project_main,
    path_to_project_requirements,
)

from pathlib import Path

import json

# в будущем везде стоит сделать так, чтобы путь передовался в фунцию, но пока один проект на всех - не критично

def check_exists(file_path: Path) -> bool:
    if not file_path.exists():
        return False
    return True

def save_messages_history(file_path: Path, messages: Sequence[BaseMessage]):
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            {
                "messages": messages_to_dict(messages)
            },
            file,
            ensure_ascii=False, # поддержка русского языка и других символов
            indent=2, # красивое формативрование
        )

def save_project_data(project_path: Path, code: str, requirements: str):
    project_path.mkdir(parents=True, exist_ok=True) # если промежуточных папок нет, то создать их тоже, если папка уже существует - не падать с ошибкой
    
    path_to_project_main.write_text(code, encoding="utf-8")
    path_to_project_requirements.write_text(requirements, encoding="utf-8")
    path_to_project_requirements.write_text(REQUIREMENTS_CONTENT, encoding="utf-8")
    path_to_project_dockerfile.write_text(DOCKERFILE_CONTENT, encoding="utf-8")
        
    return project_path
    
def load_messages_history(file_path: Path ) -> dict:
    if not check_exists(file_path):
        return {
            "messages": []
        }

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
        
    
    
def load_code():
    pass
