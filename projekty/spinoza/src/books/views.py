from django.shortcuts import render, redirect

from .models import Book, Author, Genre, Borrowing
from django.utils import timezone
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, "books/book_details.html", {"book": book})


def borrow_book(request, id):
    book = Book.objects.get(id=id)
    Borrowing.objects.create(book=book)
    return redirect(f"/books/{id}")

def return_book(request, id):
    book = Book.objects.get(id=id)
    borrowing = book.borrowing_set.last()
    borrowing.return_date = timezone.now()
    borrowing.save()
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

