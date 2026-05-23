def clean_code_block(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        lines = text.splitlines()

        # убирает первую строку: ``` или ```python
        lines = lines[1:]

        # убирает последнюю строку: ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        text = "\n".join(lines)

    return text.strip() + "\n"
