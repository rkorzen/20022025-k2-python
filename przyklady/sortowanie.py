lista = (5, 1, 4, 3, 2)

# print(lista.sort())
# print(lista)

print(sorted(lista, reverse=True))


dane = [(5, "a"), (1, "e"), (2, "c"), (3, "b"), (4, "d")]

print(sorted(dane))


def second(x):
    return x[1]


print(sorted(dane, key=second))
print(sorted(dane, key=lambda x: x[1]))


second = lambda x: x[1]

print(second("ax"))
