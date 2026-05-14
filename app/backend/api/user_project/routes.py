from fastapi import APIRouter, Form
from langchain_core.messages import HumanMessage

from app.agent.graph import agent
from app.frontend import render_prompt_form
from app.utils.path import path_to_project

router = APIRouter()


@router.get("/")
def index():
    return render_prompt_form()


@router.post("/generate")
def generate_project(
    token: str = Form(...),
    prompt: str = Form(...),
):
    result = agent.invoke({"messages": [HumanMessage(content=prompt)]})

    env_path = path_to_project / ".env"
    env_path.write_text(f"BOT_TOKEN={token}\n", encoding="utf-8")

    if result.get("is_saved"):
        return render_prompt_form(f"Проект сохранен в {result['project_path']}")

    return render_prompt_form("Не удалось сохранить проект")
