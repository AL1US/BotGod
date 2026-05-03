
import subprocess

from app.backend.utils.path import (
    DOCKER_CONTAINER_NAME,
    DOCKER_IMAGE_NAME,
    PROJECT_DIR,
    PROJECT_DOCKERFILE_PATH,
    PROJECT_ENV_PATH,
    PROJECT_MAIN_PATH,
)

def start_docker() -> str:
    if not PROJECT_MAIN_PATH.exists():
        return "Project is not ready. Generate code first."

    if not PROJECT_DOCKERFILE_PATH.exists():
        return "Project Dockerfile is missing. Generate the project first."

    try:
        subprocess.run(
            ["docker", "rm", "-f", DOCKER_CONTAINER_NAME],
            check=False,
            capture_output=True,
            text=True,
        )
        build_result = subprocess.run(
            ["docker", "build", "-t", DOCKER_IMAGE_NAME, "."],
            cwd=PROJECT_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        run_result = subprocess.run(
            [
                "docker",
                "run",
                "-d",
                "--name",
                DOCKER_CONTAINER_NAME,
                "--env-file",
                str(PROJECT_ENV_PATH),
                DOCKER_IMAGE_NAME,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return "Docker is not installed or is not available in PATH."
    except subprocess.CalledProcessError as error:
        output = error.stderr or error.stdout or str(error)
        return f"Docker command failed: {output}"

    container_id = run_result.stdout.strip()
    return (
        "Docker container started. "
        f"Image: {DOCKER_IMAGE_NAME}. "
        f"Container: {DOCKER_CONTAINER_NAME}. "
        f"ID: {container_id}. "
        f"Build output: {build_result.stdout.strip()}"
    )
