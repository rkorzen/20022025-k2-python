## instalacja

    pip install django

## 

    django-admin <polecenie>

    django-admmin startproject hellodjango
    
    cd hellodjango

    python manage.py runserver

    (ctrl+ C)

    python manage.py startapp greetings

##  praca z migracjami

    python manage.py showmigrations

    python manage.py makemigrations

    python manage.py migrate

    python manage.py sqlmigrate app_name <migration number>

    python manage.py sqlmigrate biblioteka 0001

## praca z modelem

Jak mamy taki model:

    class Book(models.Model):
    
        GENRES = (
            ('fiction', 'Fiction'),
            ('action', 'Action'),
            ('adventure', 'Adventure'),
            ('animation', 'Animation'),
            ('comedy', 'Comedy'),
            ('drama', 'Drama'),
            ('fantasy', 'Fantasy'),
            ('horror', 'Horror'),
            ('music', 'Music'),
        )
    
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        year = models.IntegerField(validators=[MaxValueValidator(2025)])
        isbn = models.CharField(max_length=255, blank=True)
        genre = models.CharField(max_length=255, blank=True, choices=GENRES)
        available = models.BooleanField(default=True)
        added_on = models.DateTimeField(auto_now_add=True)
        updated_on = models.DateTimeField(auto_now=True)
        last_borrowed_on = models.DateTimeField(blank=True, null=True)
        last_return_on = models.DateTimeField(blank=True, null=True)
    
    
        def __str__(self):
            return f"({self.id}) {self.title}"


### tworzenie instancji klasy

    book = Book(title="Diune", author="Frank Herbert", year=1965, genre="fiction")
    book.save()

albo:

    book = Book.objects.create(title="Diune", author="Frank Herbert", year=1965, genre="fiction")

### pobieranie instancji

    books = Book.objects.all()

    book = Book.objects.get(id=1)

    books = Book.objects.filter(title__icontains="Pan")


## Użytkownicy


    python manage.py createsuperuser


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


## cwiczenie 2

Dodaj szablon i zmodyfikuj funkcje widoku tak by z niego korzystaly w pozostaluch aplikacjach

uzyj render(request, template_name, context)


context to jest slownik - ktore przykazuje klucze i wartosci do szablon

uzyj extends do tego by korzystac z szablony bazowego

pamietaj o dodaniu aplikacji w settings (INSTALED_APPS)
Dodaj katalog templates w katalogu glownym projektu i uwzglednij go w settings:

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


## cwiczenie 3

utworz aplikacje biblioteka
w niej utworz services.py i dodaj kod z mini_projekt.py (w moim repo to juz jest)
dodaj aplikacje do INSTALLED_APPS
utworz routing (urls)

/books/ - widzi liste książek
/books/1 -  widzo książkę o id = 1

Dajcie znac czy jesteście :D
