"""
Stwórz modul pythona pozwalajacy na wykonywanie prostych obliczen

(dodawanie, odejmowanie, mnozenie, dzielenie, pierwiastkowanie, potegowanie)

Zaprojektuj to tak, by funkcje arytmetyczne mogly byc uzywane w innych modulach

Sam modul powinien miec tez zaimpelmentowany rodzaj tekstowego CLI

Przyklad:

$ python kalkulator.py
Podaj rodzaj operacji (+-/* ^ p): +
Podaj arg 1: 2
Podaj arg 2: 3

Wynik operacji (+) na arg: (2, 3) to: 5

Pomocne:

lista = [add, sub]

for func in lista:
    func(1, 2)
"""
import logging


logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="logs.log")
logger = logging.getLogger(__name__)



def add(a, b):
    logger.debug("Wywołano funkcję add z arg %s %s" % (a, b) )
    return a + b

def sub(a, b):
    logger.debug("Wywołano funkcję sub z arg %s %s" % (a, b))
    return a - b

def mul(a, b):
    logger.debug("Wywołano funkcję mul z arg %s %s" % (a, b))
    return a * b

def div(a, b):
    logger.debug("Wywołano funkcję div z arg %s %s" % (a, b))
    if b == 0:
        logger.warning("Wywołano funkcję div dzielnikiem 0! Sprawdz dane!!" )
        raise ValueError("Dzielnik nie może być 0")
    return a / b

def power(a, b):
    logger.debug("Wywołano funkcję div z arg %s %s" % (a, b))
    return a ** b

def get_data():
    op = input("Podaj rodzaj operacji: (+-*/^)")
    a = float(input("Podaj arg 1: "))
    b = float(input("Podaj arg 2: "))
    logger.debug("Pobrano dane %s %s %s" % (op, a, b))
    return op, a, b


def main():
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "^": power

    }

    op, a, b = get_data()

    result = operations[op](a, b)

    print(f"Wynik operacji ({op}) na arg: ({a}, {b}) to: {result}")


if __name__ == "__main__":
    main()

