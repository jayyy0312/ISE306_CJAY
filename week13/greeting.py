# greeting.py


def make_greeting(name):
    name=name.strip()
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name is required")

    return f"Hello, {name}!"