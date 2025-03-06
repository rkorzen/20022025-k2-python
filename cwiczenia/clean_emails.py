"""

dla wejscia
rafal@@wp.pl rafal@wp.pl @x.pl
rk@wp.pl
rkorzen_at_gmail.com

dostaje wyjscie

rafal@wp.pl
rk@wp.pl
rkorzen_@gmail.com


$ python clean_emails.py data/wrong_emails.txt data/cleaned_emails.txt

"""
import sys



# odczytaj plik
def odczytaj_plik(plik_wejsciowy) -> list[str]:
    with open(plik_wejsciowy) as f:
        dane = f.read().split()
    return dane

def preprocessing(lista: list[str]) -> list[str]:
    """poprawia takie rzeczy jak no _at_ -> @"""
    dane = []

    rules = [
        lambda x: x.replace("_at_", "@"),
        str.lower
    ]
    for el in lista:
        for rule in rules:
            el = rule(el)
        dane.append(el)

    return dane

# walidacja każdego z potencjalnych emaili i utworzenie listy wynikowej
def validate_email(text: str) -> bool:
    """Zwraca True jeśli text spelnia warunki bycia emailem"""

    tests = [
        lambda x: x.count("@") != 1,
        lambda x: x.startswith("@"),
    ]

    for test in tests:
        if test(text):
            return False

    return True



def validate_all(dane: list[str]) -> bool:
    output: list[str] = []
    for d in dane:
        if validate_email(d):
            output.append(d)
    return output


# zapisanie do pliku wyjściowego

def export(plik_wyjsciowy: str, dane: list[str]):
    with open(plik_wyjsciowy, "w") as f:
        f.write("\n".join(dane))


# funkcja glowna

def main(plik_wejsciowy: str, plik_wyjsciowy: str):
    dane = odczytaj_plik(plik_wejsciowy)
    dane = preprocessing(dane)
    result = validate_all(dane)
    export(plik_wyjsciowy, result)


if __name__ == "__main__":
    plik_wejsciowy = sys.argv[1]
    plik_wyjsciowy = sys.argv[2]

    main(plik_wejsciowy, plik_wyjsciowy)
