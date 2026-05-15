from fastapi import APIRouter, Form
from langchain_core.messages import HumanMessage

from app.agent.graph import agent
from app.utils.path import path_to_project

router = APIRouter()

@router.post("/generate")
def generate(prompt: str):
    return agent.invoke({
        "messages": [HumanMessage(content=prompt)]
    })
