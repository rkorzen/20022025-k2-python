"""
Napisz program wczytujący plik z logami aktywności użytkowników
w systemie. Na podstawie wczytanych danych wyświetl informację o
sumarycznym czasie przebywania każdego użytkownika w systemie.
Przykład użycia:

$ python zlicz_czasy.py

Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s

Przydatne

with open("dane/logs.txt") as f

dir(str)
split - dzieli wg podanego znaku
strip - usuwa biale znaki z krancow

from collections import defaultdict

total_time = defaultdict(int)
total_time["user-1"] += 10

sorted(total_time.items(), key=lambda x: x[1])
"""
