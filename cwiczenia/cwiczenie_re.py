"""
Z pliku dane/dane.txt wybierz przy pomocy wyrazen regularnych:

- adresy IP
- daty
- emaile

wypisz każda listę na ekranie
"""

import re

ip_pattern = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
email_pattern = re.compile(r"\w+@\w+\.\w{3}")

with open("dane/dane.txt") as f:
    text = f.read()

print(ip_pattern.findall(text))
print(date_pattern.findall(text))
print(email_pattern.findall(text))