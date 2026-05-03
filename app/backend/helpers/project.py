
import shutil
from pathlib import Path

from app.backend.utils.data import DOCKERFILE_CONTENT
from app.backend.utils.path import (
    PROJECT_DIR,
    PROJECT_DOCKERFILE_PATH,
    PROJECT_ENV_PATH,
    PROJECT_MAIN_PATH,
    PROJECT_REQUIREMENTS_PATH,
)


def create_project(code: str, bot_token: str) -> Path:
    compile(code, str(PROJECT_MAIN_PATH), "exec")

    if PROJECT_DIR.exists():
        shutil.rmtree(PROJECT_DIR)

    PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    PROJECT_MAIN_PATH.write_text(code, encoding="utf-8")
    PROJECT_REQUIREMENTS_PATH.write_text("aiogram\npython-dotenv\n", encoding="utf-8")
    write_bot_token(bot_token)
    PROJECT_DOCKERFILE_PATH.write_text(DOCKERFILE_CONTENT, encoding="utf-8")

    return PROJECT_DIR


def write_bot_token(token: str) -> None:
    PROJECT_ENV_PATH.write_text(f"BOT_TOKEN={token}\n", encoding="utf-8")
