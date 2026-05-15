from fastapi import FastAPI
from app.backend.api.user_project.routers import router as user_project_router

app = FastAPI()

app.include_router(user_project_router)