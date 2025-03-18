# Spinoza

## Setup

- będziemy używać django-extensions

    pip install django-extensions

lub

    uv add django-extensions


### w settings.py dodać do INSTALLED_APPS


    INSTALLED_APPS = [
        ...
        "django_extensions",
        ...
    ]

### Uruchomienie shell_plus

```bash
python manage.py shell_plus
```

## Migrations

```bash
python manage.py makemigrations
```


### Tworzenie instancji modelu


    author = Author(first_name="Graham", last_name="Masterton")
    author.save()

    author2 = Author.objects.create(first_name="Henryk", last_name="Sienkiewicz")

    author3 = Author.objects.get_or_create(first_name="Frank", last_name="Herbert")
    author4 = Author.objects.get_or_create(first_name="Henryk", last_name="Sienkiewicz")


### Zwracanie książki - zadanie:

Zaimplementuj widok zwracania książki. Po kliknięciu w przycisk "Return" książka powinna być dostępna do wypożyczenia.
W tabeli wypożyczeń powinna być widoczna data zwrotu.


In [2]: book = Book.objects.first()

In [3]: book
Out[3]: <Book: Manitou (Graham Mastertorn)>

In [5]: book.borrowing_set.all()
Out[5]: <QuerySet [<Borrowing: Manitou (Graham Mastertorn) (2025-03-18 10:46:34.446411+00:00 - None)>]>

In [6]: book.borrowing_set.last()
Out[6]: <Borrowing: Manitou (Graham Mastertorn) (2025-03-18 10:46:34.446411+00:00 - None)>

In [7]: borrowing = book.borrowing_set.last()

In [8]: from django.utils import timezone

In [9]: timezone.now()
Out[9]: datetime.datetime(2025, 3, 18, 10, 54, 33, 575707, tzinfo=datetime.timezone.utc)

In [10]: borrowing.return_date = timezone.now()

In [11]: borrowing.save()

In [12]: book.is_available = True

In [13]: book.save()

In [14]: borrowing = book.borrowing_set.last()

In [15]: borrowing.return_date = timezone.now()

In [16]: book.save()

In [17]: borrowing.save()

In [18]: 


### Zadanie: Dodanei widoki Home i About

Widok Home - to wyświetlenie szablonu base.html 

127.0.0.1:8000/

Widok About - to wyświetlenie szablonu about.html

127.0.0.1:8000/about/

