# Klasy w Pythonie

## Podstawy
    
    class NazwaKlasy:
        arg_klasowy = 10

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
    
    
    class NazwaKlasy(KlasaRodzica, KlasaRodzica2):
        arg_klasowy = 10

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2


## Dziedziczenie

Jak mamy klasę rodzica, która ma jakieś atrybuty i metody, 


    class Rodzic:
        atr1 = 1

        def __init__(self):
            self.x = 10

        def metoda(self):
            return self.x + self.atr1

to klasa potomna dziedziczy te atrybuty i metody po rodzicy


    class Dziecko(Rodzic):
        ...


    d = Dziecko()
    assert d.x == 10
    assert d.attr1 = 1
    assert d.metoda() == 11


gdyby zachodzila potrzeba zastapienia dzialania orygunalnej metody to po prostu ja nadpisumemy


    class Dziecko(Rodzic):
        atr1 = 10
        

    d = Dziecko()
    assert d.x == 10
    assert d.attr1 = 10
    assert d.metoda() == 20



    class Dziecko(Rodzic):
        
        def metoda():
            return self.x ** 2 + self.attr1
        
        

    d = Dziecko()
    assert d.x == 10
    assert d.attr1 = 1
    assert d.metoda() == 101


ale mozemy tez czesciowo zastapic a czesciowi wykorzystac


    class Dziecko(Rodzic):
        
        def metoda():
            wynik_z_rodzica = super().metoda()
            return wynik_z_rodzica + 1000
        
        

    d = Dziecko()
    assert d.x == 10
    assert d.attr1 = 1
    assert d.metoda() == 1011


## Atrybuty, metody i atrybuty dynamiczne

    

    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year
            self.age = 2025 - self.b_year
    

    ... mija rok i mamy 2026

    p = Person("Rafał", 1980)
    print(p.age) # 45


poprawiam...

    from datetime import datetime
    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year
            self.age = datetime.now().year - self.b_year
    

    ... mija rok i mamy 2026

    p = Person("Rafał", 1980)
    print(p.age) # 46

    ... ale... mija kolejny rok i mamy 2027

    print(p.age) # 46  (a powinno byc 47 )

poprawiam...

    from datetime import datetime
    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year

    
        def age(self):
            return datetime.now().year - self.b_year


    ... mija rok i mamy 2026

    p = Person("Rafał", 1980)
    print(p.age()) # 46

    ... ale... mija kolejny rok i mamy 2027

    print(p.age()) # 47  (a powinno byc 47 )
    print(p.age)   # bound method age of class Person.. 


poprawiam ...


    from datetime import datetime
    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year

    
        @property  # atrybut dynamiczny
        def age(self):
            return datetime.now().year - self.b_year


    ... mija rok i mamy 2026

    p = Person("Rafał", 1980)
    print(p.age) # 46

    ... ale... mija kolejny rok i mamy 2027

    print(p.age) # 47  (a powinno byc 47 )

a czy mogę zrobić teraz tak by ustawic rok urodzenia poprzez podanie wieku?


    p.age = 50
    p.b_year  # 1977 (bo mam 2027 rok)


potrzebna modyfikacja:


    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year

    
        @property  # atrybut dynamiczny - getter - co ma sie stac jak pobieram te wartosc
        def age(self):
            return datetime.now().year - self.b_year

        # do ustawienia sluzy setter
        # jak mamy gettera (property) to mozemy z niego zrobic setter

        @age.setter
        def age(self, value):
            self.b_year = datetime.now().year - value


## Przeciażanie operatorów


    class Person:
        
        def __init__(self, name, b_year):
            self.name: str = name
            self.b_year: int = b_year

    
        @property  # atrybut dynamiczny - getter - co ma sie stac jak pobieram te wartosc
        def age(self):
            return datetime.now().year - self.b_year

        def __gt__(self, other):
            if isinstance(other, self.__class__):
                return self.age > other.age

    p1 = Person("A", 1980)
    p2 = Person("B", 1970)

    p1 > p2


## Iteratory

    class Iterator:

        def __iter__(self): ...
        
        def __next__(self): ...
         