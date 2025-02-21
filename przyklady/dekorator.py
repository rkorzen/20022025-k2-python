from functools import wraps


def mydecorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """docstring wrappera"""
        print(f"Wywołuję funkcję {func.__name__}")
        r = func(*args, **kwargs)
        # kod wykonany po funkcji oryginalnej
        return r

    return wrapper


@mydecorator
def dowolna_funkcja():
    print("jestem dowolna funkcja")


@mydecorator
def add(a, b):
    """Dodawanie dwóch liczb"""
    return a + b


# dowolna_funkcja = mydecorator(dowolna_funkcja)

dowolna_funkcja()
print(add(1, 2))

print(help(add))
