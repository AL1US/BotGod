import subprocess
from pathlib import Path

def run_dockerfile(project_dir: Path) -> bool:
    """
    Находит Dockerfile в указанной директории проекта,
    собирает образ и запускает контейнер в фоне.
    """
    dockerfile_path = project_dir / "Dockerfile"
    
    # Проверяем существование Dockerfile через pathlib
    if not dockerfile_path.exists():
        print(f"❌ Ошибка: Файл не найден по пути: {dockerfile_path}")
        return False

    # .as_posix() преобразует путь в правильный формат для терминала (особенно критично на Windows)
    build_res = subprocess.run(
        f"docker build -t local-app-image '{project_dir.as_posix()}'", 
        shell=True
    )
    if build_res.returncode != 0:
        return False

    # Принудительно удаляем старый контейнер, если он есть
    subprocess.run("docker rm -f local-app-container", shell=True, capture_output=True)

    # Запуск нового контейнера
    run_res = subprocess.run("docker run -d --name local-app-container local-app-image", shell=True)
    
    return run_res.returncode == 0