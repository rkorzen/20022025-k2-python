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