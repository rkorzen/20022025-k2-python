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
    # podzielic zawartosc po bialych znakach

    text = "A B\nC\tD"
    dane = text.split()


def preprocessing(lista: list[str]) -> list[str]:
    """poprawia takie rzeczy jak no _at_ -> @"""


# walidacja każdego z potencjalnych emaili i utworzenie listy wynikowej
def validate_email(text: str) -> bool:
    """Zwraca True jeśli text spelnia warunki bycia emailem"""
    ...


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

def main():
    dane = odczytaj_plik(sys.argv[1])
    dane = preprocessing(dane)
    result = validate_all(dane)
    export(sys.argv[2], result)
