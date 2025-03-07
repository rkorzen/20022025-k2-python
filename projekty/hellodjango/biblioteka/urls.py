from django.urls import path

from .views import books_list, book_details

app_name = "books" # books:list
urlpatterns = [
    path("", books_list, name="list"),
    path("<int:id>/", book_details, name="details"),

]