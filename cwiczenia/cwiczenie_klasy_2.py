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