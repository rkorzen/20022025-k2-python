
## najprostszy przykład wyrażenia listowego

```python
lista = [10, 34, 39, 56, 232]

kwadraty = []
for liczba in lista:
    kwadraty.append(liczba ** 2)


```

wyrazenie listowe (list comprehension)



```python
lista = [10, 34, 39, 56, 232]

kwadraty = [x ** 2 for x in lista]


```

## dodanie warunku 


```python
lista = [10, 34, 39, 56, 232]

kwadraty_parzystych = []
for liczba in lista:
    if liczba % 2 == 0:
        kwadraty_parzystych.append(liczba ** 2)


```

wyrazenie listowe (list comprehension)



```python
lista = [10, 34, 39, 56, 232]

kwadraty = [x ** 2 for x in lista if x % 2 == 0]


```