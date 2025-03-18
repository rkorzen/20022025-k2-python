from django.test import TestCase
from books.models import Author, Book, Genre, Borrowing
from django.contrib.auth.models import User
# Create your tests here.


class AuthorModelTest(TestCase):

    def test_str_representation(self):
        author = Author(first_name="John", last_name="Doe")
        self.assertEqual(str(author), "John Doe")


class BookModelTest(TestCase):

    def test_str_representation(self):
        author = Author(first_name="John", last_name="Doe")
        book = Book(title="Test Book", author=author, summary="Test Description")
        self.assertEqual(str(book), "Test Book (John Doe)")

    def test_is_available(self):
        author = Author.objects.create(first_name="John", last_name="Doe")
        book = Book.objects.create(title="Test Book", author=author, summary="Test Description")
        self.assertTrue(book.is_available)

    def test_is_not_available(self):
        user = User.objects.create_user(username="John Doe", password="password")
        author = Author.objects.create(first_name="John", last_name="Doe")
        book = Book.objects.create(title="Test Book", author=author, summary="Test Description")
        borrowing = Borrowing.objects.create(user=user, book=book)
        self.assertFalse(book.is_available)


class GenreModelTest(TestCase):

    def test_str_representation(self):
        genre = Genre(name="Test Genre")
        self.assertEqual(str(genre), "Test Genre")


class BorrowingModelTest(TestCase):

    def test_str_representation(self):
        user = User.objects.create_user(username="John Doe", password="password")

        author = Author.objects.create(first_name="John", last_name="Doe")
        book = Book.objects.create(title="Test Book", author=author)

        borrowing = Borrowing.objects.create(user=user, book=book)
        self.assertEqual(str(borrowing),  f"Test Book (John Doe) ({borrowing.borrowing_date} - None)")

