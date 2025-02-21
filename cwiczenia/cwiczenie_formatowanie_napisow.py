"""
Stwórz strukture z 10 produktami
Nazwa, cena, waga

To moze byc slownik, moga to byc 3 listy.


przeiteruj po tej strukrurze i stworz napis, ktory bedzie paragonem



Efekt koncowy:

print(napis)

Gouda           1.1 kg    26.78 PLN
Szczypior       0.1 kg     5.45 PLN
tort           12.2 kg   674.56 PLN
===================================
SUMA:                    zzz.zz PLN


"""

import random
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    weight: float
    price: float


# class Product:
#
#     def __init__(self, name: str, weight: float, price: float):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#
#     def __str__(self):
#         return f"Product(name='{self.name}', weight={self.weight}, price={self.price})"
#
#     def __repr__(self):
#         return f"XXX(name='{self.name}', weight={self.weight}, price={self.price})"


nazwy = [
    "Kasza Gryczna",
    "ryż",
    "Jabłka",
    "Pomarańcze",
    "Ziemniaki",
    "Filet z sdvheoruhfskjbv owuhfv sijkbv wiure",
]


def random_price():
    return round(random.random() * random.randint(1, 100), 2)


def random_weight():
    return round(random.random() * random.randint(1, 3), 2)


produkty = [Product(nazwa, random_weight(), random_price()) for nazwa in nazwy]

max_name_length = max([len(p.name) for p in produkty])


raport = ""
suma = 0
for produkt in produkty:
    suma += round(produkt.price * produkt.weight, 2)
    raport += f"{produkt.name.lower():{max_name_length}} {produkt.weight:7.2f} kg {produkt.price:7.2f} PLN\n"

raport = f"""
{raport}
{"="*(max_name_length+23)}
SUMA: {round(suma,2):{max_name_length + 13}.2f} PLN
"""

print(raport)
