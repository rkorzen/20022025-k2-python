"""
Wykorzystując moduł collections napisz kod który zliczy ilość wystąpień każdego znaku w zadanym tekscie
"Ala ma kota"

"""
from collections import Counter, defaultdict

text = "Ala ma kota"

def rozwiazanie_1(text):
    zliczenia = {}

    for znak in text:
        if znak in zliczenia:
            zliczenia[znak] += 1
        else:
            zliczenia[znak] = 1
    return zliczenia

def rozwiazanie_2(text):
    zliczenia = {}

    for znak in text:
        zliczenia[znak] = zliczenia.get(znak, 0) + 1
    return zliczenia

def rozwiazanie_3(text):
    zliczenia = {}

    for znak in text:
        zliczenia[znak] = zliczenia.setdefault(znak, 0) + 1

    return zliczenia

def rozwiazanie_4(text):
    zliczenia = defaultdict(int)
    for znak in text:
        zliczenia[znak] += 1
    return zliczenia

def rozwiazanie_5(text):
    return Counter(text)

def rozwiazanie_6(text):
    zliczenia = {}
    for znak in set(text):
        zliczenia[znak] = text.count(znak)
    return zliczenia


print(rozwiazanie_1(text))
print(rozwiazanie_2(text))
print(rozwiazanie_3(text))
print(rozwiazanie_4(text))
print(rozwiazanie_5(text))
print(rozwiazanie_6(text))