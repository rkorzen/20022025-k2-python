from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Author, Genre, Borrowing, Review
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import GenreForm, AuthorForm, BookForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.

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
    return render(request, "books/book_list.html", {"books": books, "current_page": "books", "form": form})

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
    return render(request, "books/author_list.html", {"authors": authors, "current_page": "authors", "form": form})

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
    return render(request, "books/genre_list.html", {"genres": genres, "current_page": "genres", "form": form})

def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author=author)
    return render(request, "books/book_list.html", {"author": author, "books": books})

def genre_details(request, id):
    genre = Genre.objects.get(id=id)
    books = Book.objects.filter(genre=genre)
    return render(request, "books/book_list.html", {"genre": genre, "books": books})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # lub inna strona po zalogowaniu
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

