def hello(name=None):
    if not name:
        name = "World"

    return f"Hello {name}!"