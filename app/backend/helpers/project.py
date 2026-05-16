from pathlib import Path
import shutil

# from app.utils.path import (
#     path_to_project_dockerfile,
#     path_to_project_env,
#     path_to_project_main,
#     path_to_project_requirements,
# )

def clear_project_data(project_path: Path) -> Path:
    if project_path.exists():
        shutil.rmtree(project_path)

    project_path.mkdir(parents=True, exist_ok=True)

    return project_path

def save_project_env(project_path: Path, bot_token: str) -> Path:
    project_path.mkdir(parents=True, exist_ok=True)

    env_path = project_path / ".env"
    env_path.write_text(f"BOT_TOKEN={bot_token}\n", encoding="utf-8")

    return env_path