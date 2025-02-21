"""
Napisz dekorator, który zmierzy czas wykonania dowolnej funkcji i wypisze to na ekranie


Wykonanie funkcji add zajęło 0.1 s


Przydatne rzeczy to:

import time

t = time.time()
...
print(time.time() - t)
"""

import time
from functools import wraps


def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Wywołanie funkcji {func.__name__} zajęło {end - start}")
        return r

    return wrapper


@timeit
def moja_funkcja():
    return sum([x for x in range(100000)])


moja_funkcja()
