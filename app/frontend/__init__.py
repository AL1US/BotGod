from html import escape
from pathlib import Path

from fastapi.responses import HTMLResponse

FRONTEND_DIR = Path(__file__).resolve().parent
STATIC_DIR = FRONTEND_DIR / "static"


def read_html(name: str) -> str:
    return (FRONTEND_DIR / name).read_text(encoding="utf-8")


def render_prompt_form(message: str = "") -> HTMLResponse:
    message_html = f"<p>{escape(message)}</p>" if message else ""
    html = read_html("index.html").replace("{{ message }}", message_html)
    return HTMLResponse(html)


def render_run_status(project_dir: Path, docker_status: str) -> HTMLResponse:
    html = (
        read_html("status.html")
        .replace("{{ project_dir }}", escape(str(project_dir)))
        .replace("{{ docker_status }}", escape(docker_status))
    )
    return HTMLResponse(html)
