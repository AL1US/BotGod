
from typing import Annotated, NotRequired, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages



class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    code: str
    error: NotRequired[str]