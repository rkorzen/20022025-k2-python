from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Author, Genre, Borrowing
from django.utils import timezone
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, "books/book_details.html", {"book": book})

@login_required
def borrow_book(request, id):
    book = Book.objects.get(id=id)
    print(request.user)
    if book.is_available:
        Borrowing.objects.create(user=request.user, book=book)
        messages.success(request, "Książka została wypożyczona")
    else:
        messages.error(request, "Książka jest niedostępna")
    return redirect(f"/books/{id}")

@login_required
def return_book(request, id):
    book = Book.objects.get(id=id)
    if not book.is_available:
        borrowing = book.borrowing_set.last()
        if borrowing.user == request.user or request.user.is_superuser:
            borrowing.return_date = timezone.now()
            borrowing.save()
            messages.success(request, "Książka została zwrócona")
        else:
            messages.error(request, "Nie możesz zwrócić książki, której nie wypożyczyłeś")
    else:
        messages.error(request, "Nie można zwrócić książki, która nie została wypożyczona")
    return redirect(f"/books/{id}")

def author_list(request):
    authors = Author.objects.all()
    return render(request, "books/author_list.html", {"authors": authors})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, "books/genre_list.html", {"genres": genres})

def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author=author)
    return render(request, "books/book_list.html", {"author": author, "books": books})

def genre_details(request, id):
    genre = Genre.objects.get(id=id)
    books = Book.objects.filter(genre=genre)
    return render(request, "books/book_list.html", {"genre": genre, "books": books})

