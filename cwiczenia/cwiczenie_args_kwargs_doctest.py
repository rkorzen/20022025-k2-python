from typing import Any


def replace(*args: str, **kwargs: Any) -> str:
    """
    Replace keys from kwargs with corresponding values in concatenated texts from args.

    Examples:
    >>> replace()
    ''

    >>> replace("")
    ''

    >>> replace("A", "B")
    'A\\nB'

    >>> replace("A $a", "B", a=10)
    'A 10\\nB'

    >>> replace("A $a", "B", "$g", a=10, g="Ala ma kota")
    'A 10\\nB\\nAla ma kota'

    """
    text = "\n".join(args)

    for k, v in kwargs.items():
        text = text.replace(f"${k}", str(v))

    return text
