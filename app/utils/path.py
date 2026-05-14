from pathlib import Path


APP_ROOT = Path(__file__).resolve().parent.parent

path_to_history = APP_ROOT / "history.json"
path_to_project = APP_ROOT / "projects"

path_to_project_main = path_to_project / "main.py"
path_to_project_requirements = path_to_project / "requirements.txt"
path_to_project_env = path_to_project / ".env"
path_to_project_dockerfile = path_to_project / "Dockerfile"
