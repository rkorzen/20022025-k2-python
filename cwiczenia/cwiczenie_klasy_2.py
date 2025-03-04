"""
Stwórz system zarządzania pojazdami, w którym będą różne klasy reprezentujące środki transportu.
Każdy pojazd powinien mieć wspólne cechy, ale różnić się szczegółami implementacji.

    Stwórz klasę bazową Vehicle, która będzie miała:
        Atrybuty: name (nazwa pojazdu) oraz max_speed (maksymalna prędkość).
        Metodę describe(), która wypisze podstawowe informacje o pojeździe.
        Metodę move(), która zwróci tekst "Pojazd się porusza".

    Stwórz klasy pochodne:
        Car (samochód): dodatkowy atrybut num_wheels (liczba kół), domyślnie 4.
        Bicycle (rower): dodatkowy atrybut num_wheels ustawiony na 2.
        Boat (łódź): nadpisuje metodę move(), aby zwracała "Łódź płynie po wodzie".
        Plane: nadpisanie metody move() - "Samolo leci"


    Przetestuj działanie klas:
        Utwórz obiekty klasy Car, Bicycle, Boat.
        Wywołaj metodę describe() dla każdego obiektu.
        Wywołaj metodę move() i sprawdź, czy działa zgodnie z oczekiwaniami.
"""


class Vehicle:

    def __init__(self, name, max_speed=100):
        self.name: str = name
        self.max_speed: int = max_speed

    def describe(self):
        print(f"Pojazd typu {self.__class__.__name__} o nazwie {self.name} i prędkości maksylanej {self.max_speed}")

    def move(self):
        print("Pojazd porusza się")


class Car(Vehicle):
    num_wheels: int = 4

class Bicycle(Vehicle):
    num_wheels: int = 2

class Boat(Vehicle):
    def move(self):
        print("Lodz płynie")

class Plane(Vehicle):
    def move(self):
        print("Samolot leci")

if __name__ == "__main__":

    assert Vehicle("UFO")
    assert Car("Mustang").num_wheels == 4
    assert Bicycle("Romet").num_wheels == 2
    assert Boat("Dar Młodzieży")
    assert Plane("Jumbojet")

    Plane("Jumbojet").describe()

    print(dir(Vehicle))
    v = Vehicle("Mustang")
    print(dir(v))

    print(dir(v.__class__))
    print(v.__class__.__name__)

