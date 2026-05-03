from langchain_core.messages import SystemMessage
from pathlib import Path
import re


APP_DIR = Path(__file__).resolve().parent
DEFAULT_HISTORY_PATH = APP_DIR / "data.json"
HISTORY_CONTEXT_MESSAGES = 4


CODE_FENCE_RE = re.compile(r"```(?:python|py)?\s*(.*?)```", re.IGNORECASE | re.DOTALL)
PYTHON_START_RE = re.compile(
    r"(?m)^(?:#!.*python\s*$|from\s+\S+\s+import\s+|import\s+|[A-Z_][A-Z0-9_]*\s*=|async\s+def\s+|def\s+|class\s+)"
)


SYSTEM_MESSAGE = SystemMessage(
    content=(
        "You are a Python developer. Generate clean aiogram 3.x bot code. "
        "Return only Python code without markdown fences. "
        "If the user asks for changes, return the full updated main.py code. "
        "Telegram bot tokens must be loaded from the BOT_TOKEN environment variable. "
        "Use python-dotenv load_dotenv() and os.getenv('BOT_TOKEN'); never hard-code the token. "
        "If existing code hard-codes BOT_TOKEN or uses a placeholder token, replace it with env loading."
    )
)

SYSTEM_MESSAGE_ABOUT_TOKEN = SystemMessage(
    content=(
        "A Telegram bot token was provided by the user and will be written to the "
        "project .env file after generation. Do not include the token in the code."
    )
)
