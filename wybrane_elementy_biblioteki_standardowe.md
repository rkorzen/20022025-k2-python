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