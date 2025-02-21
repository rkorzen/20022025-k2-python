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


## Domknięcie - clojure

Domknięciem nazywamy funkcję zagnieżdzoną, która pamięta swoje otoczenie.

```python

def outer_function(msg):
    
    def inner_function():
        print(f"Zapamiętana wiadomość to: {msg}")
    
    return inner_function

closure = outer_function("Hello ALX")
closure()

```

### Dekoratory

```python

def mydecorator(func):
    
    def wrapper():
        # kod wykonany przed funkcja oryginalma
        r = func()
        # kod wykonany po funkcji oryginalnej
        return r
        
    return wrapper

def dowolna_funkcja():
    print("jestem dowolna funkcja")

dowolna_funkcja = mydecorator(dowolna_funkcja)  



```