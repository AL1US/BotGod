
def validate_python_code(code: str) -> None:
    compile(code, "generated main.py", "exec")
