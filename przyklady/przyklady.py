def add(a, b):
    return a + b


print(add(1, 2))
print(add(a=1, b=2))


# tak zakazujemy stosowani nazw
def add(a, b, /):
    return a + b


print(add(1, 2))
# print(add(a=1, b=2))


def add(*, a=1, b=2):
    return a + b


# print(add(1, 2))
print(add(a=1, b=2))


# łączenie tych ograniczen


def add(a, b, /, *, to_float=False):
    result = a + b
    if to_float:
        return float(result)
    return result


print(add(1, 2))
# print(add(a=1, b=2))
print(add(1, 2, to_float=True))


# najbardziej złożona sygnatura funkcji


def add(a, b, /, *args, to_float=False, **kwargs):
    print(args, kwargs)
    result = a + b
    if to_float:
        return float(result)
    return result


print(add(1, 2, 3, 4, 5, to_float=True, pretty_print=True))

print(add(1, 2, a=1, b=2))
