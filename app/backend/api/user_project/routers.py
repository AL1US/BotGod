from fastapi import APIRouter, Form
from langchain_core.messages import HumanMessage

from app.agent.graph import agent
from app.utils.path import path_to_project
from app.backend.helpers.project import clear_project_data, save_project_env
router = APIRouter()

@router.post("/generate")
def generate(prompt: str):
    return agent.invoke({
        "messages": [HumanMessage(content=prompt)]
    })

@router.post("/clear-project")
def clear_project():
    clear_project_data(path_to_project)
    return "Проект успешно очищен"

@router.post("/add-token")
def add_token(bot_token: str):
    save_project_env(path_to_project, bot_token)
    return "Токен успешно добавлен"