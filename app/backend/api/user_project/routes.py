from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from app.agent.build import run_agent
from app.backend.helpers.docker import start_docker
from app.backend.helpers.project import create_project
from app.frontend import render_prompt_form, render_run_status

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    return render_prompt_form()


@router.post("/generate", response_class=HTMLResponse)
def generate(prompt: str = Form(...), token: str = Form(...)) -> HTMLResponse:
    bot_token = token.strip()
    if not bot_token:
        return render_prompt_form("Укажи токен Telegram-бота перед запуском.")

    state = run_agent(prompt, bot_token=bot_token)

    if state.get("error"):
        return render_prompt_form(f"Ошибка генерации: {state['error']}")

    if not state["code"].strip():
        return render_prompt_form("Код пока пустой. Попробуй отправить запрос еще раз.")

    project_dir = create_project(state["code"], bot_token)
    docker_status = start_docker()
    return render_run_status(project_dir, docker_status)
