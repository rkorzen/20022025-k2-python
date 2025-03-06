from main import calculate


def cli():
    d = int(input("Podaj dystans: "))
    pl = float(input("Cena litra: "))
    lp100 = float(input("Spalanie na 100km: "))

    r = calculate(d, pl, lp100)

    print(f"Koszt przejazdy to {r} PLN")

cli()