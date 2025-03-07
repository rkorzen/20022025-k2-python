## instalacja

    pip install django

## 

    django-admin <polecenie>

    django-admmin startproject hellodjango
    
    cd hellodjango

    python manage.py runserver

    (ctrl+ C)

    python manage.py startapp greetings




## zadanie 1

Utwórz nową aplikację algebra

/algebra/add/1/2
    
    wynik operacji add na arg 1, 2 to 3

/algebra/sub/1/2
/algebra/div/1/2
/algebra/mul/1/2


- pamiętaj o inlcude w głownym urls

- dodaj kolejna aplikacje - optymalizacje i uzyj w niej funkcji
  (utworz modul services.py i w nim umiesc ponizsza funkcje)

    def calculate(distance: int, price_per_l: float, l_per_100: float):
        fuel = distance *  l_per_100 / 100
        return round(fuel * price_per_l, 2)

w pliku views - zaimportuj te funkcje i utworz odpowiedni widok, którą wykorzysta


/spalanie/100/4.5/7.2

...
