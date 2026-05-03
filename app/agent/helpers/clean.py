
from app.agent.utils import CODE_FENCE_RE, PYTHON_START_RE


def clean_code_block(content: str) -> str:
    content = content.strip()

    fenced_blocks = CODE_FENCE_RE.findall(content)
    if fenced_blocks:
        return fenced_blocks[0].strip()

    start_match = PYTHON_START_RE.search(content)
    if start_match:
        return content[start_match.start():].strip()

    return content
