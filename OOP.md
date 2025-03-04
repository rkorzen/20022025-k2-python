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