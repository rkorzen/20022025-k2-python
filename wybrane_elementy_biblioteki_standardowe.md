## modul re

re.match
re.findall
re.search
re.sub
re.finditer
re.split


re.compile

pattern = "\b\d{2}-\d{2}-d{4}\b"


## modul csv

Praca z plikami csv - comma separated value

delimiter - czyli to czy rozdzielami (sepratora)
quotechar - to wydziela teksty 

```
a,b,c
1,1,1
2,1,1

```

```
a;b;c
1;1;1
2;1;1

```


```
name,tags
ibm,"pecet,superkomputer"
```

praca 

import csv

with open(...)  as f:
    reader = csv.reader(f, delimiter, quotechar)
    reader = csv.DictReader(f, delimiter, quotechar)


with open(..., "w")  as f:
    writer = csv.writer(f, delimiter, quotechar)
    writer = csv.DictWriter(f, delimiter, quotechar)

## JSON

import json

structura_python = {'a':1, "b": "Zażółć gęślą jaźń"}

json.dumps(structura_python)

json_text = '{"a": 1, "b": "Za\\u017c\\u00f3\\u0142\\u0107 g\\u0119\\u015bl\\u0105 ja\\u017a\\u0144"}'

json.loads(json_text)


with open("plik.json") as f:
    dane = json.load(f)


with open("plik.json", "w") as f:
    json.dump(f, dane)

In [17]: r
Out[17]: Record(id=31, product='Tablet', price=1400, quantity=1, date='2025-03-06')

zamowienia = [r]

In [21]: json.dumps([vars(r) for r in zamowienia])
Out[21]: '[{"id": 31, "product": "Tablet", "price": 1400, "quantity": 1, "date": "2025-03-06"}]'
