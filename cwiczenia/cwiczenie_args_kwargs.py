""""
Zdefinuj funkcję replace, która przyjmie nieokreślna liczbę tekstów, oraz parametrów i na podstawie tych paranetrow
dokona zamiany napisow w tekstach

Przyklad

1.

replace("Wartość $a", "wartość $b, $a", a=10, b=20)

Wartość 10
wartość 20, 10

2.
replace("Cena produktu to $cena", "wartość vat to $vat", cena=100, vat=23)

Cena produktu to 100
wartość vat to 23

Pomocne:

"\n".join(teksty)
"t$ekst".replace("$e", "a") -> "takst"


"""