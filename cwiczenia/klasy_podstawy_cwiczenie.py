"""
Zdefiniuj klasy reprezentujace Film i Serial (obie niech na razie maja tylko tytuł)
Utwórz kilka obietkow jednej i drugiej klasy i umiesc je w liscie
Utwórz funkcję wybierz, ktora bedzie potrafila filtrowac liste i wybierc z niej tylko zadany rodzaj obiektow


lista = [f1, f2, s1, s2]

assert wybierz(lista, Film) == [f1, f2]
assert wybierz(lista, Serial) == [s1, s2]

"""
from typing import Union, Type, TypeVar, Optional

T = TypeVar("T")


class Base:
    def __init__(self, title: str):
        self.title = title
        self.odtworzenia: int = 0
        self.ocena: Optional[float] = None

class Film(Base):
    pass

class Serial(Base):

    def __init__(self, title, seria, epizod):
        super().__init__(title)

        self.title = title
        self.seria = seria
        self.epizod = epizod

def wybierz(kolekcja: list[Union[Film, Serial]], rodzaj: Type[T]) -> list[T]:
    return [x for x in kolekcja if isinstance(x, rodzaj)]

# def wybierz(kolekcja = list[Film | Serial]):
#     pass

f1 = Film("Titanic")
f2 = Film("Władca Pierścieni")
s1 = Serial("The Lost", 1, 1)
s2 = Serial("Sfora", 2, 10)


lista: list[Film | Serial] = [f1, f2, s1, s2]

assert wybierz(lista, Film) == [f1, f2]
assert wybierz(lista, Serial) == [s1, s2]
assert wybierz(lista, Base) == [f1, f2, s1, s2]