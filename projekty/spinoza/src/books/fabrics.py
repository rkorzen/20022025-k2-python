from faker import Faker
from books.models import Book, Author, Genre
from datetime import timedelta

fake = Faker()

def create_book():

    authors = Author.objects.all()
    genres = Genre.objects.all()

    title = fake.sentence()
    
    summary_length = fake.random.randint(100, 1000)
    summary = fake.text(summary_length)

    author = fake.random.choice(authors)
    genre = fake.random.choice(genres)

    book = Book.objects.create(
        title=title,
        summary=summary,
        author=author,
        genre=genre,
    )

    return book

def bulk_create_books(n):

    books = []
    for _ in range(n):
        books.append(create_book())

    return books


def create_author():
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth()
    life_span = fake.random.randint(20, 110)

    if date_of_birth.year > 1960 or date_of_birth.year + life_span > 2024:
        date_of_death = None
    else:
        date_of_death = date_of_birth + timedelta(days=life_span * 365)
    
    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        date_of_death=date_of_death,
    )

    return author


def bulk_create_authors(n):
    objects = []
    for _ in range(n):
        objects.append(create_author())

    return objects


def create_genre():
    name = fake.text(25)
    description = fake.text(500)
    genre = Genre.objects.create(name=name, description=description)

    return genre

def bulk_create_genres(n):
    objects = []
    for _ in range(n):
        objects.append(create_genre())

    return objects

