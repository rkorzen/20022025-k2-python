from django.urls import path
import books.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("books/", books.views.book_list, name="book_list"), 
    path("books/<int:id>", books.views.book_details, name="book_details"), 
    path("books/<int:id>/borrow", books.views.borrow_book, name="borrow_book"),
    path("books/<int:id>/return", books.views.return_book, name="return_book"),
    path("authors/", books.views.author_list, name="author_list"),
    path("authors/<int:id>", books.views.author_details, name="author_details"),
    path("genres/", books.views.genre_list, name="genre_list"),
    path("genres/<int:id>", books.views.genre_details, name="genre_details"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]