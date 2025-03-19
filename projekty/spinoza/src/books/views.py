from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Author, Genre, Borrowing, Review
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import GenreForm, AuthorForm, BookForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
# Create your views here.


def get_pagination_data(request, queryset):
    page_number = request.GET.get("page", 1)
    per_page_number = request.GET.get("per_page", 25)
    per_page_number = int(per_page_number)
    paginator = Paginator(queryset, per_page_number)
    
    page_obj = paginator.get_page(page_number)
    return page_obj, per_page_number

def book_list(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Książka została dodana")
        else:
            messages.error(request, "Nieprawidłowe dane")

    form = BookForm()
    books = Book.objects.all()

    page_obj, per_page_number = get_pagination_data(request, books)
    return render(request, "books/book_list.html", {"page_obj": page_obj, "current_page": "books", "form": form, "per_page_number": per_page_number})

def book_details(request, id):
    book = Book.objects.get(id=id)
    users = User.objects.all()

    if request.method == "POST":

        if request.POST.get("action") == "borrow" and request.user.is_superuser:
            user = User.objects.get(id=request.POST.get("user_id"))
            if book.is_available:
                Borrowing.objects.create(user=user, book=book)
                messages.success(request, "Książka została wypożyczona")
            else:
                messages.error(request, "Książka jest niedostępna")
        elif request.POST.get("action") == "borrow" and not request.user.is_superuser:
            messages.error(request, "Nie możesz wypożyczać książek")
        else:
            review = Review(
                book=book,
                name=request.POST.get("name") or request.user.username,
                comment=request.POST.get("comment"),
            )

            if request.user.is_authenticated:
                review.user = request.user

            review.save()
            messages.success(request, "Opinia została dodana")

    return render(request, "books/book_details.html", {"book": book, "users": users})

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
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor został dodany")
        else:
            messages.error(request, "Nieprawidłowe dane")

    form = AuthorForm()        
    authors = Author.objects.all()
    page_obj, per_page_number = get_pagination_data(request, authors)

    return render(request, "books/author_list.html", {"page_obj": page_obj, "current_page": "authors", "form": form, "per_page_number": per_page_number})

def genre_list(request):
    if request.method == "POST":
        form = GenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gatunek został dodany")
        else:
            messages.error(request, "Nieprawidłowe dane")

    form = GenreForm()
    genres = Genre.objects.all()
    page_obj, per_page_number = get_pagination_data(request, genres)

    return render(request, "books/genre_list.html", {"page_obj": page_obj, "current_page": "genres", "form": form, "per_page_number": per_page_number})

def author_details(request, id):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Książka została dodana")
        else:
            messages.error(request, "Nieprawidłowe dane")

    author = Author.objects.get(id=id)
    form = BookForm()
    
    books = Book.objects.filter(author=author)
    page_obj, per_page_number = get_pagination_data(request, books)

    return render(request, "books/book_list.html", {"author": author, "page_obj": page_obj, "form": form, "per_page_number": per_page_number})

def genre_details(request, id):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Książka została dodana")
        else:
            messages.error(request, "Nieprawidłowe dane")
    form = BookForm()
    genre = Genre.objects.get(id=id)
    books = Book.objects.filter(genre=genre)
    page_obj, per_page_number = get_pagination_data(request, books)
    return render(request, "books/book_list.html", {"genre": genre, "page_obj": page_obj, "form": form, "per_page_number": per_page_number})

