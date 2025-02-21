from pprint import pprint

lista = [10, 34, 39, 56, 232]

kwadraty_parzystych = []
for liczba in lista:
    if liczba % 2 == 0:
        kwadraty_parzystych.append(liczba**2)

print(kwadraty_parzystych)


kwadraty = [x**2 for x in lista if x % 2 == 0]
print(kwadraty)


## tabliczka

tabliczka = []
for i in range(1, 10):
    row = []
    for j in range(1, 10):
        row.append(i * j)
    tabliczka.append(row)

pprint(tabliczka)


pprint({(i * j for i in range(1, 10)) for j in range(1, 10)})


print([x for x in range(10)])
print({x for x in range(10)})
print({x: x**2 for x in range(10)})
