"""
Napisz funkcję analyze_text(content: str), która przyjmie tekst jako argument i zwróci słownik z analizą:

    word_count: liczba słów w tekście,
    longest_word: najdłuższe słowo w tekście,
    most_common_letter: najczęściej występująca litera.

📌 Wskazówki:

    Możesz użyć max() z key=len, aby znaleźć najdłuższe słowo.
    Możesz użyć Counter z collections, aby policzyć częstotliwość liter.

Napisz funkcję process_words(words: list[str], func), która przyjmuje listę słów i funkcję func,
a następnie zwraca nową listę słów przetworzonych przez tę funkcję.
📌 Wskazówka: func może być np. str.upper lub str[::-1].

Stwórz dekorator @execution_time, który będzie mierzył czas wykonania funkcji i wypisywał go w konsoli.
📌 Wskazówka: użyj time.perf_counter() przed i po wywołaniu funkcji.


Dodatkowo

Wywołaj process_words() z funkcja anonimowya lambda, np. lambda word: word[::-1] (odwracanie słów).
Dodaj dodatkowy dekorator @log_calls, który będzie logował każde wywołanie funkcji i jej argumenty.

"""
import logging
import time
from collections import Counter
from functools import wraps
from typing import TypedDict, Callable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


def log_calls(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_txt = [str(x) for x in args]
        positional_args = ", ".join(args_txt)
        kwargs_txt = [f"{k}={str(v)}" for k, v in kwargs.items()]
        keyword_args = ", ".join(kwargs_txt)

        params = ""
        if positional_args:
            params += positional_args
        if keyword_args and params:
            params += ", "
        if keyword_args:
            params += keyword_args

        logger.debug(f"Wywołano {func.__name__}({params})")
        return func(*args, **kwargs)

    return wrapper

def execution_time(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Wywołanie funkcji {func.__name__} zajęło {end - start:.9f} s")
        return result

    return wrapper


class AnalyzeResult(TypedDict):
    word_count: int
    longest_word: str
    most_common_letter: str

@log_calls
@execution_time
def analyze_text(content: str) -> AnalyzeResult:
    words = content.split()
    longest_word = max(words, key=len) if words else ""
    most_common_letter = Counter(content).most_common(1)[0][0] if content else ""

    # c = Counter(content)
    # most_common_letter = max(c, key=c.get) if content else ""

    return {
        "word_count": len(words),
        "longest_word": longest_word,
        "most_common_letter": most_common_letter,
    }

@log_calls
def process_words(words: list[str], func: Callable[[str], str]) -> list[str]:
    return [func(w) for w in words]

@log_calls
def jakas_funkcja(*args, **kwargs):
    ...

if __name__ == "__main__":
    assert analyze_text("") == {"word_count": 0, "longest_word": "", "most_common_letter": ""}
    assert analyze_text("ala") == {"word_count": 1, "longest_word": "ala", "most_common_letter": "a"}
    assert analyze_text("aaa bbbbbb ccc") == {"word_count": 3, "longest_word": "bbbbbb", "most_common_letter": "b"}

    assert process_words([], str.upper) == []
    assert process_words(["a", "b"], str.upper) == ["A", "B"]
    assert process_words(["ab", "cd"], lambda word: word[::-1]) == ["ba", "dc"]

    print(process_words(["a", "b"], str.upper))
    print(process_words.__annotations__)

    jakas_funkcja(1, 2, 3, a=10, b=20)
