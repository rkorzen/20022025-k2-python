from django.test import TestCase
from books.models import Author
# Create your tests here.


class AuthorModelTest(TestCase):

    def test_str_representation(self):
        author = Author(first_name="John", last_name="Doe")
        self.assertEqual(str(author), "John Doe")

# dopisz testy metody __str__ dla modelu Book, Genre, Borrowing