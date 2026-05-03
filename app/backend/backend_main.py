from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.backend.api.user_project.routes import router as user_project_router
from app.frontend import STATIC_DIR

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(user_project_router)
