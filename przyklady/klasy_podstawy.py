
class Osoba:
    planeta = "Ziemia"

    def __init__(self, imie: str):
        self.imie = imie

class Przedmiot:
    pass

o1 = Osoba("Rafał")
o2 = Osoba("Michał")

p1 = Przedmiot()
p2 = Przedmiot()


print(Osoba.planeta)
print(o1.planeta)
print(o2.planeta)

Osoba.planeta = "Mars"

print(Osoba.planeta)
print(o1.planeta)
print(o2.planeta)


o1.planeta = "Jowisz"

print(Osoba.planeta)
print(o1.planeta)
print(o2.planeta)


print(type(o1))
print(type(p1))

print(isinstance(o1, Przedmiot))
print(isinstance(o1, Osoba))