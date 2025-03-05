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
import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Poprawne wywołanie to:\n python zlicz_czasy.py sciezka/do/pliku")
    exit(1)

file_path = sys.argv[1]

last_login = {}
total_time = defaultdict(int)

with open(file_path) as f:
    for line in f:
        #login;action;time
        login, action, t_str = line.strip().split(";")
        t = int(t_str)

        if action == "LOGIN":
            last_login[login] = t
        elif action == "LOGOUT":
            total_time[login] += t - last_login.get(login, 0)

print("Czas przebywania w systemie:")
for u, t in sorted(total_time.items(), key=lambda x: x[1], reverse=True):
    print(f" - {u}: {t} s")

