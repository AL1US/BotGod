

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
PROJECTS_DIR = ROOT_DIR / "projects"
PROJECT_DIR = PROJECTS_DIR / "project"
PROJECT_MAIN_PATH = PROJECT_DIR / "main.py"
PROJECT_REQUIREMENTS_PATH = PROJECT_DIR / "requirements.txt"
PROJECT_ENV_PATH = PROJECT_DIR / ".env"
PROJECT_DOCKERFILE_PATH = PROJECT_DIR / "Dockerfile"
DOCKER_IMAGE_NAME = "aiogram-agent-project"
DOCKER_CONTAINER_NAME = "aiogram-agent-project"
