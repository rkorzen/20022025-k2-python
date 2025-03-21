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

### Testy

```bash
python manage.py test
```

#### testy z coverage

Instalacja coverage
```bash
pip install coverage
```
Wykonanie testów z coverage

```bash
coverage run manage.py test
coverage report
coverage html
```
Trzeba otworzyć plik index.html w katalogu htmlcov w przeglądarce


## Budowa URL

protokol://domena/path/?querystring
http://127.0.0.1:8000/contact/?name=Rafa%C5%82&email=korzeniewski%40gmail.com&message=sdsdsdsdsd#id-obiektu



## zadanie - dodanie komentarza do ksiazki:

bazujac na tym co mamy w contact dodaj mozliwosc dodawania komentarza do ksiazki.
Poki co komentarz moze dodac kazdy uzytkownik - zalogowany czy nie.

Podaje imie i tresc.

wyswietla sie to tak, ze komentarze wystepuja jeden pod drugim podajac: 

Imie
data

tresc


    class Book(models.Model):
        ...

    class Review(models.Model):
        book = models.ForeignKey(Book, on_delete=models.CASCADE)
        ...

    book = Book.objects.first()
    book.review_set.all()

### Dodaj formularze w widokach

/genres/
/authors/


które umożliwią dodawanie pozycji ale tylko przez administratora


/books/

## Crispy forms

Instalacja

    uv add crispy-bootstrap5

Dodanie do INSTALLED_APPS w settings.py


    "crispy_forms",
    "crispy_bootstrap5",

oraz na koncu

    # Crispy forms
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"


w module forms.py w aplikacji definiujemy formularz (np. oparty o model):


    class GenreForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            "to jest czesc z crisp forms - dodaje metode i przycisk" 
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id-exampleForm'
            self.helper.form_class = 'blueForms'
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Dodaj'))

        class Meta:
            model = Genre
            fields = ["name", "description"]



jeśli użyliśmy tej metody init

to w szablonie wystarczy zrobic

załadować templatetagi i filtry z crispy

    {% load crispy_forms_tags %}

potem mozemy uzywac crispy do generowania formularza

    {% crispy form %}


jeśli tego moe zrobilismy to czesc rzeczy sami musimy w szabloine dodac:

    <form method="post">
        {% csrf_token %}
        {{form|crispy}}
        <button type="submit" class="btn btn-primary">Dodaj</button>
    </form>


w widoku z koleji trzeba formularz wypelnic danymi

Kiedy obslugujemu POST

    form = MyForm(data=request.POST)
    if form.is_valid():
        form.save()

Kiedy obslugujemy GET

    form = MyForm()

i trzeba to przekazac do szablony w kontekście

    context = {"form": form}
    return render(request, "template.html", context)

## synchronizacja zależności 

    pip install faker

lub

    uv sync


## Dodanei komentarzy (inline w Adminie i pare innych rzeczy)


    # Dodaj model Comment - który jest powiązany z modelem Post i Author.
    # Komentarz ma mieć pola:
    # - content - tekst komentarza
    # - created_at - data dodania komentarza
    # - updated_at - data ostatniej modyfikacji komentarza
    # - post - powiązanie z modelem Post
    # - author - powiązanie z modelem User
    # - status - status komentarza (na_czekaniu, opublikowany, odrzucony)
    #            
    #  Dodaj formularz do dodawania komentarza.
    #  Komentarz może być dodawany tylko przez zalogowanego użytkownika i widoku post_detail.html.
    #  Wyslanie formularza powinno wysylac request metodą POST do widoku /blog/post/<pk>/add-comment/
    #  po utworzeniu komentarza wracamy na widok szzegolow danego posta i komentarz powinien byc widoczny pod postem.
    #  Dodaj w Paneu admina mozliwosc moderowania komentarzy - Inline do postu.


## Dodaj customowe akcje w PA:

- ustawienie statusu wybranych komentarzy na published, rejected, draft
- analogicznei dla postów (zgodnie z status choices)


## Dodanie context procesora dla Postow

wypisz w stopce ile jest wszystkich postow i wypisz 3 tytuly postow z najwieksza liczba komentarzy


## middleware

Dodaj middleware który doda do response nagłówek jak niżej:

response["X-Process-Time"] = czas wykonania

1. w pliku middleware.py dodaj nowy middleware
2. dodaj go do settings.py
3. sprawdz czy dziala w przegladarce np. 


# Django Rest Freamework
## Dodanie serializerow

Dodaj serializery oparte o model dla modeli Author i Genre z aplikacji books


## Dodaj widoki funkcyjne tak by obslugiwaly koncowki:

GET /api/v1/genres - lista gatunkiw
POST /api/v1/genres - dodanie nowego

GET /api/v1/authors - lista autorow
POST /api/v1/authors - dodanie nowego


## browsable API

zmien widoki tak by:
- korzystały z dekoratora api_view (patrz w snippets/views.py)
- korzystały z Response
- użyj statusów - analogicznie jak w snippets
- dodaj w widokach parametr format=None
- w api_urls.py dodaj to co w snippets/urls.py

efekt:

jesli w przegladarce wejdziemy na

http://127.0.0.1:8000/api/v1/authors/  - to mamy mieć browsable API a nie czysty JSON

## Widoki klasowe oparte o APIView

Na podstawie snippets/views.py oraz snippets/urls.py zrób zmiany w books/api_views.py oraz books/api_urls.py


## Widoki generyczne i mixny

Na podstawie snippets/views.py popraw books/api_views.py  tak by korzystać z mixinów

