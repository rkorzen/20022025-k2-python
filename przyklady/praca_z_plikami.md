## praca z plikami

```
f = open(sciezka, "w")
f.write("sasas")
# tu moze byc jakis blad
f.close()
 
r - read (domyślny)
w - write
a - append

rb
wb

```
```

try:
    f = open(sciezka, "w")
    ...
except:
    ...
finally:
    f.close()
    
```

## użycie context managera - to zalecany sposób pracy z plikami

    with open("plik.txt") as f:
        ...


## odczytywanie plikow

### odczytanie w calosci

    with open("plik.txt") as f:
        print(f.read())

### odczytuwanie linia po linii

    with open("plik.txt") as f:
        for line in f:
            print(line)


    with open("plik.txt") as f:
        for line in f.readlines():
            print(line)