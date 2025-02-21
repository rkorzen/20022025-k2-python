from functools import wraps


def limit_calls(max_calls):

    def decorator(func):
        counter = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            if counter < max_calls:
                counter += 1
                return func(*args, **kwargs)
            else:
                print(f"Limit wywołań funkcji {func.__name__} ({max_calls}) osiągnięty")

        return wrapper

    return decorator


@limit_calls(3)
def greet(name):
    print(f"Cześć {name}")


greet("A")
greet("B")
greet("C")
