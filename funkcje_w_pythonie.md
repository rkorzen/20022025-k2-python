# Funkcje

## najprostsze definicje

```
def nazw_funkcji(<opcjonale_argumenty>):
   <blok instrukcji>
   <retur> <wartosc>
   
def hello():
    print("hello world")


def hello():
    print("hello world")
    return None
    
def hello():
    print("hello world")
    return
```

### argumenty pozycujne
```
    
def funkcja_z_argumentami_pozycyjnymi(a, b, c):
    ...
    
funkcja_z_argumentami_pozycyjnymi(1, 2, 3)

to jest ok:
funkcja_z_argumentami_pozycyjnymi(c=1, b=2, a=3)   

funkcja_z_argumentami_pozycyjnymi(1, b=2, a=3)   # dwa razy podane a - raz przez pozycje raz przez przez nazwe



```

### argumenty nazwan (keyword arguments)

```
def funkcja_z_argumentami_pozycyjnymi(a=1, b=2, c=3):
    ...


tak też jest ok:
funkcja_z_argumentami_pozycyjnymi(1, 2, 3)

```

###  mozna wymusic stosowanie nazw lub zakazc stosowania nazw

patrz przyklady/funkcje.py