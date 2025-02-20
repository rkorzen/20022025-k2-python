# liczby w Pythonie

## liczby całkowite

     int

     int() -> 0
    
     int("c0ffee", base=16) -> 12648430

     1_000_000 -> 1000000
     
### operatory arytmetyczne


     +-* 
     /  -  true div - wynik liczba zmiennoprzecinkowa 
     // -  dzielenie calkowite
     %

     ** - potegowanie

### liczby zmiennoprzecinkowe


https://www.youtube.com/watch?v=9bmO4LUSAuA&embeds_referring_euri=https%3A%2F%2Fpywaw.org%2F&source_ve_path=OTY3MTQ

Uwaga na precyzję! 

    0.30000000000000004

    1200.9
    
notacja naukowa:

    12.1e2

     100000000000000000.1  -> 1e+17


wartości `nan`, `inf`


>>> 1.79e308
1.79e+308
>>> 1.8e308
inf


    float("-inf") < x < float("inf")

    >>> float("-inf") < x < float("inf")
    True
    >>> float("-inf") < float("nan") < float("inf")
    False
    >>> 1.1 == 1.1
    True
    >>> float("nan") == float("nan")
    False
    >>> import math
    >>> x = float("nan")
    >>> 
    >>> 
    >>> 
    >>> x is float("nan")
    False
    >>> import math
    >>> math.is
    math.isclose(  math.isfinite( math.isinf(    math.isnan(    math.isqrt(   
    >>> math.is
    math.isclose(  math.isfinite( math.isinf(    math.isnan(    math.isqrt(   
    >>> math.isnan(x)



## complex

    >>> liczba =  1 + 2j
    >>> liczba
    (1+2j)
    >>> liczba.real
    1.0
    >>> liczba.imag
    2.0


