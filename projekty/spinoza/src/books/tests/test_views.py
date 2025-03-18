from django.test import TestCase
from django.urls import reverse
from books.models import Author, Book, Borrowing
from django.contrib.auth.models import User
from django.template.defaultfilters import date as date_filter

class BookViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(title="Test Book", author=self.author)
        self.book2 = Book.objects.create(title="Test Book2", author=self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))  # /books/
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertContains(response, "Test Book2")

    def test_book_detail_view_for_unauthenticated_user(self):
        response = self.client.get(reverse("book_details", args=[self.book.id]))  # /books/1/
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Test Book</h1>")
        self.assertContains(response, "<p>John Doe</p>")
        self.assertNotContains(response, f'<a class="btn btn-primary" href="/books/{self.book.id}/borrow">Borrow</a>')

    def test_book_detail_view_for_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("book_details", args=[self.book.id]))  # /books/1/
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Test Book</h1>")
        self.assertContains(response, "<p>John Doe</p>")
        self.assertContains(response, f'<a class="btn btn-primary" href="/books/{self.book.id}/borrow">Borrow</a>')        

    def test_borrow_book_view_for_unauthenticated_user(self):
        response = self.client.get(reverse("borrow_book", args=[self.book.id]))  # /books/1/borrow/
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/books/1/borrow")

    def test_borrow_book_view_for_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("borrow_book", args=[self.book.id]), follow=True)  # /books/1/borrow/
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/books/1")
        self.assertContains(response, "Książka została wypożyczona")

        self.assertContains(response, "<h1>Test Book</h1>")
        self.assertContains(response, "<p>John Doe</p>")

        borrowing = Borrowing.objects.last()
        formatted_date = date_filter(borrowing.borrowing_date, "F j, Y, g:i a")

        self.assertContains(response,f"<td>{borrowing.user.username}</td>")
        self.assertContains(response,f"<td>{formatted_date}</td>")
        self.assertContains(response,f"<td>None</td>")


    def test_borrow_book_that_is_already_borrowed(self):
        self.client.force_login(self.user)
        Borrowing.objects.create(user=self.user, book=self.book)
        response = self.client.get(reverse("borrow_book", args=[self.book.id]), follow=True)  # /books/1/borrow/
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/books/1")
        self.assertContains(response, "Książka jest niedostępna")
