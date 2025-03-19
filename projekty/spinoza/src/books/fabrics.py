from faker import Faker
from books.models import Book, Author, Genre
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
    ...


def bulk_create_authors(n):
    ...


def create_genre():
    ...


def bulk_create_genres(n):
    ...
