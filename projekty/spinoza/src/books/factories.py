from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from books.models import Author, Genre, Book, Review, Borrowing



class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    date_of_birth = Faker("date_of_birth")
    date_of_death = None
    bio = Faker("text", max_nb_chars=1000)


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = Faker("text", max_nb_chars=25)
    description = Faker("text", max_nb_chars=500)


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = Faker("text", max_nb_chars=100)
    author = SubFactory(AuthorFactory)
    genre = SubFactory(GenreFactory)
    summary = Faker("text", max_nb_chars=1000)
    isbn = Faker("isbn13")
    
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")
    

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    book = SubFactory(BookFactory)
    name = Faker("name")
    user = SubFactory(UserFactory)
    comment = Faker("text", max_nb_chars=1000)

    
class BorrowingFactory(DjangoModelFactory):
    class Meta:
        model = Borrowing

    book = SubFactory(BookFactory)
    user = SubFactory(UserFactory)
    borrowing_date = Faker("date_time_this_year")
    return_date = None


