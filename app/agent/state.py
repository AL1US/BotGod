
from typing import Annotated, NotRequired, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pathlib import Path


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages] # Для истории 
    code: NotRequired[str] # Код бота для модели
    requirements: NotRequired[str] # Для файла requirements
    error: NotRequired[str] # Если были недавние ошибки
    project_path: NotRequired[Path] # Путь проекта
    is_saved: NotRequired[bool] # Сохранён ли проект
    dockerfile: NotRequired[str] # Код(содержание) докерфайла
    launched: NotRequired[bool] # Запущен ли докер контейнер с ботом