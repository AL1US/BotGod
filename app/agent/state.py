
from typing import Annotated, NotRequired, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pathlib import Path


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    code: NotRequired[str]
    requirements: NotRequired[str]
    error: NotRequired[str]
    project_path: NotRequired[Path]
    is_saved: NotRequired[bool]