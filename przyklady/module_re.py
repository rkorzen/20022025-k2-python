import re

# date_pattern = "\\b\\d{2}-\\d{2}-\\d{4}\\b"
date_pattern = r"\b(\d{2})-(\d{2})-(\d{4})\b"

data="11-02-1978"
liczby="111-02-19999"
tekst = "xxx urodzil sie 13-01-1977 roku. A yy urodzil sie 15-08-2022"

match_data = re.match(date_pattern, data)
match_liczby = re.match(date_pattern, liczby)

print(match_data)
print(match_data.group())

print(match_liczby)

# wszystkie wystapienia
print(re.findall(date_pattern, tekst))

# pierwsze wystapienie

print(re.search(date_pattern, tekst))

for match in re.finditer(date_pattern, tekst):
    print(match.group(), match.start(), match.end())

replacement = "xx-xx-xxxx"
print(re.sub(date_pattern, replacement, tekst))


print(re.split(date_pattern, tekst))


pattern = re.compile(date_pattern)

#print(re.findall(date_pattern, tekst))
print(pattern.findall(tekst))

dir(re)
help(re.findall)
