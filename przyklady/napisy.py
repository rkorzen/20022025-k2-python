napis = "Ala ma kota"
napis2 = napis
print(id(napis))
print(id(napis2))


napis = napis + " kot ma Alę"

print(id(napis))
print(id(napis2))

x = "ALA" "KOT"
print(x)

x = "ALA" "KOT"
print(x)


x = "ALA" "KOT"

print(x)

y = "ALA\nKOT"
print(y)

y = r"ALA\nKOT"
print(y)

y = "ALA\\nKOT"
print(y)


y = """ALA
KOT"""
print(y)


print("ALA\aT")


print("Ala ma %s lat i posiada %s" % (10, "KOTA"))
print("Ala ma %d lat i posiada %s" % (10, "KOTA"))
print("Ala ma %.2f lat i posiada %s" % (10, "KOTA"))

print("Ala ma {:.2f} lat i posiada {}".format(10, "KOTA"))
print("Ala ma {} lat i posiada {}".format(10, "KOTA"))


print("Ala ma {wiek:.2f} lat i posiada {zwierz}".format(wiek=10, zwierz="KOTA"))
print("Ala ma {wiek} lat i posiada {zwierz}".format(wiek=10, zwierz="KOTA"))


wiek = 10
zwierz = "KOTA"


print(f"Ala ma {wiek:6.2f} lat i posiada {zwierz:^30}")
print(f"Ala ma {wiek} lat i posiada {zwierz}")
