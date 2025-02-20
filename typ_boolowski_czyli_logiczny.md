# bool

    bool() -> False

    True, False

    and, or, not


Te wartosci beda np zawsze wynikiem operacji porownania (o ile można porownywac)


### operatory porownania ( i inne) zwróca nam zawsze typ logiczny:

    >
    <
    >=
    <=
    ==
    !=

    is

    in

### uogolnione typy logiczne


    if lista:
        print("zrob cos")

    - jeśli lista = []  to nie wykona sie
    - jeślu lista zawiera jakies elementy to wykona sie


    bool([]) -> False
    bool([False]) -> True

    wszystko co jest puste lub jest zerem moze by traktowane jako False w wyrazeniach warunkowych lyb przy jawnej zamianie na typ bool
    wszystko inne bedze jako True


    if bool(lista) is True

    da taki sam efekt jak:

    if lista

### mamy funkcje `all` i `any`


    >>> any([x>y, x+1 > y, x == 1])
    True
    >>> x>y or x+1 > y or x == 1
    True

    >>> y = 0
    >>> any([x>y, x+1 > y, x == 1, x % y == 0])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    >>> x>y or x+1 > y or x == 1 or x % y == 0
    True


### typ `bool` to podzbior `int`

    
    bool + 2 -> 3

    3 / False -> ZeroDivisionError


    x = 0
    x == False -> True