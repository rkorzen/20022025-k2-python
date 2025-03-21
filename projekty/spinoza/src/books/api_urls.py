from django.urls import path
from .api_views import genre_list, author_list

urlpatterns = [
    path("genres/", genre_list),
    path("authors/", author_list),

]